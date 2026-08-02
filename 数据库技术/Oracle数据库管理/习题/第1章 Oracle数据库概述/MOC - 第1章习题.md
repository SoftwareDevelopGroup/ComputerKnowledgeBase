---
domain: 数据库技术
subject: Oracle数据库管理
type: exercise
chapter: 第1章 Oracle数据库概述
section: 1.1 Oracle发展与版本体系
tags: [Oracle,习题,DBA,体系结构,实例,RAC]
prerequisites: ["数据库原理", "MOC - 第1章 Oracle数据库概述"]
---

# MOC - 第1章 Oracle数据库概述 习题

> [!tip] 做题建议
> 本章习题侧重基础概念辨析，重点掌握实例与数据库的本质区别、启动三阶段、版本体系。先独立完成再看答案。

---

## 一、单选题（10题×2分=20分）

### 1.
Oracle 19c属于什么类型的版本？（  ）
A. 创新版（Innovation Release）
B. 长期支持版LTS（Long Term Support）
C. 测试版
D. 免费版XE

<details>
<summary>查看答案</summary>
**B**。Oracle 19c是长期支持版本LTS，主支持到2027年，扩展支持到2032年。18c/21c是创新版本，支持周期较短。
</details>

### 2.
Oracle数据库启动过程中，读取控制文件（Control File）是在哪个阶段完成的？（  ）
A. NOMOUNT
B. MOUNT
C. OPEN
D. SHUTDOWN

<details>
<summary>查看答案</summary>
**B**。MOUNT阶段读取控制文件，获取数据文件和重做日志文件的位置信息。NOMOUNT阶段仅读参数文件。
</details>

### 3.
Oracle 12c引入的"c"代表什么含义？（  ）
A. Client
B. Cloud
C. Cluster
D. Core

<details>
<summary>查看答案</summary>
**B**。12c的"c"=Cloud（云），12c首次引入多租户CDB/PDB架构，全面支持云部署。
</details>

### 4.
以下哪个是Oracle实例（Instance）的组成部分？（  ）
A. 数据文件.dbf
B. 控制文件.ctl
C. SGA系统全局区内存
D. 重做日志文件.log

<details>
<summary>查看答案</summary>
**C**。实例由SGA内存+后台进程组成。A/B/D都是物理文件，属于Database数据库的组成部分。
</details>

### 5.
RAC集群环境下，实例与数据库的映射关系是？（  ）
A. 1:1 一一对应
B. 1:N 一个实例对应多个数据库
C. N:1 多个实例对应一个数据库
D. N:N 多对多

<details>
<summary>查看答案</summary>
**C**。RAC是多实例共享存储架构：多个节点上的多个Instance对应同一个共享存储上的Database。
</details>

### 6.
Oracle监听器默认使用的端口号是？（  ）
A. 3306
B. 5432
C. 1433
D. 1521

<details>
<summary>查看答案</summary>
**D**。1521是Oracle监听默认端口。3306=MySQL、5432=PostgreSQL、1433=SQL Server。
</details>

### 7.
本地BEQueath方式连接Oracle时，用于标识连接目标实例的环境变量是？（  ）
A. ORACLE_HOME
B. ORACLE_SID
C. ORACLE_BASE
D. NLS_LANG

<details>
<summary>查看答案</summary>
**B**。ORACLE_SID是操作系统级别的System Identifier，标识本地连接的实例。
</details>

### 8.
以下哪个版本不支持RAC集群多节点（超过2节点）？（  ）
A. Enterprise Edition 企业版
B. Standard Edition 2 标准版
C. Personal Edition 个人版
D. 都支持

<details>
<summary>查看答案</summary>
**B**。SE2标准版RAC最多支持2节点，且功能受限。超过2节点必须EE企业版。
</details>

### 9.
Oracle Express Edition（XE）免费版对用户数据的最大限制是？（  ）
A. 2GB
B. 12GB
C. 50GB
D. 无限制

<details>
<summary>查看答案</summary>
**B**。Oracle 19c XE限制：最多2个CPU线程、2GB内存、12GB用户数据。
</details>

### 10.
`sqlplus / as sysdba`本地连接使用的认证方式是？（  ）
A. 密码文件认证
B. 操作系统认证 OS Authentication
C. LDAP认证
D. Kerberos认证

