---
domain: 数据库技术
subject: Oracle数据库管理
type: exercise
chapter: 第10章 性能监控与基础优化
section: 10.9 第10章习题
tags: [Oracle,习题,DBA,性能优化,执行计划,AWR,V$视图,锁等待,SQL调优]
prerequisites: ["10.1 常用数据字典视图", "10.2 SQL执行计划查看", "10.3 锁等待与会话排查", "10.4 基础优化思路"]
---

# MOC - 第10章习题

> [!info] 习题说明
> 本习题集覆盖 [[MOC - 第10章]] 全部知识点，共 30 题，分六类：单选 10、多选 5、判断 5、简答 4、分析 4（含 V$ 视图查询 SQL 书写、锁等待链分析、执行计划判读改错）、综合 2（AWR 报告解读 + 完整慢 SQL 优化案例）。重点考查：DBA_/ALL_/USER_ 三大前缀与 V$ 静态/动态视图区别、执行计划四种查看方法与判读要点（TABLE ACCESS FULL/索引扫描/NL vs HASH JOIN）、锁等待排查流程与 SQL 脚本（V$SESSION/V$LOCK/V$LOCKED_OBJECT）、常见等待事件含义、五层面优化方法论与 AWR 报告八大必看板块。分析题与综合题答案给出完整 SQL 代码、执行计划解读与优化前后对比数据。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | DBA_/ALL_/USER_ 前缀区别 | 概念理解 |
| 单2 | 单选 | V$ 视图 vs DBA_ 视图本质区别 | 概念理解 |
| 单3 | 单选 | 执行计划 EXPLAIN PLAN 四种方法的真实执行与否 | 概念理解 |
| 单4 | 单选 | TABLE ACCESS FULL vs INDEX RANGE SCAN 选用时机 | 概念理解 |
| 单5 | 单选 | NESTED LOOPS vs HASH JOIN 适用场景 | 概念理解 |
| 单6 | 单选 | Oracle 锁类型：TX / TM 锁的保护对象与粒度 | 概念理解 |
| 单7 | 单选 | 阻塞会话查找 V$SESSION.BLOCKING_SESSION 列 | 概念理解 |
| 单8 | 单选 | 等待事件 db file scattered read 的含义与根因 | 概念理解 |
| 单9 | 单选 | 五层面优化框架自顶向下顺序与 ROI | 概念理解 |
| 单10 | 单选 | AWR 报告 Top 5 Timed Events 第一诊断入口 | 综合应用 |
| 多1 | 多选 | 常用 DBA_/V$ 静态动态视图：表空间/段/会话/SQL | 概念辨析 |
| 多2 | 多选 | 执行计划判读的"危险信号" | 概念辨析 |
| 多3 | 多选 | Oracle 锁模式（0-6）与 TM 锁相容矩阵 | 概念辨析 |
| 多4 | 多选 | 常见 Top 等待事件含义与优化方向：TX / scattered read / log file sync / buffer busy | 概念辨析 |
| 多5 | 多选 | SQL 层优化手段：索引列不加函数 / UNION ALL / 绑定变量 / 覆盖索引 / 分页 Seek | 概念辨析 |
| 判1 | 判断 | USER_TABLES 查不到刚 CREATE TABLE 的表时 DBA_TABLES 同样查不到 | 概念理解 |
| 判2 | 判断 | DISPLAY_CURSOR 配合 STATISTICS_LEVEL=ALL 能拿到真实 A-Rows/Buffers/A-Time，而 EXPLAIN PLAN FOR 只有估算值 | 概念理解 |
| 判3 | 判断 | 两个会话对同一表不同行做 UPDATE，会在 TX 行锁层面冲突 | 概念理解 |
| 判4 | 判断 | enq: TX - row lock contention 等待事件说明当前有大量全表扫描 | 概念理解 |
| 判5 | 判断 | AWR 报告里 Soft Parse% 只有 70%，说明应用大量使用绑定变量 | 概念理解 |
| 简1 | 简答 | 对比 DBA_ / ALL_ / USER_ 前缀；V$ 与 DBA_ 本质区别；GV$ 含义；举例 6 个常用 V$ 视图名+用途 | 分析说明 |
| 简2 | 简答 | 4 种查看执行计划方法的语法/是否真实执行/是否真实统计/适用场景对比表；执行计划 Id/Operation/Predicate access/filter 含义；为什么 E-Rows vs A-Rows 偏差是优化第一线索 | 分析说明 |
| 简3 | 简答 | 锁等待排查 8 步流程；TX vs TM 锁区别；V$LOCK block=1/request>0 含义；ALTER SYSTEM KILL SESSION 语法 + 至少 3 个生产风险 | 分析说明 |
| 简4 | 简答 | 五层面优化框架（自上而下）与每层 3+ 优化手段；AWR 报告 8 大必看板块；为什么优化后要前后对比 AUTOTRACE consistent gets + DML 回归测试 | 分析说明 |
| 分1 | 分析 | V$ 视图查询 SQL 书写：写 SQL 查"Top 10 最耗时 SQL"、"阻塞会话对"、"TEMP 临时段占用者" | 综合应用 |
| 分2 | 分析 | 执行计划判读改错：给出一个慢 SQL + EXPLAIN 输出，指出问题点 + 改写 SQL + 建索引语句 + 给出优化后预期计划 | 综合应用 |
| 分3 | 分析 | 锁等待链场景分析：给出 V$LOCK/V$SESSION 表格数据，找出阻塞者/被阻塞者、被锁对象名、判断生产处理决策（沟通 or KILL）+ 写 KILL 命令 | 综合应用 |
| 分4 | 分析 | 等待事件分析：给出 AWR Top 5 Events 表格，分别诊断每个等待的根因 + 对应优化方案 | 综合应用 |
| 综1 | 综合 | 完整慢 SQL 优化：订单表 + 原 SQL + 优化前执行计划 + AUTOTRACE 数据 → 走完整 5 步优化法，写出：定位 SQL/分析问题（缺索引+函数失效+NL选错）/ 优化动作（复合索引+SQL改写+HASH Hint）/ 优化后 AUTOTRACE 预期数据 / DML 回归验证 | 综合应用 |
| 综2 | 综合 | AWR 报告全案解读：给出一份 AWR 的 8 大板块关键数据（命中率/Top Events/Time Model/Top SQL/Segments），写出完整诊断报告：问题优先级排序 + 每条的优化建议 + 预期收益评估 | 综合应用 |

---

## 一、单选题（每题 2 分，共 10 题）

**1. 关于数据字典视图三大前缀 USER_ / ALL_ / DBA_，下列说法正确的是（　）。**
A. 三者的区别只在于视图名不同，内容完全一样
B. USER_ 只能看到当前会话的临时对象；ALL_ 看到所有会话对象；DBA_ 看到 DBA 用户创建的对象
C. USER_ 范围最小（当前用户自己拥有的对象），ALL_ 是当前用户有权限访问的所有对象，DBA_ 是全库所有用户的所有对象（需 DBA 权限/SELECT_CATALOG_ROLE）
D. DBA_ 只存 DBA 用户建的对象，普通用户的对象在 USER_ 里

**2. 关于 Oracle 动态性能视图 V$ 与静态 DBA_ 视图的本质区别，下列说法正确的是（　）。**
A. 两者底层都来自数据字典基表，持久化存储在 SYSTEM/SYSAUX 表空间，实例关闭也存在
B. V$ 视图底层是 SGA 内存中的 X$ 表，只在实例运行时存在且重启清零；DBA_ 视图底层是 SYSTEM/SYSAUX 表空间中持久化的字典基表，实例关闭也存在
C. V$ 视图只能由 SYS 用户查询，普通用户永远不能查 V$SESSION
D. V$ 视图存的是昨天的历史数据，DBA_ 是现在实时数据

**3. 四种查看 Oracle 执行计划的方法：① EXPLAIN PLAN FOR + DBMS_XPLAN.DISPLAY；② SQL*Plus SET AUTOTRACE ON；③ DBMS_XPLAN.DISPLAY_CURSOR(sql_id)；④ AWR DBA_HIST_SQL_PLAN + DISPLAY_AWR。关于它们"是否真实执行 SQL"与"是否能拿到真实运行统计（A-Rows / Buffers / A-Time）"，下列排序正确的是（　）。**
A. ①真实执行+真实统计；②③④都不执行
B. ①不执行（只有估算）；②③④都真实执行，其中②③能拿到真实统计
C. ①不执行（估算）；②真实执行 AUTOTRACE STAT 能拿真实逻辑读/物理读/排序统计；③ DISPLAY_CURSOR 配合 STATISTICS_LEVEL=ALL/GATHER_PLAN_STATISTICS Hint 能拿真实 A-Rows/Buffers/A-Time 每步骤统计；④是历史真实执行过的快照估算
D. 四种方法都真实执行 SQL 并拿真实统计，只是输出格式不同

**4. 关于 TABLE ACCESS FULL（全表扫描）与 INDEX RANGE SCAN（索引范围扫）+ TABLE ACCESS BY INDEX ROWID 的选择，下列说法正确的是（　）。**
A. 任何时候走索引都比全表扫描快
B. 当查询选择率高（WHERE 条件过滤后取表总行数 >15% 左右）时，索引+回表大量随机读的总代价可能高于全表扫描多块读，优化器可能选 FTS 更优
C. FTS 只扫 1 个区，所以比索引快
D. 索引只适合数字类型列，VARCHAR2 不能建索引

**5. 关于 Oracle 三大连接方法 NESTED LOOPS / HASH JOIN / SORT MERGE JOIN 的适用场景，下列说法正确的是（　）。**
A. 三张表 1000 万行量级 JOIN 统计查询，驱动表 100 万行，应该用 NESTED LOOPS
B. 两张大表等值 JOIN、内表连接列无索引、输出不需要首行快速返回 → 优先 HASH JOIN（大数据量最常用）
C. SORT MERGE JOIN 只适合等值连接，不能处理 >=/>/< 范围连接
D. 小表（10 行）JOIN 大表（1 亿行）且被驱动表连接列无索引 → 用 NESTED LOOPS 最快

**6. 关于 Oracle 锁 TX / TM 锁，下列说法正确的是（　）。**
A. TX 锁是表级锁，保护表结构；TM 锁是行级锁，保护每一行被修改
B. TX 是事务行锁（Transaction Lock），行级排他保护被修改的行；TM 是 DML 表锁（Table Lock），表级，DML 时自动持有，防止其他会话做 DDL 改表结构
C. 做 INSERT 时只获取 TX 锁，不获取 TM 锁
D. 两个会话 UPDATE 同一张表的不同行会产生 TM 锁冲突

**7. 某应用"卡死"，查 V$SESSION 有 50 个会话 STATUS=ACTIVE，EVENT='enq: TX - row lock contention'，BLOCKING_SESSION_STATUS='VALID'，快速定位"谁在阻塞别人"的最直接方法是（　）。**
A. 看每个会话的 SQL_ID 去 V$SQL 查 SQL 文本
B. V$SESSION.BLOCKING_SESSION 列（11g+ 新增）直接指向阻塞者 SID，不用再手动关联 V$LOCK
C. 直接重启实例解决
D. 查 USER_SOURCE 看是谁的过程

**8. AWR 报告 Top 5 Timed Events 第一名是 `db file scattered read`，占总 DB Time 的 52%。下列对该等待事件的解释、根因、优化方向全部正确的是（　）。**
A. 含义：索引单块读，每次1块 → 根因：索引树太深 → 重建索引
B. 含义：多块读 = 大量 TABLE ACCESS FULL（全表扫）/ INDEX FAST FULL SCAN → 根因：大量 SQL 缺索引，走全表扫描 → 优化：Top SQL 加合适索引 / 改写 SQL 避免不带 WHERE
C. 含义：提交时等 LGWR 写 redo 日志 → 根因：redo 慢盘 + commit 太频繁 → redo 迁 SSD
D. 含义：buffer cache 热块争用 → 根因：热点块 → 分区 / 反向键索引

