---
domain: 数据库技术
subject: Oracle数据库管理
type: exercise
chapter: 第7章 Oracle重做日志、归档模式
section: 第7章 习题总览
tags: [Oracle,习题,DBA,备份恢复,重做日志,归档,RMAN]
prerequisites: ["7.1 联机重做日志组工作机制", "7.2 ARCH归档模式开启与关闭", "7.3 日志切换、检查点", "7.4 归档日志维护策略"]
---

# MOC - 第7章习题

> [!info] 习题说明
> 本习题集覆盖[[MOC - 第7章]]全部知识点，共30题，分六类：单选10题、多选5题、判断5题、简答4题、分析4题（含CURRENT组丢失场景、ORA-00257故障处理、SQL日志组操作编程）、综合2题（含RMAN归档删除完整流程、生产归档模式切换完整演练）。重点考查重做日志组状态转换、ARCHIVELOG/NOARCHIVELOG模式差异、检查点三类区别、FRA空间管理。答案折叠于details块，配套知识点见各题后链接。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | WAL先写日志原则 | 概念理解 |
| 单2 | 单选 | 日志组状态CURRENT含义 | 概念理解 |
| 单3 | 单选 | 日志组多路复用最低要求 | 概念理解 |
| 单4 | 单选 | NOARCHIVELOG vs ARCHIVELOG恢复能力 | 概念理解 |
| 单5 | 单选 | 归档模式切换状态要求 | 概念理解 |
| 单6 | 单选 | ORA-00257成因 | 概念理解 |
| 单7 | 单选 | 增量检查点特点 | 概念理解 |
| 单8 | 单选 | SWITCH LOGFILE vs ARCHIVE LOG CURRENT | 概念辨析 |
| 单9 | 单选 | RMAN vs OS rm删归档 | 概念辨析 |
| 单10 | 单选 | CURRENT组丢失处理 | 综合应用 |
| 多1 | 多选 | LGWR触发写条件 | 概念辨析 |
| 多2 | 多选 | 日志组状态说明 | 概念辨析 |
| 多3 | 多选 | ARCHIVELOG模式恢复能力 | 概念辨析 |
| 多4 | 多选 | 完全检查点触发场景 | 概念辨析 |
| 多5 | 多选 | FRA包含文件类型 | 概念辨析 |
| 判1 | 判断 | WAL原则：先写数据后写日志 | 概念理解 |
| 判2 | 判断 | 删除日志组后剩余≥2组每组≥2成员 | 概念理解 |
| 判3 | 判断 | 切换ARCHIVELOG后旧备份仍有效 | 概念理解 |
| 判4 | 判断 | FAST_START_MTTR_TARGET单位是秒 | 概念理解 |
| 判5 | 判断 | OS rm删归档后RMAN无需其他操作 | 概念理解 |
| 简1 | 简答 | 日志组六种状态及转换条件 | 分析说明 |
| 简2 | 简答 | 完全/增量/局部三类检查点对比 | 分析说明 |
| 简3 | 简答 | ORA-00257紧急处理步骤 | 分析说明 |
| 简4 | 简答 | RMAN删除归档的安全步骤与OS rm区别 | 分析说明 |
| 分1 | 分析 | 日志组操作SQL编程+危险标注 | 综合应用 |
| 分2 | 分析 | ARCHIVELOG切换完整演练+SQL | 综合应用 |
| 分3 | 分析 | 归档目的地ERROR状态排查案例 | 综合应用 |
| 分4 | 分析 | FRA ORA-19809空间不足完整处理 | 综合应用 |
| 综1 | 综合 | CURRENT组丢失场景完整处理流程 | 综合应用 |
| 综2 | 综合 | 生产归档维护策略设计+RMAN脚本 | 综合应用 |

## 一、单选题（每题2分，共10题）

**1. Oracle数据库遵循的WAL（Write-Ahead Logging）原则是指（　）。**
A. 先写数据文件，后写日志文件
B. 先写日志文件，后写数据文件
C. 日志文件与数据文件同时写
D. COMMIT时只写数据文件即可

