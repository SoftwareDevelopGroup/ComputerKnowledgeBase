---
domain: 数据库技术
subject: Oracle数据库管理
type: exercise
chapter: 第4章 Oracle数据库启动与关闭
section: 4.7 习题MOC
tags: [Oracle,习题,DBA,启动模式,关闭模式,启动故障,参数文件,告警日志]
prerequisites: ["4.1 数据库四种启动模式", "4.2 正常关闭、立即关闭、事务关闭、中止关闭", "4.3 启动故障简单排查", "4.4 参数文件SPFILE与PFILE详解", "4.5 告警日志、跟踪文件与ADR自动诊断库"]
aliases: [MOC - 第4章习题]
---

# MOC - 第4章习题

> [!info] 习题说明
> 本习题集覆盖 [[MOC - 第4章]] 全部知识点，共30题，分六类：单选10、多选5、判断5、简答4、操作命令匹配5、故障分析1（综合启动故障完整排查）。重点考查四种启动模式阶段任务与可执行SQL、STARTUP参数FORCE/RESTRICT、四种关闭模式对比（尤其是IMMEDIATE vs ABORT的后果）、7类启动故障的ORA错误与解决方案对应、SPFILE与PFILE的修改规则与SCOPE、告警日志与ADR的定位。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | NOMOUNT阶段操作 | 概念理解 |
| 单2 | 单选 | MOUNT阶段可执行SQL | 概念理解 |
| 单3 | 单选 | STARTUP RESTRICT作用 | 概念理解 |
| 单4 | 单选 | V$INSTANCE.STATUS对应 | 概念理解 |
| 单5 | 单选 | SHUTDOWN NORMAL特点 | 概念理解 |
| 单6 | 单选 | SHUTDOWN ABORT后果 | 概念理解 |
| 单7 | 单选 | ORA-00205原因与处理 | 应用分析 |
| 单8 | 单选 | ORA-00257紧急处理 | 应用分析 |
| 单9 | 单选 | ALTER SYSTEM SCOPE=SPFILE | 概念理解 |
| 单10 | 单选 | 告警日志路径 | 概念理解 |
| 多1 | 多选 | NOMOUNT阶段可执行操作 | 概念辨析 |
| 多2 | 多选 | SHUTDOWN IMMEDIATE执行步骤 | 概念辨析 |
| 多3 | 多选 | ORA-01078/LRM-00109解决 | 概念辨析 |
| 多4 | 多选 | SPFILE vs PFILE | 概念辨析 |
| 多5 | 多选 | ADR目录诊断文件 | 概念辨析 |
| 判1 | 判断 | STARTUP FORCE = SHUTDOWN ABORT + STARTUP | 概念理解 |
| 判2 | 判断 | 静态参数可用SCOPE=BOTH修改 | 概念理解 |
| 判3 | 判断 | SHUTDOWN TRANSACTIONAL等待事务提交但不等用户断开 | 概念理解 |
| 判4 | 判断 | 控制文件一个完好即可多路复用覆盖损坏的 | 概念理解 |
| 判5 | 判断 | 普通业务错误ORA-00942会写入告警日志 | 概念理解 |
| 简1 | 简答 | 四种启动模式阶段任务与视图 | 分析说明 |
| 简2 | 简答 | 四种关闭模式对比表 | 分析说明 |
| 简3 | 简答 | ALTER SYSTEM SCOPE=MEMORY/SPFILE/BOTH区别 | 分析说明 |
| 简4 | 简答 | 启动故障排查通用流程 | 分析说明 |
| 命1 | 命令匹配 | 操作场景 → 正确命令 | 综合应用 |
| 命2 | 命令匹配 | ORA错误 → 解决方案 | 综合应用 |
| 命3 | 命令匹配 | 启动参数文件修改场景 → SCOPE取值 | 综合应用 |
| 命4 | 命令匹配 | 关闭模式 → 触发场景 | 综合应用 |
| 命5 | 命令匹配 | 诊断工具 → 输出文件 | 综合应用 |
| 分1 | 故障分析 | 综合启动故障：ABORT后CURRENT日志损坏启动失败完整排查 | 综合应用 |

---

## 一、单选题（每题 2 分，共 10 题）

