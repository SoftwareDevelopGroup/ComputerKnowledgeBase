---
domain: 数据库技术
subject: Oracle数据库管理
type: exercise
chapter: 第3章 Oracle实例与存储结构
section: 3.1 内存结构SGA、PGA
tags: [Oracle,习题,DBA,SGA,PGA,后台进程,表空间,数据文件,重做日志,段,块]
prerequisites: ["数据库原理", "MOC - 第3章 Oracle实例与存储结构"]
---

# MOC - 第3章 Oracle实例与存储结构 习题

> [!tip] 做题建议
> 本章习题核心偏DBA实战诊断：SGA命中率调优、LGWR/DBWn触发条件、物理文件丢失恢复、表空间/段/块管理SQL。建议结合实验环境实操每一条SQL。

---

## 一、单选题（10题×2分=20分）

### 1.
用户执行COMMIT提交事务时，以下哪个后台进程会立即被触发写盘？（  ）
A. DBWn 把脏块写盘
B. LGWR 把Redo Buffer写在线日志
C. CKPT 触发检查点
D. ARCn 归档日志

<details>
<summary>查看答案</summary>
**B**。Oracle快速提交机制Fast-Commit：COMMIT返回的唯一条件是LGWR成功写Redo日志（含COMMIT记录）到磁盘，不需要DBWn写数据块（延迟写）。
</details>

### 2.
以下哪个SGA组件不存在？（  ）
A. Shared Pool共享池
B. Large Pool大型池
C. Temporary Pool临时池
D. Redo Log Buffer重做日志缓冲区

<details>
<summary>查看答案</summary>
**C**。Oracle SGA五大组件：DB Buffer Cache、Shared Pool、Large Pool、Java Pool、Redo Log Buffer（可选Streams Pool/In-Memory池）。没有Temporary Pool，临时段在TEMP临时表空间磁盘中。
</details>

### 3.
以下关于LGWR触发条件描述错误的是？（  ）
A. 用户COMMIT提交
B. 每10秒超时（10秒写一次）
C. Redo Log Buffer 1/3满或超过1MB
D. DBWn写脏块前检查Redo同步（SCN一致性）

<details>
<summary>查看答案</summary>
**B**。LGWR超时是**每3秒**写一次，不是10秒。其他3个是正确的5大触发条件。
</details>

### 4.
控制文件损坏了其中一个多路复用成员（control_files='/c1/c1.ctl','/c2/c2.ctl'，/c2磁盘坏了c2.ctl损坏丢失），数据库当前OPEN状态。正确的恢复步骤是？（  ）
A. 直接操作系统cp /c1/c1.ctl /c2/c2.ctl → 重启
B. SHUTDOWN ABORT → cp好的覆盖坏的 → STARTUP
C. SHUTDOWN IMMEDIATE → 操作系统层面复制好的控制文件覆盖损坏的 → STARTUP
D. 执行CREATE CONTROLFILE重建控制文件

<details>
<summary>查看答案</summary>
**C**。步骤：①一致性关库SHUTDOWN IMMEDIATE（不能ABORT会破坏好的控制文件）；②OS复制好的控制文件到损坏成员路径；③STARTUP启动。A错误：数据库OPEN状态下复制的控制文件不一致（SCN不匹配）；B错误：ABORT风险；D太复杂，只有全部控制文件丢失才重建。
</details>

### 5.
Oracle在线重做日志组至少应该有几组？每组至少应该有几个多路复用成员？（  ）
A. 至少1组，每组至少1个成员
B. 至少2组，每组至少2个成员
C. 至少3组，每组至少3个成员
D. 至少4组，每组可以1个成员

<details>
<summary>查看答案</summary>
**B**。官方最佳实践：至少**2组Redo日志组**（循环写至少2组）；**每组至少2个多路复用成员**，成员存放在不同物理磁盘。
</details>

### 6.
Oracle四层逻辑存储结构从大到小正确顺序是？（  ）
A. Block块→Extent区→Segment段→Tablespace表空间
B. Tablespace表空间→Segment段→Extent区→Block块
C. Tablespace表空间→Extent区→Segment段→Block块
D. Segment段→Tablespace表空间→Extent区→Block块

<details>
<summary>查看答案</summary>
**B**。从大到小：表空间→段（表/索引）→区（连续块）→块（最小I/O单元默认8KB）。
</details>

### 7.
以下哪个不是默认永久表空间？（  ）
A. SYSTEM
B. SYSAUX
C. TEMP
D. USERS

<details>
<summary>查看答案</summary>
**C**。TEMP是**临时**表空间（不是永久表空间），存储排序/哈希/临时段，实例重启后清空。SYSTEM/SYSAUX/USERS都是永久表空间。
</details>

### 8.
Buffer Cache命中率（OLTP系统生产理想值是？（  ）
A. ≥80%
B. ≥90%
C. ≥95%
D. ≥99%

<details>
<summary>查看答案</summary>
**D**。OLTP在线交易系统DB Buffer Cache命中率≥99%（低于95%需要加大SGA_TARGET或优化SQL减少全表扫，减少物理读）。DSS分析系统≥90%即可。
</details>

### 9.
行迁移Row Migration发生的原因是？（  ）
A. 行长超过一个Block大小（大行长）
B. UPDATE变长行增长，PCTFREE预留空间不够，整行搬到新块留转发指针
C. INSERT时一行放不下两个Block
D. DELETE操作导致块碎片

<details>
<summary>查看答案</summary>
**B**。行迁移=UPDATE变长行增长（如VARCHAR2(100)从5字节→95字节）导致原块PCTFREE预留空间不足，整行搬家到新块，原块只留一个转发指针。A是行链接Row Chaining（不是迁移）。
</details>