<details>
<summary>查看答案</summary>
**B**。"/"表示使用操作系统认证，当前Unix下当前用户需属于dba组。远程连接无法使用"/"必须使用密码。
</details>

---

## 二、多选题（5题×3分=15分）

### 11.
以下哪些属于Oracle数据库（Database）的物理文件组成？（  ）
A. 数据文件 .dbf
B. 控制文件 .ctl
C. SGA系统全局区
D. 重做日志文件 .log
E. 后台进程PMON

<details>
<summary>查看答案</summary>
**ABD**。Database是物理文件集合。C（SGA）和E（PMON）属于Instance实例。
</details>

### 12.
以下关于Service Name相比SID的优势有哪些？（  ）
A. 支持负载均衡
B. 支持连接时故障转移
C. 支持应用透明故障转移TAF
D. 一个数据库可注册多个服务名
E. 本地BEQueath连接必须使用

<details>
<summary>查看答案</summary>
**ABCD**。E错误：本地BEQueath使用ORACLE_SID，不需要Service Name。
</details>

### 13.
以下哪些是Oracle独有的企业级特性？（  ）
A. RAC真正应用集群
B. Active Data Guard
C. 闪回数据库 Flashback Database
D. 多租户CDB/PDB架构
E. InnoDB存储引擎

<details>
<summary>查看答案</summary>
**ABCD**。InnoDB是MySQL的存储引擎。
</details>

### 14.
MOUNT阶段可以执行的操作有？（  ）
A. 重命名数据文件
B. 启用/禁用归档模式
C. 查询V$DATABASE视图
D. SELECT查询用户表数据
E. 执行数据库介质恢复

<details>
<summary>查看答案</summary>
**ABCE**。MOUNT阶段数据文件未打开，D错误（OPEN阶段才能查询用户表）。
</details>

### 15.
以下哪些关闭模式会导致下次启动触发实例恢复？（  ）
A. SHUTDOWN NORMAL
B. SHUTDOWN IMMEDIATE
C. SHUTDOWN TRANSACTIONAL
D. SHUTDOWN ABORT
E. 服务器断电强制关机

<details>
<summary>查看答案</summary>
**DE**。ABORT和断电属于异常关闭，下次启动SMON需要前滚+回滚做实例恢复。A/B/C是一致性关闭方式，下次启动无需恢复。
</details>

---

## 三、判断题（5题×2分=10分）

### 16.
Oracle数据库关闭后，Instance实例仍然存在于操作系统中。（  ）

<details>
<summary>查看答案</summary>
**×**。实例是临时的运行态实体，关闭后SGA内存释放、后台进程终止，实例不再存在。只有物理文件永久保存。
</details>

### 17.
Oracle 19c的完整版本号19.3.0.0.0中，19是主版本号，3是发布版本号。（  ）

<details>
<summary>查看答案</summary>
**√**。格式MAJOR.MINOR.RELEASE.UPDATE.PATCH，19.3.0.0.0=19主版本.3发布版本.0更新版本.0补丁集.0单补丁。
</details>

### 18.
RAC集群中，每个节点都有自己独立的一份数据库物理文件。（  ）

<details>
<summary>查看答案</summary>
**×**。RAC共享存储架构：所有节点共享同一份物理文件集合，每个节点有自己独立的Instance实例（独立的SGA和后台进程）。
</details>

### 19.
本地BEQueath连接Oracle需要先启动监听器Listener才能连接。（  ）

<details>
<summary>查看答案</summary>
**×**。本地BEQueath不通过监听，sqlplus / as sysdba直接fork服务器进程，和监听器无关。远程连接才需要启动监听。
</details>

### 20.
Oracle Database和MySQL Database在Oracle的Database概念完全等价，都是逻辑命名空间。（  ）

<details>
<summary>查看答案</summary>
**×**。Oracle Database=物理文件集合（全局唯一，重量级）；MySQL Database=SCHEMA逻辑命名空间（mysqld下有N个，轻量级）。两者本质完全不同。
</details>

---

## 四、简答题（4题×5分=20分）

### 21.
请说明Oracle实例（Instance）与数据库（Database）的核心区别，并说明为什么要做这样的拆分设计。