**1. STARTUP NOMOUNT阶段，Oracle完成的操作不包括（　）。**
A. 读取参数文件spfile/pfile  
B. 分配SGA共享内存并启动后台进程  
C. 读取控制文件获取数据文件清单  
D. 打开告警日志alert_SID.log与跟踪文件  

**2. 下列SQL操作，必须在MOUNT阶段（及以上）才能执行的是（　）。**
A. CREATE SPFILE FROM PFILE  
B. SELECT status FROM v$instance  
C. ALTER DATABASE ARCHIVELOG  
D. SELECT name, value FROM v$sga  

**3. 关于STARTUP RESTRICT，下列说法正确的是（　）。**
A. 只允许SYS用户登录  
B. 只允许拥有RESTRICTED SESSION权限的用户登录  
C. 不允许任何用户登录，只能在服务器本地操作  
D. 只允许DBA角色用户登录  

**4. V$INSTANCE.STATUS值为MOUNTED时，对应启动模式是（　）。**
A. SHUTDOWN  
B. NOMOUNT  
C. MOUNT  
D. OPEN  

**5. SHUTDOWN NORMAL模式下，下列行为最先发生的是（　）。**
A. 强制断开所有用户会话  
B. 回滚所有未提交事务  
C. 写检查点、刷脏块到数据文件  
D. 禁止新连接请求接入  

**6. 执行SHUTDOWN ABORT后，下列说法错误的是（　）。**
A. 未提交事务不会被回滚，下次启动时由SMON回滚  
B. 不写检查点，Buffer Cache脏块不会刷盘  
C. 下次启动不需要实例恢复，与正常关闭完全一致  
D. 数据库关闭速度最快，几乎瞬间完成  

**7. 启动到MOUNT阶段报错ORA-00205: error in identifying control file，第一步应做的是（　）。**
A. 立即执行CREATE CONTROLFILE重建控制文件  
B. 查看告警日志确定是哪个控制文件路径出了问题  
C. 用SHUTDOWN ABORT关闭并重启  
D. 从RMAN备份恢复整个数据库  

**8. 生产环境ARCHIVELOG模式下，业务突然HANG住并报ORA-00257: archiver error，最正确的紧急处理是（　）。**
A. 直接SHUTDOWN ABORT再重启  
B. 用OS rm命令删除最旧的归档日志文件  
C. 用RMAN执行BACKUP ARCHIVELOG ALL DELETE INPUT或DELETE OBSOLETE释放FRA空间  
D. 切换到NOARCHIVELOG模式  

**9. 下列关于ALTER SYSTEM修改Oracle 19c参数，说法正确的是（　）。**
A. 静态参数processes必须使用SCOPE=BOTH修改  
B. 静态参数processes必须使用SCOPE=SPFILE修改，修改后重启实例生效  
C. 动态参数memory_target必须使用SCOPE=SPFILE修改  
D. ALTER SYSTEM默认SCOPE=MEMORY，重启后失效  

**10. Oracle 11g+的告警日志alert_SID.log默认位于ADR的哪个子目录？**
A. $ORACLE_BASE/diag/rdbms/<dbname>/<SID>/alert/  
B. $ORACLE_BASE/diag/rdbms/<dbname>/<SID>/trace/  
C. $ORACLE_BASE/diag/rdbms/<dbname>/<SID>/incident/  
D. $ORACLE_HOME/rdbms/log/  

---

## 二、多选题（每题 3 分，共 5 题，多选少选均不得分）

**1. STARTUP NOMOUNT阶段，可以成功执行的SQL操作包括（　）。**
A. CREATE DATABASE ... 手工建库  
B. CREATE SPFILE FROM PFILE 或 CREATE PFILE FROM SPFILE  
C. ALTER DATABASE MOUNT  
D. SELECT file#, name FROM v$datafile  

**2. 关于SHUTDOWN IMMEDIATE，下列说法正确的有（　）。**
A. 禁止新连接与新事务开始  
B. 回滚所有未提交事务  
C. 强制断开所有用户会话  
D. 写检查点，将已提交脏块刷盘  
E. 下次启动必须由SMON执行实例恢复  

**3. 启动时出现ORA-01078 failure in processing system parameters和LRM-00109 could not open parameter file，可行的解决方案有（　）。**
A. 用备份的PFILE通过STARTUP NOMOUNT PFILE='...'应急启动  
B. STARTUP NOMOUNT后执行CREATE SPFILE FROM MEMORY从内存重建（如已启动成功过）  
C. 从RMAN备份RESTORE SPFILE  
D. 直接拷贝其他数据库的spfile<SID>.ora覆盖即可，无需调整参数  