### 10.
用户COMMIT后，此时LGWR已经写Redo日志成功，但是DBWn还没把脏块写回数据文件。服务器断电重启后SMON会怎么处理？（  ）
A. 丢数据，因为脏块还没写盘→已提交事务丢失
B. SMON做实例恢复：应用Redo前滚所有变更→回滚未提交事务→已提交事务数据不丢失
C. 自动从RMAN备份恢复数据文件
D. 需要手动执行RECOVER DATABASE命令

<details>
<summary>查看答案</summary>
**B**。Oracle WAL预写式日志保证：只要Redo写盘成功→已提交事务永不丢失。重启OPEN阶段SMON自动实例恢复：前滚Redo（包括已提交的变更回滚到数据块）→回滚断电未提交事务→ACID。不需要手动恢复（正常OPEN自动完成）。
</details>

---

## 二、多选题（5题×3分=15分）

### 11.
DBWn数据库写进程写脏块的触发条件包括？（  ）
A. 检查点触发（CKPT触发
B. DB Buffer Cache中脏块/空闲缓冲区不足
C. 每3秒超时自动检查
D. RAC ping远程节点请求脏块
E. 表空间BEGIN BACKUP热备开始
F. 用户COMMIT提交触发

<details>
<summary>查看答案</summary>
**ABCDE**。F错误：COMMIT只触发LGWR，不触发DBWn（延迟写）。其他5个都是DBWn触发条件（共8个）。
</details>

### 12.
以下关于SGA和PGA描述正确的是？（  ）
A. SGA=所有进程共享的全局内存；PGA=每个服务器进程私有
B. SGA生命周期随实例启动/关闭；PGA随服务器进程创建/终止
C. DB Buffer Cache属于SGA；排序工作区Sort Area属于PGA
D. Shared Pool缓存SQL执行计划；PGA缓存用户会话变量
E. Oracle推荐生产用AMM（MEMORY_TARGET）自动调SGA+PGA统一管理

<details>
<summary>查看答案</summary>
**ABCD**。E错误：19c生产**不推荐**AMM（MEMORY_TARGET，tmpfs问题多，生产推荐ASMM：SGA_TARGET+PGA_AGGREGATE_TARGET分开自动调）。
</details>

### 13.
以下哪些属于表空间Tablespace的正确特性？（  ）
A. 一个表空间可以属于多个数据库
B. 一个表空间可以包含一个或多个数据文件
C. 表空间可以在OPEN状态下OFFLINE/ONLINE（SYSTEM/UNDO/TEMP默认除外）
D. LMT本地管理表空间使用位图块管理Extent，是19c默认创建方式
E. 表空间可以READ ONLY只读模式做冷备

<details>
<summary>查看答案</summary>
**BCDE**。A错误：一个表空间只能属于一个数据库（Database中的表空间，全局唯一在当前库）。一个数据库可以有多个表空间；一个表空间可以有多个数据文件，正确。
</details>

### 14.
以下关于Redo日志组状态描述正确的是？（  ）
A. CURRENT：LGWR当前正在写入的组
B. ACTIVE：刚切换下来的组，实例崩溃SMON做实例恢复还需要这组Redo，ARCn还没归档完不能覆盖
C. INACTIVE：检查点已推进+ARCn归档完成（归档模式），可以被LGWR循环覆盖重用
D. DROP LOGFILE GROUP 3时GROUP3状态必须是CURRENT才能删除
E. 日志切换时执行ALTER SYSTEM SWITCH LOGFILE;

<details>
<summary>查看答案</summary>
**ABCE**。D错误：删除日志组必须是**INACTIVE状态（CURRENT/ACTIVE都不能删！删CURRENT组会导致实例崩溃。先切到其他组等ARCn归档完变INACTIVE才能删。
</details>

### 15.
以下关于后台进程唯一性和启动条件正确的是？（  ）
A. LGWR严格唯一：实例中只能有1个LGWR进程，负责Redo顺序写保证一致性
B. DBWn可以启动多个（DBW0~DBW9、DBWa~DBWz，最多100+），多进程写脏块增加吞吐量
C. PMON和SMON都是唯一的
D. ARCn归档进程只在数据库处于ARCHIVELOG模式时才启动
E. CKPT检查点进程在检查点时才启动，平时不运行

<details>
<summary>查看答案</summary>
**ABCD**。E错误：CKPT检查点进程是常驻进程，一直运行。平时每3秒推进检查点队列RBA指针（增量检查点），检查点事件时更新控制文件和数据文件头SCN。
</details>

---

## 三、判断题（5题×2分=10分）

### 16.
Shared Pool Library Cache命中率太低，原因一般是大表全表扫描导致，应该加大DB_CACHE_SIZE。（  ）

<details>
<summary>查看答案</summary>
**×**。Library Cache命中率低→SQL没有绑定变量，硬解析频繁（CPU飙升）。应该：①加大SHARED_POOL_SIZE参数；②SQL改成绑定变量；③设置CURSOR_SHARING=FORCE临时顶。DB_CACHE_SIZE解决Buffer Cache命中率（物理读）。
</details>

### 17.
用户执行DELETE大表删除所有1亿行后，表占用的空间会自动释放给其他段使用（表空间可用空间增加）。（  ）

<details>
<summary>查看答案</summary>
**×**。DELETE操作只删除行数据，段占用的Extent/Block不会释放（HWM高水位线不变），段大小不变（占用空间不变。查询全表扫还是扫原来的HWM以下所有块。需要用：①TRUNCATE TABLE（DDL立即释放段）；②ALTER TABLE xxx SHRINK SPACE（ASSM段收缩回收）；③ALTER TABLE xxx MOVE（重建表段）才能释放空间。
</details>

### 18.
TEMP临时表空间数据文件丢失损坏，数据库仍然可以正常OPEN，只是大排序/哈希连接操作会报错。（  ）

<details>
<summary>查看答案</summary>
**√**。TEMP临时文件属于临时表空间，实例重启TEMP自动重建，丢失不会导致数据库不能OPEN。但大排序（ORDER BY/GROUP BY）、大哈希连接、CREATE INDEX等需要临时段操作会报ORA-25153临时表空间为空。修复：删除旧的TEMPFILE+新建TEMPFILE即可。
</details>

