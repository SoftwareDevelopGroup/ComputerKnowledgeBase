---
domain: 数据库技术
subject: Oracle数据库管理
type: knowledge
chapter: 第3章 Oracle实例与存储结构
tags: [Oracle,DBA,SGA,PGA,后台进程,表空间,数据文件,控制文件,重做日志,段,区,块]
prerequisites: ["数据库原理", "MOC - 第1章 Oracle数据库概述", "MOC - 第2章 Oracle安装与环境配置"]
---

# MOC - 第3章 Oracle实例与存储结构

> [!info] 本章定位
> 本章深入Oracle内核的**两大支柱**：**实例内部（SGA/PGA内存 + 六大后台进程）**和**存储体系（五大物理文件 + 四层逻辑存储结构**，是DBA调优、故障诊断、备份恢复的理论基础。所有性能问题和恢复问题最终都可以追溯到本章的某个组件。

## 学习路线图

```mermaid
flowchart LR
    A["3.1 内存结构SGA、PGA"] --> B["3.2 后台进程作用"]
    B --> C["3.3 物理文件：数据文件、控制文件、重做日志"]
    C --> D["3.4 逻辑存储：表空间、段、区、块"]
    style A fill:#4F86F7,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#C30045,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#6FB98F,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#FF8C42,stroke:#333,stroke-width:2px,color:#fff
```

## 知识点导航

| 节 | 主题 | 核心要点 | 入口 | 重要度 |
|---|---|---|---|---|
| 3.1 | 内存结构SGA、PGA | SGA五大组件（Buffer Cache/Shared Pool/Large Pool/Java Pool/Redo Buffer）+ PGA四区 + 对比表 + v$SGA/v$PGASTAT查询 | [[3.1 内存结构SGA、PGA]] | ⭐⭐⭐⭐⭐ |
| 3.2 | 后台进程作用 | PMON/SMON/DBWn/LGWR/CKPT/ARCn六大核心进程的触发条件+作用+协作流程Mermaid | [[3.2 后台进程作用]] | ⭐⭐⭐⭐⭐ |
| 3.3 | 物理文件 | 数据文件/控制文件/重做日志/参数文件/密码文件各文件作用、丢失后果、典型SQL查询 | [[3.3 物理文件：数据文件、控制文件、重做日志]] | ⭐⭐⭐⭐⭐ |
| 3.4 | 逻辑存储四层映射 | 表空间→段→区→块四层结构+各层管理命令+DBA_TABLESPACES等视图查询 | [[3.4 逻辑存储：表空间、段、区、块]] | ⭐⭐⭐⭐ |

## 核心考点

> [!warning] 重点掌握（8点）
> 1. **SGA vs PGA本质**：SGA=全局共享内存（所有进程共享，所有会话共用），PGA=每个服务器进程私有（不共享）
> 2. **SGA五大组件**：Buffer Cache（数据块缓存）、Shared Pool（SQL解析+数据字典）、Redo Log Buffer（预写式日志缓冲）、Large Pool（共享服务器/RMAN/并行I/O）、Java Pool（Java存储过程）
> 3. **LGWR触发的5大条件**：用户COMMIT提交/每3秒/重做日志缓冲区1/3满/缓存1MB满/DBWn写之前同步
> 4. **DBWn写触发条件**：检查点/脏缓冲区不足/超时3秒/RAC ping/表空间offline/read only/drop/begin backup
> 5. **检查点CKPT的作用**：更新数据文件头SCN、更新控制文件SCN、触发DBWn将脏块写盘
> 6. **控制文件的核心内容**：数据库名、数据/日志文件列表、检查点SCN、日志历史、备份元信息（RMAN Catalog外部目录替代方案
> 7. **重做日志三大要素**：循环复用（至少2组）、多路复用成员（每组至少2个）、三种状态CURRENT/ACTIVE/INACTIVE
> 8. **四层逻辑存储映射**：表空间(Tablespace)→段(Segment)→区(Extent)→块(Block)；每个表空间含N个段，每个段由N个区（连续块）组成，块是最小I/O单元（默认8KB）

## 自测题

> [!question] 自测题1
> Shared Pool由哪两大部分组成？各自的作用是什么？如何调整？命中率太低会导致什么问题？
> 
> > [!check]- 参考答案
> > Shared Pool = **Library Cache（库缓存）** + **Data Dictionary Cache（数据字典缓存）**
> > - Library Cache：缓存SQL/PLSQL执行计划、解析树、执行代码。避免重复做硬解析（Hard Parse），减少CPU消耗
> > - Data Dictionary Cache：缓存数据字典信息（表/列/用户/权限定义，dba_*视图）。避免每次SQL解析去读SYSTEM表空间
> > - 调整参数：SHARED_POOL_SIZE（ASMM下自动调，SGA_TARGET/SGA_MAX_SIZE自动管理）
> > - 命中率低后果：① Library Cache命中率低→频繁硬解析→CPU使用率飙升（SQL解析CPU 90%在解析上）② Row Cache命中率低→频繁读SYSTEM表空间产生物理I/O