**9. Oracle 五层面优化框架（自上而下按 ROI 从高到低）正确顺序是（　）。**
A. OS 硬件层 → 内存参数层 → IO 表空间层 → 索引层 → 应用 SQL 层
B. 应用 SQL 层 → 索引层 → 表空间与 I/O 布局层 → 内存与参数层 → OS/网络/硬件层
C. 索引层 → SQL 层 → 内存层 → 硬件层 → IO 层
D. 内存参数层 → SQL 层 → 索引层 → IO 层 → 硬件层

**10. 某数据库 DB Time = 4500s（1 小时快照），AWR Top 5 Timed Events 第一名是 `enq: TX - row lock contention` 等待时间 2600s，第二名是 `DB CPU` 950s，第三名是 `db file sequential read` 400s。第一优先级优化方向是（　）。**
A. 加索引优化全表扫描
B. 加 CPU 核数
C. 排查 V$SESSION 阻塞链，找出持有行锁不释放的会话（通常是应用漏 COMMIT 僵尸 INACTIVE 会话），联系开发修复代码及时 COMMIT
D. 加内存调 DB_CACHE_SIZE

---

## 二、多选题（每题 3 分，共 5 题）

**1. 下列 Oracle 视图中，名称和用途对应正确的有（　）。**
A. DBA_SEGMENTS：查每个段（表/索引/回滚段）占用磁盘字节数，找大表大索引
B. V$SESSION：当前实例所有会话详情，含 SID、SERIAL#、USERNAME、STATUS、EVENT（当前等什么）、SQL_ID、BLOCKING_SESSION
C. V$SQL / V$SQLAREA：Library Cache 中共享 SQL 的统计（执行次数、CPU 时间、总耗时、逻辑读、物理读），找 Top SQL
D. V$LOCK：当前所有持有的锁 + 等待锁，block=1 是阻塞者，request>0 是被阻塞者，通过 id1/id2 关联同一资源
E. DBA_SOURCE：存数据库错误代码和编译错误，查 `SHOW ERRORS`

**2. 下列属于"执行计划危险信号"，看到就需要优先排查的有（　）。**
A. 大表（几十万~亿行级）Operation=TABLE ACCESS FULL，Predicate只有 filter(...) 没有 access(...) = 无索引全表扫
B. NESTED LOOPS 的外表（Id 小的子节点）E-Rows / A-Rows 估算几万行以上（小表驱动原则被违反）
C. 计划 Id 中出现 SORT(ORDER BY / GROUP BY / JOIN)，输入 Rows 很大，而 ORDER BY / GROUP BY 列本可建索引避免排序
D. INDEX UNIQUE SCAN，access 谓词是主键等号查询，只返回 1 行
E. VIEW 视图内层输出几万行，外层 filter 条件本可推入内层合并谓词但没有合并（视图未合并），最后只返回几行

**3. 关于 Oracle 锁模式（0~6 共 7 种模式，SS=1/SX=2/S=3/SSX=4/X=5）和 TM 表锁相容矩阵（✓=相容、✗=冲突需等待），下列说法正确的有（　）。**
A. SX（Row Exclusive，INSERT/UPDATE/DELETE 默认获取的 TM 表锁）互相之间是相容 ✓ → 两个会话 UPDATE 不同行时表级不冲突；但 SX 与 S（Share）表锁冲突 ✗
B. X（Exclusive，DROP/ALTER TABLE DDL 获取）与所有锁模式（包括 X 自己）都冲突 ✗ → DDL 执行时其他会话 DML 会等待 enq: TM - contention
C. 事务 A UPDATE 表 A 的 empno=7369 行；事务 B UPDATE 表 A 的 empno=7499 行 → TM 层面两个 SX 相容 ✓ → 不等待；TX 层面不同行 ✓ → 不等待
D. SS（Row Share，SELECT ... FOR UPDATE 获取）与 X 冲突 ✗
E. 两个事务 SX 冲突 ✗，互相等待导致死锁

**4. 关于常见等待事件和优化方向，下列说法正确的有（　）。**
A. `log file sync`：前台 COMMIT 等 LGWR 把 redo buffer 写 redo logfile 刷盘 → 根因：redo 在慢 HDD；代码循环 1000 次 COMMIT 1000 次 → 优化：redo 迁 SSD / NVMe；改为批量 COMMIT（每 500 条一次）
B. `buffer busy waits`：Buffer Cache 里同一块被大量并发读/改，块头/段头/undo 头类热块争用 → 优化：大表 HASH 分区/反向键索引分散热点；ASSM 更大的 EXTENT SIZE 减少段头 BITMAP 争用；热点小表扔 KEEP POOL
C. `enq: TX - index contention`：高并发 INSERT 单调递增 B 树索引的叶块（右增长热点索引块）→ 优化：REVERSE 反向键索引 / HASH 分区索引
D. `db file sequential read`（索引单块读，每次 1 块）占比非常高且平均等待时间长（>10ms）→ 可能是索引回表选择率太高（大量 TABLE ACCESS BY ROWID）或存储慢 → 优化：选择性高的查询可换覆盖索引避免回表；提升存储 IOPS；blevel 高的索引重建
E. `direct path read temp`：排序/哈希连接/临时表溢出写 TEMP 临时表空间 → 根因：PGA_AGGREGATE_TARGET 设置太小导致工作区不够 → 加大 PGA；TEMP 放最快盘

**5. 属于"应用 SQL 层优化手段（ROI 最高层面）"的有（　）。**
A. 去掉 SELECT *，只取应用实际需要的列
B. 对索引列写函数（如 `WHERE UPPER(name)=?` / `WHERE TO_CHAR(date_col)=?`）→ 改写成范围条件或建函数索引 FBI
C. 业务语义确定结果集不重复时用 UNION ALL 代替 UNION，避免不必要的排序去重
D. 应用代码 JDBC Statement 拼字面量 SQL → 改 PreparedStatement 占位符实现绑定变量，减少硬解析和 library cache latch 争用
E. 把所有表迁到 NVMe SSD 上

---

## 三、判断题（每题 2 分，共 5 题）

**1. 当前 SCOTT 用户刚执行 `CREATE TABLE t_test(id NUMBER);`（空表，还没 INSERT 数据），SCOTT 查 USER_TABLES 能查到 T_TEST，此时 SELECT * FROM DBA_SEGMENTS WHERE OWNER='SCOTT' AND SEGMENT_NAME='T_TEST' 一定能查到该段。**

**2. 对于某已经在生产执行过的慢 SQL，用 `SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR('SQL_ID', NULL, 'ALLSTATS LAST'));`（配合会话先 `ALTER SESSION SET STATISTICS_LEVEL='ALL'` 或 SQL 加 `/*+ GATHER_PLAN_STATISTICS */`）能拿到每个步骤真实执行的 A-Rows（实际行数）、Buffers（逻辑读块数）、A-Time（实际累积耗时）；而 `EXPLAIN PLAN FOR` 只有优化器估算的 E-Rows 与 Cost，不执行 SQL。**

**3. 会话 1：`UPDATE emp SET sal=1000 WHERE empno=7369; COMMIT;`；会话 2：`UPDATE emp SET sal=2000 WHERE empno=7499;`。因为两个 SQL UPDATE 的是同一个表 EMP，所以在 TM 表锁层面冲突，会话 2 会等待会话 1。**

**4. 某应用 SQL 平均耗时 20s，V$SESSION 中该会话 EVENT='enq: TX - row lock contention'，持续 SECONDS_IN_WAIT=15s 持续增长。DBA 看到这个等待事件应该立刻加索引，这是全表扫描导致的。**

**5. 某 AWR 报告 Instance Efficiency 显示 Soft Parse % = 70.3%，Library Hit % = 84%。这说明应用绑定变量用得非常好，软解析比例理想。**

---

## 四、简答题（每题 5 分，共 4 题）

**1. 回答下列数据字典视图相关问题：**
- (1) 对比 DBA_ / ALL_ / USER_ 三大前缀的范围差异和权限要求；
- (2) 说明 V$ 动态性能视图和 DBA_ 静态视图的本质区别（底层来源、生命周期、重启数据保留情况）；
- (3) GV$ 视图是什么？和 V$ 多了什么列？什么环境用？
- (4) 任意列举 6 个你认为排查性能必备的 V$ 视图名，并一句话说明用途（例如：V$SESSION → 会话详情+等什么事件）。

**2. 回答执行计划相关：**
- (1) 画出 4 种查看执行计划方法对比表：方法名/语法要点/是否真实执行/是否有真实运行统计/适用场景；
- (2) 执行计划表格中 Id、Operation、Predicate 下的 access(...) 与 filter(...) 分别是什么含义？
- (3) DISPLAY_CURSOR 输出的 "E-Rows" 和 "A-Rows" 分别代表什么？为什么两者数量级相差悬殊（如 E=1 / A=10000）时通常意味着执行计划选错？

**3. 回答锁等待相关：**
- (1) 描述锁等待排查的标准 8 步流程（从"症状→找被阻塞→找阻塞者→找对象→找SQL→决策→止血→根因修复"）；
- (2) TX 锁 vs TM 锁的区别（保护对象、粒度、获取时机）；
- (3) V$LOCK 视图中 block=1、request>0 各代表什么？如何关联 V$LOCK 和 V$SESSION 找阻塞链？
- (4) 写出完整的"安全 KILL 阻塞会话"流程：至少查哪 3 个 V$SESSION 列？ALTER SYSTEM KILL SESSION 语法？生产执行 KILL 的 3 大风险是什么？

**4. 回答优化方法论相关：**
- (1) 自上而下画出 5 层面优化框架，注明 ROI 星级；每层列举至少 3 条具体优化手段；
- (2) AWR 报告的 8 大必看板块（打开 AWR 后依次看什么），每块说一句话怎么解读；
- (3) 为什么优化完成后必须做两方面验证：① AUTOTRACE consistent gets 等 SQL 指标前后对比；② DML（INSERT/UPDATE/DELETE）TPS 回归测试。只看"秒数降了"为什么不够？

---

## 五、分析题（每题 8 分，共 4 题）

### 分析题 1：V$ 视图 SQL 书写（8 分）

请根据下列需求，分别写出对应的 Oracle 19c SQL 语句（均为 DBA 视角，权限已授予）。给出关键列别名、排序方向。

**需求 1（2 分）：** 写出查找"当前库过去 24 小时内总耗时前 10 名 SQL"的 SQL，列至少包括：SQL_ID、子游标号、执行次数 execs、总耗时 total_elapsed_s（秒）、总 CPU 秒、平均单次耗时 per_exec_ms（毫秒）、物理读、逻辑读、SQL_TEXT 前 80 字符预览。排除 SYS/SYSMAN/DBSNMP 用户，按总耗时倒序取前 10。

**需求 2（3 分）：** 写出"锁等待链排查 SQL"：从 V$LOCK/V$SESSION 关联查询，输出如下列：
- `block_chain`：文字显示 阻塞者（BLOCKER SID=xx SERIAL=xx USER@MACHINE PROG=xx）阻塞了 被阻塞者（WAITER SID=xx SERIAL=xx USER@MACHINE PROG=xx 已等待 N 秒）；
- lock_type/lock_resource：锁类型 + (id1, id2)；
- blocker_hold_mode：阻塞者持有锁模式文字（lmode 转 0-6 对应名称：2→RowShare/3→RowExcl/4→Share/5→ShareRowExcl/6→Exclusive）；
- waiter_request_mode：被阻塞者请求锁模式文字；
- blocker_sqlid / waiter_sqlid：阻塞者和被阻塞者当前 SQL_ID。
按等待秒数倒序。

