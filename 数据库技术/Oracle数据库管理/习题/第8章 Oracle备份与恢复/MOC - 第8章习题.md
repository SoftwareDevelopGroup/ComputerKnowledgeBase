---
domain: 数据库技术
subject: Oracle数据库管理
type: exercise
chapter: 第8章 Oracle备份与恢复
section: 第8章 习题总览
tags: [Oracle,习题,DBA,备份恢复,RMAN,冷备份,热备份,完全恢复,不完全恢复,闪回]
prerequisites: ["8.1 备份分类：冷备份、热备份", "8.2 RMAN工具基础使用", "8.3 完全恢复与不完全恢复", "8.4 闪回技术基础", "MOC - 第7章"]
---

# MOC - 第8章习题

> [!info] 习题说明
> 本习题集覆盖[[MOC - 第8章]]全部知识点，共30题，分六类：单选10题（备份类型判断、RMAN命令、闪回选型）、多选5题（RMAN配置项、三类恢复对比、七类闪回对比）、判断5题（OPEN RESETLOGS/控制文件自动备份关键风险点）、简答4题（冷备vs热备、RMAN vs UMB、恢复黄金步骤、七类闪回选型）、分析4题（RMAN BACKUP脚本编写、完全恢复/不完全恢复场景分析、闪回场景选择题、FRA空间满结合ORA-19809+RMAN DELETE综合）、综合2题（生产备份策略设计+RMAN脚本完整编写、严重误操作DROP TABLESPACE完整恢复演练含三种方案对比）。答案折叠于details块，配套知识点见各题后链接。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | NOARCHIVELOG模式可用备份方式 | 概念理解 |
| 单2 | 单选 | BEGIN BACKUP期间Oracle专有的Whole Block Image机制 | 概念理解 |
| 单3 | 单选 | NOCATALOG模式必须开启的CONFIGURATION | 概念理解 |
| 单4 | 单选 | RMAN BACKUP DATABASE PLUS ARCHIVELOG 执行顺序 | 概念辨析 |
| 单5 | 单选 | 非SYSTEM表空间损坏的恢复策略 | 概念辨析 |
| 单6 | 单选 | OPEN RESETLOGS后必须立即做什么 | 概念辨析 |
| 单7 | 单选 | 误DROP TABLE且DROP时未加PURGE的首选恢复方案 | 综合应用 |
| 单8 | 单选 | Flashback Database的前提条件 | 概念理解 |
| 单9 | 单选 | Recover Table单表恢复(Oracle 12c+)适用场景 | 概念辨析 |
| 单10 | 单选 | RESTORE vs RECOVER两个命令的区别 | 概念理解 |
| 多1 | 多选 | 冷备份必须备份的文件 | 概念辨析 |
| 多2 | 多选 | RMAN Backup Set相对Image Copy的优势 | 概念辨析 |
| 多3 | 多选 | 不完全恢复的类型 | 概念辨析 |
| 多4 | 多选 | 完全恢复的特点 | 概念辨析 |
| 多5 | 多选 | Oracle七类闪回技术中底层依赖UNDO的 | 概念辨析 |
| 判1 | 判断 | 热备份必须在ARCHIVELOG模式下做 | 概念理解 |
| 判2 | 判断 | SHUTDOWN ABORT后直接做冷备份，备份仍然是一致性的 | 概念理解 |
| 判3 | 判断 | RMAN DELETE OBSOLETE只删RMAN元数据，不删物理文件 | 概念理解 |
| 判4 | 判断 | FLASHBACK TABLE前必须先对该表执行ALTER TABLE ... ENABLE ROW MOVEMENT | 概念理解 |
| 判5 | 判断 | OPEN RESETLOGS后旧归档旧备份都可以直接DELETE丢弃，不再需要保留 | 概念理解 |
| 简1 | 简答 | 冷备份 vs 热备份（UMB）：对比前提条件、步骤、优缺点、适用场景 | 分析说明 |
| 简2 | 简答 | RMAN备份 vs 用户管理备份UMB：至少5个维度对比 | 分析说明 |
| 简3 | 简答 | 不完全恢复（DBPITR）的黄金步骤，指出每一步中高风险操作及理由 | 分析说明 |
| 简4 | 简答 | 七类闪回技术选型判断：给定6类典型误操作场景，分别推荐对应闪回/恢复方案并说明理由 | 分析说明 |
| 分1 | 分析 | RMAN BACKUP脚本编写+关键配置 | 综合应用 |
| 分2 | 分析 | 非SYSTEM表空间损坏在线完全恢复SQL+RMAN全过程 | 综合应用 |
| 分3 | 分析 | 误操作场景闪回方案选择（3个小场景） | 综合应用 |
| 分4 | 分析 | ORA-19809 FRA空间满+备份恢复结合故障处理 | 综合应用 |
| 综1 | 综合 | 生产备份策略设计（全备+增量+归档+保留策略）+完整RMAN脚本+监控脚本 | 综合应用 |
| 综2 | 综合 | DROP TABLESPACE严重误操作三种恢复方案对比演练（闪回DB vs RMAN DBPITR vs TSPITR） | 综合应用 |

## 一、单选题（每题2分，共10题）

**1. 数据库运行在NOARCHIVELOG模式下，唯一可用的物理备份方式是（　）。**
A. 热备份（ALTER TABLESPACE ... BEGIN BACKUP）
B. 冷备份（SHUTDOWN IMMEDIATE后OS cp）
C. RMAN联机全备（BACKUP DATABASE PLUS ARCHIVELOG）
D. 以上都可以

**2. 执行 `ALTER TABLESPACE users BEGIN BACKUP` 时，Oracle专有的防块断裂机制是（　）。**
A. 暂停所有DML操作直到END BACKUP
B. 冻结数据文件头SCN，且首次修改的数据块写入**Whole Block Image完整块映像**到重做日志
C. 自动复制数据文件到备份目录
D. 自动将所有脏缓冲立即刷盘

**3. RMAN运行在NOCATALOG模式下，以下哪条CONFIGURATION必须强制开启？（　）**
A. CONFIGURE RETENTION POLICY TO NONE;
B. CONFIGURE CONTROLFILE AUTOBACKUP OFF;
C. CONFIGURE CONTROLFILE AUTOBACKUP ON;
D. CONFIGURE DEVICE TYPE DISK PARALLELISM 1;

**4. 关于 `BACKUP DATABASE PLUS ARCHIVELOG` 命令的执行顺序，下列正确的是（　）。**
A. 直接备份数据文件→备份归档→结束
B. ALTER SYSTEM SWITCH LOGFILE→备份所有归档→备份数据文件→再次SWITCH→备份新产生归档→备份控制文件+SPFILE
C. 只备份数据文件，不备份归档
D. 只备份归档，不备份数据文件