**4. 关于SPFILE（服务器参数文件）与PFILE（文本参数文件）的对比，正确的有（　）。**
A. SPFILE是二进制文件，必须通过ALTER SYSTEM修改，不可直接文本编辑  
B. PFILE是文本文件，可用vi直接编辑  
C. STARTUP默认优先查找spfile<SID>.ora，找不到才回退到init<SID>.ora  
D. RAC集群环境下只能使用PFILE，SPFILE不支持多实例  

**5. ADR（自动诊断库）目录中，可能包含的诊断文件类型有（　）。**
A. trace目录下的alert_SID.log告警日志  
B. alert目录下的log.xml（XML格式告警日志）  
C. incident目录下按错误号组织的.trc跟踪文件  
D. cdump目录下进程崩溃产生的core dump文件  

---

## 三、判断题（每题 2 分，共 5 题，对打√错打×）

**1. STARTUP FORCE命令的效果等价于先执行SHUTDOWN ABORT，再执行STARTUP。（　）**

**2. Oracle静态参数sga_max_size可以用ALTER SYSTEM SET sga_max_size=6G SCOPE=BOTH修改，修改后立即生效且永久保留。（　）**

**3. SHUTDOWN TRANSACTIONAL模式会等待所有正在执行的事务COMMIT/ROLLBACK，事务结束后立即断开该用户会话，但不会等待用户主动退出连接。（　）**

**4. 多路复用的控制文件，只要至少还有一个控制文件完好，就可以用OS命令cp用好的控制文件覆盖所有损坏的副本，再重新启动即可恢复。（　）**

**5. 用户登录后执行SELECT * FROM non_existent_table;报ORA-00942 table or view does not exist，这个错误一定会被写入告警日志alert_SID.log。（　）**

---

## 四、简答题（每题 5 分，共 4 题）

**1. 简述Oracle数据库四种启动模式（SHUTDOWN/NOMOUNT/MOUNT/OPEN）每一阶段完成的关键操作，并说明V$INSTANCE、V$DATAFILE、DBA_USERS三个视图分别在哪个阶段开始可以查询。**

**2. 试以"是否允许新连接 / 是否等待事务提交 / 是否等待用户主动断开 / 是否写检查点 / 下次启动是否需要实例恢复 / 生产使用频率"为列，对比SHUTDOWN的NORMAL、TRANSACTIONAL、IMMEDIATE、ABORT四种关闭模式。**

**3. 说明ALTER SYSTEM SET parameter=value命令中SCOPE=MEMORY、SCOPE=SPFILE、SCOPE=BOTH三者的区别，并说明静态参数与动态参数分别允许使用哪些SCOPE。**

**4. 某Oracle 19c数据库执行STARTUP失败（屏幕只报一个笼统的ORA错误号），请写出你作为DBA的通用排查步骤（从发现错误到定位原因、给出解决方案的完整流程），必须包含涉及的关键诊断文件与视图。**

---

## 五、操作命令匹配题（每题 4 分，共 5 题，匹配对应）

### 命1：操作场景 → 正确启动/关闭命令

| 编号 | 操作场景 | 正确命令 |
| ---- | ---- | ---- |
| (a) | 正常计划内停机维护，生产环境最常用的关闭方式 | ① STARTUP RESTRICT |
| (b) | 例程挂起，SHUTDOWN IMMEDIATE等待1小时仍卡住无响应，最后手段 | ② STARTUP NOMOUNT PFILE='/backup/init.ora.20240101' |
| (c) | 数据库打补丁维护窗口，只允许DBA登录，阻止普通业务用户接入 | ③ SHUTDOWN IMMEDIATE |
| (d) | 控制文件全部丢失，准备用CREATE CONTROLFILE命令重建，需先启动实例 | ④ STARTUP FORCE NOMOUNT |
| (e) | SPFILE损坏，用历史备份的PFILE应急启动实例 | ⑤ SHUTDOWN ABORT |

### 命2：ORA错误 → 最直接的解决方案