**2. 关于联机重做日志组的CURRENT状态，下列说法正确的是（　）。**
A. LGWR已写完该组，ARCn正在归档
B. 检查点已完成，可被覆盖复用
C. LGWR正在写入该组，实例崩溃恢复必需
D. 该组从未被写入

**3. Oracle单实例数据库重做日志的多路复用最低要求是（　）。**
A. 至少1组，每组至少1成员
B. 至少2组，每组至少2成员
C. 至少3组，每组至少3成员
D. 至少4组，每组至少4成员

**4. 数据库运行在NOARCHIVELOG模式下，若发生介质故障（数据文件损坏），下列说法正确的是（　）。**
A. 可恢复到故障前最新状态
B. 可恢复到故障前任意时间点
C. 只能恢复到最后一次冷备份时刻，之后数据全部丢失
D. 用热备份即可恢复

**5. 执行 `ALTER DATABASE ARCHIVELOG;` 命令时，数据库必须处于（　）状态。**
A. NOMOUNT
B. MOUNT（且必须是一致性SHUTDOWN后启动的MOUNT）
C. OPEN READ WRITE
D. OPEN READ ONLY

**6. ORA-00257错误的典型成因是（　）。**
A. 数据文件磁盘空间满
B. 归档目的地磁盘空间满，ARCn无法继续归档，LGWR冻结数据库
C. SGA内存不足
D. 控制文件损坏

**7. 关于Oracle增量检查点，下列说法错误的是（　）。**
A. 每3秒定时推进
B. 一次性把所有脏缓冲写盘，I/O尖峰
C. 根据FAST_START_MTTR_TARGET目标渐进推进
D. 平滑I/O，避免完全检查点的瞬间I/O洪峰

**8. 关于 `ALTER SYSTEM SWITCH LOGFILE` 和 `ALTER SYSTEM ARCHIVE LOG CURRENT` 的区别，下列说法正确的是（　）。**
A. 两者完全等价
B. 前者是同步等待归档完成，后者是异步立即返回
C. 前者是异步立即返回，后者是同步等待当前日志切换+归档完成
D. 前者只切换不归档，后者只归档不切换

**9. 删除过期归档日志的安全方式是（　）。**
A. 直接OS层 `rm` 归档文件
B. 先OS层 `rm`，再 `RESET DATABASE`
C. 使用RMAN的 `DELETE OBSOLETE` 或 `DELETE ARCHIVELOG ...`
D. 直接清空V$ARCHIVED_LOG表

**10. 生产数据库CURRENT组所有成员物理损坏且无多路复用完好成员，正确处理是（　）。**
A. 直接DROP LOGFILE GROUP当前组
B. SHUTDOWN ABORT → STARTUP MOUNT → 重建控制文件 → USING BACKUP CONTROLFILE UNTIL CANCEL → OPEN RESETLOGS → 立即全备
C. STARTUP FORCE 强制打开
D. ALTER DATABASE CLEAR UNARCHIVED LOGFILE GROUP n; 正常打开

## 二、多选题（每题3分，共5题）

**1. LGWR写重做日志的触发条件包括（　）。**
A. 用户执行COMMIT
B. 每3秒定时触发
C. 重做缓冲区1/3满或达到1MB
D. DBWn写脏块前同步要求先写对应重做
E. 执行 `ALTER SYSTEM SWITCH LOGFILE` 或实例正常关闭前

**2. 下列关于联机重做日志组状态的说明，正确的是（　）。**
A. ACTIVE组崩溃恢复仍需要
B. INACTIVE组表示检查点已完成、归档已完成（ARCHIVELOG下），可被LGWR覆盖复用
C. UNUSED组是新建或CLEAR后从未被写入
D. CLEARING表示正在执行 `ALTER DATABASE CLEAR LOGFILE`

**3. ARCHIVELOG模式下，数据库支持（　）。**
A. 热备份（数据库OPEN状态下的联机备份）
B. 完全恢复（到故障前最新时刻）
C. 不完全恢复（到任意中间时间点/SCN/日志序列号）
D. Data Guard备库同步