<details>
<summary>查看答案</summary>
**Instance实例 = SGA内存 + 后台进程**，是运行时的引擎，临时存在；
**Database数据库 = 磁盘物理文件集合**（.dbf/.ctl/.log等），是永久存储的数据仓库。
**拆分设计的优势**：
① **高可用支持**：RAC多实例共享一个数据库，单实例故障不影响；
② **备份恢复灵活**：实例崩溃不影响物理文件，重启即可；介质损坏只需恢复文件，可启动实例到MOUNT状态做恢复；
③ **资源隔离**：一个数据库可以被不同配置的实例加载（如先启动到不同阶段），灵活运维灵活管理。
</details>

### 22.
请描述Oracle启动的三个阶段（NOMOUNT/MOUNT/OPEN），每阶段读取的关键文件和可执行的关键操作。

<details>
<summary>查看答案</summary>
**NOMOUNT阶段**：
- 动作：读spfile/pfile参数文件→分配SGA内存→启动后台进程
- 文件：仅读参数文件
- 操作：创建数据库、重建控制文件
- 视图：V$INSTANCE/V$SGA/V$PARAMETER

**MOUNT阶段**：
- 动作：从参数中找控制文件位置→读控制文件→获取数据/日志文件清单
- 文件：读控制文件
- 操作：重命名数据文件、切换归档模式、介质恢复、改数据库名
- 视图：+V$DATABASE/V$DATAFILE/V$LOG/V$TABLESPACE

**OPEN阶段**：
- 动作：检查数据文件存在性→SMON实例恢复（如需要）→打开文件对外服务
- 文件：所有数据文件+日志文件
- 操作：所有DML/DDL/查询
- 视图：DBA_*/ALL_*/USER_*全部可用
</details>

### 23.
请说明SID（ORACLE_SID）和Service Name的区别，各自应用场景。

<details>
<summary>查看答案</summary>
**ORACLE_SID（System Identifier）**：
- 定义：操作系统级别的实例标识符，标识实例的唯一名称
- 场景：本地BEQueath连接（sqlplus / as sysdba）；默认参数/密码/日志文件命名
- 特点：一个实例对应一个SID，1:1

**Service Name**：
- 定义：数据库对外服务名是对外的逻辑服务标识
- 场景：远程客户端JDBC应用连接；监听器注册，支持负载均衡和故障转移TAF
- 特点：一个数据库可注册多个服务名（SERVICE_NAMES参数），N:1映射

**关键区别**：SID是实例名（给OS/本地连接用），Service Name是服务名（给远程客户端/应用用）。
</details>

### 24.
对比Oracle EE企业版与MySQL社区版在高可用方案上的差异。

<details>
<summary>查看答案</summary>

| 维度 | Oracle EE | MySQL 社区版 |
|---|---|---|
| 多活集群 | RAC真正应用集群，多节点多活读写，Cache Fusion高速内存融合 | 无原生多活，MySQL Cluster是NDB引擎（非InnoDB），社区版是Group Replication主从复制 |
| 主备容灾 | Active Data Guard：物理备库实时查询+实时查询，备库可读查询报表卸载 | 异步/半同步复制，备库只读（通过binlog逻辑复制） |
| 数据保护 | 最大可用/最大性能/最大保护三种保护模式 | 异步/半同步模式 |
| 闪回能力 | Flashback Query/Table/Database/Drop/Archive全系列时间点回退 | 无同等深度，仅通过binlog恢复 |
| RPO/RTO | 零数据丢失+秒级RPO（ADG最大保护模式） | RPO（异步复制可能丢数据，半同步改进） |
</details>

---

## 五、分析实操题（4题×7分=28分）

### 25.
分析以下操作场景，说明连接使用的连接方式、是否需要监听器、认证方式：

场景A：DBA在数据库服务器本机执行 `export ORACLE_SID=orcl; sqlplus / as sysdba`
场景B：应用服务器JDBC串：`jdbc:oracle:thin:@//db1.example.com:1521/oltp.example.com`

<details>
<summary>查看答案</summary>
**场景A**：
- 连接方式：本地BEQueath连接
- 是否需要监听：否（不需要启动监听）
- 认证方式：操作系统认证OS Authentication（当前用户属于dba组）
- 说明：通过ORACLE_SID指定连接的实例，sqlplus直接fork服务器进程

**场景B**：
- 连接方式：远程Thin驱动JDBC Thin Driver
- 是否需要监听：是（必须启动监听器运行）
- 认证方式：密码认证（用户名/密码认证，非OS认证
- 说明：使用Service Name `oltp.example.com`连接远程数据库服务，通过1521端口
</details>