**需求 3（3 分）：** 写 SQL 排查"谁占用了 TEMP 临时表空间？"，从 V$SORT_USAGE / V$TEMPSEG_USAGE / V$SESSION 关联查询，输出列：用户 USERNAME、会话 SID/SERIAL#、MACHINE/PROGRAM、SQL_ID、占用 MB 数、临时段类型（SORT/HASH/DATA/INDEX），按占用 MB 倒序取前 20。

---

### 分析题 2：执行计划判读改错 + 优化（8 分）

**背景：** 订单表 t_order 共 520 万行，列 order_id(PK)、user_id、amount、status、create_time(DATE)。user_id 和 create_time 两个单列索引：IDX_USER(IDX_USER_ID)、IDX_TIME(IDX_CREATE_TIME)。应用某慢 SQL（查询 2024-01-01~2024-02-01 某用户 20 条订单）每次耗时 26s，AWR Top 1。

**原 SQL：**
```sql
SELECT * FROM (
    SELECT t.*, ROW_NUMBER() OVER (ORDER BY create_time DESC) rn
      FROM t_order t
     WHERE TO_CHAR(t.create_time, 'YYYYMMDD') BETWEEN '20240101' AND '20240131'
       AND t.user_id = 10086
) WHERE rn BETWEEN 1 AND 20;
```

**EXPLAIN PLAN FOR 输出（优化前）：**
```
| Id | Operation                     | Name          | Rows   | Cost  |
|----|-------------------------------|---------------|--------|-------|
| 0  | SELECT STATEMENT              |               |    20  | 95000 |
| *1 |  VIEW                         |               |    20  | 95000 |
| 2  |   WINDOW SORT                 |               | 260000 | 95000 |
| 3  |    CONCATENATION              |               |        |       |
| 4  |     TABLE ACCESS BY INDEX ROWID| T_ORDER       | 130000 | 48000 |
| *5 |      INDEX RANGE SCAN         | IDX_USER_ID   | 130000 |   200 |
| 6  |     TABLE ACCESS BY INDEX ROWID| T_ORDER       | 130000 | 47000 |
| *7 |      INDEX RANGE SCAN         | IDX_CREATE_TIME| 520000|   800 |
Predicate:
   1 - filter("RN">=1 AND "RN"<=20)
   5 - access("T"."USER_ID"=10086)
   7 - access(INTERNAL_FUNCTION("T"."CREATE_TIME")>=... AND INTERNAL_FUNCTION(...)<=...)
       filter(TO_CHAR(INTERNAL_FUNCTION("CREATE_TIME"),'YYYYMMDD')<='20240131')
```

**AUTOTRACE（部分）：** consistent gets = 486,230；physical reads = 402,100；sorts(disk) = 3；rows processed = 20。

请回答：
- (1) 指出这个执行计划存在的至少 **4 处具体问题**（指出 Id 行号+原因）；
- (2) 给出 **SQL 改写方案**（如何改 TO_CHAR 函数导致的索引失效）；
- (3) 给出**新建索引的 DDL**（提示：复合索引 + 排序方向，让 Oracle 可以 WINDOW NOSORT STOPKEY 直接停）；
- (4) 给出**优化后预期的执行计划 Id 操作链**（每个 Id 的 Operation / Name，不需要数字），并估算 AUTOTRACE 指标大概降到什么数量级（consistent gets / physical reads / sorts）。

---

### 分析题 3：锁等待链实战分析（8 分）

DBA 在生产库执行下列两条排查 SQL，得到如下表格结果：

**查 V$LOCK + V$SESSION（节选 4 行）：**
| SID  | USERNAME | STATUS | EVENT                          | SECS_IN_WAIT | BLOCKING_SESSION | LADDR    | TYPE | ID1  | ID2  | LMODE | REQUEST | BLOCK |
|------|----------|--------|--------------------------------|--------------|------------------|----------|------|------|------|-------|---------|-------|
| 118  | PAY_APP  | ACTIVE | enq: TX - row lock contention  | 582          | 253              | ...      | TX   | 524296| 2183 | 0     | 6       | 0     |
| 253  | PAY_APP  | INACTIVE | SQL*Net message from client  | 734          | NULL             | ...      | TX   | 524296| 2183 | 6     | 0       | 1     |
| 253  | PAY_APP  | INACTIVE | SQL*Net message from client  | 734          | NULL             | ...      | TM   | 87123| 0     | 3     | 0       | 0     |
| 118  | PAY_APP  | ACTIVE | enq: TX - row lock contention  | 582          | 253              | ...      | TM   | 87123| 0     | 3     | 0       | 0     |

**查 V$LOCKED_OBJECT + DBA_OBJECTS：**
| SESSION_ID | OWNER | OBJECT_NAME | OBJECT_TYPE | HELD_MODE |
|------------|-------|-------------|-------------|-----------|
| 118        | PAY PAY | - |
| ...      | PAY PAY | PAY PAY PAY TABLE | PAY PAY | PAY PAY PAY TX? 根据 ID1=87123 查询 DBA_OBJECTS 得到：OWNER=APP_USER、OBJECT_NAME=T_PAY_ORDER、OBJECT_TYPE=TABLE。

请完成下列分析：
- (1) 指出**阻塞者 SID** 和**被阻塞者 SID**，并说明判断依据（V$LOCK 哪两个字段/值）；
- (2) 解释阻塞者 STATUS=INACTIVE 却 BLOCK=1 持有 734 秒锁不放的典型场景是什么？（开发下班了没 COMMIT？异常没 ROLLBACK？连接池泄漏？）
- (3) 被锁对象是哪张表？类型是什么？
- (4) 生产决策：假设现在是下午 14:30 高峰期，被阻塞的是支付接口，PAY 用户报告"支付卡住 5 分钟以上"，电话联系 PAY 团队的支付开发同学没人接。你作为 DBA 会不会执行 KILL？如果会写出完整 SQL（先查 serial# 的语句 + KILL 语句）；如果不会，说明决策依据和下一步行动方案。至少阐述 3 条决策理由。

---

### 分析题 4：AWR Top 5 Events 诊断（8 分）

某业务库高峰期（下午 14:00-15:00）用户反馈"系统整体慢"，取该时段 AWR 报告 Top 5 Timed Foreground Events 如下：

| Event                              | Waits  | Time(s) | Avg wait(ms) | % DB time | Wait Class      |
|------------------------------------|--------|---------|--------------|-----------|-----------------|
| **DB CPU**                         | —      | 1842    | —            | 40.9%     | —               |
| enq: TX - row lock contention      | 46,203 | 1128    | 24           | 25.1%     | Concurrency     |
| db file scattered read             | 802,110| 720     | 0.9          | 16.0%     | User I/O        |
| log file sync                      | 210,993| 435     | 2.1          | 9.7%      | Commit          |
| db file sequential read            | 601,334| 210     | 0.35         | 4.7%      | User I/O        |
| * Other *                          | —      | 160     | —            | 3.6%      | —               |

（总 DB Time = 4500s；DB Time = 前台会话 CPU + 非空闲等待总和）

请回答：
- (1) 分别诊断这 5 条事件各自的含义 + 该场景下可能的根因；
- (2) 按"优先级从高到低（%DB time 大的先处理，ROI 高）"排序给出 4 条具体优化建议，每条对应哪条事件、怎么做、预期收益（%DB time 大概降到多少）；
- (3) 为验证优化效果，优化前后你会保存哪几项关键数据（至少列举 AWR/V$ 5 项指标），怎么判断优化有效？
- (4) 除了 Top 5 Events，接下来你会接着看 AWR 报告的哪两个板块进一步定位"具体是哪条 SQL 导致的问题"？

---

## 六、综合题（每题 10 分，共 2 题）

### 综合题 1：完整慢 SQL 优化案例（走 5 步法）（10 分）

**背景：** 某 SaaS ERP 客户应收账龄报表，高峰期每跑一次 72s，占 DB Time 31%，导致批量月结任务超时。DBA 接到优化需求。

**表结构：**
- t_invoice（发票主表 860 万行）：invoice_id(PK), customer_id, invoice_no, amount, invoice_date(DATE), status(VARCHAR2(10))；索引 PK_INVOICE(invoice_id)、IDX_INV_CUST(customer_id)、IDX_INV_DATE(invoice_date)。
- t_customer（客户表 4.2 万行）：customer_id(PK), customer_name, credit_level。
- t_invoice_detail（发票行表 1.2 亿行）：detail_id(PK), invoice_id, product_id, qty, unit_price, subtotal；索引 PK_DETAIL(detail_id)、IDX_DET_INV(invoice_id)。

**原慢 SQL（取 2024 年高价值客户未付清发票，带行明细合计）：**
```sql
SELECT c.customer_name,
       i.invoice_no,
       i.invoice_date,
       i.amount,
       (SELECT SUM(subtotal) FROM t_invoice_detail d WHERE d.invoice_id = i.invoice_id) detail_sum
  FROM t_customer c, t_invoice i
 WHERE c.customer_id = i.customer_id
   AND c.credit_level = 'HIGH'
   AND TO_CHAR(i.invoice_date, 'YYYY') = '2024'
   AND i.status = 'UNPAID'
   AND i.amount > 5000
 ORDER BY i.invoice_date DESC;
```

**优化前 AUTOTRACE 关键指标：** elapsed=72.3s；consistent gets=1,980,400；physical reads=1,210,500；sorts(disk)=2；rows processed=14,520。
**优化前 EXPLAIN PLAN（核心步骤文字）：**
```
0 SELECT STATEMENT Cost=380000 Rows=14520
1  SORT ORDER BY Cost=380000 Rows=14520 Input=14520
2    NESTED LOOPS
3      NESTED LOOPS OUTER
4        NESTED LOOPS
5          JOIN c (TABLE ACCESS FULL T_CUSTOMER 42000 rows filter CREDIT_LEVEL='HIGH') → 3200 rows
6          JOIN i (TABLE ACCESS BY INDEX ROWID T_INVOICE 1 row per loop)
7            INDEX RANGE SCAN IDX_INV_CUST (per loop) → 180+ hits each → 3200 × 180 = 576k probes
8        SORT AGGREGATE (子查询 SELECT SUM(subtotal) ...)
9          TABLE ACCESS FULL T_INVOICE_DETAIL? NO——Index Range Scan IDX_DET_INV 每次 invoice_id 扫 14 行
10     INDEX FULL SCAN PK_DETAIL ...（略）
Predicate: 7 access(i.customer_id=c.customer_id)
           filter(TO_CHAR(i.invoice_date,'YYYY')='2024' AND i.status='UNPAID' AND i.amount>5000)
```

**要求：严格按 SQL 优化标准 5 步法答题：**

1. **Step 1 定位问题点（2 分）：** 根据 AUTOTRACE/执行计划指出至少 4 个具体瓶颈点（每个指出 Plan Id + 原因 + 对应指标）；
2. **Step 2 获取真实执行计划 + Step 3 等待事件（2 分）：** 写出"拿真实执行计划含 A-Rows/Buffers/A-Time"的 SQL 语法；推测这条 SQL 的主要 V$SESSION_WAIT 等待事件是什么（3 项以内）；
3. **Step 4 优化动作（4 分）：** 从 5 个层面给出具体可行的优化动作。至少 6 条，例如：
   - 应用 SQL 层：如何改 TO_CHAR 函数失效？如何改写子查询为 JOIN + GROUP BY 避免相关子查询每行执行一次？ORDER BY 怎么配合索引避免 SORT ORDER BY？
   - 索引层：写 DDL 建什么复合索引（列顺序+原因），什么函数/覆盖索引；
   - 其他层：可以给什么 Hint（如 USE_HASH / LEADING 强制换连接算法？）
4. **Step 5 验证（2 分）：** 给出优化后 AUTOTRACE 指标的预期值区间（elapsed / consistent gets / physical reads / sorts(disk)）；说明 DML 回归怎么测（TPS 下降多少算合格，为什么必须测）。