**4. 完全检查点（Complete Checkpoint）的触发场景包括（　）。**
A. SHUTDOWN NORMAL
B. SHUTDOWN IMMEDIATE
C. `ALTER SYSTEM CHECKPOINT` 手动执行
D. 每3秒定时触发

**5. Oracle闪回恢复区（FRA）中自动管理的文件包括（　）。**
A. 归档日志
B. RMAN备份集/镜像副本
C. 控制文件自动备份
D. 闪回日志（Flashback Database启用时）

## 三、判断题（每题2分，共5题）

**1. Oracle的WAL先写日志原则是：先把数据变更写入数据文件，再写对应重做日志。**

**2. 执行 `ALTER DATABASE DROP LOGFILE MEMBER ...` 前，必须确认该成员所属组删除后剩余成员数仍≥2，删除后总组数仍≥2。**

**3. 数据库从NOARCHIVELOG切换到ARCHIVELOG后，切换前的所有冷备份仍然有效，可用于介质恢复。**

**4. 初始化参数 `FAST_START_MTTR_TARGET` 的单位是秒，用于控制期望的平均崩溃恢复时长。**

**5. 用OS命令 `rm` 直接删除归档文件后，RMAN会自动检测并同步更新其存储库元数据，无需任何额外操作。**

## 四、简答题（每题5分，共4题）

**1. 列出联机重做日志组的六种状态，并说明从CURRENT到INACTIVE每一步状态转换的触发条件。**

**2. 比较Oracle三类检查点（完全检查点、增量检查点、局部检查点）的触发时机、写脏缓冲范围与I/O特征。**

**3. 生产数据库接到ORA-00257告警（归档错误），普通用户会话冻结，请给出紧急处理的完整步骤。**

**4. 简述使用RMAN删除归档日志的安全规范步骤，并说明为何严禁OS直接rm；若DBA误rm了归档，后续应如何纠正。**

## 五、分析题（每题8分，共4题，需给出完整SQL或步骤）

**1. 日志组操作SQL编程题。** 某Oracle 19c单实例数据库当前有3组日志（每组2成员，200M），发现切换频率过高（平均3分钟一次），DBA决定：①新增第4组，2成员500M；②向第4组追加第3成员；③删除旧第4组（假设其变为INACTIVE后）。要求：写出完整SQL，并在每一处高风险命令前加 > [!danger] 危险说明与前提检查。

**2. ARCHIVELOG模式切换演练SQL。** 某测试库从NOARCHIVELOG切换到ARCHIVELOG。当前：数据库OPEN状态，SPFILE已使用，FRA未配置。给出完整的SQL步骤：关库→MOUNT→切换→OPEN→验证模式→配置本地2个归档目的地+日志格式→设置最少成功归档数=2→立即做一次数据库全备的RMAN脚本。

**3. 归档目的地ERROR状态排查。** `V$ARCHIVE_DEST` 查询显示 DEST_ID=2 状态ERROR，DESTINATION是'/u02/arch/ORCL'，ERROR列显示'Error 19504 Creating archived log file'。请给出：(1) 可能的三条原因；(2) 每一条原因对应的排查命令；(3) 修复后如何验证目的地恢复VALID状态。

**4. FRA空间不足处理案例。** V$RECOVERY_FILE_DEST显示SPACE_LIMIT=500G，SPACE_USED=495G，SPACE_RECLAIMABLE=50G，报错ORA-19809。RMAN保留策略是REDUNDANCY 2。请给出：(1) 从紧急到长期的三步处理方案（每步写出具体RMAN/SQL）；(2) 解释为何SPACE_RECLAIMABLE有50G但仍报空间不足。

## 六、综合题（每题10分，共2题）