**5. 生产数据库中，USERS表空间（非SYSTEM、非UNDO）的某个数据文件磁盘物理损坏，数据库仍OPEN但访问USERS报错。最佳恢复策略是（　）。**
A. 立即SHUTDOWN ABORT，整库RESTORE+RECOVER
B. 保持数据库OPEN状态：ALTER DATABASE DATAFILE ... OFFLINE → RESTORE DATAFILE → RECOVER DATAFILE → ONLINE
C. 先DROP TABLESPACE users再重建
D. 执行FLASHBACK DATABASE回到损坏前时刻

**6. 执行 `ALTER DATABASE OPEN RESETLOGS` 成功后，下一步必须立刻做什么？（　）**
A. 什么都不做，让用户继续使用
B. 立即全库备份（RMAN> BACKUP AS COMPRESSED BACKUPSET DATABASE PLUS ARCHIVELOG;）
C. 删除所有旧归档文件
D. 重建控制文件

**7. 9:05执行了`DROP TABLE HR.SALARY`（没有加PURGE），9:06发现错误立即求助DBA。数据库版本19c，默认参数配置。首选且最快的恢复方案是（　）。**
A. 闪回数据库 FLASHBACK DATABASE TO TIMESTAMP ...
B. 闪回回收站 FLASHBACK TABLE hr.salary TO BEFORE DROP;
C. RMAN不完全恢复UNTIL TIME 9:04:59
D. RMAN RECOVER TABLE hr.salary UNTIL TIME ...（单表PITR）

**8. 使用 Flashback Database 的前提条件不包括（　）。**
A. 数据库处于ARCHIVELOG模式
B. 已配置FRA闪回恢复区（DB_RECOVERY_FILE_DEST+SIZE）
C. 执行过 `ALTER DATABASE FLASHBACK ON;`（MOUNT状态下）
D. RECYCLEBIN参数必须为ON

**9. Oracle 12c+的`RMAN> RECOVER TABLE ... UNTIL ... AUXILIARY DESTINATION`单表时间点恢复，相比传统DBPITR不完全恢复的最大优势是（　）。**
A. 不需要备份，直接从UNDO恢复
B. 恢复时不需要ARCHIVELOG模式
C. **不影响其他表/业务，数据库不重启**（内部创建临时辅助实例只恢复该表，再导回主库）
D. 恢复速度比Flashback Drop回收站还快

**10. 关于RMAN的RESTORE和RECOVER两个命令的区别，下列说法正确的是（　）。**
A. 两者完全等价，可以互换
B. RESTORE=从备份拷贝数据文件回磁盘；RECOVER=应用归档+在线重做推进SCN到指定点
C. RESTORE=应用重做；RECOVER=拷贝备份
D. RESTORE只用于冷备恢复；RECOVER只用于热备恢复

## 二、多选题（每题3分，共5题）

**1. 做冷备份时，下列哪些文件必须一起备份？（　）**
A. 所有数据文件（V$DATAFILE）
B. 所有控制文件多路复用成员（V$CONTROLFILE）
C. 所有联机重做日志成员（V$LOGFILE）
D. SPFILE或PFILE
E. 密码文件（orapw<sid>）

**2. 相比Image Copy镜像副本，RMAN Backup Set备份集的优势包括（　）。**
A. 自动跳过从未使用的数据块（空块不备份），备份集体积远小于原文件
B. 支持RMAN内置压缩算法，体积进一步减小
C. 写时自动做Oracle逻辑块校验，坏块自动标记
D. 多个数据文件块可合并存到同一备份片段，便于管理
E. 可执行SWITCH DATABASE TO COPY即时切换，不需要拷贝

**3. Oracle RMAN不完全恢复的类型包括（　）。**
A. UNTIL TIME：基于时间点
B. UNTIL SCN：基于系统改变号（最精确）
C. UNTIL SEQUENCE n THREAD t：基于日志序列号
D. UNTIL CANCEL：基于CANCEL取消
E. UNTIL CHECKPOINT：基于检查点编号

**4. 关于完全恢复，下列说法正确的是（　）。**
A. 应用所有可用归档日志+在线重做日志，不丢失任何已提交事务
B. 完成后用普通ALTER DATABASE OPEN;打开，不需要OPEN RESETLOGS
C. 日志序列号继续递增，不产生新Incarnation
D. 非SYSTEM/UNDO表空间损坏时可在数据库OPEN状态下OFFLINE→RESTORE→RECOVER→ONLINE
E. 即使丢失某段归档日志也能完成

**5. 下列Oracle七类闪回技术中，底层依赖UNDO表空间（而非FRA/闪回日志/回收站）的有（　）。**
A. Flashback Query（AS OF TIMESTAMP/SCN）
B. Flashback Version Query（VERSIONS BETWEEN）
C. Flashback Transaction Query（FLASHBACK_TRANSACTION_QUERY）
D. Flashback Table（闪回表）
E. Flashback Database（闪回数据库）
F. Flashback Drop（回收站）

## 三、判断题（每题2分，共5题）

**1. 执行用户管理的热备份（BEGIN BACKUP / END BACKUP）必须在ARCHIVELOG模式下，否则无法通过归档把不一致备份恢复成一致。**

**2. 用`SHUTDOWN ABORT`关库后直接做OS cp物理文件，得到的备份仍然是一致性备份。**

**3. RMAN命令`DELETE OBSOLETE`只删除RMAN存储库中的备份记录（元数据），不删除备份集物理文件。**

**4. 执行`FLASHBACK TABLE ... TO TIMESTAMP`之前，必须先执行`ALTER TABLE <表名> ENABLE ROW MOVEMENT;`，否则报错ORA-08189。**

**5. 执行`ALTER DATABASE OPEN RESETLOGS`之后，所有旧归档日志和旧备份文件都可以直接物理删除，绝对不会有任何潜在恢复风险。**

## 四、简答题（每题5分，共4题）

**1. 对比冷备份（Offline Cold Backup）与热备份（Online Hot Backup / UMB）：从前提模式、操作步骤、备份一致性、恢复时是否需重做、业务停机时间、优缺点、适用场景7个维度做对比表。**

**2. 对比RMAN备份工具与用户管理备份（UMB，OS cp + BEGIN/END BACKUP）：至少5个维度（空块处理、块校验、增量备份、压缩、自动化程度、保留策略与过期自动管理、恢复易用性、备份加密等至少选5项），说明为什么生产环境默认用RMAN。**

**3. 写出RMAN不完全恢复（DBPITR）的完整黄金步骤，明确标注> [!danger] 高风险操作（至少3处），并解释每一步的必要性。**