| 编号 | ORA错误 | 首选解决方案 |
| ---- | ---- | ---- |
| (a) | ORA-12514 TNS:listener does not currently know of service | ① RMAN备份归档后DELETE OBSOLETE/DELETE INPUT释放空间 |
| (b) | ORA-01078 + LRM-00109 parameter file could not be opened | ② lsnrctl start启动监听 + ALTER SYSTEM REGISTER |
| (c) | ORA-00205 error in identifying control file | ③ orapwd重建密码文件 |
| (d) | ORA-00257 archiver error, Connect internal only | ④ 用好的多路控制文件cp覆盖损坏的副本 |
| (e) | ORA-01031 insufficient privileges（远程AS SYSDBA登录失败，本机/没问题） | ⑤ 从备份PFILE或RMAN备份恢复/重建SPFILE |

### 命3：参数修改场景 → 正确的ALTER SYSTEM SCOPE取值

| 编号 | 参数修改场景（Oracle 19c） | SCOPE取值 |
| ---- | ---- | ---- |
| (a) | 临时打开SQL_TRACE跟踪当前实例上所有新会话的SQL，不希望重启后保留 | ① SCOPE=MEMORY |
| (b) | 永久调整open_cursors=500，动态参数，立即生效且重启后仍保留 | ② SCOPE=SPFILE |
| (c) | 扩容最大OS进程数processes=500（静态参数） | ③ SCOPE=BOTH |
| (d) | 调大sga_max_size上限（静态参数） |  |
| (e) | 临时调高undo_retention=86400秒仅当前实例生效，下次启动恢复为原值 |  |

### 命4：关闭模式 → 典型触发场景

| 编号 | 典型场景 | 推荐关闭模式 |
| ---- | ---- | ---- |
| (a) | 数据库服务器计划内重启，业务已切换但仍有应用连接池保持着连接 | ① SHUTDOWN NORMAL |
| (b) | 夜间批处理窗口，有1个大结算事务还在跑，跑完后就关库 | ② SHUTDOWN TRANSACTIONAL |
| (c) | 内存报错实例HANG住，IMMEDIATE等待回滚卡死无响应，最后手段 | ③ SHUTDOWN IMMEDIATE |
| (d) | 开发测试库下班后无用户，准备做冷备 | ④ SHUTDOWN ABORT |
| (e) | RAC某个节点后台进程异常退出，需紧急停机修复 |  |

### 命5：诊断工具 / 命令 → 输出 / 效果

| 编号 | 诊断操作 | 效果 / 输出 |
| ---- | ---- | ---- |
| (a) | `ALTER SESSION SET EVENTS '10046 trace name context forever, level 12'` | ① 在trace目录生成用户会话.trc文件（含绑定变量与等待事件） |
| (b) | `tkprof orcl_ora_12345.trc report.txt explain=hr/hr sort=exeela` | ② 启动ADRCI后查看告警日志最后50行 |
| (c) | `SELECT value FROM v$diag_info WHERE name='Alert Log'` | ③ 格式化原始.trc为易读汇总报告，附执行计划并按执行时间排序 |
| (d) | `adrci> SHOW ALERT -TAIL 50` | ④ 返回alert_SID.log的完整绝对路径 |
| (e) | `adrci> PURGE -AGE 10080` | ⑤ 删除7天前（10080分钟）的旧诊断数据，释放ADR磁盘空间 |

---

## 六、故障分析题（共 15 分，完整解答）

**综合启动故障分析：** 某生产Oracle 19c数据库，DBA执行SHUTDOWN ABORT紧急关闭后（因业务系统严重卡死），重新执行STARTUP时出现以下错误：

```
SQL> STARTUP
ORACLE instance started.
Total System Global Area 3221225472 bytes
Fixed Size                  9139328 bytes
Variable Size             805306368 bytes
Database Buffers         2399141888 bytes
Redo Buffers                7665664 bytes
Database mounted.
ORA-00313: open failed for members of log group 3 of thread 1
ORA-00312: online log 3 thread 1: '/u01/app/oracle/oradata/orcl/redo03a.log'
ORA-00312: online log 3 thread 1: '/u02/fra/orcl/redo03b.log'
ORA-27041: unable to open file
Linux-x86_64 Error: 2: No such file or directory
```

请作为DBA完成以下问题：

(1)（3分）判断故障发生在启动四阶段的哪一步？根据错误号，说明重做日志组3的损坏程度。