**1. CURRENT组丢失场景完整处理。** 场景：生产单实例数据库CURRENT组（GROUP#=3）的两个成员分别在磁盘A、B上，磁盘A、B同时物理损坏，GROUP 3所有成员彻底丢失。发现时实例仍在运行但业务缓慢，LGWR报错无法写入CURRENT组。请给出：(1) 按优先级的完整处理步骤（每步写出具体SQL/RMAN命令）；(2) 此场景下哪些已提交事务可能永久丢失，说明原因；(3) OPEN RESETLOGS后必须做什么，原因是什么；(4) 如何通过架构改进彻底避免此类灾难。

**2. 生产归档维护策略设计。** 某24×7核心业务Oracle 19c数据库，要求：(a) 保证任意时刻可恢复到最近30天内任意时间点；(b) 本地磁盘归档保留14天，14天前归档备份到磁带后从本地删除；(c) 使用FRA自动管理，本地归档双目的地（一主一备磁盘）。请给出：(1) 所有初始化参数设置SQL（FRA路径/大小、归档双目的地、最少成功数、日志格式、MTTR目标）；(2) RMAN持久化配置（保留策略、控制文件自动备份、通道配置）；(3) 一个每日执行的RMAN归档维护脚本（备份14天前归档到磁带+删除本地过期归档+报告空间情况）；(4) 监控脚本（查询FRA使用率、归档目的地ERROR状态、日志切换频率）。

## 答案与解析

<details>
<summary>单选题答案与解析</summary>

1. **B**。WAL先写日志后写数据。A说反了。参见[[7.1 联机重做日志组工作机制]]。
2. **C**。CURRENT是LGWR正在写的组，崩溃恢复必需。A是ACTIVE；B是INACTIVE；D是UNUSED。
3. **B**。单实例每个重做线程至少2组，每组至少2成员多路复用。
4. **C**。NOARCHIVELOG模式只能冷备且只能恢复到备份时刻。AB是ARCHIVELOG能力；D热备只能ARCHIVELOG模式下做。
5. **B**。ALTER DATABASE ARCHIVELOG只能在一致性SHUTDOWN后的MOUNT状态执行。参见[[7.2 ARCH归档模式开启与关闭]]。
6. **B**。ORA-00257是归档空间满，ARCn无法归档导致LGWR挂起冻结数据库。
7. **B**。B描述的是完全检查点特征，不是增量。增量只部分写出、渐进平滑I/O。
8. **C**。SWITCH LOGFILE立即返回（异步），ARCHIVE LOG CURRENT切换并等待归档完成（同步）。
9. **C**。RMAN DELETE系列同时删除物理文件+更新元数据。OS rm会导致RMAN元数据不一致。参见[[7.4 归档日志维护策略]]。
10. **B**。CURRENT组全损坏需重建控制文件+UNTIL CANCEL恢复+OPEN RESETLOGS。A不能删CURRENT；C强制打开会报更多错；D CLEAR UNARCHIVED只适合INACTIVE/UNUSED，CURRENT无法CLEAR。

</details>

<details>
<summary>多选题答案与解析</summary>

1. **ABCDE**。LGWR五大触发条件：COMMIT、3秒、1/3或1MB、DBWn同步、切换/关库。
2. **ABCD**。四选项均为四种状态的正确描述。
3. **ABCD**。ARCHIVELOG支持热备、完全恢复、不完全恢复、Data Guard同步。
4. **ABC**。SHUTDOWN NORMAL/IMMEDIATE/TRANSACTIONAL + 手动ALTER SYSTEM CHECKPOINT触发完全检查点。D「每3秒」是增量检查点触发。
5. **ABCD**。FRA包含：归档日志、RMAN备份集/镜像副本、控制文件自动备份、闪回日志。

</details>

<details>
<summary>判断题答案与解析</summary>

1. **×**。WAL先写日志后写数据文件，题干说反。
2. **√**。删除操作必须保证剩余多路复用满足最低要求：线程≥2组、每组≥2成员。
3. **×**。切换后旧备份失效——之前无归档日志，旧备份无法和切换后重做流拼接。必须立即做新的全备。
4. **√**。FAST_START_MTTR_TARGET单位是秒，推荐值300（5分钟）。
5. **×**。OS rm后RMAN不会自动感知。必须CROSSCHECK ARCHIVELOG ALL + DELETE EXPIRED ARCHIVELOG ALL 清理元数据。