### 19.
在线Redo日志组只有在INACTIVE状态下才能被ARCn归档后才能被LGWR循环覆盖重写。（  ）

<details>
<summary>查看答案</summary>
**√**（归档模式下成立）。CURRENT正在写→ACTIVE（实例恢复还需要+ARCn没归档完→不能覆盖重写）→INACTIVE（检查点已推进ARCn已归档完成→可以覆盖。NOARCHIVELOG模式：检查点推进ACTIVE→INACTIVE就能覆盖，不需要ARCn归档（NOARCHIVELOG模式没有ARCn进程。题目默认归档模式，正确。
</details>

### 20.
LMT本地管理表空间使用数据字典表（FETS$/UET$）管理区分配，产生递归SQL性能较差。（  ）

<details>
<summary>查看答案</summary>
**×**。题目描述的是**DMT字典管理**（已淘汰）。LMT本地管理是用数据文件头部的Bitmap位图管理区分配/回收，无递归SQL性能好，19c默认创建。
</details>

---

## 四、简答题（4题×5分=20分）

### 21.
说明Oracle WAL预写式日志Write-Ahead Logging机制：用户提交COMMIT时LGWR和DBWn分别做什么？为什么这样设计？有什么优势？

<details>
<summary>查看答案</summary>

**COMMIT瞬间流程（Fast-Commit快速提交：
1. 服务器进程把COMMIT记录（含SCN号写Redo Log Buffer
2. **立即触发LGWR**把该事务的所有Redo条目（变更记录+COMMIT记录）顺序写到在线重做日志文件
3. LGWR写盘成功后→返回给用户`Commit complete`（此时用户得到提交成功响应
4. **此时DBWn不立即写脏块**（脏块在Buffer Cache，延迟写）
5. DBWn后续批量合并I/O写脏块（检查点/脏块不足/3秒超时才写

**WAL设计优势**：
① **已提交事务永不丢失（持久性Durability）**：Redo在磁盘→哪怕脏块没写断电→重启SMON前滚Redo恢复所有已提交
② **提交响应极快（毫秒级**：Redo顺序写（512字节块连续写，磁盘顺序写比随机写数据快几十上百倍；DBWn延迟写脏块不阻塞COMMIT提交
③ **I/O批量合并减少随机I/O次数**：脏块合并相邻块一次写盘，减少DBWR写次数，降低磁盘IOPS
</details>

### 22.
对比说明DMT字典管理 vs LMT本地管理表空间（Extent区管理方式）的区别。19c生产推荐哪种？为什么？

<details>
<summary>查看答案</summary>

| 维度 | DMT字典管理（Dictionary Managed | LMT本地管理（Locally Managed Tablespace |
|---|---|---|
| 区分配/回收方式 | 数据字典基表FETS$/UET$记录空闲/已用区 | 每个数据文件头部**位图块Bitmap**记录（0/1位标识空闲/使用） |
| 性能 | 分配/回收频繁查字典表→**递归SQL多→性能差+数据字典争用严重 | 更新位图极快，原子操作无递归SQL，高并发无争用 |
| 碎片 | 易产生Extent碎片，需定期`ALTER TABLESPACE xxx COALESCE;`手工合并 | 位图自动跟踪碎片合并 |
| 存储参数 | NEXT/PCTINCREASE/MINEXTENTS/MAXEXTENTS | AUTOALLOCATE Oracle自动区大小递增64K→1M→8M→64M；UNIFORM SIZE n统一大小 |
| 现状 | 8i以前默认；Oracle 9i后淘汰；19c不支持CREATE创建DMT | ✅19c默认创建+生产唯一推荐 |

**生产推荐**：LMT本地管理 + AUTOALLOCATE + ASSM段自动管理。原因：性能好、无碎片、无递归SQL、高并发下稳定。
</details>

### 23.
说明在线Redo日志的三大状态（CURRENT/ACTIVE/INACTIVE）的含义、流转条件和覆盖规则。

<details>
<summary>查看答案</summary>

| 状态 | 含义 | 何时进入 | 能否被LGWR覆盖重写 |
|---|---|---|---|
| **UNUSED** | 新建日志组从未写过（刚ADD LOGFILE后 | CREATE后 | - |
| **CURRENT** | LGWR**此刻正在写入**的组（当前组） | ALTER SYSTEM SWITCH LOGFILE切换后就变CURRENT | ❌绝对不能覆盖；实例恢复必须 |
| **ACTIVE** | 刚写满切换下来：① 检查点还没推进完（脏块还没完全写盘→崩溃SMON实例恢复还需要这组Redo；② 归档模式下ARCn还没归档完成 → 两个条件都满足才离开ACTIVE | LGWR写满后切换Next那一刻进入 | ❌不能覆盖（归档模式下没归档完覆盖会报错ORA-00257归档错误；实例恢复ACTIVE组覆盖=崩溃后恢复失败 |
| **INACTIVE** | ①检查点已推进完（脏块都写盘完成不需要实例恢复用这组Redo；②归档模式ARCn已归档完成→满足这两个条件ACTIVE→INACTIVE | 检查点CKPT推进+ARCn归档完 | ✅ 可以被LGWR循环写满覆盖重用（下一轮循环写回来覆盖 |

**流转顺序**：UNUSED→CURRENT→ACTIVE→INACTIVE→CURRENT（循环覆盖
</details>

### 24.
说明ASSM（Automatic Segment Space Management自动段空间管理 vs MSSM手动段空间管理的区别，生产用哪种？PCTFREE参数在ASSM下是否生效？

<details>
<summary>查看答案</summary>