**4. 七类闪回技术+RMAN恢复选型。给定6类误操作场景，分别推荐最优恢复方案并简述理由：**
- ①场景A：9:50误`UPDATE ... WHERE`误COMMIT，需要查看9:49的正确数据核对
- ②场景B：9:55误`DROP TABLE HR.TEST1 PURGE;`（加了PURGE绕过回收站）
- ③场景C：9:58误`TRUNCATE TABLE HR.BIG_DATA;`（大表，回收站对TRUNCATE无效）
- ④场景D：10:00误`DROP TABLESPACE TBS_APP INCLUDING CONTENTS AND DATAFILES;`（删除了整个业务表空间及数据文件），但FLASHBACK ON已开启，5分钟内发现
- ⑤场景E：审计要求查询某员工7年前（2017年）的薪资记录，UNDO只保留24小时
- ⑥场景F：系统打补丁升级后业务异常，要求10分钟内回到升级前状态，升级前做过Guaranteed Restore Point

## 五、分析题（每题8分，共4题，需给出完整SQL/RMAN）

**1. RMAN备份脚本编写。** 场景：Oracle 19c生产单实例数据库ORCL，要求编写每周日晚22:00执行的**增量0级全备**RMAN脚本。要求：①并行度2，磁盘通道格式`/backup/rman/orcl/%d_L0_%Y%M%D_%s_%p.bak`；②采用压缩备份集；③`BACKUP DATABASE PLUS ARCHIVELOG DELETE ALL INPUT`（备完归档删除输入）；④额外单独备份控制文件到`/backup/rman/orcl/ctl_%F.bak`和SPFILE；⑤开启备份优化；⑥作业执行完成后执行`CROSSCHECK`+`DELETE OBSOLETE NOPROMPT`自动清理过期；⑦日志输出到`/backup/rman/log/L0_$(date +%Y%M%D).log`。

**2. 非SYSTEM表空间在线完全恢复。** 场景：应用报错`ORA-01115: IO error reading block from file 6`，V$DATAFILE显示6号文件属于`TBS_SALE`销售表空间（非SYSTEM、非UNDO），数据库仍OPEN中。请写出：(1)完整的恢复流程说明（是否需关库）；(2)每个步骤对应的SQL/RMAN命令；(3)非SYSTEM表空间在线恢复的优势。

**3. 误操作闪回方案三小场景：**
- (a) 场景1：`UPDATE hr.employees SET salary=salary*1.1 WHERE department_id=80;` COMMIT后发现应该是10%下调不是上涨。要求把80号部门员工工资恢复到UPDATE前（9:30之前）。写出SQL，标明所需前提和高风险提示。
- (b) 场景2：`TRUNCATE TABLE hr.job_history;` COMMIT后无法撤销。数据库版本19c，已启用FLASHBACK ON（保留目标内）。写出恢复方案（两种），对比优缺点。
- (c) 场景3：需要追查是谁（数据库用户+操作系统用户）、在什么时间，把`HR.COUNTRIES`表中某一行从'CHINA'改成了'CN'，并生成反向修复SQL。写出版本查询+事务查询的完整SQL链。

**4. ORA-19809 FRA空间满故障处理：** 上午10:30告警：`ORA-19815: WARNING: db_recovery_file_dest_size of 209715200000 bytes is 99.00% used`，业务侧归档卡住。RMAN保留策略是`RECOVERY WINDOW OF 30 DAYS`。查询：
```
SPACE_LIMIT=200G, SPACE_USED=198G, SPACE_RECLAIMABLE=60G,
V$FLASH_RECOVERY_AREA_USAGE中 ARCHIVED LOG占80%。
```
请给出：(1)按紧急到长期的3步处理方案（含具体SQL/RMAN命令）；(2)解释为何`SPACE_RECLAIMABLE`有60G还告警；(3)1周/1个月的预防措施。

## 六、综合题（每题10分，共2题）

**1. 生产备份策略完整设计。** 要求：24×7核心交易库（Oracle 19c RAC单节点=简化版），业务重做量峰值约50GB/天。合规要求可恢复到最近30天内任意时间点，备份本地磁盘保留30天，30天外备份到磁带。RMAN NOCATALOG模式，已配置FRA=500G（归档放FRA）。请设计：
- (1) **备份策略组合**：全备/增量/归档的频率、级别（0级/1级累计/1级差异），并画图说明各备份之间的关系（周日晚上是什么、周一到周六晚上是什么、归档的备份频率）。
- (2) **RMAN持久化配置**（CONFIGURE全部必要配置，控制文件自动备份格式，保留策略，通道默认并行度，归档删除策略为「备磁带1次后可删本地」）。
- (3) **3个关键RMAN脚本**：①周日L0全备、②周中L1累计/差异增量备、③每小时归档备。要求：run块结构，通道分配，FORMAT符，完成后CROSSCHECK+DELETE OBSOLETE。
- (4) **日常监控脚本**（SQL*Plus）：①FRA使用率阈值>85%告警；②RMAN近7天备份作业成功率（V$RMAN_BACKUP_JOB_DETAILS）；③归档目的地ERROR状态检查。

**2. 严重误操作DROP TABLESPACE三方案对比演练。** 场景：15:05 DBA误执行`DROP TABLESPACE TBS_FIN INCLUDING CONTENTS AND DATAFILES;`（删除了财务核心表空间）。15:07发现。备份：昨晚22:00有RMAN L0全备，之后归档齐全。数据库：19c ARCHIVELOG，FLASHBACK ON，TBS_FIN是普通TBS（非SYSTEM/UNDO/SYSAUX）。请给出三种方案的对比+完整步骤命令：
- 方案A：**Flashback Database**整库回退到15:04（前提：FLASHBACK ON保留窗口≥7分钟）。写出完整命令步骤。对业务的影响？（所有表空间15:04~15:07之间已提交的其他表业务变更会怎么样？）
- 方案B：**RMAN Tablespace Point-in-Time Recovery (TSPITR)**（表空间级时间点恢复，只回退TBS_FIN）。写出命令：`RECOVER TABLESPACE tbs_fin UNTIL TIME '...' AUXILIARY DESTINATION '...';`。优点？（只影响财务表空间，其他业务不变）前提？（TSPITR的自包含检查：`SYS.TS_PITR_CHECK`）
- 方案C：**传统整库DBPITR不完全恢复**。> [!danger] 先备份当前故障态文件→STARTUP MOUNT→UNTIL TIME 15:04:59→RESTORE DATABASE→RECOVER DATABASE→OPEN RESETLOGS→立即全备。对比三方案的：业务停机时间、业务影响范围（仅财务表空间/整库）、恢复速度、对操作人员的技术要求、风险等级。

## 答案与解析

<details>
<summary>单选题答案与解析</summary>