---

### 综合题 2：AWR 报告全案诊断 + 优化建议书（10 分）

某电商库（19c，RHEL 7，单实例，80 核 512G，存储全闪），818 大促前压测，QPS 上不去，响应时间飙升。DBA 取 14:00-15:00 AWR 关键数据如下：

**【板块 A：快照 & Load Profile】**
- DB Time(s) = 108,000；Elapsed = 3,600s → **DB Time / Elapsed = 30.0**（80 核，说明 CPU 并发跑满 30 个核；可接受的理论值 ≤ CPU 核数 × 0.7 = 56，暂时 CPU 没满但 DB Time 全耗在等待）
- TPS = 2,340/s（每秒事务数 2340，偏低）
- SQL 执行次数 Executions = 18,200/s（正常）
- **Redo size：2,340KB/s × 3600s ≈ 8.4TB/hour？过高**
- **Hard parses：940/s**（硬解析每秒 940 次，极高！）

**【板块 B：Instance Efficiency】**
- Buffer Cache Hit %：98.37% ✅
- **Library Hit %：62.8% ❌（目标 ≥ 99%）**
- **Soft Parse %：64.4% ❌（目标 ≥ 95%）**
- Execute to Parse %：41.2% ❌（低 = 执行一次解析一次）
- % Non-Parse CPU：58.0% ❌（42% CPU 用在解析，不是执行！）
- Parse CPU to Total CPU：41.9%

**【板块 C：Top 5 Timed Events（占总 DB Time 108000s）】**
| Event                              | Waits     | Time(s) | Avg(ms) | % DB Time |
|------------------------------------|-----------|---------|---------|-----------|
| latch: shared pool                 | 2,340,200 | 36,800  | 15.7    | 34.1%     |
| latch: library cache lock          | 1,980,400 | 21,200  | 10.7    | 19.6%     |
| **DB CPU**                         | —         | 19,800  | —       | 18.3%     |
| log file sync                      | 8,424,000 | 14,500  | 1.7     | 13.4%     |
| cursor: pin S wait on X            | 480,100   | 5,200   | 10.8    | 4.8%      |

**【板块 D：Time Model（Top 时间项）】**
| Statistic Name                     | Time(s) | % DB Time |
|------------------------------------|---------|-----------|
| sql execute elapsed time           | 88,500  | 81.9%     |
| parse time elapsed                 | **37,200** | 34.4%   |
| hard parse elapsed time            | **26,800** | 24.8%   |
| connection management call elapsed | 600     | 0.6%      |
| PL/SQL execution elapsed time      | 2,100   | 1.9%      |

**【板块 E：Top SQL by Elapsed Time（前 3 条占 DB Time 42%）】**
| SQL_ID       | Executions | Elapsed(s) | CPU(s) | per Exec(ms) | Parse Calls | SQL Text 前 50 字 |
|--------------|------------|------------|--------|--------------|-------------|-------------------|
| a1b2c3d4e5f6 | 9,400,000  | 18,200     | 8,200  | 1.93         | 9,400,000   | SELECT col1,col2 FROM t_user WHERE user_id = 10001 AND ... |
| g7h8i9j0k1l2 | 11,200,000 | 14,600     | 7,800  | 1.30         | 11,200,000  | UPDATE t_acc SET balance = balance - 10 WHERE acc_id = 8888 ... |
| m3n4o5p6q7r8 | 7,800,000  | 12,400     | 4,600  | 1.59         | 7,800,000   | SELECT COUNT(*) FROM t_order WHERE user_id = 90001 AND TO_CH... |
| (其余 SQL)   | ...        | 42,800     | ...    | ...          | ...         |                   |
*观察：每条 SQL 的 Parse Calls ≈ Executions！Parse Calls 等于执行次数 = 完全没绑定！*

**【板块 F：Segments by Logical Reads（Top 3 段）】**
| Owner | Segment Name | Type | %Total |
|-------|--------------|------|--------|
| APP   | T_USER       | TABLE| 12.2%  |
| APP   | IDX_T_USER_UID | INDEX | 9.4% |
| APP   | T_ACC        | TABLE| 8.7%  |

**【板块 G：Enqueue & Latch Activity】**
- Latch Miss 排名 #1 shared pool (sleeps=2.3M)，#2 library cache (sleeps=2.0M)
- Row Lock Waits：很低，正常
- TM/TX Enqueue：占比可忽略

**【板块 H：Buffer Pool Advisory & PGA Advisory】**
- DB Buffer Cache Size 从 16G → 32G，预估物理读减少 0.9% → 收益不明显 ✅ 不用加 DB Cache
- PGA Target 从 8G → 16G，预估 Extra Read/Write 0 → 已经够 ✅ 不用加 PGA

请你作为性能优化顾问，写出一份**结构化的 AWR 诊断报告**，必须包含：

1. **问题优先级排序清单（Top 5 Problem List，按严重度/收益排序）（3 分）：**
   每条写清楚：问题 ID/名称/AWR 证据（哪板块哪些数字）/根因假设 / 预期影响 DB Time %。
2. **对应每条问题的具体优化建议（共 5 条以上，可操作）（5 分）：**
   例如"问题 1：latch: shared pool 占 34.1% DB Time + 硬解析 940/s + Soft Parse 64% + Parse Calls=Executions → 根因：完全没绑定变量。建议：① 短期救急：`ALTER SYSTEM SET CURSOR_SHARING=FORCE SCOPE=BOTH;`（临时！） ② 中期治本：开发代码 Java Statement 全部改 PreparedStatement 占位符 / .NET 参数化查询。③ 加大 SESSION_CACHED_CURSORS=300 减少会话内反复解析。④ 验证：1 小时后 AWR Hard parses < 20/s、Soft Parse% > 95%、latch 等待下降。"每条建议要能落地（SQL 语法/改代码方向）、给出验证方式。
3. **预估整体收益：** 执行完 5 条后，预计 DB Time / Elapsed 能降到多少？TPS / 平均响应时间预期提升多少？（给出定量区间）（2 分）
4. **附加题：** 为了防止下次大促前再遇到这个问题，你会建立哪些**日常监控告警项**？至少写 4 条（指标名+阈值+通知方式）。

---

## 答案与解析

<details>
<summary>单选题答案与解析</summary>

1. **C**。USER_ ⊆ ALL_ ⊆ DBA_，权限与范围一一对应。
2. **B**。V$ 动态视图来源于 X$ 内存表，实例生命周期内存在，重启清零；DBA_ 静态来自 SYSTEM/SYSAUX 字典基表持久化。
3. **C**。① EXPLAIN PLAN 不执行只估算；② AUTOTRACE 真实执行出 STAT 逻辑读/物理读/排序统计；③ DISPLAY_CURSOR 真实执行过的，配合 GATHER_PLAN_STATISTICS/ALLSTATS LAST 有 A-Rows/Buffers/A-Time；④ AWR 是快照历史估算。
4. **B**。选择率 > ~15% 时索引回表大量随机读总代价 > FTS 多块读，优化器选 FTS 合理。
5. **B**。HASH JOIN 是大数据量等值连接首选。NL 驱动表必须小；SM 适合非等值/结果有序。
6. **B**。TX 事务行级保护行，TM 表级 DML 锁防 DDL。
7. **B**。Oracle 11g+ V$SESSION.BLOCKING_SESSION 列直接给阻塞者 SID，懒人神器。
8. **B**。db file scattered read = 多块读 = FTS/FFS，缺索引。
9. **B**。SQL > 索引 > IO > 内存 > 硬件，ROI 递减。
10. **C**。58% DB Time 在锁等待，先找阻塞者+修复应用 COMMIT。

</details>

<details>
<summary>多选题答案与解析</summary>

1. **ABCD**。E 错误：DBA_SOURCE 存 PL/SQL 源代码，编译错误查 DBA_ERRORS / USER_ERRORS。
2. **ABCE**。D 是 INDEX UNIQUE SCAN 1 行 = 最优计划，不是问题。
3. **ABCD**。E 错误：SX 之间相容不冲突；死锁由 TX 不同行循环等待产生（A 锁 R1 等 R2，B 锁 R2 等 R1），非 TM 冲突。
4. **ABCDE**。5 个全对。
5. **ABCD**。E 是 OS/硬件层，SQL 层是最上层。

</details>

<details>
<summary>判断题答案与解析</summary>

1. **×**。空表刚 CREATE 未插入数据时 Oracle 采用延迟段创建（DEFERRED_SEGMENT_CREATION=TRUE，11g+ 默认）→ 段还没分配，DBA_SEGMENTS 查不到。插入第一条数据才分配段。
2. **√**。EXPLAIN 不执行只有估算；ALLSTATS LAST 输出真实 A-Rows/Buffers/A-Time。
3. **×**。两个会话 UPDATE **不同行**：TM 层面 SX vs SX 相容 ✓；TX 行级层面锁**不同行** ✓ → 完全不等待。
4. **×**。enq: TX 是行锁等待，说明在等别人 COMMIT，应查 V$SESSION.BLOCKING_SESSION 找阻塞者 KILL/沟通，跟全表扫描（db file scattered read）完全两回事。
5. **×**。Soft Parse 目标 ≥ 95%，Library Hit% ≥ 99%。70% 和 84% = 差得远 = 应用**大量没绑变量**，硬解析多。

</details>

<details>
<summary>简答题参考答案</summary>

**1. 数据字典视图：**
- **(1) 前缀对比表：**
| 前缀 | 范围 | 权限 |
| ---- | ---- | ---- |
| USER_ | 当前登录用户自己拥有的所有对象 | 任何用户不需要额外权限 |
| ALL_ | 当前用户**有权访问**的所有对象（自己的 + 其他用户 GRANT 过的） | 普通用户即可 |
| DBA_ | 全库所有用户的所有对象 | DBA 角色 / SELECT ANY DICTIONARY 系统权限 / SELECT_CATALOG_ROLE 角色 |
| 覆盖范围：USER_ ⊆ ALL_ ⊆ DBA_。
- **(2) V$ vs DBA_ 本质：**
  | | 底层来源 | 生命周期 | 实例重启 |
  |---|---|---|---|
  | V$ 动态视图 | SGA 内存中的 X$ 表（内存数组/结构体） | 仅实例 STARTUP 后存在 | 关闭立即消失；重启后所有计数器清零 |
  | DBA_ 静态视图 | SYSTEM/SYSAUX 表空间内的数据字典基表（如 TAB$/IND$/USER$/SEG$） | 随数据库创建存在，持久化 | 关闭也保留，重启后数据不变 |
- **(3) GV$：Global V$，RAC 集群环境用，对每个实例的 V$ 做 UNION ALL，多一列 INST_ID（1/2/... 节点号），WHERE INST_ID = 1 过滤某个节点。单实例也能查，结果与 V$ 基本一致。**
- **(4) 6 个常用 V$：**
  V$INSTANCE → 实例名/版本/状态/启动时间；V$SESSION → 会话详情+SQL_ID+EVENT+阻塞者；V$SQL / V$SQLAREA → 共享 SQL 统计，找 Top SQL；V$LOCK → 当前锁（谁阻塞谁）；V$SYSTEM_EVENT / V$SESSION_EVENT → 实例/会话级等待事件累计；V$SGA / V$PGASTAT → SGA/PGA 内存分配。（或答 V$SESSION_WAIT / V$SESSTAT / V$TRANSACTION / V$LOCKED_OBJECT 都可）