| 维度 | MSSM手动段管理（Manual | ASSM自动段空间管理（Automatic |
|---|---|---|
| 块内空闲空间管理方式 | 空闲块链表FREELIST（链表结构+FREELIST GROUPS组 + PCTUSED参数控制（<40%使用率才能再INSERT | **位图块（3个位图块，位图中记录每个块4个状态：空/<25%/25-50%/50-75%/75-100%填充率**，自动管理 |
| 高并发INSERT性能 | 高并发INSERT：FREELIST链表头争用严重（等待事件buffer busy waits/free list waits | 位图管理，无链表争用 |
| 段空间管理参数 | FREELISTS / FREELIST GROUPS / PCTUSED（4个参数） | 无FREELIST/PCTUSED |
| 现状 | 8i前默认；不推荐 | ✅19c默认创建SEGMENT SPACE MANAGEMENT AUTO生产推荐 |
| PCTFREE作用 | ✅生效（预留UPDATE空间） | ✅仍然生效（PCTFREE控制预留多少%给UPDATE行增长，ASSM中INSERT新行时位图就不会把块填超过(100-PCTFREE)% |

**生产**：统一使用ASSM自动段空间管理，建表空间必须加`SEGMENT SPACE MANAGEMENT AUTO`。
**PCTFREE在ASSM仍然生效！**：PCTFREE=10表示块最多被INSERT填90%，留10%给UPDATE变长行增长（避免行迁移Row Migration。
</details>

---

## 五、分析实操题（4题×7分=28分）

### 25.
某Oracle 19c生产库（OLTP）AWR报告显示：
- Buffer Cache Hit Ratio = 92%
- Library Cache Hit Ratio = 78%
- Top5等待事件第一名：**free buffer waits**，第二名log file sync

请分析上述指标/等待事件的根因，给出优化建议。

<details>
<summary>查看答案</summary>

**症状分析：
① Buffer Cache命中率92%→太低（OLTP≥99%理想），空闲缓冲区不足
② Library Cache命中率78%→严重低，硬解析严重
③ free buffer waits等待→DB Buffer Cache中**空闲缓冲区严重不足**，服务器进程想读新块进Buffer Cache没空闲块→触发DBWn写脏块腾空间→等待DBWn写盘导致卡
④ log file sync→用户COMMIT等LGWR写Redo慢（COMMIT延迟大

**优化建议分四块：

① 加大SGA（解决命中率+free buffer waits：
```sql
-- 128GB RAM服务器，SGA从32GB→加大到64GB
ALTER SYSTEM SET SGA_MAX_SIZE=64G SCOPE=SPFILE;   -- 静态
ALTER SYSTEM SET SGA_TARGET=64G SCOPE=SPFILE;     -- ASMM自动调内部各组件
-- 重启实例生效
```

② 解决Library Cache命中率低（硬解析严重→78%）：
- 根因：应用SQL没绑定变量（where id=1/where id=2/where id=3每个SQL算不同硬解析
- 短期紧急缓解：`ALTER SYSTEM SET CURSOR_SHARING=FORCE SCOPE=BOTH;`（Oracle强制把字面量替换成绑定变量，副作用未知
- 长期根本解决：应用代码修改+PreparedStatement绑定变量
- 适当加大SHARED_POOL_SIZE：ALTER SYSTEM SET SHARED_POOL_SIZE=4G SCOPE=BOTH;

③ 解决log file sync等待（LGWR写Redo慢）：
- ①在线日志放到**高速SSD（甚至PCIe闪存卡），顺序写性能提升
- ②日志组太小切换太频繁→加大到2G/组+8组：`ALTER DATABASE ADD LOGFILE GROUP 5 SIZE 2G;`
- ③多路复用成员放不同物理磁盘避免I/O竞争
- ④应用过度每行COMMIT→批量COMMIT（每500~1000行COMMIT一次

④ 验证优化后监控：
- 命中率≥99%；free buffer waits等待消失；log file sync平均等待<1ms
</details>

### 26.
场景：某DBA执行RMAN热备时，归档空间满，数据库出现：
```
SQL> UPDATE hr.employees SET salary=salary*1.1;
第1行出现错误:
ORA-00257: Archiver error. Connect AS SYSDBA only until resolved.
```
请分析：①什么是ORA-00257？根因；②完整的排查+应急处理步骤（保证数据库尽快恢复业务）。

<details>
<summary>查看答案</summary>

**① 错误根因分析**：
ORA-00257 = **归档程序错误，只有AS SYSDBA才能连接直到解决
根因：ARCHIVELOG归档模式下，ARCn归档进程**归档目的（FRA闪回恢复区或本地归档目录磁盘空间满/权限只读/路径不存在→ARCn无法归档填满的在线日志组→在线Redo日志变成ACTIVE→LGWR不能覆盖重用这组→所有COMMIT DML被阻塞**→数据库HANG住

**② 排查步骤**（按顺序）：
```sql
-- 步骤1：SYS登录查看归档模式、归档目的地、FRA使用率：
archive log list;  -- 查看归档是否启用、归档目的地、当前序列号
SELECT * FROM v$recovery_file_dest;  -- 看FRA空间使用（SPACE_LIMIT/SPACE_USED
SELECT * FROM v$flash_recovery_area_usage;  -- 各文件类型FRA占比

-- 步骤2：查看归档失败原因：
SELECT dest_id, status, error, destination FROM v$archive_dest;
-- error字段可能显示：磁盘空间不足OS error或权限错误
SELECT message FROM v$dataguard_status WHERE facility='ARCn' ORDER BY timestamp;
```

**③ 恢复业务的应急处理步骤（按优先级）**：

**紧急方案A：RMAN删除过期归档（优先！生产推荐保留备份后删
```bash
# RMAN登录，删除已备份到磁带上的归档（如果备份策略有备份归档到磁带/NFS
rman target /
RMAN> CROSSCHECK ARCHIVELOG ALL;  -- 核对归档文件和RMAN仓库
RMAN> DELETE NOPROMPT EXPIRED ARCHIVELOG ALL;  -- 删除不存在的归档记录
RMAN> DELETE NOPROMPT ARCHIVELOG ALL COMPLETED BEFORE 'SYSDATE-7';  -- 删除7天前归档（应急临时删7天前
-- 或删所有已备份2次到磁带的归档：
-- DELETE NOPROMPT ARCHIVELOG ALL BACKED UP 2 TIMES TO DEVICE TYPE SBT_TAPE;
```