> [!question] 自测题2
> 请按顺序说明用户执行`COMMIT`命令时，LGWR、DBWn、CKPT、用户进程、服务器进程之间的协作流程。说明为什么Oracle设计成"先写日志后写数据"（WAL预写式日志）？
> 
> > [!check]- 参考答案
> > ```
> > COMMIT协作流程（Fast-Commit机制：
> > 1. 用户进程发出COMMIT命令→服务器进程
> > 2. 服务器进程生成一条COMMIT记录→写入Redo Log Buffer
> > 3. 服务器进程**立即触发LGWR**把Redo Buffer中该事务的所有redo条目（含COMMIT记录**连同SCN**写到在线重做日志文件
> > 4. LGWR写盘成功后→给用户进程返回"Commit complete
> > 5. **此时数据块DB Buffer Cache中修改的数据块（脏块）并不立即写盘！**（延迟写）
> > 6. DBWn在后续检查点/脏块不足时**批量**把脏块写回数据文件
> > 7. CKPT定期触发，更新控制文件和数据文件头的SCN同步
> > 
> > WAL预写式日志Write-Ahead Logging设计优势：
> > ① 保证事务持久性D：只要redo日志写盘成功→即使脏块没写盘实例崩溃→下次启动SMON前滚redo恢复已提交事务
> > ② 提交响应极快：写redo是顺序写（512字节块，比随机写数据快几十上百倍
> > ③ I/O合并：脏块延迟写→DBWn可以批量合并相邻脏块一次写，大幅减少随机I/O
> > ```

> [!question] 自测题3
> 控制文件损坏一个成员如何修复？（control_files='/disk1/control01.ctl','/disk2/control02.ctl'，不小心删除了disk2的control02.ctl，数据库此时处于OPEN状态。请写出恢复步骤。
> 
> > [!check]- 参考答案
> > **多路复用控制文件丢失一个的恢复步骤（最简单的多路复用恢复：
> > ```sql
> > -- ① 立即关闭数据库（必须一致性关闭，不能ABORT
> > SHUTDOWN IMMEDIATE;
> > 
> > -- ② 操作系统层面复制剩余好的控制文件到损坏丢失位置
> > -- cp /disk1/control01.ctl /disk2/control02.ctl
> > 
> > -- ③ 启动数据库
> > STARTUP;
> > 
> > -- ④ 验证
> > SELECT name FROM v$controlfile;   -- 两条记录状态都OK
> > ```
> > **注意事项**：
> > - 如果是全部控制文件都丢失：必须从备份恢复或重建控制文件`CREATE CONTROLFILE REUSE DATABASE...`（复杂很多
> > - 数据库OPEN状态下直接复制控制文件无效（一致性问题，必须关库后复制！
> > - 最佳实践：控制文件至少3路复用+ASM磁盘组normal冗余双镜像
> > - 定期备份控制文件：`ALTER DATABASE BACKUP CONTROLFILE TO '/backup/control.ctl.bak';` 或 `ALTER DATABASE BACKUP CONTROLFILE TO TRACE;`

> [!question] 自测题4
> 什么是表空间？SYSTEM/SYSAUX/UNDOTBS/TEMP/USERS这5个默认表空间各自作用？DROP TABLESPACE时INCLUDING CONTENTS AND DATAFILES参数的作用？
> 
> > [!check]- 参考答案
> > **表空间Tablespace定义**：
> > Oracle数据库中的最大逻辑容器，物理上对应一个或多个数据文件(.dbf)。用来组织管理段（表/索引），便于DBA做空间管理、配额分配、备份恢复、冷热数据分离。
> > 
> > **五大默认表空间**：
> > | 表空间 | 作用 | 能否删除 |
> > |---|---|---|
> > | **SYSTEM** | 系统表空间，存储数据字典（dba_*表定义）、PL/SQL源代码、SYSTEM回滚段 | ❌绝对不能删 |
> > | **SYSAUX** | SYSTEM辅助表空间，AWR/ASH/ADDM、OEM、Oracle Text、XDB、Data Pump等辅助组件数据 | ❌不能删 |
> > | **UNDOTBS1** | UNDO撤销表空间，存储UNDO数据（回滚未提交、读一致性、闪回查询） | ❌删之前要先切换到新UNDO表空间 |
> > | **TEMP** | 临时表空间，存储排序/哈希连接/临时表/索引创建等临时数据，实例重启自动清空 | ❌默认TEMP不能删，需先建临时表空间替换 |
> > | **USERS** | 默认用户数据表空间，新建用户默认在USERS建表 | ⚠️可删（要先迁移用户数据；生产一般不用USERS，独立创建业务专用表空间 |
> > 
> > **INCLUDING CONTENTS AND DATAFILES**：
> > DROP TABLESPACE时：
> > - 不加参数：表空间必须空（无任何段）才能删
> > - `INCLUDING CONTENTS`：删除表空间里的所有段（表/索引等
> > - `INCLUDING CONTENTS AND DATAFILES`：删除段+同时删除操作系统层面的物理数据文件.dbf（彻底删除，省得手工rm文件
> > - 强烈建议生产：DROP之前先备份！
> > ```sql
> > -- 示例：删除业务表空间彻底删除
> > DROP TABLESPACE sale_tbs INCLUDING CONTENTS AND DATAFILES CASCADE CONSTRAINTS;
> > -- CASCADE CONSTRAINTS：同时删除其他表空间中表引用本表空间的外键约束
> > ```

## 章节导航

- 上一级：[[MOC - Oracle数据库管理]]
- 上一章：[[MOC - 第2章 Oracle安装与环境配置]]
- 下一章：[[MOC - 第4章]]（规划中：SQL与PLSQL编程
- 本章习题：[[MOC - 第3章习题]]
- 上一章习题：[[MOC - 第2章习题]]
- 下一章习题：[[MOC - 第4章习题]]
