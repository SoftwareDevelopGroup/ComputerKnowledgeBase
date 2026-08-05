---
domain: 数据库技术
subject: Oracle数据库管理
type: knowledge
chapter: 第4章 Oracle数据库启动与关闭
tags: [Oracle,DBA,启动模式,关闭模式,启动故障,NOMOUNT,MOUNT,OPEN,SHUTDOWN]
prerequisites: ["数据库原理", "第3章 Oracle实例与存储结构"]
aliases: [MOC - 第4章, 第4章 Oracle数据库启动与关闭]
---

# MOC - 第4章 Oracle数据库启动与关闭

> [!info] 本章定位
> 本章是Oracle DBA实操的**入门核心章**，解决"如何正确启动Oracle数据库、如何安全关闭数据库、启动失败怎么办"这三个运维最常见问题。它从Oracle数据库的四层启动模式（SHUTDOWN → NOMOUNT → MOUNT → OPEN）入手，阐明每个阶段实例与数据库的交互细节及可执行操作；对比四种关闭模式（NORMAL/TRANSACTIONAL/IMMEDIATE/ABORT）的使用场景与数据一致性差异；最后给出常见启动故障的排查流程与对应ORA错误的解决方案。
>
> 本章是后续章节的运维操作基础：[[第8章 Oracle备份与恢复]]中的恢复操作依赖NOMOUNT/MOUNT阶段执行；[[第7章 Oracle重做日志、归档模式]]中的归档模式切换需在MOUNT阶段执行；理解启动故障排查是判断实例/介质故障的前提。

## 学习路线图

```mermaid
flowchart LR
    S1[4.1 数据库四种启动模式<br/>NOMOUNT / MOUNT / OPEN<br/>各阶段可执行操作]
    S2[4.2 四种关闭模式<br/>NORMAL / TRANSACTIONAL<br/>IMMEDIATE / ABORT对比]
    S3[4.3 启动故障简单排查<br/>ORA错误分析<br/>告警日志与V$视图]

    S1 --> S2
    S2 --> S3

    S1 -.操作前提.-> S2
    S2 -.异常场景.-> S3
```

> [!tip] 路线说明
> 推荐按 4.1 → 4.2 → 4.3 顺序学习。4.1 建立启动四阶段的层级认知，配合Mermaid状态转换图理解；4.2 对比四种关闭模式的一致性与速度权衡，记住生产最常用IMMEDIATE；4.3 综合前两节知识，结合ORA错误号与告警日志形成排查思路。每节均配有SQL命令示例、高风险Callout警告与Mermaid流程图。

## 知识点导航

| 节 | 主题 | 核心要点 | 入口链接 |
| ---- | ---- | ---- | ---- |
| 4.1 | 数据库四种启动模式 | 四层启动模式层级、各阶段可执行SQL、STARTUP参数、V$INSTANCE视图 | [[4.1 数据库四种启动模式]] |
| 4.2 | 四种关闭模式 | NORMAL/TRANSACTIONAL/IMMEDIATE/ABORT对比、检查点与实例恢复、RAC集群注意事项 | [[4.2 正常关闭、立即关闭、事务关闭、中止关闭]] |
| 4.3 | 启动故障简单排查 | 7类常见启动故障、对应ORA错误号、告警日志定位、V$视图辅助排查 | [[4.3 启动故障简单排查]] |

## 核心考点

> [!warning] 重点掌握
> 1. **四种启动模式的层级关系**：SHUTDOWN → NOMOUNT → MOUNT → OPEN，每个阶段的操作内容与可执行的SQL命令。
> 2. **STARTUP命令参数**：FORCE、RESTRICT、OPEN READ ONLY/READ WRITE/UPGRADE的含义与使用场景。
> 3. **V$INSTANCE.STATUS**三个状态值：STARTED（NOMOUNT）、MOUNTED（MOUNT）、OPEN（OPEN）。
> 4. **四种关闭模式对比**：是否允许新连接、是否等待事务、是否等待用户断开、是否需要实例恢复、典型使用场景。
> 5. **SHUTDOWN ABORT的后果**：未提交事务不回滚、不写检查点、下次启动必须实例恢复（SMON自动前滚+回滚）。
> 6. **7类常见启动故障及解决方案**：监听未启动（ORA-12514）、参数文件丢失（ORA-01078）、控制文件损坏（ORA-00205）、数据文件损坏（ORA-01157）、重做日志损坏、归档空间不足（ORA-00257）、密码文件丢失。
> 7. **告警日志alert_SID.log**的路径位置与排查流程：启动失败 → 看告警日志 → 看错误号 → 查V$视图 → 解决路径。