**方案B：FRA扩容（如果归档目录磁盘空间不够扩容更稳妥**
```sql
-- 扩大DB_RECOVERY_FILE_DEST_SIZE=FRA总上限：
ALTER SYSTEM SET DB_RECOVERY_FILE_DEST_SIZE=500G SCOPE=BOTH;
```

**方案C：归档目的地改到其他空磁盘**
```sql
-- 新增一个归档目的地到/u05/arch（空盘大空间）：
ALTER SYSTEM SET LOG_ARCHIVE_DEST_2='LOCATION=/u05/arch VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME=orcl' SCOPE=BOTH;
-- 后续ARCn会把归档写两个地方1和2
```

**验证数据库恢复**：
- RMAN删/扩容后，等ARCn自动重试归档成功（或手动切换日志触发：`ALTER SYSTEM SWITCH LOGFILE;`）
- 普通用户测试执行UPDATE/COMMIT成功=恢复
- 持续监控FRA使用率，后续优化备份策略（备份+删除归档
</details>

### 27.
某Oracle 19c数据库执行以下SQL，报错：
```
SQL> CREATE TABLE sale_order TABLESPACE users AS SELECT * FROM sh.sales WHERE 1=2;
表已创建。
SQL> ALTER TABLE sale_order ADD (c5 VARCHAR2(2000) DEFAULT LPAD('X',2000,'X'));
表已更改。
SQL> UPDATE sale_order SET c1=c1+1;
UPDATE sale_order SET c1=c1+1
*
第1行出现错误:
ORA-01653: unable to extend table SH.SALE_ORDER by 8 in tablespace USERS
```
请分析①什么是ORA-01653？②原因；③完整的解决方案SQL。

<details>
<summary>查看答案</summary>

**① 错误含义**：
ORA-01653 = 表SH.SALE_ORDER无法在USERS表空间中扩展8个块（申请新Extent分配失败）→USERS表空间**没有足够的连续空闲块空间给新Extent**，表空间满了。

**② 根因**：
- USERS表空间数据文件大小满了（USERS通常默认很小，5G左右
- UPDATE变长行+默认PCTFREE可能不够也行迁移但本质还是表空间空间不足
- 表空间AUTOEXTEND OFF或已到MAXSIZE上限

**③ 排查+解决方案SQL**：
先排查表空间使用率和数据文件状态：
```sql
-- 1. 排查USERS表空间总大小/剩余大小：
SELECT tablespace_name,
       SUM(bytes)/1024/1024 total_mb,
       SUM(bytes - SUM(NVL(f.bytes,0)/1024/1024 used_mb,
       ROUND(SUM(NVL(f.bytes,0))/SUM(t.bytes)*100 free_pct
FROM dba_data_files t LEFT JOIN dba_free_space f
  ON t.file_id = f.file_id
WHERE t.tablespace_name='USERS'
GROUP BY tablespace_name;

-- 2. 查看USERS下数据文件自动扩展参数：
SELECT file_id, file_name, autoextensible, maxbytes/1024/1024 max_mb
FROM dba_data_files WHERE tablespace_name='USERS';
```

**解决方案（三种任选组合）**：
```sql
-- 方案1：启用数据文件自动扩展AUTOEXTEND ON（最常用）
ALTER DATABASE DATAFILE '/u01/app/oracle/oradata/ORCL/users01.dbf'
AUTOEXTEND ON NEXT 500M MAXSIZE 30G;

-- 方案2：手动RESIZE扩大已存在数据文件大小（比如5GB→10GB
ALTER DATABASE DATAFILE '/u01/app/oracle/oradata/ORCL/users01.dbf' RESIZE 10G;

-- 方案3：给USERS表空间加新的第二个数据文件（加文件分散I/O
ALTER TABLESPACE USERS ADD DATAFILE '/u02/oradata/ORCL/users02.dbf'
SIZE 10G AUTOEXTEND ON NEXT 500M MAXSIZE 30G;
```

**验证**：重新执行UPDATE/INSERT成功。

**生产最佳实践**：USERS表空间默认小，通常不要用USERS放业务表。建议：
```sql
-- 业务表放到独立业务表空间（磁盘独立）：
CREATE TABLESPACE sale_tbs DATAFILE '/u02/oradata/sale01.dbf' SIZE 10G
EXTENT MANAGEMENT LOCAL AUTOALLOCATE SEGMENT SPACE MANAGEMENT AUTO;
ALTER TABLE sh.sale_order MOVE TABLESPACE sale_tbs UPDATE INDEXES;  -- 迁移业务表到独立表空间
```
</details>

### 28.
场景：误操作`DROP TABLESPACE sales_tbs INCLUDING CONTENTS;`，忘加`AND DATAFILES`。OS层面数据文件`/u02/oradata/sales01.dbf`还在磁盘上未删除。现在要恢复sales_tbs表空间。已知：数据库处于ARCHIVELOG模式，今天凌晨0点RMAN Level 0全备+归档日志备份齐全。请写出完整的恢复步骤。

<details>
<summary>查看答案</summary>

```
步骤说明：
DROP TABLESPACE sales_tbs INCLUDING CONTENTS;
注意：INCLUDING CONTENTS只删除字典表中该表空间所有段（表/索引）定义，不加AND DATAFILES操作系统数据文件物理文件真实存在（磁盘上sales01.dbf没被rm掉。

恢复方案（两方案按复杂度优先级：
```