(2)（4分）说明你下一步要查询的视图与SQL，以及查询结果如何帮助你判断该重做日志组的状态（CURRENT/ACTIVE/INACTIVE）与归档情况，以及是否还有一个成员完好。

(3)（5分）分三种情况给出完整的处理方案：
- 情况A：查询发现日志组3是**INACTIVE**状态（非当前组），且已归档。
- 情况B：查询发现日志组3是**ACTIVE**状态，已归档，只是两个成员中redo03a.log丢失、redo03b.log还在。
- 情况C：查询发现日志组3是**CURRENT**状态（LGWR正在写入），redo03a.log与redo03b.log两个多路复用成员同时物理损坏。

(4)（3分）从预防角度，总结至少3条可避免此类故障再次发生的运维措施。

---

## 答案与解析

<details>
<summary>单选题答案与解析</summary>

1. **C**。读取控制文件是MOUNT阶段的任务，NOMOUNT还未装载数据库，不会读控制文件。A/B/D都是NOMOUNT阶段完成的操作。参见 [[4.1 数据库四种启动模式]]。
2. **C**。切换ARCHIVELOG/NOARCHIVELOG必须在MOUNT状态执行。A/B/D在NOMOUNT即可。
3. **B**。RESTRICT模式要求用户拥有RESTRICTED SESSION系统权限，不只是SYS或DBA角色。维护完成后需ALTER SYSTEM DISABLE RESTRICTED SESSION解除。
4. **C**。V$INSTANCE.STATUS：NOMOUNT→STARTED，MOUNT→MOUNTED，OPEN→OPEN。
5. **D**。NORMAL第一步先禁止新连接，然后无限等待用户主动断开、等事务结束，最后写检查点关闭。
6. **C**。ABORT不写检查点不回滚，下次启动必须实例恢复（SMON前滚+回滚）。C说法错误。
7. **B**。任何ORA错误第一反应都是看告警日志，确定具体是哪个控制文件路径出错，再决定是多路覆盖还是重建控制文件。
8. **C**。归档满了必须先用RMAN备份归档（满足保留策略）后再删除释放空间。严禁直接rm，会导致RMAN元数据不一致。切换NOARCHIVELOG模式需要关闭数据库重启，业务停机时间更长，不合适。
9. **B**。静态参数只能SCOPE=SPFILE，必须重启。动态参数可用SCOPE=MEMORY/BOTH，默认SCOPE=BOTH。
10. **B**。ADR中trace/目录存放文本格式的告警日志alert_SID.log和普通.trc文件。alert/目录下是XML格式的log.xml。

</details>

<details>
<summary>多选题答案与解析</summary>

1. **ABC**。D选项的V$DATAFILE从控制文件读取，必须MOUNT起才能查询。NOMOUNT阶段可执行建库、参数文件互转、以及ALTER DATABASE MOUNT（进阶到MOUNT）。
2. **ABCD**。E错误：IMMEDIATE写了检查点，文件SCN一致，下次启动不需实例恢复。ABORT才需要。
3. **ABC**。D错误：不同数据库的db_name、control_files、memory等参数完全不同，不能直接覆盖使用。
4. **ABC**。D错误：RAC推荐用单份SPFILE放在共享存储上，所有节点共用，通过`<SID>.*`前缀区分各节点私有参数。SPFILE原生支持RAC。
5. **ABCD**。ADR统一管理所有诊断文件，四个选项都是ADR目录下的标准内容。

</details>

<details>
<summary>判断题答案与解析</summary>

1. **√**。STARTUP FORCE = SHUTDOWN ABORT + STARTUP，用于例程挂起无法正常关闭的紧急情况，会触发实例恢复。
2. **×**。sga_max_size是静态参数，SCOPE只能是SPFILE，用SCOPE=BOTH会直接报ORA-02095: specified initialization parameter cannot be modified。
3. **√**。TRANSACTIONAL的核心特征：等待事务提交但不等用户，事务一结束就断。介于NORMAL和IMMEDIATE之间。
4. **√**。多路复用控制文件互为镜像，只要有一个好的，cp覆盖即可恢复一致性。前提是**先SHUTDOWN ABORT关闭实例**再复制。
5. **×**。ORA-00942属于业务用户SQL语法/对象权限错误，不会写入告警日志。只有实例级错误（ORA-600/7445/启动关闭/结构变更/归档等）才会记录。

</details>

<details>
<summary>简答题参考答案</summary>