**2. 执行计划：**
- **(1) 4 种方法对比：**
| 方法 | 语法要点 | 真执行？ | 真实统计？ | 适用场景 |
| ---- | ---- | ---- | ---- | ---- |
| ① EXPLAIN PLAN FOR + DISPLAY | `EXPLAIN PLAN FOR sql; SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);` | ❌ 不执行 | ❌ 只有 E-Rows/Cost 估算 | 开发看估算计划、SQL 解析报错、长 SQL 不想真跑 |
| ② SQL*Plus SET AUTOTRACE | `SET AUTOTRACE ON EXPLAIN STATISTICS; SELECT ...; SET AUTOTRACE OFF;`（需要 PLUSTRACE 角色） | ✅ 真实执行（TRACEONLY STAT 不输出结果集） | ✅ 会话级真实统计：consistent gets / physical reads / redo size / sorts(memory/disk) / rows processed | 开发前后对比 SQL 工作量（consistent gets 最客观） |
| ③ DBMS_XPLAN.DISPLAY_CURSOR | `SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR('sql_id', child_no, 'ALLSTATS LAST'));` 前会话 `ALTER SESSION SET STATISTICS_LEVEL='ALL'` 或 SQL 加 `/*+ GATHER_PLAN_STATISTICS */` | ✅ SQL 已真实执行过（从 Library Cache 里拿） | ✅ 每一步有 A-Rows 真实行数、Buffers 真实逻辑读、A-Time 真实累计时间、Reads 真实物理读 | **⭐生产排查首选：看某条慢 SQL 真实走了什么计划、哪步耗时最多、哪步估算偏差最大** |
| ④ AWR DISPLAY_AWR | `SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_AWR('sql_id'));` / 跑 `@awrrpt.sql` | ✅ AWR 快照当时真实执行过 | ❌ 只有快照时的估算 Rows/Cost | "过去快现在慢"对比历史 vs 当前执行计划是否变更；历史 Top SQL 分析 |
- **(2) 列含义：**
  - **Id**：计划树步骤编号，**缩进深度优先执行**（越靠右缩进越多越先执行），同级从上到下，父节点等所有子节点执行完才输出。
  - **Operation**：具体操作名（TABLE ACCESS FULL、INDEX RANGE SCAN、NESTED LOOPS、SORT ORDER BY 等），前带 `*` 表示对应 Id 有 Predicate 条件。
  - **access("COL"=...)**：**访问谓词（Access Predicate）**——通过索引/B 树结构直接定位到匹配行的键值条件，索引高效扫的核心；
  - **filter(...)**：**过滤谓词（Filter Predicate）**——取出行后逐行判断是否满足，如果出现在 TABLE ACCESS FULL 中 = 全表逐行扫过滤 = 极慢。
- **(3) E-Rows = 优化器根据统计信息**估算**该步骤输出行数；A-Rows = 该步骤**实际**输出行数（ALLSTATS LAST 才有）。两者差几个数量级说明：①统计信息过期（LAST_ANALYZED 几个月前）→ 立刻 GATHER_TABLE_STATS；②列值倾斜（如某状态 99%=PAID 1%=REFUND，优化器以为均匀分布）→ 加直方图 FOR COLUMNS SIZE AUTO；③绑定变量窥探选错 ACS 子游标→刷共享池。估算 1 行实际 1 万行 → 优化器按"1 行"选 NL，实际 1 万行导致 1 万次索引扫 → 改 HASH JOIN 立刻快百倍。

**3. 锁排查：**
- **(1) 8 步：**
① 症状（应用报错超时、ORA-00054/00060）→ ② 看 V$SESSION event 列（'enq: TX - row lock contention' 等锁事件）→ ③ 找被阻塞者：WHERE event LIKE 'enq:%' AND SECONDS_IN_WAIT 高 → ④ 找阻塞者：V$SESSION.BLOCKING_SESSION 列（11g+）或 V$LOCK block=1 同 id1/id2 关联 request>0 → ⑤ 找被锁对象：V$LOCKED_OBJECT + DBA_OBJECTS 得 OWNER.OBJECT_NAME TYPE → ⑥ 阻塞者详情：PROGRAM/MACHINE/USERNAME/SQL_ID/PREV_SQL_ID → 找业务方"谁的程序"在干什么 → ⑦ 决策：能联系开发让他 COMMIT/ROLLBACK 优先；联系不上+业务受损严重→KILL；⑧ 根因修复：开发代码漏 COMMIT / FOR UPDATE 跨用户操作 / 外键未建索引 / 批量 DML 分批 COMMIT 等 + 后续监控锁等待比例。
- **(2) TX vs TM：**
| 锁 | Type | 保护对象 | 粒度 | 获取时机 |
|---|---|---|---|---|
| TX | Transaction Lock | 具体被修改行的行级排他 + 事务 ITL 槽 | 行级（事务里每条 DML 修改行在行块里锁标记，事务本身只有一个 TX 条目） | 事务第一条 DML 时分配一个 TX Enqueue；每行被 UPDATE/DELETE/INSERT 时在行头加锁标记 |
| TM | DML Enqueue (Table Lock) | 整张表结构，防止 DML 过程中其他会话 DDL DROP/ALTER 表结构 | 表级 | 任何 DML(INSERT/UPDATE/DELETE/MERGE) 执行时自动对被修改表加 TM（模式 SX=3），外键父子表涉及操作还会给父/子表加 TM |
- **(3) V$LOCK.block=1 → 该会话**持有锁**并且正在阻塞别人（别人在等它释放）；request>0 → 该会话在**请求锁**、正在等待别人释放。关联：`WHERE l1.block=1 AND l2.request>0 AND l1.id1=l2.id1 AND l1.id2=l2.id2 AND l1.type=l2.type`，然后 l1.sid 连阻塞者会话信息，l2.sid 连被阻塞者。
- **(4) 安全 KILL 流程：**
  ① 先 `SELECT sid, serial#, username, status, program, machine, sql_id, prev_sql_id, logon_time FROM V$SESSION WHERE sid = <阻塞者SID>`；（SID+SERIAL# 必须配对，同一个 SID 在不同时间可能是完全不同会话！同时存档信息，方便追责）；
  ② KILL 语法：`ALTER SYSTEM KILL SESSION '<sid>,<serial#>' IMMEDIATE;`（IMMEDIATE 不等待当前语句完成，立即回滚释放锁）；或 12c+ 更激进 `ALTER SYSTEM DISCONNECT SESSION '<sid>,<serial#>' IMMEDIATE;`；OS 层最后手段：Linux `kill -9 <V$PROCESS.SPID>`。
  **风险**：
  - ⚠️ **大事务回滚**：被杀会话如果 UPDATE 了几百万行，回滚可能需要几十分钟，期间锁仍然不释放、产生大量 redo/undo IO 拖慢整体；
  - ⚠️ **应用报错**：被 KILL 的应用收到 ORA-00028 "your session has been killed"，如果应用没有重试机制会直接功能异常；
  - ⚠️ **误 KILL 关键业务会话**：KILL 了正在批量跑日结/对账的核心任务 → 业务数据不一致，只能重跑几小时。
  **生产原则：能不杀就不杀，优先联系业务；杀前截图保存证据 + 口头告知负责人。**

**4. 优化方法论：**
- **(1) 5 层面自上而下 ROI 与手段：**
| 层面 | ROI | 至少 3 手段 |
|---|---|---|
| ① 应用 SQL 层 | ⭐⭐⭐⭐⭐ 最高 | 去掉 SELECT *；UNION ALL 替 UNION；索引列不写函数/避免隐式转换；Java Statement 改 PreparedStatement 绑定变量；深分页 Seek 方法（基于上次排序键）；相关子查询改 JOIN + GROUP BY；PLSQL 逐行 UPDATE 改单条集合化 MERGE。 |
| ② 索引层 | ⭐⭐⭐⭐ 高 | WHERE AND 等值列在前、范围列在后建 B 树复合索引；表达式查询建函数索引 FBI；外键列 100% 建索引（防 DELETE 父表锁全表 + 死锁）；DELETE 多的索引定期 ONLINE REBUILD 碎片；从未用索引 DROP。 |
| ③ 表空间/IO 层 | ⭐⭐⭐ 中 | 数据/索引/TEMP/UNDO/FRA 各自独立表空间散列到不同 Diskgroup；大表 1000 万+按时间 RANGE 分区 + 本地索引，分区剪枝；TEMP 放最快 NVMe；LMT+ASSM；小表 KEEP POOL；报表并行查询 DOP。 |
| ④ 内存/参数层 | ⭐⭐ 中低 | 11g+ 开 AMM MEMORY_TARGET；V$DB_CACHE_ADVICE 加 DB_CACHE_SIZE 命中率 <95%；SESSION_CACHED_CURSORS=100；OPEN_CURSORS=1000；PGA_AGGREGATE_TARGET 使 sorts(disk)=0。 |
| ⑤ OS/网络/硬件层 | ⭐ 最低 | 核心数据 + redo 放本地 NVMe；应用 DB 同机房 RTT<1ms；CPU 40%~60% 稳态；OS preinstall RPM 改内核；关 THP；ASM 多路径冗余。 |
- **(2) AWR 8 大板块：**
① Load Profile：TPS/SQL 执行/s / Redo / Hard Parse 是否异常暴涨（判断是业务量大还是 SQL 变差）；
② Instance Efficiency：命中率 > 目标线（Buffer 95%+、Library 99%+、Soft Parse 95%+）→ 不达标说明解析/内存层有问题；
③ ⭐ Top 5 Timed Foreground Events：第一诊断入口，看 DB Time 主要耗在 CPU / IO / 锁 / 日志 / latch 哪一类 → 决定后续排查方向；
④ Time Model：parse time elapsed 占比高=解析多绑变量差；PL/SQL time 高=慢过程用 HPROF 剖；
⑤ ⭐ SQL Statistics 8 个 Top：Elapsed/CPU/Gets/Reads/Executions/Parse/Version Count 各取前 10，80% 慢 SQL 就在这里；
⑥ Tablespace/File IO：哪个文件 Avg Rd(ms) >10ms 慢盘迁走；
⑦ Segments by Logical Reads / Row Lock Waits：热点对象是谁 → 针对性加索引/分区；
⑧ Advisory：Buffer / PGA / Shared Pool Advisory 看加大内存是否明显降物理读 → 决策要不要加内存。
- **(3) ① AUTOTRACE 对比：秒数受并发/缓存冷热影响极大，同一 SQL 冷跑 30s 热跑 0.5s 很正常，不稳定；但 consistent gets（逻辑读块数）是客观反映 SQL 本身工作量的金指标，100 万 → 1000 就是真优化了。物理读、排序次数也更客观；
  ② DML 回归：加索引加速 SELECT，但每条 INSERT/UPDATE/DELETE 要维护多棵索引树，假设订单表 5 个索引增到 8 个，INSERT TPS 可能从 2000 降到 1200（-40%）就不达标了，必须模拟生产写比例压测，TPS 下降低于 20% 才算通过。否则线上 SELECT 快了但用户下单卡死，得不偿失。

</details>

<details>
<summary>分析题参考答案</summary>

### 分析题 1 V$ SQL 书写

**需求 1（Top 10 耗时 SQL 24h）：**
```sql
SELECT * FROM (
    SELECT
        sql_id,
        child_number,
        executions                                                      AS execs,
        ROUND(elapsed_time  / 1000000, 2)                               AS total_elapsed_s,
        ROUND(cpu_time      / 1000000, 2)                               AS total_cpu_s,
        ROUND((elapsed_time / NULLIF(executions,0)) / 1000, 2)          AS per_exec_ms,
        disk_reads                                                      AS phys_reads,
        buffer_gets                                                     AS logical_reads,
        SUBSTR(sql_text, 1, 80)                                         AS sql_text_preview
      FROM V$SQLAREA
     WHERE parsing_schema_name NOT IN
             ('SYS','SYSTEM','SYSMAN','DBSNMP','GSMADMIN_INTERNAL','ORACLE_OCM')
       AND last_active_time > SYSDATE - 1
     ORDER BY elapsed_time DESC
) WHERE ROWNUM <= 10;
```