### 26.
DBA执行以下命令序列，请说明每一步执行后数据库所处状态、执行了哪些动作、读取了哪些文件：
```sql
SQL> STARTUP NOMOUNT;
SQL> ALTER DATABASE MOUNT;
SQL> ALTER DATABASE OPEN;
```

<details>
<summary>查看答案</summary>

**① STARTUP NOMOUNT**：
- 状态：STARTED (NOMOUNT)
- 动作：读spfile/pfile参数文件；分配SGA内存；启动PMON/SMON/DBWn/LGWR/CKPT等后台进程
- 文件：仅读取参数文件 spfileorcl.ora / initorcl.ora
- 视图可用：V$INSTANCE、V$SGA、V$PARAMETER、V$PROCESS

**② ALTER DATABASE MOUNT**：
- 状态：MOUNTED
- 动作：从control_files参数中找控制文件路径，读取控制文件，获取数据文件/重做日志列表
- 文件：读取控制文件（多路复用的所有.ctl文件
- 新增可用：V$DATABASE、V$DATAFILE、V$LOG、V$TABLESPACE

**③ ALTER DATABASE OPEN**：
- 状态：OPEN
- 动作：检查所有数据文件头、检查SCN同步；如异常关闭则SMON做实例恢复（前滚+回滚未提交）；打开数据文件和重做日志文件对外服务
- 文件：读取所有.dbf数据文件+ .log重做日志文件
- 新增可用：DBA_TABLES/DBA_DATA_FILES/DBA_SEGMENTS等DBA视图及全部业务表数据
</details>

### 27.
某Oracle 19c数据库服务器意外断电（异常SHUTDOWN ABORT效果），请分析：

① 断电后Instance和Database哪个丢失了，哪个还在？
② 来电后启动时会发生什么？哪个后台进程负责什么工作？

<details>
<summary>查看答案</summary>
**① 断电后状态**：
- Instance（实例）丢失：SGA内存数据丢失，后台进程全部终止，属于崩溃实例消失
- Database（数据库）存在：磁盘上的.dbf/.ctl/.log物理文件仍然存在，数据持久化

**② 来电后STARTUP启动时**：
- NOMOUNT：读参数，重建新的实例（全新实例）
- MOUNT：读控制文件
- OPEN阶段：**SMON进程自动实例恢复（Instance Recovery），分为两步：
  - **前滚（Roll Forward）**：LGWR将Redo Log中记录的所有变更（含未提交的也前滚到SGA，恢复到断电瞬间的状态
  - **回滚（Roll Back）**：回滚断电时未提交的事务（利用UNDO段撤销未提交）
- 结果：数据库恢复到**提交一致性状态，已提交事务的数据不丢失
</details>

### 28.
请写出Oracle 19c环境下执行以下查询的作用：
```sql
SELECT name FROM v$controlfile;
SELECT member FROM v$logfile;
SELECT file_name, tablespace_name FROM dba_data_files;
```
分别说明每一条SQL所属的启动阶段才能执行（NOMOUNT/MOUNT/OPEN）。

<details>
<summary>查看答案</summary>

**① SELECT name FROM v$controlfile;**
- 作用：查询控制文件的物理位置和状态
- 阶段：**MOUNT及以上（含MOUNT、OPEN）
- 原因：v$controlfile信息来自控制文件本身，MOUNT阶段读入内存中

**② SELECT member FROM v$logfile;**
- 作用：查询重做日志组成员文件路径
- 阶段：**MOUNT及以上
- 原因：重做日志文件清单存储于控制文件，MOUNT后可读

**③ SELECT file_name, tablespace_name FROM dba_data_files;**
- 作用：查询所有数据文件路径及所属表空间
- 阶段：**OPEN阶段**（必须OPEN
- 原因：DBA_DATA_FILES数据字典视图（属于DBA_*开头的存放在数据字典，存储于SYSTEM表空间中，数据文件必须打开才能读取字典表
</details>

---

## 六、综合设计题（2题×8分=16分）

### 29.
某企业核心业务系统，选型数据库选型评估Oracle 19c，业务要求：
- 7×24小时不间断，不可停机
- 核心交易库RPO=0（零数据丢失
- 允许瞬间（服务器故障数据库秒级恢复
- 同时有一个异地灾备
- 报表查询业务需大量并发查询卸载