1. **B**。NOARCHIVELOG只能做冷备，热备和RMAN联机备都依赖归档恢复不一致备份，NOARCHIVELOG无归档无法恢复，会报检查点SCN不一致。
2. **B**。BEGIN BACKUP期间Oracle专有动作：冻结文件头SCN（备份起点一致）+首次修改块Whole Block Image写重做（防OS cp拆分读造成的Fractured Block断裂块）。A错，DML照常；C不自动复制；D不刷盘。
3. **C**。必须`CONTROLFILE AUTOBACKUP ON`——NOCATALOG所有元数据只在控制文件，控制文件没自动备份则全丢了，RMAN恢复瘫痪。
4. **B**。PLUS ARCHIVELOG执行顺序：切归档→备全部旧归档→备数据文件→切新归档→备期间新产生归档→自动备控制文件+SPFILE。确保备份前后的归档都齐，可直接RESTORE+RECOVER到一致性状态。
5. **B**。非核心非SYSTEM表空间，保持数据库OPEN做OFFLINE→RESTORE→RECOVER→ONLINE，最小化业务影响（DBA核心最佳实践）。A整库恢复影响太大；C重建TBS会丢数据；D Flashback Database会影响所有表空间。
6. **B**。> [!danger] OPEN RESETLOGS后旧备份/归档对新Incarnation基本失效。必须立即做新化身下的首次全备，否则新化身之后发生故障将无可用备份。A不做备份风险极大；C旧归档在跨Incarnation恢复时还可能用到，不能乱删；D控制文件已存在不用重建。
7. **B**。Flashback Drop回收站秒级还原DROP的表（且未加PURGE时默认进回收站），最快最无业务影响。A闪回数据库会影响所有业务表；C RMAN DBPITR停机数小时；D单表PITR比回收站慢。
8. **D**。RECYCLEBIN是Flashback Drop的前提，不是Flashback Database的。ABC都是必需前提：ARCHIVELOG模式、FRA已配置、MOUNT下开启FLASHBACK ON。
9. **C**。单表PITR只恢复目标表，内部创建临时辅助实例还原SYSTEM/UNDO/SYSAUX+目标表空间，应用重做后Data Pump把表导回主库。主库全程OPEN，其他业务完全不受影响。这是12c+最重要的恢复增强。
10. **B**。RESTORE=还原备份文件到磁盘；RECOVER=应用重做（归档+在线）推进SCN。这是Oracle备份恢复的核心两阶段命令。

</details>

<details>
<summary>多选题答案与解析</summary>

1. **ABCDE**。冷备要备份：①所有数据文件、②所有控制文件成员、③所有在线重做日志、④SPFILE/PFILE（否则重启没参数）、⑤密码文件（否则本地OS认证之外的远程登录失败，虽不是核心数据库文件但建议一并）。
2. **ABCD**。Backup Set的优势：空块跳过(A)+压缩(B)+块校验(C)+多文件合并(D)。E是Image Copy镜像副本的独有优势：SWITCH DATABASE TO COPY可立即切换，不需要再拷贝一次（秒级）。
3. **ABCD**。四类不完全恢复：UNTIL TIME / UNTIL SCN / UNTIL SEQUENCE / UNTIL CANCEL。UNTIL CHECKPOINT不是RMAN支持的UNTIL类型。
4. **ABCD**。完全恢复四正确：A不丢任何提交事务；B普通OPEN不需要RESETLOGS；C不产生新Incarnation；D非SYSTEM TBS可在线OFFLINE恢复。E错误：缺归档无法完全恢复，只能退化成不完全恢复到缺失归档前。
5. **ABCD**。依赖UNDO的四个（查询/版本查询/事务查询/闪回表都是用UNDO前像重建历史版本）。E Flashback Database依赖FRA里的闪回日志Flashback Logs；F Flashback Drop依赖RECYCLEBIN逻辑段，与UNDO无关。

</details>

<details>
<summary>判断题答案与解析</summary>

1. **√**。热备是不一致备份（不同文件SCN不同），必须用归档日志把各文件SCN同步才能OPEN。NOARCHIVELOG无归档做不了，因此只能ARCHIVELOG模式下做热备。
2. **×**。SHUTDOWN ABORT等价于断电，数据库是「不一致的」：部分已提交事务还在SGA没写入数据文件，部分未提交事务的脏缓冲可能已写入。此时cp出来的是不一致副本——要一致必须SHUTDOWN IMMEDIATE/NORMAL/TRANSACTIONAL（这三个都是一致性关闭，SMON/DBWn会把缓冲刷盘，所有文件SCN一致）。
3. **×**。RMAN的DELETE系列命令（DELETE OBSOLETE/EXPIRED/BACKUPSET/ARCHIVELOG等）是**同时删除物理文件+更新RMAN元数据**。这正是DBA应该用RMAN DELETE而非OS rm的原因——rm只删文件不更元数据，RMAN DELETE两者同时做保持一致。
4. **√**。`ALTER TABLE ... ENABLE ROW MOVEMENT`是FLASHBACK TABLE的前置条件。闪回表会修改行的物理ROWID（逻辑回退表相当于DELETE旧行+INSERT新行），必须先允许行移动，否则报ORA-08189: cannot flashback the table because row movement is not enabled。
5. **×**。> [!danger] 旧备份/归档在「跨Incarnation恢复」或「OPEN RESETLOGS之后发现又想退回旧化身」时仍可能用得到。Oracle 10g+支持`RESET DATABASE TO INCARNATION <旧化身号>`在RMAN中切回旧化身，用旧备份+旧归档恢复。直接OS rm旧归档=堵死了这条退路。正确做法：按保留策略保留旧归档/旧备份到过期，用RMAN DELETE OBSOLETE安全删除。

</details>

<details>
<summary>简答题答案</summary>

**1. 冷备 vs 热备（UMB）七维对比表：**
| 维度 | 冷备份 Cold Backup | 热备份 Hot Backup (UMB) |
| ---- | ---- | ---- |
| 前提模式 | NOARCHIVELOG也可 / ARCHIVELOG也可 | 必须ARCHIVELOG（否则不一致备份无法恢复） |
| 操作步骤 | SHUTDOWN IMMEDIATE → OS cp所有数据/控制/日志文件/SPFILE → STARTUP | ALTER TABLESPACE ... BEGIN BACKUP → OS cp数据文件 → ALTER TABLESPACE ... END BACKUP；可ALTER DATABASE BEGIN/END BACKUP全库；额外BACKUP CONTROLFILE |
| 备份一致性 | 一致性备份（所有文件SCN一致，SHUTDOWN IMMEDIATE刷盘） | 不一致备份（备份中数据文件SCN不同，需要归档同步） |
| 恢复需重做？ | 不需要，拷回去直接OPEN | 必须，应用BEGIN到END期间+之后所有归档重做才能OPEN |
| 业务停机 | 需要，冷备期间数据库不可用 | 零停机，DML照常（会多产生Whole Block Image归档量增大） |
| 优点 | 简单直观、一致、开箱即用 | 零停机、24×7可用 |
| 缺点 | 必须停机、无法恢复到备份之后点（NOARCHIVELOG时）、TB级拷贝时间太长 | 产生大量额外重做/归档、BEGIN/END管理麻烦易错、OS cp整个文件空块也备份 |
| 适用场景 | NOARCHIVELOG模式下的唯一选择；小型测试库夜间窗口停机备份 | 生产24×7核心数据库（现主流用RMAN联机备替代手工UMB） |