**方案A（极简单！OS数据文件没删除的最快方案：重建控制文件法**
OS数据文件真实存在的情况下，因为DROP TABLESPACE更新了控制文件中表空间/数据文件清单（把sales_tbs从控制文件移除，但数据文件在磁盘上完好！用Create Controlfile重建控制文件时把sales01.dbf重新加回控制文件：
```sql
-- 1. 备份现有控制文件（以防搞坏）
ALTER DATABASE BACKUP CONTROLFILE TO TRACE AS '/tmp/create_ctl.sql';
ALTER DATABASE BACKUP CONTROLFILE TO '/tmp/control_bak.ctl';

-- 2. 启动到NOMOUNT
SHUTDOWN IMMEDIATE;
STARTUP NOMOUNT;

-- 3. 执行CREATE CONTROLFILE重建控制文件（从TRACE脚本提取改造，DATAFILE列表手动加入sales01.dbf
CREATE CONTROLFILE REUSE DATABASE "ORCL" RESETLOGS ARCHIVELOG
    MAXLOGFILES 16
    MAXLOGMEMBERS 3
    MAXDATAFILES 100
    MAXINSTANCES 8
    MAXLOGHISTORY 292
LOGFILE
  GROUP 1 SIZE 2G,
  GROUP 2 SIZE 2G,
  GROUP 3 SIZE 2G
DATAFILE
  '/u01/app/oracle/oradata/ORCL/system01.dbf',
  '/u01/app/oracle/oradata/ORCL/sysaux01.dbf',
  '/u01/app/oracle/oradata/ORCL/undotbs01.dbf',
  '/u01/app/oracle/oradata/ORCL/users01.dbf',
  '/u02/oradata/sales01.dbf'   -- ←关键！手动加回被DROP的表空间数据文件！
CHARACTER SET AL32UTF8;

-- 4. 恢复数据库（因为控制文件重建SCN信息要应用归档：
RECOVER DATABASE USING BACKUP CONTROLFILE;
-- 提示 AUTO → 自动应用归档；

-- 5. 打开数据库（因为用了备份控制文件，必须RESETLOGS：
ALTER DATABASE OPEN RESETLOGS;

-- 6. 验证：
SELECT tablespace_name, status FROM dba_tablespaces WHERE tablespace_name='SALES_TBS';
SELECT count(*) FROM sh.sale_order;  -- 数据完整回来
```

**方案B（标准备份恢复法）：需要RMAN备份**（方案A不行时用
复杂很多，考法一般考方案A（数据文件还存在=无需RMAN RESTORE

如果OS数据文件也被删除了（AND DATAFILES也删了→必须RMAN恢复：
```bash
# 1. RMAN恢复表空间（数据库可以保持OPEN：
RMAN> SQL 'ALTER TABLESPACE sales_tbs OFFLINE IMMEDIATE;';
RMAN> RESTORE TABLESPACE sales_tbs;
RMAN> RECOVER TABLESPACE sales_tbs;
RMAN> SQL 'ALTER TABLESPACE sales_tbs ONLINE;';

# 2. 或按时间点PITR恢复DROP前时刻：
RMAN> RUN {
SET UNTIL TIME "TO_DATE('2024-01-01 09:59:00','YYYY-MM-DD HH24:MI:SS')";
RESTORE DATABASE;
RECOVER DATABASE;
}
SQL> ALTER DATABASE OPEN RESETLOGS;
```

**本题推荐方案A**：数据文件磁盘没删，用Create Controlfile重建控制文件把数据文件加回控制文件最简单，不丢数据。
</details>

---

## 六、综合设计题（2题×8分=16分）

### 29.
某大型电商交易库Oracle 19c EE，服务器配置：48核CPU、512GB RAM、8块4TB NVMe SSD做ASM DATA磁盘组、4块4TB SSD做FRA闪回恢复区。业务特点：60万TPS高并发OLTP订单提交+大量大并发查询报表（同一库）。请设计Oracle内存参数和表空间架构（至少8张表空间规划）。

<details>
<summary>查看答案</summary>

**一、内存参数设计（ASMM自动SGA+PGA分开）**：
512GB RAM：OS保留约10%=50GB（内核+buffer cache + 其他进程≈余462GB给Oracle
SGA分配：SGA_MAX_SIZE=360G / SGA_TARGET=360G（≈78%给SGA，Buffer Cache占大头
PGA分配：PGA_AGGREGATE_TARGET=96G（≈20%给PGA，大排序+大并发查询报表需要大PGA
```sql
ALTER SYSTEM SET SGA_MAX_SIZE=360G SCOPE=SPFILE;
ALTER SYSTEM SET SGA_TARGET=360G SCOPE=SPFILE;
ALTER SYSTEM SET PGA_AGGREGATE_TARGET=96G SCOPE=BOTH;
-- AMM不使用（MEMORY_TARGET=0）
ALTER SYSTEM SET MEMORY_TARGET=0 SCOPE=SPFILE;
ALTER SYSTEM SET MEMORY_MAX_TARGET=0 SCOPE=SPFILE;

-- 手动分配关键SGA组件下限（ASMM自动不会低于下限
ALTER SYSTEM SET SHARED_POOL_SIZE=16G SCOPE=SPFILE;   -- 60万TPS大量SQL必须大共享池防硬解析
ALTER SYSTEM SET DB_CACHE_SIZE=256G SCOPE=SPFILE;     -- Buffer Cache大头，热数据订单/用户/商品表缓存
ALTER SYSTEM SET LARGE_POOL_SIZE=16G SCOPE=SPFILE;    -- RMAN备份+并行查询报表共享服务器
-- Redo Buffer隐含自动调整，不用手动设LOG_BUFFER

-- PGA参数（60万并发查询报表，自动PGA管理，大SQL工作区上限：
ALTER SYSTEM SET PGA_AGGREGATE_LIMIT=128G SCOPE=BOTH;  -- PGA硬上限（防止单个SQL吃掉所有内存）
ALTER SYSTEM SET SORT_AREA_SIZE=0 SCOPE=BOTH;          -- 保持自动（手动设会禁用自动PGA
```