</details>

<details>
<summary>简答题答案</summary>

**1. 六种状态与转换条件：**
| 状态 | 转换进入条件 |
| ---- | ---- |
| UNUSED | 新建日志组 / ALTER DATABASE CLEAR LOGFILE完成后 |
| CURRENT | UNUSED首次被LGWR写入 / INACTIVE循环复用时被LGWR写入 |
| ACTIVE | LGWR写满CURRENT组切换下一组 → 原CURRENT变为ACTIVE（检查点未完成+归档未完成） |
| INACTIVE | ACTIVE组的检查点完成（DBWn写完全部脏缓冲）+ ARCHIVELOG模式下ARCn归档完成 → 变为INACTIVE |
| CLEARING | 执行ALTER DATABASE CLEAR LOGFILE过程中 |
| CLEARING_CURRENT | 执行ALTER DATABASE CLEAR LOGFILE时恰好该组是CURRENT，极少见 |

转换链路核心：UNUSED/INACTIVE → CURRENT → ACTIVE → INACTIVE → CURRENT。

**2. 三类检查点对比：**
| 类型 | 触发时机 | 写脏缓冲范围 | I/O特征 |
| ---- | ---- | ---- | ---- |
| 完全 | SHUTDOWN NORMAL/IMMEDIATE/TRANSACTIONAL / ALTER SYSTEM CHECKPOINT | SGA全部脏缓冲 | 瞬间I/O尖峰，大量写盘 |
| 增量 | 每3秒定时 / 按FAST_START_MTTR_TARGET目标 | 检查点队列尾部的部分脏缓冲 | 渐进分批写，I/O平滑（生产主力） |
| 局部 | 表空间OFFLINE/BEGIN BACKUP / RMAN备份 / 数据文件离线 | 仅对应表空间/数据文件的脏缓冲 | 局部I/O |

**3. ORA-00257紧急处理：**
1. SYS以SYSDBA登录：`sqlplus / as sysdba`
2. 查看归档目的地与空间：`ARCHIVE LOG LIST;` + OS `df -h`
3. 若空间真满：
   - 先确认过期归档已备份：`RMAN> LIST BACKUP OF ARCHIVELOG ALL;`
   - 按保留策略删除：`RMAN> DELETE OBSOLETE;`
   - 或按时间删除7天前：`RMAN> DELETE ARCHIVELOG ALL COMPLETED BEFORE 'SYSDATE-7';`
4. 若空间未满：`SELECT dest_id, status, error FROM v$archive_dest;` 排查目的地路径/权限/网络问题，修复后DEST_STATE = DEFER再ENABLE。
5. 验证ARCn恢复：多次`ALTER SYSTEM SWITCH LOGFILE;`，再查`SELECT * FROM v$archive_dest_status;`无ERROR。

**4. RMAN删除归档安全规范：**
安全步骤：①确认过期归档已备份到磁带/远程；②`RMAN> REPORT OBSOLETE;`预演；③`RMAN> DELETE OBSOLETE;`同时删物理文件+更新RMAN元数据。
为何严禁OS rm：OS rm只删物理文件，RMAN存储库仍记录存在，后续BACKUP/RESTORE会报错找不着文件。
误rm后纠正：①`RMAN> CROSSCHECK ARCHIVELOG ALL;`核对物理文件，标记不存在的为EXPIRED；②`RMAN> DELETE EXPIRED ARCHIVELOG ALL;`清理RMAN元数据。

</details>

<details>
<summary>分析题答案与SQL</summary>