参见[[8.1 备份分类：冷备份、热备份]]。

**2. RMAN vs UMB 至少5维对比：**
| 维度 | 用户管理备份UMB | RMAN工具 |
| ---- | ---- | ---- |
| 空块处理 | OS cp整个文件，空块全备份，占用空间大 | 备份集Backup Set自动跳过从未使用的空块，体积小 |
| 块校验 | OS不校验Oracle块损坏，坏块也被备份走 | 每个块自动做逻辑一致性校验，自动标记坏块并报告（V$DATABASE_BLOCK_CORRUPTION） |
| 增量备份 | 无法增量，每次全文件cp | 支持0级+1级累计/1级差异增量，节省90%以上备份时间和空间 |
| 压缩 | 只能OS层gzip/bzip2，额外步骤慢 | 内置AS COMPRESSED BACKUPSET压缩算法，比gzip快且率更高 |
| 自动化程度 | DBA手写BEGIN/END+cp脚本，易漏易忘 | 单条BACKUP DATABASE PLUS ARCHIVELOG自动切归档+备归档+备文件+备ctl+备spfile，一条龙 |
| 保留策略/过期管理 | DBA手动管理备份目录，写find mtime脚本删旧文件 | CONFIGURE RETENTION POLICY TO RECOVERY WINDOW / REDUNDANCY，REPORT OBSOLETE + DELETE OBSOLETE自动识别过期并删除 |
| 恢复易用性 | DBA手动RESTORE每个文件+手动RECOVER步骤，易出错 | 单条RESTORE DATABASE + RECOVER DATABASE自动选备份链、自动找齐需要的归档，大幅降低误操作风险 |
| 备份加密 | OS层额外加密工具 | 11g+透明数据加密TDE + 备份集加密，集成度高 |

生产默认选RMAN的原因：RMAN在几乎所有维度都优于UMB，且是Oracle官方持续增强的工具，从9i到23c每个版本都有重大新特性（12c的RECOVER TABLE，18c的ML自动恢复建议等），UMB只是兼容模式保留。

**3. 不完全恢复（DBPITR）黄金步骤：**
> [!danger] 高风险操作1（步骤0）：先备份当前故障态下的所有数据文件/控制文件/在线重做/归档到安全目录。一旦误判恢复时间点，可退回重来。没有这步就是不可逆操作。
1. **前置保护备份**：OS级复制所有$ORACLE_BASE/oradata下的数据文件、控制文件、在线日志、FRA下归档、SPFILE等。
2. **SHUTDOWN ABORT; STARTUP MOUNT;**（OPEN态下不能RESTORE DATABASE，必须MOUNT）。
3. **RUN块中SET UNTIL**：根据误操作发生时刻，`SET UNTIL TIME` 或 `SET UNTIL SCN`（推荐SCN最精确）。
4. **RESTORE DATABASE;** → 还原最近备份到磁盘。
5. **RECOVER DATABASE;** → 自动应用归档重做，直到UNTIL指定点停止。
> [!danger] 高风险操作2（步骤6）：ALTER DATABASE OPEN RESETLOGS; 执行后产生新Incarnation，旧备份/归档在新化身下大部分无法直接使用，且该操作不可逆。
6. **ALTER DATABASE OPEN RESETLOGS;** → 必须RESETLOGS，因为不完全恢复后日志序列号从1重新开始，新分支Incarnation生成。
> [!danger] 高风险操作3（步骤7）：OPEN RESETLOGS后立即全新全备。不做的话，新化身下后续任何故障发生都将无备份可用——> 这是DBA常犯错误之一，必须强制执行。
7. **立即全备**：`BACKUP AS COMPRESSED BACKUPSET DATABASE PLUS ARCHIVELOG DELETE ALL INPUT; BACKUP CURRENT CONTROLFILE; BACKUP SPFILE;`。
8. **验证**：SQL查询表/数据是否到达预期状态，`SELECT ... AS OF`对比。

**4. 6类场景闪回选型：**
- ①场景A → Flashback Query：`SELECT * FROM hr.employees AS OF TIMESTAMP ... WHERE department_id=80;`。只需要查过去的正确值，不用恢复表。
- ②场景B → RMAN单表PITR（12c+）：`RECOVER TABLE hr.test1 UNTIL TIME ... AUXILIARY DESTINATION ...;`。PURGE绕过了回收站，Flashback Drop不行；整库DBPITR影响大；Flashback Database影响全库。单表PITR只影响TEST1表，其他业务不受影响。
- ③场景C → 方案一Flashback Database（只要闪回窗口覆盖，分钟级整库回退到TRUNCATE前）；方案二RMAN单表PITR（只恢复BIG_DATA表不影响其他，12c+）。两个方案二选一，根据是否开启Flashback ON决定优先级。
- ④场景D → 方案一 Flashback Database（分钟级回退整库）。方案二 TSPITR表空间时间点恢复：`RECOVER TABLESPACE tbs_app UNTIL TIME ... AUXILIARY DESTINATION ...;`只回退应用表空间不影响其他。
- ⑤场景E → Flashback Data Archive（FDA）：UNDO只保留24小时，但FDA把历史版本写入独立归档表空间，保留7年+。`SELECT * FROM hr.payroll AS OF TIMESTAMP ADD_MONTHS(SYSDATE, -84) WHERE emp_id=...;`（前提是7年前就给这个表启用了FDA，否则无解只能磁带备份恢复）。
- ⑥场景F → Flashback Database + Guaranteed Restore Point：`FLASHBACK DATABASE TO RESTORE POINT before_upgrade_2024xx;`。GRP强制保留了闪回日志不会被FRA压力删除，10分钟内可完成整库回退到升级前，完美匹配「升级补丁前的兜底快照」场景。

</details>

<details>
<summary>分析题答案与SQL/RMAN</summary>

**1. L0全备脚本。**
Shell脚本`/home/oracle/scripts/rman_L0.sh`：
```bash
#!/bin/bash
export ORACLE_SID=ORCL
export ORACLE_HOME=/u01/app/oracle/product/19.0.0/dbhome_1
export PATH=$ORACLE_HOME/bin:$PATH
export BACKUP_DIR=/backup/rman/orcl
export LOG_DIR=/backup/rman/log
export DATE=$(date +%Y%m%d)
mkdir -p $BACKUP_DIR $LOG_DIR

rman target / log=${LOG_DIR}/L0_${DATE}.log <<EOF
CONFIGURE BACKUP OPTIMIZATION ON;
RUN {
  ALLOCATE CHANNEL c1 TYPE DISK FORMAT '${BACKUP_DIR}/ORCL_L0_${DATE}_%s_%p.bak';
  ALLOCATE CHANNEL c2 TYPE DISK FORMAT '${BACKUP_DIR}/ORCL_L0_${DATE}_%s_%p.bak';
  CONFIGURE DEVICE TYPE DISK PARALLELISM 2 BACKUP TYPE TO COMPRESSED BACKUPSET;
  BACKUP AS COMPRESSED BACKUPSET DATABASE PLUS ARCHIVELOG DELETE ALL INPUT;
  BACKUP CURRENT CONTROLFILE FORMAT '${BACKUP_DIR}/ctl_%F.bak';
  BACKUP SPFILE FORMAT '${BACKUP_DIR}/spfile_%U.bak';
  RELEASE CHANNEL c1;
  RELEASE CHANNEL c2;
}
CROSSCHECK BACKUP;
CROSSCHECK ARCHIVELOG ALL;
DELETE NOPROMPT OBSOLETE;
LIST BACKUP SUMMARY;
REPORT NEED BACKUP;
EXIT;
EOF
```
crontab调度：
```bash
# 每周日22:00执行
00 22 * * 0 /home/oracle/scripts/rman_L0.sh >> /home/oracle/scripts/rman_L0_cron.log 2>&1
```
> [!danger] 风险提示：DELETE OBSOLETE在脚本中加了NOPROMPT自动删除，需先手动`REPORT OBSOLETE`确认删除列表符合保留策略，再正式启用自动删除。