## 自测题

> [!question] 1. STARTUP NOMOUNT阶段，Oracle完成了哪些操作？此阶段可执行哪些SQL？
> > [!check]- 参考答案
> > **NOMOUNT阶段完成的操作**：读取参数文件（spfile优先，其次pfile）→ 分配SGA共享内存区 → 启动DBWn、LGWR、CKPT等后台进程 → 打开告警日志alert_SID.log和跟踪文件。此时实例已启动但**未关联数据库**。
> > **可执行的操作**：CREATE DATABASE（新建数据库）、CREATE SPFILE FROM PFILE / CREATE PFILE FROM SPFILE（参数文件互转）、SHUTDOWN系列命令、查询V$INSTANCE视图（STATUS=STARTED）。典型场景：重建控制文件、新建数据库、备份恢复中的参数文件修复。

> [!question] 2. 为什么生产环境最常用SHUTDOWN IMMEDIATE而不是SHUTDOWN NORMAL？
> > [!check]- 参考答案
> > - **SHUTDOWN NORMAL**（默认）：等待所有用户主动断开连接，不允许新连接；等待所有事务提交；写检查点后关闭。最干净但可能**无限等待**（有用户未断开就一直卡住），实际运维几乎不用。
> > - **SHUTDOWN IMMEDIATE**：不允许新事务开始；**回滚所有未提交事务**；强制断开所有会话；写检查点后关闭。**不等待用户、不等待事务**，速度快且能保证数据一致性（未提交事务被回滚）。因此是**生产环境最常用**的关闭方式。
> > - SHUTDOWN TRANSACTIONAL介于两者之间（等待事务提交但不等待用户断开），适合批处理窗口关闭。

> [!question] 3. 启动时出现ORA-00205: error in identifying control file, check alert log for more info，应如何排查与处理？
> > [!check]- 参考答案
> > **原因**：多路复用的控制文件中部分或全部丢失/损坏/路径不一致。Oracle要求所有CONTROL_FILES参数指定的控制文件必须同时可用且内容一致。
> > **排查步骤**：
> > 1. 查看告警日志alert_SID.log，确认哪个控制文件出问题。
> > 2. 操作系统层面检查CONTROL_FILES指定的所有路径是否存在、文件权限是否正确、文件大小是否一致。
> > **处理方法**：
> > - 若**至少有一个控制文件完好**：关闭数据库，用完好的控制文件**覆盖**所有损坏/丢失的控制文件（多路复用），再启动。
> > - 若**全部控制文件丢失**：需从备份恢复控制文件，或用CREATE CONTROLFILE命令重建（需掌握数据文件与重做日志清单），详见备份恢复章节。

> [!question] 4. STARTUP FORCE的本质是什么？RESTRICT模式有什么作用？
> > [!check]- 参考答案
> > - **STARTUP FORCE**：本质上 = `SHUTDOWN ABORT` + `STARTUP`。用于实例挂起无法正常关闭的紧急情况。
> > > [!danger] 注意
> > > STARTUP FORCE会触发SHUTDOWN ABORT，因此下次启动（紧随其后的STARTUP）需要SMON进行实例恢复。仅在数据库无法正常关闭时使用。
> > - **STARTUP RESTRICT**：启动后只有拥有**RESTRICTED SESSION系统权限**的用户（如SYS、SYSTEM）才能登录。用于数据库维护窗口（如补丁升级、结构变更），在维护期间阻止普通用户接入。维护完成后用`ALTER SYSTEM DISABLE RESTRICTED SESSION;`解除限制。

## 章节导航

- 上一级：[[MOC - Oracle数据库管理]]
- 上一章：[[MOC - 第3章 Oracle实例与存储结构]]
- 下一章：[[MOC - 第5章 用户、权限与角色管理]]
- 本章习题：[[MOC - 第4章习题]]