**需求 2（锁等待链）：**
```sql
SELECT
    '(BLOCKER sid='||b.sid||', serial#='||b.serial#||', user='||b.username||
        '@'||b.machine||', prog='||b.program||', status='||b.status||
        ')  ↓阻塞了↓  (WAITER sid='||w.sid||', serial#='||w.serial#||', user='||
        w.username||'@'||w.machine||', prog='||w.program||', 已等待='||
        w.seconds_in_wait||'s)'                                      AS block_chain,
    l.type || '(' || l.id1 || ',' || l.id2 || ')'                      AS lock_resource,
    DECODE(l.lmode, 0,'None',1,'Null(1)',2,'RowShare RS(2)',
           3,'RowExcl RX(3)',4,'Share S(4)',5,'SRowExcl SRX(5)',
           6,'Exclusive X(6)','?'||l.lmode)                            AS blocker_hold_mode,
    DECODE(wl.request,0,'None',1,'Null(1)',2,'RowShare RS(2)',
           3,'RowExcl RX(3)',4,'Share S(4)',5,'SRowExcl SRX(5)',
           6,'Exclusive X(6)','?'||wl.request)                         AS waiter_request_mode,
    b.sql_id                                                           AS blocker_sqlid,
    w.sql_id                                                           AS waiter_sqlid,
    w.event                                                            AS waiter_event
  FROM V$LOCK   l,
       V$LOCK   wl,
       V$SESSION b,
       V$SESSION w
 WHERE l.block    = 1
   AND wl.request > 0
   AND l.id1      = wl.id1
   AND l.id2      = wl.id2
   AND l.type     = wl.type
   AND l.sid      = b.sid
   AND wl.sid     = w.sid
 ORDER BY w.seconds_in_wait DESC;
```

**需求 3（TEMP 占用 Top 20）：**
```sql
SELECT * FROM (
    SELECT
        s.username,
        s.sid, s.serial#,
        s.machine, s.program, s.module,
        s.sql_id,
        ROUND(u.blocks * tb.block_size / 1024 / 1024, 2)                AS used_mb,
        u.segtype                                                         AS temp_seg_type,
        u.tablespace                                                      AS temp_tbs
      FROM V$TEMPSEG_USAGE u,     -- 11g+ 推荐 V$TEMPSEG_USAGE；老版本也可 V$SORT_USAGE
           V$SESSION     s,
           DBA_TABLESPACES tb
     WHERE u.session_addr = s.saddr
       AND u.tablespace   = tb.tablespace_name
     ORDER BY used_mb DESC
) WHERE ROWNUM <= 20;
```

---

### 分析题 2 执行计划判读优化

**(1) 4 处具体问题：**
① **Id=7/filter 行 TO_CHAR(i.create_time)：对 DATE 列 CREATE_TIME 套 TO_CHAR 函数 → IDX_CREATE_TIME 索引列函数失效 → 优化器只能用 INTERNAL_FUNCTION 转换 access，导致实际扫描 52 万行 + filter 后才几万 → 逻辑读爆炸；**
② **Id=3 CONCATENATION：OR-expansion 拼接 USER_ID 单列索引 + CREATE_TIME 单列索引的结果，本可一个复合索引一步到位，现在两条索引扫 13 万 + 52 万，回表两次；**
③ **Id=2 WINDOW SORT：ROW_NUMBER() OVER (ORDER BY create_time DESC) 需要对 26 万候选行全排序 → sorts(disk)=3 写 TEMP，因为输出按 create_time DESC 排序但 Oracle 无法利用单列索引（且前面 TO_CHAR 失效），SORT 26 万行耗 25s；**
④ **Id=1 filter RN BETWEEN 1 AND 20 只取 20 条 → 但前面 26 万行都 SORT 了，典型"大量计算最后只取 N 行"，应该让排序停在第 20 行就停止 STOPKEY。**
⑤ **SELECT *：只取前 20 条但所有列全取，回表多余 IO。（答 4 条即可满分）**

**(2) SQL 改写（去掉 TO_CHAR 改为 DATE 范围比较，保留原语义取 2024 年 1 月）：**
```sql
SELECT * FROM (
    SELECT t.*, ROW_NUMBER() OVER (ORDER BY create_time DESC) rn
      FROM t_order t
     WHERE t.create_time >= DATE '2024-01-01'
       AND t.create_time <  DATE '2024-02-01'   -- 上闭下开写法（避免时间部分截断误差）
       AND t.user_id = 10086
) WHERE rn BETWEEN 1 AND 20;
-- 或者 Oracle 12c+ 更简洁（应用不改造数据库端也 OK，老版还是 ROWNUM 包）
SELECT t.* FROM t_order t
 WHERE t.create_time >= DATE '2024-01-01'
   AND t.create_time <  DATE '2024-02-01'
   AND t.user_id = 10086
 ORDER BY t.create_time DESC
 FETCH FIRST 20 ROWS ONLY;
```

**(3) 复合索引 DDL（等值 user_id 在前，排序+范围 create_time 在后；DESC 让索引有序+ROW_NUMBER 不用 SORT）：**
```sql
CREATE INDEX idx_order_uid_ctime_desc ON t_order(user_id, create_time DESC)
  TABLESPACE users ONLINE NOLOGGING COMPUTE STATISTICS PARALLEL 4;
ALTER INDEX idx_order_uid_ctime_desc NOPARALLEL;
```
原因：user_id 等值先 B 树定位 = 10086 的子树 → 子树内 create_time DESC 天然有序 → ROW_NUMBER() 就是按这个顺序数 → 数到第 20 就可以停（STOPKEY），不需要 SORT 26 万行。

**(4) 优化后预期执行计划：**
```
| Id | Operation                        | Name                    |
|----|----------------------------------|-------------------------|
| 0  | SELECT STATEMENT                 |                         |
|* 1 |  VIEW                            |                         | filter("RN">=1 AND "RN"<=20)
| 2  |   WINDOW NOSORT STOPKEY          |                         | ✅ 索引有序，不用 SORT，停在第 20
| 3  |    TABLE ACCESS BY INDEX ROWID   | T_ORDER                 | 只回表 20 行
|* 4 |     INDEX RANGE SCAN            | IDX_ORDER_UID_CTIME_DESC| ✅ access("USER_ID"=10086 AND "CREATE_TIME">=... <...)
```
**预期 AUTOTRACE：** consistent gets ≈ 40~80（原来 48 万 → 千倍降）；physical reads ≈ 10~40（冷缓存首次 40，后续 0）；sorts(memory)=0、sorts(disk)=0（WINDOW NOSORT，无排序）；rows processed=20；总耗时从 26s → **约 0.05s~0.2s（100 倍 ~500 倍提升）**。

---

### 分析题 3 锁等待链实战

**(1) 阻塞者 SID = 253，被阻塞者 SID = 118。判断依据：**
- 方法 A V$SESSION：118 BLOCKING_SESSION_STATUS=VALID，BLOCKING_SESSION=253；
- 方法 B V$LOCK：同一资源 TX(524296,2183)，SID=253 行 block=1，lmode=6（持有排他锁）；SID=118 行 request=6（请求排他锁）→ block=1 是阻塞者，request>0 是被阻塞者；正确。

**(2) 阻塞者 STATUS=INACTIVE（当前没在执行 SQL）却持有排他锁 734 秒的典型场景：**
- **场景 1（最常见 70%）：应用代码漏 COMMIT / ROLLBACK。** 开发用 SQL Developer / Navicat / JDBC 连接执行 UPDATE ...，执行完 SQL 成功但忘了写 `connection.commit()`，连接归还到连接池时框架没有 auto-commit（或 auto-commit=false），连接 INACTIVE 但事务未结束锁持有。
- **场景 2（15%）：应用异常中断没处理。** 代码 UPDATE 后抛 RuntimeException，catch 块没写 ROLLBACK，异常吞掉连接归还连接池，事务仍活跃锁没释放；
- **场景 3（10%）：开发同学下班电脑关盖睡眠，SQL Developer 会话断开不彻底（PMON 没来得及回收）或 TCP 超时 2 小时才探测；**
- **场景 4（5%）：批量程序设计问题。** 一个大事务里先 UPDATE 某些行然后调外部接口等 10 分钟（HTTP/短信/支付回调），接口期间事务不结束锁一直挂着。

**(3) 被锁对象：** 根据 V$LOCKED OBJECT 中 TM 锁 ID1=87123（TM 的 id1 就是 OBJECT_ID），DBA_OBJECTS WHERE OBJECT_ID=87123 → OWNER=PAY，**OBJECT_NAME=T_PAY_ORDER，OBJECT_TYPE=TABLE**。（就是支付订单表）

**(4) 决策（无统一答案，** 阐述合理 3 条理由即可满分 **）：**
**方案 A（多数 DBA 会选）：KILL。决策理由：**
① 业务影响紧急：支付是核心链路，"支付卡住 582 秒 + 用户大面积投诉"，持续等待会造成资损（订单超时取消/用户重复下单/客诉量爆炸），ROI 最高是立即止血；
② 联系不上负责人：尝试联系 PAY 团队没人接，超过可等待时限（大促通常规定 5 分钟联系不上 DBA 有权决策 KILL，事后补报告）；
③ 阻塞者 INACTIVE 没在执行关键操作（STATUS=ACTIVE 跑批不能杀），KILL 仅回滚 734 秒前那次 UPDATE 而非大事务 → 回滚代价极低（<1 秒完成），几乎无副作用。
**杀会话完整 SQL：**
```sql
-- 查 SERIAL#
SELECT s.sid, s.serial#, s.username, s.status, s.program, s.machine, s.logon_time
  FROM V$SESSION s WHERE s.sid = 253;
-- 假设查到 SERIAL#=31578
ALTER SYSTEM KILL SESSION '253,31578' IMMEDIATE;
-- 1 分钟后确认 V$SESSION 查不到 SID=253，再看 118 的 EVENT 是不是从 TX 锁等待变成执行中 / SQL*Net message，再看应用支付成功率恢复。
```

**方案 B：不杀。决策理由（保守 DBA）：**
① 杀会话是高风险操作，PAY 方没授权不能随便杀；如果是支付对账批量程序在跑，KILL 回滚可能导致对账数据不一致要重跑几小时；
② 立即升级：电话 + 钉钉 + 微信拉 3 方群（DBA + PAY 架构 + 运维主管）升级决策，5 分钟内联系不到再升级 CEO 批；
③ 临时兜底：PAY 应用开**只读降级**或转备用库，减少主库锁等待压力，等批量结束锁自然释放。

（两种都可，关键是理由要配套决策，不是拍脑袋。）

---

### 分析题 4 AWR Top 5 Events 诊断

**(1) 每个事件含义 + 根因：**
| 事件 | 含义 | 场景根因推测 |
|---|---|---|
| DB CPU 1842s 40.9% | CPU 时间（解析 + SQL 执行 + 排序哈希） | CPU 占大头正常，但后续看到 Parse CPU 占 42% 就知道 CPU 浪费在硬解析而非执行 |
| enq: TX - row lock contention 1128s 25.1% | 行锁等待：大量会话在等其他事务释放某行 | 支付场景高频 UPDATE 同一账户余额行热点；或批量进程长事务占着行不放；或应用漏 COMMIT 僵尸 INACTIVE 锁 |
| db file scattered read 720s 16% | 多块读 FTS/FFS，全表/全索引扫 | 很多 SQL 缺索引，全表扫 I/O；Top SQL 是哪张表在 Segments 里查 |
| log file sync 435s 9.7% | COMMIT 等 LGWR 把 redo buffer 写 redo 日志刷盘完才返回 OK | ① commit 太频繁（每 1 行就 COMMIT，每秒 21 万次等待 × 1 行事务）；② redo 放在慢盘（虽然全闪但 LUN 队列拥塞？）；③ redo logfile 太小、切换太频繁 |
| db file sequential read 210s 4.7% | 索引单块读回表（正常读，不高） | 索引选择性好 + 回表量不大，占比低说明大部分 SQL 索引 OK |