**2. 非SYSTEM表空间USERS（文件6）损坏在线完全恢复：**
(1) 不需要关库。保持数据库OPEN状态，仅OFFLINE损坏文件，用户继续访问其他业务。
(2) 完整步骤：
```sql
-- SQL*Plus / as sysdba
-- 步骤1：定位损坏文件
SELECT file#, name, status, enabled, checkpoint_change#
FROM   v$datafile WHERE file# = 6;
SELECT t.name tablespace_name, d.file#, d.name
FROM   v$tablespace t JOIN v$datafile d ON t.ts# = d.ts#
WHERE  d.file# = 6; -- 确认是 TBS_SALE

-- 步骤2：仅将损坏数据文件OFFLINE（不能OFFLINE整个数据库！）
ALTER DATABASE DATAFILE 6 OFFLINE;
-- 或ALTER TABLESPACE tbs_sale OFFLINE IMMEDIATE;（如果整个TBS都要恢复）

-- RMAN终端执行：
RMAN> RESTORE DATAFILE 6;
RMAN> RECOVER DATAFILE 6;
-- 可选：RESTORE TABLESPACE tbs_sale; RECOVER TABLESPACE tbs_sale;

-- SQL*Plus中重新ONLINE：
ALTER DATABASE DATAFILE 6 ONLINE;
-- 或ALTER TABLESPACE tbs_sale ONLINE;
```
(3) 在线恢复优势：①零业务停机，其他所有表空间/业务照常运行；②恢复粒度细，只动TBS_SALE的文件；③对24×7核心系统是最佳实践，把DBA操作的业务影响降到最低。

**3. 三个闪回小场景：**
(a) 80号部门工资误上调恢复：
> [!warning] 前提1：UNDO_RETENTION足够覆盖9:30到现在；否则ORA-01555快照过旧。
> [!danger] 高风险：操作前先备份EMP当前状态（CTAS）防再犯：`CREATE TABLE hr.emp_before_202401151000 AS SELECT * FROM hr.employees;`
```sql
-- SQL*Plus
ALTER TABLE hr.employees ENABLE ROW MOVEMENT;

-- 方法1：闪回表整表回到9:29:59（如果80号部门之外的其他部门9:30-9:50没有更新）
FLASHBACK TABLE hr.employees TO TIMESTAMP
  TO_TIMESTAMP('2024-01-15 09:29:59','YYYY-MM-DD HH24:MI:SS');

-- 方法2（更安全，仅修80号部门，不影响其他部门）：
MERGE INTO hr.employees e
USING (SELECT * FROM hr.employees AS OF TIMESTAMP
         TO_TIMESTAMP('2024-01-15 09:29:59','YYYY-MM-DD HH24:MI:SS')
       WHERE department_id = 80) old_e
ON (e.employee_id = old_e.employee_id)
WHEN MATCHED THEN UPDATE SET e.salary = old_e.salary;
COMMIT;
ALTER TABLE hr.employees DISABLE ROW MOVEMENT;
```
方法2只修80号部门，不会误撤销其他部门在这20分钟内的其他合法更新，生产更推荐。

(b) TRUNCATE HR.JOB_HISTORY两方案：
方案一：Flashback Database（前提：FLASHBACK ON，窗口覆盖10分钟内）。
```sql
SHUTDOWN IMMEDIATE; STARTUP MOUNT;
FLASHBACK DATABASE TO TIMESTAMP TO_TIMESTAMP('2024-01-15 09:57:59', 'YYYY-MM-DD HH24:MI:SS');
ALTER DATABASE OPEN READ ONLY; -- 验证
SHUTDOWN IMMEDIATE; STARTUP MOUNT;
ALTER DATABASE OPEN RESETLOGS;
BACKUP DATABASE PLUS ARCHIVELOG; -- 立即全备> [!danger]
```
优点：恢复速度快（分钟级）。缺点：**整库回退，9:58之后所有其他业务表的合法更新全部被撤销！**
方案二（推荐12c+）：RMAN单表PITR
```
RMAN> RECOVER TABLE hr.job_history
  UNTIL TIME "TO_DATE('2024-01-15 09:57:59','YYYY-MM-DD HH24:MI:SS')"
  AUXILIARY DESTINATION '/u02/rman_aux';
```
优点：只影响JOB_HISTORY表，其他表/业务完全不受影响，数据库不重启。操作复杂度低，风险小，优先选方案二。

(c) 追查行变更者+生成反向SQL：
```sql
-- 步骤1：版本查询找到该行变更的XID事务ID
SELECT versions_starttime, versions_endtime, versions_xid, versions_operation,
       country_id, country_name
FROM   hr.countries
       VERSIONS BETWEEN TIMESTAMP
         TO_TIMESTAMP('2024-01-15 08:00:00','YYYY-MM-DD HH24:MI:SS')
         AND MAXVALUE
WHERE  country_id = 'CN';
-- 假设找到VERSIONS_XID = 0A000F0089030000，OPERATION=U（UPDATE），NAME从'CHINA'→'CN'

-- 步骤2：事务查询查到谁干的+生成反向UNDO_SQL
SELECT xid, start_scn, commit_scn, commit_timestamp,
       logon_user, os_user_name, machine_name,
       operation, undo_sql
FROM   flashback_transaction_query
WHERE  xid = HEXTORAW('0A000F0089030000')
ORDER  BY undo_sql;
```
结果中`os_user_name`=Windows/Linux登录OS账号，`logon_user`=数据库账号，`undo_sql`=反向UPDATE SQL直接复制执行即可修复该行。