**1. 日志组操作SQL编程题：**
```sql
-- 第①步：新增第4组（500M，2成员）
ALTER DATABASE ADD LOGFILE GROUP 4 (
  '/u01/app/oracle/oradata/ORCL/redo04a.log',
  '/u02/app/oracle/oradata/ORCL/redo04b.log'
) SIZE 500M;

-- 第②步：向第4组追加第3成员
ALTER DATABASE ADD LOGFILE MEMBER
  '/u03/app/oracle/oradata/ORCL/redo04c.log' REUSE
  TO GROUP 4;

-- > [!danger] 前提检查：删除前必须确认G4状态为INACTIVE，且删除后总组数≥2
-- 先确认G4状态：
SELECT group#, status, members FROM v$log;
-- 若G4是CURRENT：ALTER SYSTEM SWITCH LOGFILE; 循环切换几次直到INACTIVE
-- 若G4是ACTIVE：等检查点+归档完成再查

-- > [!danger] 删除前必须确认删除后总组数仍≥2，这里假设原来3组，删后剩3组≥2，满足
ALTER DATABASE DROP LOGFILE GROUP 4;

-- > [!danger] 若要删除某成员，必须保证该组删除后成员仍≥2
-- 删除第4组第3成员（假设G4仍存在，删后剩2成员≥2）：
ALTER DATABASE DROP LOGFILE MEMBER
  '/u03/app/oracle/oradata/ORCL/redo04c.log';
```

**2. ARCHIVELOG切换完整演练：**
```sql
-- 步骤1：干净关库（SQL*Plus）
SHUTDOWN IMMEDIATE;

-- 步骤2：启动到MOUNT
STARTUP MOUNT;

-- 步骤3：切换为归档模式
ALTER DATABASE ARCHIVELOG;

-- 步骤4：打开
ALTER DATABASE OPEN;

-- 步骤5：验证模式
ARCHIVE LOG LIST;
SELECT name, log_mode FROM v$database; -- LOG_MODE=ARCHIVELOG

-- 步骤6：配置2个本地归档目的地+格式
ALTER SYSTEM SET LOG_ARCHIVE_DEST_1 =
  'LOCATION=/u01/arch/ORCL VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME=ORCL'
  SCOPE=BOTH;
ALTER SYSTEM SET LOG_ARCHIVE_DEST_2 =
  'LOCATION=/u02/arch/ORCL VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME=ORCL'
  SCOPE=BOTH;

-- 归档格式（SPFILE级别，重启生效）
ALTER SYSTEM SET LOG_ARCHIVE_FORMAT='%t_%s_%r.dbf' SCOPE=SPFILE;

-- 最少成功归档数=2
ALTER SYSTEM SET LOG_ARCHIVE_MIN_SUCCEED_DEST=2 SCOPE=BOTH;

-- 步骤7：立即RMAN全备
$ rman target /
RMAN> RUN {
   allocate channel c1 type disk format '/backup/rman/%d_full_%U.bak';
   BACKUP DATABASE PLUS ARCHIVELOG DELETE ALL INPUT;
   BACKUP CURRENT CONTROLFILE FORMAT '/backup/rman/%d_cf_%U.bak';
   BACKUP SPFILE FORMAT '/backup/rman/%d_spfile_%U.bak';
   release channel c1;
}
```

**3. 归档目的地ERROR状态排查：**
(1) 三条可能原因：①路径不存在或权限错误；②磁盘空间满；③NFS挂载盘掉了。
(2) 排查命令：
①OS：`ls -ld /u02/arch/ORCL` 看权限；`touch /u02/arch/ORCL/test` 看是否可写；`su - oracle` 下验证oracle用户是否有权限。
②OS：`df -h /u02/arch/ORCL` 看空间；
③OS：`mount | grep /u02` 看是否NFS，`ls /u02` 看挂载是否还活着。
(3) 修复：①`mkdir -p /u02/arch/ORCL && chown oracle:oinstall /u02/arch/ORCL && chmod 750 /u02/arch/ORCL`；②扩容或清理；③`mount /u02` 重新挂载。验证：`ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_2 = DEFER; ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_2 = ENABLE;` 再`SELECT status, error FROM v$archive_dest WHERE dest_id=2;`应为VALID/null。