**(2) 优化建议（按 ROI/占比优先级）：**
① **P0：锁等待（25.1%）→ 目标降到 <5%。** 做法：立刻跑前面分析题 3 的"锁等待链 SQL"找阻塞者 SID → 看是不是 INACTIVE 僵尸会话 + 应用漏 COMMIT → 联系支付团队立即发 Hotfix：所有数据库操作框架加 finally 块 COMMIT/ROLLBACK，连接池 `testOnBorrow=true` + rollback 归还；热点账户行改成排队/分库分表缓解。预期从 25% → 3% 左右（1000s 省下）。
② **P1：DB CPU 高 + 硬解析（结合 Time Model Parse 42%）→ 锁搞定后下一个。** 做法：V$SQL 找 Top CPU SQL（前面单 10 的 SQL 1）→ 看执行计划是不是 TABLE ACCESS FULL（对应 scattered read 根因）→ 加复合索引（ scattered read 顺带下降 16%）；另外如果 Parse Calls/Executions≈1，代码改绑定变量（ALTER SYSTEM SET cursor_sharing=FORCE 先临时救急），CPU 应该从 40% 降到 20%。
③ **P2：db file scattered read 16%。** 做法：Segments by Physical Reads / Top SQL by Reads 找对应的 SQL_ID + 表 → DISPLAY_CURSOR 看 FTS → 建索引（一般和 P1 是同一批 SQL），预期 16% → 3%。
④ **P3：log file sync 9.7%。** 做法：a. 查 V$SYSMETRIC "redo writes per second" / Top SQL by Executions 是不是每条小事务 commit 太多（Java 循环里每 update 一次 commit）→ 改批量 200 条一次 COMMIT；b. V$LOG 看 logfile 每组 < 1G 且切换 > 每 15 分钟一次 → 改 4~8 组每组 4G/8G；c. 虽然全闪，redo 成员有没有和 datafiles 放在同一块 ASM Diskgroup 抢 IO → 独立 REDO DG。预期 9.7% → 2%。
**整体预期：** DB Time 从 4500s 降到约 1300s（70%+ 下降），平均响应时间 × 4~5 倍提升。

**(3) 优化前后关键指标保存（验证数据）：**
AWR 层：① Load Profile 整体 TPS、Executions/s、Hard parses/s；② Instance Efficiency 全命中率（Buffer/Library/Soft Parse/Execute2Parse）；③ Top 5 Events 每个事件的 Time(s) 和 % DB Time；④ Top 10 SQL by Elapsed 的 per Exec(ms) 指标。
V$ 层（SQL 级）：⑤ Top SQL 的 AUTOTRACE consistent gets + physical reads + sorts(disk)（每条 Top SQL 前后快照）。
判断有效：Top 事件 % DB Time 加起来 < 25%（之前 96%），Top SQL per Exec 平均下降 > 50%，业务侧 TPS 提升 > 50% 且 P99 响应时间下降一半。

**(4) AWR 下一步定位具体 SQL 的两个板块：**
① **SQL ordered by Elapsed（或 CPU / Gets / Reads）**：直接拿具体 SQL_ID，哪个 SQL 耗时最多一条就改哪条；
② **Segments by Logical Reads / Physical Reads / Row Lock Waits**：定位到"热点表和索引"是什么，再结合 SQL 的 FROM 表反推。（这两块一般能锁定 90% 的性能问题的具体代码位置。）

</details>

<details>
<summary>综合题参考答案</summary>

### 综合题 1：完整慢 SQL 优化 5 步法

**Step 1 定位瓶颈点（至少 4 条）：**
① **相关子查询每行执行 → Id 8~9 SELECT SUM(subtotal) 对 14520 条发票每条子查询执行一次，每次 INDEX RANGE SCAN IDX_DET_INV 扫 14 行，合计 14520 × 14 = 20 多万次探针 + 回表 → 物理读 121 万条占比大头；**
② **TO_CHAR(i.invoice_date,'YYYY')='2024' 函数导致 IDX_INV_DATE 索引失效 → Id 7 filter 而不是 access，3200 × 180 ≈ 576k 次 NL 探针 + 回表逐行判断 TO_CHAR → consistent gets 爆炸 198 万；**
③ **NL 驱动表选反/索引不匹配：Id 5 c T_CUSTOMER FULL 扫 42000 行 credit_level='HIGH' filter 到 3200 行作为驱动表，Id 6 i T_INVOICE 按 customer_id 用 IDX_INV_CUST 每次回表 180 行才满足 status/amount/date → NL 外表 3200 大了，应该先过滤 i T_INVOICE 再 NL 小结果集，或者直接 HASH JOIN 两张；**
④ **SORT ORDER BY 输入 14520 行排序，虽然 sorts(disk)=2 不多，但如果配合复合索引 (customer_id, invoice_date DESC) 包含所有 WHERE 条件 + ORDER BY 列 → 完全避免 SORT ORDER BY（14520 行排序秒级但前面代价大）；**
⑤ **SELECT c.customer_name... + 相关子查询 = 每行额外执行 → 改写子查询 JOIN 表 + GROUP BY 聚合一次，避免相关子查询；**
（写出 4 条即可，每条 0.5 分）

**Step 2 拿真实执行计划 + 等待事件：**
```sql
-- 先开启统计收集，再跑一次 SQL
ALTER SESSION SET STATISTICS_LEVEL = 'ALL';
SELECT /*+ GATHER_PLAN_STATISTICS */ c.customer_name, ... -- 原SQL完整语句;
-- 查 DISPLAY_CURSOR：ALLSTATS LAST 拿 A-Rows/Buffers/A-Time
SELECT prev_sql_id FROM V$SESSION WHERE sid = USERENV('SID');
-- 假设 prev_sql_id = abcd1234
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR('abcd1234', NULL, 'ALLSTATS LAST +PEEKED_BINDS'));
```
**主要 V$SESSION_WAIT 等待事件（基于 198 万逻辑读 + 121 万物理读）：**
- ① `db file sequential read`（INDEX RANGE SCAN 相关子查询每次回表单块读，最多）；
- ② `db file scattered read`（T_CUSTOMER 全表扫 + T_INVOICE 部分多块读）；
- ③ `direct path read temp`（sorts(disk)=2 的写临时段排序/聚合，有就有，不多）。

**Step 3 优化动作（至少 6 条，覆盖多层）：**
*① SQL 层 3 条 + 索引层 2 条 + 其他层 1 条*
**SQL 层 a：去函数失效。** TO_CHAR(i.invoice_date,'YYYY') = '2024' → 改为 `i.invoice_date >= DATE'2024-01-01' AND i.invoice_date < DATE'2025-01-01'`（上闭下开，不截断时间精度，后续索引能走 access）。
**SQL 层 b：相关子查询 → JOIN + GROUP BY，聚合一次。** 把 `SELECT SUM(subtotal) FROM detail d WHERE d.invoice_id=i.invoice_id` → 改写成子查询 `(SELECT invoice_id, SUM(subtotal) detail_sum FROM detail GROUP BY invoice_id)` 左 JOIN 主查询，只执行一次 GROUP BY 聚合（1.2 亿行 GROUP 用 HASH GROUP BY）。
**SQL 层 c：ORDER BY 配合索引消除排序。** 主查询 WHERE 过滤后按 i.invoice_date DESC，建完索引就天然有序，不需要 SORT（或加 `/*+ FIRST_ROWS(20) */` Hint 让优化器倾向 NL 快速返回前 N 行，如果报表有分页只看第一页）。
**SQL 层 d（可选）：先过滤驱动表，小表驱动。** 先过滤 i T_INVOICE 的 2024 年 UNPAID >5000 得到一个小结果集，再 NL JOIN c T_PAY 小表。
**索引层 a：T_INVOICE 复合索引覆盖 WHERE + ORDER BY。** CREATE INDEX idx_inv_2024_filter ON t_invoice(customer_id, invoice_date DESC, status, amount) ONLINE TABLESPACE users COMPUTE STATISTICS；（customer_id 等值 JOIN，invoice_date 范围+排序 DESC，后面 status/amount 作为 filter 列，建立后 WHERE customer_id = ? AND invoice_date >=? AND <? AND status='UNPAID' AND amount>5000 全部 access/filter 在索引完成，不必大量回表）。
**索引层 b：T_INVOICE_DETAIL 覆盖索引加速 SUM 聚合。** CREATE INDEX idx_det_inv_subtotal ON t_invoice_detail(invoice_id, subtotal) ONLINE TABLESPACE users；（SUM(subtotal) 只要这两列，索引本身就是覆盖查询直接 INDEX FAST FULL SCAN / RANGE SCAN，不必回 1.2 亿行表）。
**其他层（参数/Hint）：如果连接方式还是选错 NL，加 Hint `/*+ LEADING(i c) USE_HASH(c d) FULL(d) PARALLEL(8) */`（i 过滤后小结果集先 JOIN c，再 HASH JOIN 聚合子查询，报表场景允许并行）。**

**综合改写 SQL 示例：**
```sql
SELECT /*+ FIRST_ROWS(1000) */
       c.customer_name,
       i.invoice_no,
       i.invoice_date,
       i.amount,
       d_sum.detail_sum
  FROM t_invoice i
  JOIN t_customer c
    ON c.customer_id = i.customer_id
  LEFT JOIN (
    SELECT /*+ INDEX_FFS(d IDX_DET_INV_SUBTOTAL) */
           invoice_id, SUM(subtotal) AS detail_sum
      FROM t_invoice_detail d
     GROUP BY invoice_id
  ) d_sum ON d_sum.invoice_id = i.invoice_id
 WHERE c.credit_level = 'HIGH'
   AND i.invoice_date >= DATE '2024-01-01'
   AND i.invoice_date <  DATE '2025-01-01'
   AND i.status = 'UNPAID'
   AND i.amount > 5000
 ORDER BY i.invoice_date DESC;
```

**Step 4 验证预期指标 + DML 回归：**
| 指标 | 优化前 | 优化后预期 | 下降比 |
|---|---|---|---|
| Elapsed | 72.3s | 1.5s ~ 4s | **约 20~50 倍** |
| consistent gets | 1,980,400 | 15,000 ~ 40,000 | **50 ~ 130 倍** |
| physical reads | 1,210,500 | 500 ~ 3,000（冷缓存首次，后续为 0） | **几百倍** |
| sorts(disk) | 2 | 0 | 消除磁盘排序 |
| rows processed | 14,520 | 14,520（不变） | 结果不变 ✅ |
**DML 回归：** 取 t_invoice/t_invoice_detail 生产 1% 数据做压测，对比建索引前后 INSERT/UPDATE/DELETE TPS：
- T_INVOICE INSERT：原 TPS = 2300/s → 新 TPS ≥ 2300 × 80% = 1840/s ✅ 合格（新增 idx_inv_2024_filter 复合索引，1 个索引增 TPS 降 ≤20% 可接受）；
- T_INVOICE UPDATE(amount/status)：降幅类似，≤ 25% ✅；
- T_INVOICE_DETAIL INSERT：新增 IDX_DET_INV_SUBTOTAL (invoice_id, subtotal) → 原 5400/s → ≥ 4500/s ✅。
**为什么必须测：** ERP 月结 SELECT 快了，但日常单据录入 INSERT/UPDATE 不能因为多了两个索引 TPS 掉 50%（否则月结 1 小时完成但订单录入 8 小时堵塞，得不偿失）。索引是 SELECT/DML 间的 trade-off，要平衡。

---

### 综合题 2：AWR 全案诊断报告