**4. ORA-19809 FRA空间满三步处理：**
(1) 处理方案（紧急→短期→长期）：
①**紧急方案（立即释放空间）**：扩容FRA大小上限。
```sql
ALTER SYSTEM SET DB_RECOVERY_FILE_DEST_SIZE='400G' SCOPE=BOTH;
```
> 这是最快的方式，无需删备份，立即解除告警，给DBA留时间做清理。
②**短期方案（按保留策略删过期）**：
```
RMAN> CROSSCHECK BACKUP;
RMAN> CROSSCHECK ARCHIVELOG ALL;
RMAN> REPORT OBSOLETE;  -- 预演看一下会删什么
RMAN> DELETE NOPROMPT OBSOLETE;
```
> [!danger]  REPORT必须先看，确认过期列表匹配30天恢复窗口预期。
③**长期方案（架构优化）**：把30天前的归档/备份备份到磁带后删本地，缓解FRA压力。归档本地保留7天，磁带保留3年。RMAN配置：
```
CONFIGURE ARCHIVELOG DELETION POLICY TO BACKED UP 1 TIMES TO SBT_TAPE;
```
(2) 为何有SPACE_RECLAIMABLE但仍告警：SPACE_RECLAIMABLE是「理论上可回收空间」——RMAN根据保留策略判定这些备份/归档是OBSOLETE的，但Oracle不会自动删这些文件；必须DBA手动执行DELETE OBSOLETE才会真正从磁盘释放空间。
(3) 预防措施：
- 1周：部署监控告警脚本。①FRA>85%短信/邮件告警；②归档目的地ERROR状态每5分钟检查；③每天早上邮件RMAN备份作业报告LIST BACKUP SUMMARY。
- 1个月：做一次「RMAN恢复测试演练」，实际RESTORE+RECOVER到测试机确保备份可用。扩容磁盘，FRA建议设为数据库大小的1.5~3倍（视重做量而定）。

</details>

<details>
<summary>综合题答案与完整设计</summary>

**1. 生产备份策略设计：**
(1) **备份策略组合**：周日晚L0=增量0级（=全备基底）；周一~周六晚L1=差异增量（备份自昨晚以来变化）；每小时备份归档日志1次+删已备输入。画图说明：
```
周日22:00 [Incremental Level 0]
   |
周一22:00 [Level 1 Differential] ← 变化自周日晚
   |
周二22:00 [Level 1 Differential] ← 变化自周一晚
   |
...以此类推...
   |
周六22:00 [Level 1 Differential]
   |
周日22:00 新的Level 0开始新一轮

每小时整点: [Archive Log Backup + DELETE ALL INPUT]
```
**恢复时**：RESTORE最近周日L0 → RESTORE之后每天L1应用（差异） → 应用当天所有归档备 + 当前在线重做。恢复链短（最多7份备份+归档）。
*如果希望每天应用的增量更少，可以把周三晚改为Cumulative累计增量（备份自周日的所有变化）：周一差异+周二差异+周三累计+周四差异+周五差异+周六差异，恢复时只需0级→周三累计→周四差异→周五差异→周六差异（减少恢复时应用的备份数）。*

(2) **RMAN持久化配置**（一次配置永久生效）：
```
RMAN> CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 30 DAYS;
RMAN> CONFIGURE CONTROLFILE AUTOBACKUP ON;
RMAN> CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '/backup/rman/orcl/cf_%F';
RMAN> CONFIGURE DEFAULT DEVICE TYPE TO DISK;
RMAN> CONFIGURE DEVICE TYPE DISK PARALLELISM 2 BACKUP TYPE TO COMPRESSED BACKUPSET;
RMAN> CONFIGURE BACKUP OPTIMIZATION ON;
RMAN> CONFIGURE ARCHIVELOG DELETION POLICY TO BACKED UP 1 TIMES TO SBT_TAPE;
RMAN> SHOW ALL; -- 核对
```

(3) **三个关键RMAN脚本：**
①周日L0（复用分析题1脚本，此处精简）：
```bash
rman target / <<EOF
RUN {
  ALLOCATE CHANNEL c1 TYPE DISK FORMAT '/backup/rman/orcl/L0_%Y%M%D_%s_%p.bak';
  ALLOCATE CHANNEL c2 TYPE DISK FORMAT '/backup/rman/orcl/L0_%Y%M%D_%s_%p.bak';
  BACKUP INCREMENTAL LEVEL 0 AS COMPRESSED BACKUPSET DATABASE PLUS ARCHIVELOG DELETE ALL INPUT;
  BACKUP CURRENT CONTROLFILE FORMAT '/backup/rman/orcl/ctl_%F.bak';
  BACKUP SPFILE FORMAT '/backup/rman/orcl/spfile_%U.bak';
  RELEASE CHANNEL c1;
  RELEASE CHANNEL c2;
}
CROSSCHECK BACKUP; CROSSCHECK ARCHIVELOG ALL;
DELETE NOPROMPT OBSOLETE;
EXIT;
EOF
```
②周中L1差异（周一/二/四/五/六晚）：
```bash
rman target / <<EOF
RUN {
  ALLOCATE CHANNEL c1 TYPE DISK FORMAT '/backup/rman/orcl/L1_diff_%Y%M%D_%s_%p.bak';
  ALLOCATE CHANNEL c2 TYPE DISK FORMAT '/backup/rman/orcl/L1_diff_%Y%M%D_%s_%p.bak';
  BACKUP INCREMENTAL LEVEL 1 AS COMPRESSED BACKUPSET DATABASE PLUS ARCHIVELOG DELETE ALL INPUT;
  RELEASE CHANNEL c1; RELEASE CHANNEL c2;
}
CROSSCHECK BACKUP; CROSSCHECK ARCHIVELOG ALL;
DELETE NOPROMPT OBSOLETE;
EXIT;
EOF
```
*（周三晚改成累计增量：把 LEVEL 1 改为 LEVEL 1 CUMULATIVE）*
③每小时归档备（crontab每小时0分执行）：
```bash
rman target / <<EOF
RUN {
  ALLOCATE CHANNEL a1 TYPE DISK;
  BACKUP AS COMPRESSED BACKUPSET ARCHIVELOG ALL DELETE ALL INPUT;
  RELEASE CHANNEL a1;
}
EXIT;
EOF
```

(4) **日常监控脚本**：
```sql
-- ①FRA使用率（>85%告警）
SELECT round(space_used/space_limit*100,2) pct_used,
       round(space_reclaimable/space_limit*100,2) pct_reclaim
FROM   v$recovery_file_dest
WHERE  round(space_used/space_limit*100,2) > 85;

-- ②RMAN近7天备份作业状态（FAILED的要告警）
SELECT session_key, start_time, end_time, status,
       time_taken_display, compression_ratio,
       input_bytes_display, output_bytes_display
FROM   v$rman_backup_job_details
WHERE  start_time >= trunc(sysdate) - 7
ORDER  BY start_time DESC;

-- ③归档目的地ERROR状态检查
SELECT dest_id, status, destination, error
FROM   v$archive_dest
WHERE  dest_id <= 10 AND status <> 'VALID';
```