请为该企业设计Oracle高可用架构方案，说明用到哪些Oracle特性、各特性解决什么问题。

<details>
<summary>查看答案</summary>

**方案设计：Oracle EE企业版 + RAC + ADG 两地三中心**

**① 本地高可用层：**
  - **Oracle RAC 2~4节点集群**：多节点多活读写，任何单节点故障（服务器故障秒级切换；剩余节点自动接管连接，业务不中断（解决7×24可用性、秒级故障转移
  - **ASM自动存储管理**：管理共享存储，磁盘组镜像，解决存储高可用

**② 同城/异地容灾层：**
- **Active Data Guard 最大保护模式**：
  - 物理备库实时应用Redo，Zero Data Loss（零数据丢失RPO=0）
  - 备库**实时查询**Active Data Guard DML重定向
  - 解决异地容灾：同城同步灾备库

**③ 报表卸载层：**
  - ADG备库同时承担**只读报表查询**（Active Data Guard实时查询功能），主库交易OLTP与报表查询从主库卸载

**④ 快速数据修复层：**
  - **闪回数据库/闪回表/闪回查询**：逻辑错误秒级快速回退
  - **RMAN块介质恢复**：坏块无需恢复整个文件

**⑤ 备份层：**
  - RMAN增量备份累积+归档备份策略保留策略

**总结：EE企业版许可（RAC+ADG+闪回+RMAN高级特性），满足RPO=0、RTO秒级、7×24、报表卸载。
</details>

### 30.
对比Oracle 19c SE2标准版与EE企业版，说明以下业务中哪些功能差异，并给出企业选型建议。

业务场景1：100人规模的部门级OA系统，月流水10万，数据100GB，预算有限
业务场景2：省级核心交易库，日交易百万级，要求RPO=0，预算充足预算充足

<details>
<summary>查看答案</summary>

| 功能差异：Oracle 19c SE2 vs EE

| 对比维度 | SE2 标准版 | EE 企业版 |
|---|---|---|
| CPU限制 | 最多16线程CPU插槽 | 不限 |
| RAC | 最多2节点RAC | 不限节点数 |
| ADG Active Data Guard | ❌不支持 | ✅最大可用| ✅支持（物理/逻辑/ADG查询卸载 |
| 分区表 | ❌ | ✅范围/列表/哈希/间隔/复合分区 |
| 高级压缩 | ❌ | ✅OLTP/查询/备份压缩 |
| 高级安全TDE透明加密 | ❌ | ✅TDE列加密表空间加密 |
| 闪回数据库 | ❌ | ✅闪回全系列 |
| RMAN高级特性 | 基础RMAN | ✅块恢复、表级时间点恢复 |
| 性能调优AWR/ASH/ADDM | ❌诊断包授权分离 | ✅诊断包+调优包 |

**选型建议**：

**场景1（100人OA系统，预算有限，数据量小）：**
✅ 选SE2标准版（100GB数据+低并发+无容灾要求，SE2足够
- 2节点RAC满足基本高可用
- 成本远低于EE

**场景2（核心交易库日交易百万级，RPO=0，预算充足）：**
✅ 必须EE企业版
- RAC多节点高并发吞吐
- ADG最大保护模式RPO=0
- 分区表+高级压缩支撑百万级性能
- 高级安全TDE合规
- AWR/ASH/ADDM性能诊断
</details>

---

## 考点统计表

| 考点 | 题号 | 分值 | 合计占比 |
|---|---|---|---|
| Oracle发展与版本体系 | 1,3,8,9,13,17,30 | 30 | 30% |
| 体系结构总览 | 6,7,10,12,18,19,21,23,25 | 41 | 41% |
| 数据库与实例概念区分 | 2,4,5,11,14,15,16,20,22,24,26,27,28,29 | 59 | 59% |
| RAC与高可用 | 5,8,13,18,24,27,29,30 | 35 | 35% |
| 启动三阶段 | 2,14,15,16,22,26,28 | 45 | 45% |

## 章节导航

- 上一级：[[MOC - Oracle数据库管理]]
- 本章知识点：[[MOC - 第1章 Oracle数据库概述]]
- 下一章习题：[[MOC - 第2章习题]]