**4. FRA ORA-19809处理：**
(1) 三步方案：
第一步（紧急扩容）：`ALTER SYSTEM SET DB_RECOVERY_FILE_DEST_SIZE='800G' SCOPE=BOTH;`——最快，无需删数据。
第二步（备份后删除）：
```
RMAN> RUN {
   allocate channel t1 type sbt_tape; -- 假设有磁带
   BACKUP RECOVERY AREA DELETE INPUT;
   release channel t1;
}
RMAN> DELETE OBSOLETE;
```
第三步（长期）：调大FRA大小上限；调整保留策略窗口；定期自动执行上述备份脚本。
(2) 为何SPACE_RECLAIMABLE有50G仍报错：SPACE_RECLAIMABLE是理论上可回收的OBSOLETE备份大小，但Oracle在写新文件前不会自动触发DELETE，实际可用空间=SPACE_LIMIT-SPACE_USED。需要手动执行DELETE OBSOLETE才会真正释放物理空间。

</details>

<details>
<summary>综合题答案与完整推导</summary>

**1. CURRENT组丢失场景完整处理：**
(1) 处理步骤：
①保护现场，防止扩大：不做常规SHUTDOWN IMMEDIATE（会触发更多写CURRENT组），直接：`SHUTDOWN ABORT;`
②备份当前所有现存文件（防止操作错误二次破坏）：OS级备份数据文件、控制文件、剩余在线日志。
③启动到MOUNT：`STARTUP MOUNT;`
④查看在线日志状态：`SELECT group#, status FROM v$log;` 确认G3是CURRENT且成员全坏。
⑤重建控制文件流程（UNTIL CANCEL恢复）：
```sql
RECOVER DATABASE USING BACKUP CONTROLFILE UNTIL CANCEL;
-- 提示输入归档日志：一路AUTO应用到最后，当提示需要G3的CURRENT日志时，输入CANCEL取消
CANCEL
```
⑥OPEN RESETLOGS：`ALTER DATABASE OPEN RESETLOGS;`
⑦`> [!danger] 立即新全备！` 因为OPEN RESETLOGS后旧归档、旧备份大部分失效。RMAN全备：
```
RMAN> BACKUP AS COMPRESSED BACKUPSET DATABASE PLUS ARCHIVELOG;
RMAN> BACKUP CURRENT CONTROLFILE;
RMAN> BACKUP SPFILE;
```

(2) 数据丢失评估：G3（CURRENT组）中所有已COMMIT但日志切换尚未进入后续组的事务——其重做记录随G3物理损坏永久丢失，数据无法恢复。所有已切换到G3之前组（即已归档或已进入INACTIVE）的事务无影响。
(3) OPEN RESETLOGS后必须立刻做全新全备，因为RESETLOGS后日志序列号从1重新开始，新数据库分支（Incarnation）产生，之前的备份大部分无法用于恢复新分支。
(4) 架构改进：①每组至少4个成员，分散到4块独立物理磁盘或ASM磁盘组（NORMAL/HIGH冗余）；②使用FRA做在线日志成员的第二镜像；③Data Guard物理备库同步重做流，主库CURRENT丢失可failover到备库。