**二、ASM磁盘组规划（8块DATA SSD / 4块FRA SSD）**：
- DATA磁盘组：8块SSD Normal冗余（2向镜像，可用容量≈16TB）→存数据文件/控制文件/在线Redo日志
- FRA磁盘组：4块SSD Normal冗余（可用≈8TB）→归档日志、RMAN备份集、闪回日志、控制文件多路复用、Redo成员多路复用

| 磁盘组 | 磁盘数 | 冗余 | 容量 | 存什么文件 |
|---|---|---|---|---|
| +DATA | 8 NVMe SSD 4TB | NORMAL(2镜像) | 8×4TB/2≈16TB | 数据文件、控制文件在线日志成员1 |
| +FRA | 4 SSD 4TB | NORMAL(2镜像) | 4×4TB/2≈8TB | 归档日志、RMAN备份、闪回日志、控制文件成员2、Redo成员2 |
| +REDO（可选新增2块SSD | 2 SSD | HIGH(3镜像) | 冗余用 | 在线日志组专用磁盘（减少LGWR和DATA I/O竞争） |

**三、表空间架构设计（至少8张表空间）
按冷热、业务模块、对象类型分表空间：

| 序号 | 表空间名 | 对象类型 | 用途 | 初始大小 |
|---|---|---|---|---|
| 1 | SYSTEM | 系统表空间 | 数据字典 | 2G（默认） |
| 2 | SYSAUX | 系统辅助 | AWR/ASH/OEM组件 | 5G（默认 |
| 3 | UNDOTBS1 | UNDO撤销表空间 | 回滚+读一致性 | 32G（高并发OLTP大UNDO） |
| 4 | TEMP | 临时表空间 | 排序/哈希/临时表 | 64G（大报表查询排序大临时段） |
| 5 | ORDER_DATA | 订单模块数据表空间 | 订单表/订单明细表/退款表等热表 | 500G |
| 6 | ORDER_IDX | 订单模块索引表空间 | 订单表所有索引独立 | 300G |
| 7 | USER_DATA | 用户/商品数据表空间 | 用户表、商品表、地址表 | 200G |
| 8 | USER_IDX | 用户/商品索引表空间 | 对应索引 | 120G |
| 9 | REPORT_DATA | 报表历史冷数据表空间（只读+压缩） | 历史订单/报表（按月分区，历史只读，压缩节省空间 | 1TB（高级压缩OLTP压缩） |
| 10 | LOB_DATA | LOB大对象表空间 | 商品图片CLOB/BLOB、物流轨迹 | 1TB |
| 11 | USERS | 默认用户表空间 | 测试用户/临时对象 | 10G（不存业务 |

**建表空间SQL示例：
```sql
CREATE BIGFILE TABLESPACE order_data DATAFILE '+DATA' SIZE 500G
AUTOEXTEND ON NEXT 10G MAXSIZE UNLIMITED
EXTENT MANAGEMENT LOCAL AUTOALLOCATE
SEGMENT SPACE MANAGEMENT AUTO
DEFAULT COMPRESS FOR OLTP;  -- 订单表启用OLTP高级压缩
CREATE TABLESPACE order_idx DATAFILE '+DATA' SIZE 300G
AUTOEXTEND ON NEXT 5G MAXSIZE 16T
EXTENT MANAGEMENT LOCAL AUTOALLOCATE SEGMENT SPACE MANAGEMENT AUTO;
CREATE BIGFILE TABLESPACE report_data DATAFILE '+DATA' SIZE 1T
EXTENT MANAGEMENT LOCAL AUTOALLOCATE SEGMENT SPACE MANAGEMENT AUTO
DEFAULT ROW STORE COMPRESS ADVANCED;  -- 报表历史表高级压缩只读
ALTER TABLESPACE report_data READ ONLY;  -- 历史数据变成只读（不产生UNDO/Redo
```

**四、Redo日志规划：
- 16组Redo日志组，每组大小8G
- 每组3个成员（DATA 1个 + FRA 1个 + REDO磁盘组1个）=3路多路复用
- 目标切换每30分钟切一次

```sql
-- 8组→16组
BEGIN
 FOR i IN 4..16 LOOP
  EXECUTE IMMEDIATE 'ALTER DATABASE ADD LOGFILE GROUP '||i||' (
    ''+DATA'', ''+FRA'', ''+REDO''
  ) SIZE 8G';
 END LOOP;
END;
/
```

**五、检查点调优**：
```sql
ALTER SYSTEM SET FAST_START_MTTR_TARGET=60 SCOPE=BOTH;  -- 实例恢复目标60秒，调CKPT检查点频率
```
</details>

### 30.
某Oracle 19c 两节点RAC集群，节点1异常宕机（硬件故障），存储完好。节点2正常。请回答：①此时业务是否中断？为什么？②实例重启顺序和恢复步骤详解；③SMON在节点2实例恢复中做什么？④应用透明故障转移TAF怎么配置保障连接不断？

<details>
<summary>查看答案</summary>

**① 业务不中断！**
Oracle RAC是多实例共享存储架构：节点1宕机（其Instance 1崩溃，但**数据库物理文件（.dbf/.ctl/.log在共享存储上完好无损）**，节点2 Instance 2 正常运行，业务自动漂移到节点2继续处理。
缓存融合（Cache Fusion）节点2会接管节点1持有的锁资源+重做日志，SMON自动在节点2上**做节点1的实例恢复（Instance Recovery/Crash Recovery）**，整个过程自动完成DBA无需手工RECOVER。

**② 宕机场景的RAC完整恢复步骤**：