**1. 四种启动模式与视图：**

| 阶段 | 关键操作 | V$INSTANCE | V$DATAFILE | DBA_USERS |
| ---- | ---- | ---- | ---- | ---- |
| SHUTDOWN | 关闭所有进程释放SGA | ❌ 不可查 | ❌ | ❌ |
| NOMOUNT | 读参数文件、分配SGA、启动后台进程 | ✅ STATUS=STARTED | ❌ 基于控制文件 | ❌ 基于SYSTEM表空间 |
| MOUNT | 读控制文件、关联实例与数据库 | ✅ STATUS=MOUNTED | ✅ 从控制文件读取文件清单 | ❌ |
| OPEN | 打开数据文件与重做日志、SMON回滚未提交事务 | ✅ STATUS=OPEN | ✅ | ✅ 数据字典表已打开 |

**2. 四种关闭模式对比：**

| 对比项 | NORMAL | TRANSACTIONAL | IMMEDIATE | ABORT |
| ---- | ---- | ---- | ---- | ---- |
| 允许新连接 | ❌ | ❌ | ❌ | ❌（直接终止） |
| 等待事务提交 | ✅ 等全部 | ✅ 等进行中的 | ❌ 回滚 | ❌ 不处理 |
| 等待用户断开 | ✅ 无限等 | ❌ 事务完就断 | ❌ 直接断 | ❌ 直接断 |
| 写检查点 | ✅ | ✅ | ✅ | ❌ |
| 下次启动实例恢复 | ❌ | ❌ | ❌ | ✅ 必须 |
| 生产使用频率 | 几乎不用 | 偶尔（批处理） | **最常用** | 仅紧急 |

**3. SCOPE取值区别：**
- **SCOPE=MEMORY**：只修改当前实例内存中的参数值，立即生效，重启后失效（参数恢复为SPFILE中存储的旧值）。
- **SCOPE=SPFILE**：只修改SPFILE磁盘文件，当前不生效，必须重启实例后才生效。
- **SCOPE=BOTH**（默认值）：同时修改内存与SPFILE，立即生效且重启后仍保留。

参数类型限制：
- **动态参数（ISSYS_MODIFIABLE=IMMEDIATE/DEFERRED）**：MEMORY/SPFILE/BOTH三种SCOPE都可。
- **静态参数（ISSYS_MODIFIABLE=FALSE）**：仅SCOPE=SPFILE可用。用MEMORY或BOTH直接报错ORA-02095。

**4. 启动失败通用排查步骤：**
1. **看告警日志尾部**：`tail -n 200 $ALERT_LOG`，配合grep搜索ORA-错误，定位**错误发生在启动哪个阶段**（NOMOUNT/MOUNT/OPEN）。
2. **查V$DIAG_INFO**：`SELECT * FROM v$diag_info;` 确认ADR路径正确，找到所有.trc跟踪文件路径。
3. **按错误号匹配故障类型**：ORA-125xx→监听；ORA-01078→参数文件；ORA-00205→控制文件；ORA-01157/01113→数据文件；ORA-00312→重做日志；ORA-00257→归档空间。
4. **查对应V$视图补全上下文**：V$DATAFILE/V$LOG/V$CONTROLFILE看文件状态；V$RECOVERY_FILE_DEST看空间；V$PARAMETER看参数值。
5. **确定方案分级执行**：优先方案A（简单，如监听启动、多路复制）→ 再方案B（备份恢复）→ 最后方案C（重建/不完全恢复）。
6. **重启验证**：修复后STARTUP，检查V$INSTANCE.STATUS=OPEN、检查业务用户登录测试、检查告警日志无新错误。

</details>

<details>
<summary>匹配题参考答案</summary>

**命1：场景 → 命令**
(a)→③ IMMEDIATE是生产计划内停机首选；(b)→⑤ ABORT是最后手段；(c)→① RESTRICT只让DBA进；(d)→④ NOMOUNT下才能重建控制文件，例程挂起可用FORCE；(e)→② 指定PFILE应急启动。

**命2：ORA错误 → 解决方案**
(a)→② 监听未启动/未注册；(b)→⑤ 参数文件恢复；(c)→④ 多路覆盖控制文件；(d)→① 归档满了先备份再删；(e)→③ 密码文件丢失重建。