**2. 生产归档维护策略设计：**
(1) 初始化参数SQL：
```sql
ALTER SYSTEM SET DB_RECOVERY_FILE_DEST='/u02/fra/ORCL' SCOPE=BOTH;
ALTER SYSTEM SET DB_RECOVERY_FILE_DEST_SIZE='2T' SCOPE=BOTH;

ALTER SYSTEM SET LOG_ARCHIVE_DEST_1 =
  'LOCATION=/u01/arch/ORCL VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME=ORCL' SCOPE=BOTH;
ALTER SYSTEM SET LOG_ARCHIVE_DEST_2 =
  'LOCATION=/u02/arch/ORCL VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME=ORCL' SCOPE=BOTH;
ALTER SYSTEM SET LOG_ARCHIVE_MIN_SUCCEED_DEST=2 SCOPE=BOTH;
ALTER SYSTEM SET LOG_ARCHIVE_FORMAT='%t_%s_%r.dbf' SCOPE=SPFILE;
ALTER SYSTEM SET FAST_START_MTTR_TARGET=300 SCOPE=BOTH; -- 5分钟恢复目标
```
(2) RMAN持久化配置：
```
RMAN> CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 30 DAYS;
RMAN> CONFIGURE CONTROLFILE AUTOBACKUP ON;
RMAN> CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '/backup/rman/cf_%F';
RMAN> CONFIGURE DEVICE TYPE DISK PARALLELISM 2 BACKUP TYPE TO COMPRESSED BACKUPSET;
RMAN> CONFIGURE DEVICE TYPE SBT_TAPE PARALLELISM 2;
RMAN> CONFIGURE DEFAULT DEVICE TYPE TO DISK;
RMAN> CONFIGURE ARCHIVELOG DELETION POLICY TO APPLIED ON ALL STANDBY BACKED UP 1 TIMES TO SBT_TAPE;
```
(3) 每日归档维护脚本 `daily_arch.sh`：
```bash
#!/bin/bash
export ORACLE_SID=ORCL
export ORACLE_HOME=/u01/app/oracle/product/19.0.0/dbhome_1
export PATH=$ORACLE_HOME/bin:$PATH
rman target / <<EOF
RUN {
  ALLOCATE CHANNEL t1 TYPE SBT_TAPE PARMS 'ENV=(NB_ORA_CLIENT=oradbprod)';
  ALLOCATE CHANNEL t2 TYPE SBT_TAPE PARMS 'ENV=(NB_ORA_CLIENT=oradbprod)';
  BACKUP ARCHIVELOG ALL NOT BACKED UP 1 TIMES DELETE ALL INPUT;
  RELEASE CHANNEL t1;
  RELEASE CHANNEL t2;
}
DELETE OBSOLETE;
REPORT NEED BACKUP DATABASE;
REPORT OBSOLETE;
EXIT;
EOF
```
(4) 监控脚本：
```sql
-- FRA使用率（>85%告警）
SELECT round(space_used/space_limit*100,2) pct_used,
       round(space_reclaimable/space_limit*100,2) pct_reclaim
FROM v$recovery_file_dest;

-- 目的地ERROR
SELECT dest_id, status, error FROM v$archive_dest WHERE status <> 'VALID';

-- 日志切换频率（小时级）
SELECT to_char(first_time,'YYYY-MM-DD HH24') h, count(*) sw
FROM v$log_history WHERE first_time >= trunc(sysdate)-1
GROUP BY to_char(first_time,'YYYY-MM-DD HH24') ORDER BY h DESC;
```

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | WAL原则、日志组状态、多路复用最低要求、归档模式切换、ORA-00257/19809、检查点、SWITCH vs ARCHIVE CURRENT、RMAN vs rm、CURRENT丢失处理 |
| 多选 | 5 | 15 | LGWR触发条件、日志组状态、ARCHIVELOG恢复能力、完全检查点触发、FRA文件类型 |
| 判断 | 5 | 10 | WAL顺序、删除后多路复用最低限、切换后旧备份失效、MTTR单位、OS rm后RMAN操作 |
| 简答 | 4 | 20 | 日志组6状态+转换、三类检查点对比、ORA-00257步骤、RMAN删除安全规范+OS rm纠正 |
| 分析 | 4 | 32 | 日志组操作SQL+危险标注、归档模式切换SQL演练、归档目的地ERROR排查、FRA ORA-19809处理 |
| 综合 | 2 | 20 | CURRENT组丢失完整处理（含数据丢失评估+架构改进）、生产归档维护策略（参数+RMAN配置+备份脚本+监控） |
| 合计 | 30 | 117 | 覆盖第7章全部核心考点，重故障场景分析与SQL/RMAN编程 |

## 章节导航

- 上级MOC：[[MOC - Oracle数据库管理]]
- 本章知识点：[[MOC - 第7章]]（[[7.1 联机重做日志组工作机制]]、[[7.2 ARCH归档模式开启与关闭]]、[[7.3 日志切换、检查点]]、[[7.4 归档日志维护策略]]）
- 上一章习题：[[MOC - 第6章习题]]
- 下一章习题：[[MOC - 第8章习题]]