**(1) Top 5 Problem List（按严重度排序）：**
| ID | 问题名称 | AWR 证据 | 根因假设 | 影响 DB Time 占比 |
|----|----------|----------|----------|-------------------|
| P1 | 严重缺乏绑定变量 + 硬解析爆炸 | Load Profile: Hard Parse = 940/s；Instance Eff: Soft Parse=64.4% / Library Hit=62.8% / Execute2Parse=41.2% / %Non-Parse CPU=58%；Time Model parse time 34.4%，hard parse 24.8%；Top SQL Parse Calls = Executions；Top Events latch shared pool 34.1% + library cache lock 19.6% | 99% 应用代码**全部用 String 拼 SQL**，Java 用 Statement + 字符串拼接用户 ID/金额，完全没 PreparedStatement，每条 SQL 都是硬解析。 | latch shared pool 34.1% + library cache 19.6% + parse time 34.4% ≈ 约 **60%~70% DB Time** 直接浪费在解析而非执行。 |
| P2 | log file sync 提交等待占 13.4% | Top Event log file sync = 14500s 9.7%，Avg 1.7ms；Load Profile Redo 2340KB/s（虽全闪，但每秒事务 TPS 2340 → 每行 commit 1 次） | 支付账户 UPDATE 余额代码 **每条 UPDATE 后立即 COMMIT**（单行一次事务），没有批量；或者 redo logfile 太小切换太频繁。 | 13.4% DB Time，约 1/7。 |
| P3 | DB CPU 占 18.3% 但大部分 CPU 耗在解析 | Time Model Parse CPU = 41.9% 总 CPU → 18.3% × 42% ≈ 7.7% DB CPU 是解析浪费；加上 P1 解决后 CPU 自然下降 | P1 派生问题，绑变量后 CPU 应该剩一半不到。 | 独立影响约 7%，P1 修复后同降。 |
| P4 | 个别 Top SQL 可能还有索引优化空间（虽然主要矛盾是解析） | Top SQL by Elapsed 第 1 条 per Exec 1.93ms / 第 3 条有 TO_CHAR 可能函数失效；Segments by Logical Reads：T_USER + 它索引占 21.6% + T_ACC 8.7% 共 30% | T_USER 查询可能还是函数失效 / 复合索引缺失；T_ACC 账户热点 UPDATE 也许能热点分片。 | 不是主要矛盾，但 P1P2 解决后能再降 5%~8%。 |
| P5 | cursor: pin S wait on X 占 4.8% | Top Events 4.8%；和 P1 解析风暴相关：某条 SQL 正在硬解析，其他同 SQL 会话等游标互斥 X 锁。 | P1 派生问题，绑变量后自然消失。 | 4.8% 派生。 |

**(2) 可操作优化建议（每条落地 + 验证）：**
**建议 1（针对 P1/P3/P5，最高优先级 本周完成）：**
- **短期救急（0.5 小时生效 + 风险告知）：** `ALTER SYSTEM SET CURSOR_SHARING = FORCE SCOPE = BOTH;` → Oracle 自动把 SQL 中的字面量（数字/字符串）替换成绑定变量 :SYS_B_0/:SYS_B_1，瞬间复用 cursor 大幅减少硬解析。⚠️ 风险：可能改变个别 SQL 的执行计划（ACS 自适应游标）；CLOB/某些复杂 SQL 替换失败；先在备库/UAT 压测验证没回归再改生产，改完盯 1 小时 AWR。
- **中期治本（1~2 周开发发版）：** 全量代码改造：Java 所有 JDBC Statement 改 `PreparedStatement` 占位符 `?`（MyBatis 用 `#{}` 不要 `${}`）；.NET 用 `SqlParameter` 参数化查询；静态 SQL 统一封装，禁止任何 String 拼接字面量到 SQL。
- **参数配合（立即生效）：** `ALTER SYSTEM SET SESSION_CACHED_CURSORS = 300 SCOPE=BOTH;`（会话缓存 300 个 cursor，减少会话内反复解析同一个 SQL）；`OPEN_CURSORS=1500`（默认一般够，不够就加）。
- **验证：** 1 小时后 AWR：Hard parses/s < 20（降 97%+）；Soft Parse% > 95%；Library Hit% > 99%；Top Events latch shared pool 占比 < 2%。
预期收益：latch + 解析浪费的 60%~70% DB Time 降到 < 5% → DB Time 立刻砍半以上，**QPS 从 2340 → 5000+ 翻倍，立竿见影**。

**建议 2（针对 P2 log file sync，次高 3 天内）：**
- **a. 代码批量 COMMIT：** 支付批量扣款/对账任务里 `UPDATE acc SET balance = balance - 1` 循环 1000 次 → 加计数器每 500 条 COMMIT 一次，减少 log file sync 次数 × 500；OLTP 单笔支付本来就是一次事务，不用改。
- **b. 调整 Redo Logfile 大小组数：** `SELECT GROUP#, BYTES/1024/1024 MB, MEMBERS, STATUS FROM V$LOG;` 如果每组 < 1G 且 `SELECT * FROM V$LOG_HISTORY WHERE FIRST_TIME > SYSDATE-1` 看切换频率 > 每 15 分钟一次就加大：`ALTER DATABASE ADD LOGFILE GROUP 4 ('+DATA/...') SIZE 8G BLOCKSIZE 512;` 建 4~6 组每组 4G~8G，避免频繁切换 checkpoint；
- **c.（架构层）redo 独立 ASM Diskgroup**，不要和 data/FRA 共用一块盘组（虽然全闪，队列也会抢）。
- **验证：** AWR Top Events log file sync 占比 < 2%；Avg wait < 1ms。
预期收益：13.4% → < 2%，DB Time 再降 11%。

**建议 3（针对 P4 Top SQL 索引 + SQL 改造，与 P1 并行 1 周内）：**
- **Top 1 SELECT T_USER：** 拿 SQL_ID = a1b2c3d4e5f6 → `SELECT sql_fulltext FROM V$SQLAREA WHERE sql_id='a1b2c3d4e5f6';` 取完整 SQL 文本 → DISPLAY_CURSOR ALLSTATS LAST → 如果有 `WHERE TO_CHAR(create_time)=...` → 改范围条件 + 建立 (user_id, create_time, ...) 复合覆盖索引，逻辑读再降 90%+。
- **Top 3 SELECT COUNT(*) FROM T_ORDER TO_CHAR：** 同上去掉 TO_CHAR；高频 COUNT(\*) 走 IDX_ORDER_STATUS_CTIME 复合索引扫索引不回表；报表走物化视图每 5 分钟刷新一次。
- **验证：** 每条 Top SQL per Exec(ms) 下降 > 50%；Segments by Logical Reads Top 1 段占比 < 5%。
预期收益：Top SQL 单独各降 50% 耗时，整体 DB Time 再降 5%~8%。

**建议 4（针对热点账户行锁 P1 收尾后排查 TX 锁占比，2 周内架构优化）：**
- 如果 P1 搞定后 enq: TX 占比还高 → Segments by Row Lock Waits 看 T_PAY / T_ACC 占大头 → 账户余额"热点行"瓶颈：① 应用层**账户拆分子账户**（按金额分桶 100 个子行，扣款随机选某子行 UPDATE，冲突 × 1/100）；② 缓存层 Redis 扣库存，异步队列落 DB；③ 热点更新用 `SELECT ... FOR UPDATE NOWAIT` 立即报错不排队。
- 验证：TX 锁等待占比 < 1%。

**建议 5（监控告警长效机制 + 压测回归）：**
- 所有优化上线后 818 前，连续 3 天每天 2 小时全链路压测，QPS 到目标 10000，记录基线 AWR 报告；
- **建立 4 项日常核心告警（Prometheus/Grafana + Zabbix）：**
  ① DB Time / CPU Count > 0.7（当前是 0.375 正常，但 > 0.7 = CPU 开始饱和，P1 级短信 + 电话）；
  ② Hard Parse per sec > 50（P2 级短信，立即通知 DBA + 应用负责人）；
  ③ Library Cache Hit% < 95%（P2）；
  ④ enq: TX row lock 每秒等待次数 > 100 且 平均等待 > 100ms（P3 钉钉群报警）；
  ⑤ Top Session SECONDS_IN_WAIT(TX 锁) > 60s（P2 告警阻塞链自动推）。
（4 条即可。）

**(3) 整体优化收益预估：**
P1 + P2 + P3 + P4 全部落地后，**DB Time / Elapsed = 30.0 → 预计降到 7~9**（约 1/4）；**总 DB Time 从 108000s 降到 25000s~32000s 范围**（减 70%~75%）。
业务指标：**QPS 从 2340/s 提升到 6000~8000/s（2.5~3.5 倍）；平均响应时间从 X ms 降到 X/3~X/4 ms（60%~75% 降）；P99 响应更明显降一个数量级。818 峰值应该扛得住。**

**(4) 日常监控告警（4 条以上）：**
① **DB Time / (Elapsed × CPU Count) > 0.7**（实例级负载健康度）、**DB CPU 利用率 > 80%**：P1 电话 + 钉钉，30 分钟内 DBA 介入；
② **硬解析 Hard Parses / sec > 50**（连续 5 分钟）、**Soft Parse % < 90%**：P2 短信 + 邮件，推送给应用负责人 + DBA 群；
③ **锁等待告警：V$SESSION SECONDS_IN_WAIT > 120s 且 EVENT LIKE 'enq: TX%' 会话数 ≥ 5**：自动推锁阻塞链（blocker SID/SERIAL#@PROG → waiter 清单 + 被锁对象）到 DBA + 业务线钉钉群；
④ **Top Temp Usage > 50GB 且 30s 内不下降** → 查 V$TEMPSEG_USAGE 告警；
⑤ **AWR 日报告自动发邮件**（夜间 23:00-0:00 快照）：自动比对昨日命中率、Top SQL 新增异常 SQL、Top Events 占比变化；
⑥ **Latch Misses > 500/s**（shared pool / library cache）→ P2 短信。
（答 4 条以上即满分。）

</details>

---

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | 字典前缀/V$本质/执行计划方法/FTS vs Index/NL vs Hash/TX TM/Blocking_Session/等待 scattered read/优化顺序/AWR Top 入口 |
| 多选 | 5 | 15 | 常用视图用途/执行计划危险信号/TM相容矩阵/等待事件优化/SQL层优化手段 |
| 判断 | 5 | 10 | 延迟段创建/ALLSTATS LAST真实统计/TM冲突不同行不等待/等待事件与锁≠全表扫/软解析低=差 |
| 简答 | 4 | 20 | 视图对比表+V$6个；4种执行计划对比表+列含义+E/A-Rows；锁排查8步+KILL风险；5层面优化+AWR8板块+回归验证 |
| 分析 | 4 | 32 | V$SQL Top 10/锁链SQL/TEMP占用SQL书写；慢SQL执行计划4问题+TO_CHAR改法+复合索引DDL+预期计划；锁链实战阻塞者INACTIVE场景+生产KILL决策3理由；AWR Top5诊断+优先级建议+指标验证 |
| 综合 | 2 | 20 | 完整慢SQL 5步法（定位瓶颈+真实计划+6条优化动作+指标回归）；AWR全案诊断（Top5问题列表+5条优化建议+定量收益+4项监控告警） |
| **合计** | **30** | **117** | 覆盖第10章全部核心考点，重在 DBA 工具 SQL 书写、执行计划实战判读、锁等待生产场景决策、AWR 全案诊断优化思维 |

---

## 章节导航

- 上级 MOC：[[MOC - Oracle数据库管理]]
- 本章知识点 MOC：[[MOC - 第10章]]（[[10.1 常用数据字典视图]]、[[10.2 SQL执行计划查看]]、[[10.3 锁等待与会话排查]]、[[10.4 基础优化思路]]）
- 上一章习题：[[MOC - 第9章习题]]