**命3：场景 → SCOPE**
(a)→① MEMORY临时生效不保留；(b)→③ BOTH立即+永久；(c)(d)静态参数→② SPFILE必须重启；(e)→① MEMORY临时调大。

**命4：场景 → 模式**
(a)→③ IMMEDIATE断连接回滚事务；(b)→② TRANSACTIONAL等事务；(c)→④ ABORT最后手段；(d)→① NORMAL无用户时可用；(e)→④ ABORT紧急。

**命5：诊断操作 → 效果**
(a)→① 10046 level 12生成带绑定+等待的.trc；(b)→③ tkprof格式化trc为报告；(c)→④ V$DIAG_INFO查Alert Log路径；(d)→② ADRCI SHOW ALERT看告警最后50行；(e)→⑤ PURGE清理7天前历史。

</details>

<details>
<summary>故障分析题完整解答</summary>

**(1) 故障阶段判断：**
- 输出显示"Database mounted."，即NOMOUNT、MOUNT都通过了，错误发生在**OPEN阶段**尝试打开重做日志文件时。
- ORA-00313/00312表明**日志组3的两个多路复用成员redo03a.log与redo03b.log同时物理丢失**（OS级找不到文件，Error 2=No such file or directory）。大概率是SHUTDOWN ABORT瞬间加上存储/OS层面的误操作或文件系统异常同时导致两个磁盘路径的日志成员丢失。

**(2) 下一步查询视图与SQL：**
```sql
STARTUP MOUNT;   -- 先启动到MOUNT阶段，不要直接OPEN

-- 查所有日志组的状态与归档情况
SELECT group#, thread#, sequence#, status, archived, bytes/1024/1024 "MB"
  FROM v$log
 ORDER BY group#;
-- 重点看：STATUS列值（INACTIVE/ACTIVE/CURRENT）与ARCHIVED列（YES/NO）

-- 查每个成员文件的物理路径与状态
SELECT group#, member, status, is_recovery_dest_file
  FROM v$logfile
 WHERE group# = 3
 ORDER BY member;
-- 看是否有一个成员STATUS为VALID（说明可能只是路径没配上或ASM磁盘组未挂载）
-- 如果两个成员都INVALID/不存在 → 真丢了
```
判断逻辑：
- GROUP3.STATUS=INACTIVE + ARCHIVED=YES → 幸运，最简单，直接DROP+重建。
- GROUP3.STATUS=ACTIVE + ARCHIVED=YES → 清除日志组（CLEAR）。
- GROUP3.STATUS=CURRENT → 最糟，需不完全恢复。
- V$LOGFILE中只要有一个成员STATUS=VALID → 检查是否路径拼写错误或存储未挂载。

**(3) 三种情况处理方案：**

**情况A：INACTIVE+已归档（最简单）**
```sql
-- 日志组内容已完成检查点、已归档，丢失对实例恢复无影响
-- 直接删除日志组3重建
ALTER DATABASE DROP LOGFILE GROUP 3;
-- 重建两个多路复用成员
ALTER DATABASE ADD LOGFILE GROUP 3 (
  '/u01/app/oracle/oradata/orcl/redo03a.log',
  '/u02/fra/orcl/redo03b.log'
) SIZE 500M REUSE BLOCKSIZE 512;
-- 验证创建成功
SELECT group#, status FROM v$log;
-- 打开数据库
ALTER DATABASE OPEN;
```

**情况B：ACTIVE+已归档+还有redo03b.log完好**
```sql
-- ACTIVE状态意味着刚切换不久，检查点还没完全做完，但已归档
-- 因redo03b.log完好，先把损坏的成员文件替换（把好的成员复制补回缺失的路径）
SHUTDOWN ABORT;
HOST cp /u02/fra/orcl/redo03b.log /u01/app/oracle/oradata/orcl/redo03a.log;
STARTUP MOUNT;
ALTER DATABASE OPEN;

-- 或者（更安全）：如果CP也不行，直接用CLEAR UNARCHIVED重建日志组内容
-- ALTER DATABASE CLEAR LOGFILE GROUP 3;
-- 注意：只有已归档才能CLEAR！未归档的CLEAR会破坏归档链，需要后续立即做一次全备
```