```
第一阶段：RAC自动故障转移（0-5分钟自动完成，无人工
1. 节点1硬件宕机→CSS集群件检测到节点1网络心跳/磁盘心跳超时→驱逐节点1（Split Brain脑裂保护）
2. 节点2存活→接管整个集群资源（VIP/VIP漂移到节点2；SCAN IP漂移；Service从节点1失败的服务重定位到节点2
3. 节点2的SMON进程自动启动**前滚+回滚节点1的实例恢复：
   - 读取节点1的Redo线程1日志→应用所有已提交变更到数据块前滚（Cache Recovery
   - 回滚节点1未提交的事务（Transaction Recovery）
   - UNDO段自动回滚未提交事务
4. 应用TAF（Transparent Application Failover配置后→JDBC/OCI客户端自动重连到节点2→SELECT查询断点续传→用户无感，业务继续
5. DBA视角：业务不中断（5分钟VIP漂移+恢复）

第二阶段：人工修复节点1硬件后（第N天修完硬件）
1. 修复节点1硬件（换CPU/内存/主板/磁盘等
2. 节点1开机网络配置OK→GI集群自动启动（GI设为开机自启=enable
3. DBA节点1上启动GI+ASM+RDBMS实例：
   # 节点1 root执行（GI已自动启动后确认实例：
   srvctl status database -d orcl  # 应该显示：实例orcl1节点1运行、orcl2节点2运行
   -- 如果节点1实例未启动：
   srvctl start instance -d orcl -i orcl1 -n node1
4. 验证集群：
   SELECT inst_id, instance_name, status, host_name FROM gv$instance;
   -- 两行输出：inst_id=1（节点1）/2（节点2）都是OPEN
5. 验证服务：
   srvctl status service -d orcl   -- 服务运行在两个节点
6. Rebalance负载均衡：Services自动按配置的 preferred/available 节点分配连接
```

**③ 节点2 SMON做节点1的实例恢复详细流程**：
1. **前滚阶段（Rolling Forward/Cache Recovery**：
   - 从节点1 Redo Thread 1（在线日志线程1，RAC每个实例有独立Redo线程）读取节点1的所有Redo记录
   - 应用所有变更Redo条目到SGA Buffer Cache的数据块（包括未提交的）
   - 数据文件中崩溃瞬间的数据块恢复到崩溃前状态
2. **回滚阶段（Rolling Back/Transaction Recovery**：
   - 查找节点1崩溃时所有未提交事务（对应UNDO段的TX锁）
   - 读取对应UNDO数据→撤销所有未提交变更→事务回滚
   - 释放所有节点1持有的Enqueue锁、Buffer Pin等资源
3. **资源释放完**→节点2可以处理这些锁的新请求→业务完全正常
4. 恢复速度通常秒级-分钟级，依据FAST_START_MTTR_TARGET和节点1当时Redo量

**④ 应用端TAF透明故障转移配置方案**：

**Step1：Server端创建Service（Server-side TAF，用srvctl，客户端不用改）**：
```bash
# 创建服务oltp_srv（订单交易服务），首选节点1/2，TAF类型BASIC：
srvctl add service -d orcl -s oltp_srv \
  -preferred orcl1,orcl2 \
  -tafpolicy BASIC \
  -failovertype SELECT \     -- SELECT查询断点续传（结果集自动重查）
  -failovermethod BASIC \    -- 失败后才创建备用连接
  -failoverretry 180 \       -- 重试180次
  -failoverdelay 5           -- 每次重试间隔5秒
srvctl start service -d orcl -s oltp_srv
```

**Step2：客户端tnsnames.ora配置SCAN+Service+客户端TAF**：
```
# 使用SCAN IP（RAC 11g+SCAN=3个IP负载均衡+故障转移）：
OLTP_SRV =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (LOAD_BALANCE = ON)
      (FAILOVER = ON)
      (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.1.30)(PORT = 1521)) # SCAN VIP1
      (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.1.31)(PORT = 1521)) # SCAN VIP2
      (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.1.32)(PORT = 1521)) # SCAN VIP3
    )
    (CONNECT_DATA =
      (SERVICE_NAME = oltp_srv.example.com)
      (FAILOVER_MODE =
        (TYPE = SELECT)         -- SELECT查询自动重连+续跑查询
        (METHOD = BASIC)
        (RETRIES = 180)
        (DELAY = 5)
      )
    )
  )
```

**Step3：JDBC应用连接串（Java应用推荐UCP连接池+Fast Connection Failover）：
```
jdbc:oracle:thin:@(DESCRIPTION=
  (ADDRESS_LIST=(LOAD_BALANCE=ON)(FAILOVER=ON)
    (ADDRESS=(PROTOCOL=TCP)(HOST=192.168.1.30)(PORT=1521))
    (ADDRESS=(PROTOCOL=TCP)(HOST=192.168.1.31)(PORT=1521)))
  (CONNECT_DATA=(SERVICE_NAME=oltp_srv)))
```

**效果**：节点1宕机瞬间
- SCAN自动把新连接转到节点2；存活的TCP连接在TAF下自动重连节点2；SELECT查询自动从断点续查（不用用户重跑SQL）；DML事务失败回滚（应用捕获异常重试提交）
- 用户无感知=业务7×24零宕机
</details>

---

## 考点统计表

| 考点 | 题号 | 分值 | 合计占比 |
|---|---|---|---|
| SGA/PGA内存组件与调优命中率 | 2,8,12,16,21,25,29 | 55 | 55% |
| 六大后台进程PMON/SMON/DBWn/LGWR/CKPT/ARCn触发条件 | 1,3,10,11,15,21 | 47 | 47% |
| 物理文件数据/控制/Redo丢失恢复 | 4,5,14,17,18,19,26,28,30 | 66 | 66% |
| 四层逻辑存储表空间/段/区/块管理+SQL | 6,7,9,13,20,22,23,24,27 | 51 | 51% |
| 综合诊断调优设计题 | 25,26,27,28,29,30 | 44 | 44% |

## 章节导航

- 上一级：[[MOC - Oracle数据库管理]]
- 本章知识点：[[MOC - 第3章 Oracle实例与存储结构]]
- 上一章知识点：[[MOC - 第2章 Oracle安装与环境配置]]
- 下一章知识点：[[MOC - 第4章]]（规划中
- 上一章习题：[[MOC - 第2章习题]]
- 下一章习题：[[MOC - 第4章习题]]（规划中