**2. DROP TABLESPACE TBS_FIN三方案对比演练：**
**方案A：Flashback Database**
(1) 前提：已启用ARCHIVELOG + FRA + `ALTER DATABASE FLASHBACK ON` + `DB_FLASHBACK_RETENTION_TARGET`≥7分钟 + 15:04的SCN在闪回窗口内。
(2) 步骤：
```sql
SHUTDOWN IMMEDIATE;  -- > [!danger] 先备份当前故障态所有文件防二次破坏！
STARTUP MOUNT EXCLUSIVE;
-- 先做READ ONLY验证，发现错了还能MOUNT再改
FLASHBACK DATABASE TO TIMESTAMP
  TO_TIMESTAMP('2024-01-15 15:04:00','YYYY-MM-DD HH24:MI:SS');
ALTER DATABASE OPEN READ ONLY;
SELECT count(*) FROM dba_tablespaces WHERE tablespace_name='TBS_FIN'; -- 应有TBS_FIN
-- 再验证财务表
SELECT count(*) FROM fin.gl_accounts; -- 正常
SHUTDOWN IMMEDIATE; STARTUP MOUNT;
ALTER DATABASE OPEN RESETLOGS; -- > [!danger] 新Incarnation
BACKUP AS COMPRESSED BACKUPSET DATABASE PLUS ARCHIVELOG; -- 立即全备> [!danger]
BACKUP CURRENT CONTROLFILE; BACKUP SPFILE;
```
(3) 业务影响：**15:04~15:07之间，除财务外的其他所有已提交业务变更（比如销售/HR模块）全部被回滚！这是最大痛点。**仅适用于全库在此期间几乎无业务的场景（例如凌晨维护窗口的误操作）。

**方案B：RMAN TSPITR表空间时间点恢复（推荐）**
(1) 前提：`SYS.TS_PITR_CHECK`通过（TBS_FIN自包含——其对象不依赖其他TBS中的对象，或依赖的UNDO/SYSTEM除外）。
```sql
-- 先做自包含检查
EXEC DBMS_TTS.TRANSPORT_SET_CHECK('TBS_FIN', TRUE);
SELECT * FROM transport_set_violations; -- 无行返回=自包含通过
```
(2) 步骤：
```
RMAN> RECOVER TABLESPACE tbs_fin
  UNTIL TIME "TO_DATE('2024-01-15 15:04:00','YYYY-MM-DD HH24:MI:SS')"
  AUXILIARY DESTINATION '/u02/rman_aux';
```
RMAN内部：自动创建辅助实例→还原SYSTEM/UNDO/SYSAUX/TBS_FIN→在辅助实例上UNTIL TIME 15:04做不完全恢复→把TBS_FIN通过传输表空间技术导回主库。**主库全程OPEN**。
(3) 优点：**只影响TBS_FIN财务表空间本身，其他所有业务表空间（SALES/HR/APP）15:04~15:07之间的合法业务变更完全不受影响，数据库不重启。** 这是24×7生产系统的最佳实践，优先选择。

**方案C：传统整库DBPITR不完全恢复（兜底）**
步骤同简答题3（不完全恢复黄金步骤）：①> [!danger] OS先备份当前故障态；②SHUTDOWN ABORT; STARTUP MOUNT; ③RUN块SET UNTIL TIME 15:04:59; ④RESTORE DATABASE; ⑤RECOVER DATABASE; ⑥> [!danger] ALTER DATABASE OPEN RESETLOGS; ⑦> [!danger] 立即全新全备。
业务影响同方案A：整库回退，15:04~15:07之间所有其他业务变更全部丢弃。

**三方案对比总结表：**
| 维度 | 方案A：Flashback Database | 方案B：TSPITR（推荐） | 方案C：传统DBPITR |
| ---- | ---- | ---- | ---- |
| 业务停机时间 | ~10~30分钟（MOUNT+FLASHBACK+RESETLOGS） | **~0停机**（数据库全程OPEN） | ~数小时（RESTORE+RECOVER TB级库） |
| 业务影响范围 | **全库回退**（其他业务15:04~15:07变化全丢） | **仅TBS_FIN回退**（其他业务100%保留） | 全库回退（同A） |
| 恢复速度 | 分钟级（最快的整库回退方案） | 小时级以内（只恢复单TBS） | 最慢（数小时） |
| 对DBA技术要求 | 中（熟悉Flashback命令+RESETLOGS流程） | 低（一条RECOVER TABLESPACE命令，RMAN全自动） | 高（必须严格按黄金步骤走，> [!danger] 一步错可能永久丢数据） |
| 风险等级 | 中（回退其他业务的风险高） | **低（只影响目标TBS）** | 极高（备份误删/UNTIL点选错/没备份故障态都可能不可逆） |
| 前提条件 | FLASHBACK ON启用+FRA足够 | TBS自包含通过 + 有L0备+归档齐全 | 有L0备+归档齐全 |

*生产结论：方案B（TSPITR）> 方案A > 方案C。有12c+的前提下用方案B最稳妥。*

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | NOARCHIVELOG备份方式、BEGIN BACKUP的Oracle专有机制、RMAN NOCATALOG必备配置、PLUS ARCHIVELOG执行顺序、非SYSTEM在线恢复、OPEN RESETLOGS后全备、DROP TABLE恢复优先级、Flashback Database前提、单表PITR、RESTORE vs RECOVER |
| 多选 | 5 | 15 | 冷备份文件清单、Backup Set优势、不完全恢复四类型、完全恢复四特点、依赖UNDO的四类闪回 |
| 判断 | 5 | 10 | 热备需ARCHIVELOG、ABORT关库后冷备一致性、RMAN DELETE删物理+元数据、闪回表需ROW MOVEMENT、旧归档乱删风险 |
| 简答 | 4 | 20 | 冷备vs热备七维对比、RMAN vs UMB至少五维对比、不完全恢复黄金步骤+三处danger标注、六类误操作闪回选型决策 |
| 分析 | 4 | 32 | L0全备RMAN脚本+crontab、非SYSTEM在线恢复完整SQL+优势、三类闪回小场景编程、FRA ORA-19809空间满三步处理+原因解释 |
| 综合 | 2 | 20 | 生产备份策略设计（L0/L1增量组合+配置+三脚本+监控）、DROP TABLESPACE三方案完整演练对比表（业务停机/影响范围/速度/风险/前提） |
| 合计 | 30 | 117 | 覆盖第8章全部核心考点，重RMAN命令编程与故障场景方案选型对比 |

## 章节导航

- 上级MOC：[[MOC - Oracle数据库管理]]
- 本章知识点：[[MOC - 第8章]]（[[8.1 备份分类：冷备份、热备份]]、[[8.2 RMAN工具基础使用]]、[[8.3 完全恢复与不完全恢复]]、[[8.4 闪回技术基础]]）
- 上一章习题：[[MOC - 第7章习题]]
- 下一章习题：[[MOC - 第9章习题]]