**情况C：CURRENT状态+两个成员全丢（最严重）**
CURRENT是LGWR当前正在写的组，ABORT瞬间丢失意味着最后提交的部分事务在重做日志里已找不到了。**必须做不完全恢复+OPEN RESETLOGS，会丢失最后未写入归档的事务。**
```sql
-- (1) 确保已有RMAN全备+归档链完整（必须！否则无法恢复）
STARTUP NOMOUNT;
-- 如果控制文件还好：
ALTER DATABASE MOUNT;

-- (2) RMAN做不完全恢复，恢复到损坏日志组之前的那个SCN或时间点
-- 方法一：按日志序列号恢复（恢复到seq#= <GROUP3的seq# -1>）
RMAN TARGET /
RMAN> RUN {
    SET UNTIL SEQUENCE 1234 THREAD 1;  -- 1234是GROUP3的sequence#减1
    RESTORE DATABASE;
    RECOVER DATABASE;
  }

-- (3) 不完全恢复完成后，用RESETLOGS打开（会重置日志序列号，重建全部重做日志）
SQLPLUS / AS SYSDBA
ALTER DATABASE OPEN RESETLOGS;

-- (4) ★ 立即执行一次全库备份（RESETLOGS后之前的备份理论上失效（11g+虽可但不推荐））
RMAN> BACKUP AS COMPRESSED BACKUPSET DATABASE PLUS ARCHIVELOG;

-- 业务侧核对最后一笔事务的一致性，必要时补录（因最后CURRENT组丢失的事务会回滚）
```

**(4) 预防措施：**
1. **重做日志组多路复用必须跨物理存储**：每个日志组的两个成员绝对不能放在同一个磁盘/同一个存储卷/同一个ASM磁盘组故障组里，像本题中redo03a与redo03b都丢了的情况，大概率是放在了同一个底层存储上，没有真正做到多路复用容灾。
2. **避免生产环境使用SHUTDOWN ABORT作为常规关闭手段**：ABORT瞬间LGWR可能正在写CURRENT日志组，配合存储写入异常容易导致CURRENT组损坏。优先SHUTDOWN IMMEDIATE，即使IMMEDIATE慢也要耐心等回滚完成。
3. **RMAN全备+归档日志每日必做，并定期演练恢复**：本题情况C如果没有备份只能重建库（丢所有数据），有了备份+归档最多丢最后未归档的少量事务。每周至少做一次恢复演练，确认备份链有效。
4. **监控OS与存储层错误**：提前发现磁盘坏块、文件系统满、HBA卡闪断等底层问题，避免存储故障传导到数据库日志文件。
5. **重做日志组数量与大小科学配置**：一般2~4组，每组至少2成员，切换频率15~30分钟一次（通过v$log_history切换次数统计），减少CURRENT日志组内"积压"的未归档事务量。

</details>

---

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | 启动模式阶段任务、RESTRICT模式、关闭模式特点、ORA错误首步处理、SCOPE规则、ADR路径 |
| 多选 | 5 | 15 | NOMOUNT可执行操作、SHUTDOWN IMMEDIATE步骤、参数文件恢复方法、SPFILE/PFILE对比、ADR文件结构 |
| 判断 | 5 | 10 | STARTUP FORCE等价性、静态参数SCOPE限制、TRANSACTIONAL特点、多路控制文件恢复、告警日志记录范围 |
| 简答 | 4 | 20 | 启动模式与视图关系、四种关闭模式对比表、SCOPE区别与限制、通用排查流程 |
| 匹配 | 5 | 20 | 场景命令匹配、ORA错误-方案匹配、SCOPE使用匹配、关闭模式匹配、诊断工具效果匹配 |
| 故障分析 | 1 | 15 | 启动阶段定位、日志组状态判断、三种情况分级方案（INACTIVE/ACTIVE/CURRENT）、预防措施 |
| 合计 | 30 | 100 | 覆盖第4章全部核心考点，重操作命令与故障排查思路 |

## 章节导航

- 上级MOC：[[MOC - Oracle数据库管理]]
- 本章知识点：[[MOC - 第4章]]（[[4.1 数据库四种启动模式]]、[[4.2 正常关闭、立即关闭、事务关闭、中止关闭]]、[[4.3 启动故障简单排查]]、[[4.4 参数文件SPFILE与PFILE详解]]、[[4.5 告警日志、跟踪文件与ADR自动诊断库]]）
- 上一章习题：[[MOC - 第3章习题]]
- 下一章习题：[[MOC - 第5章习题]]
