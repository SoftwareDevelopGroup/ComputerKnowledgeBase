---
domain: 数据库技术
subject: Oracle数据库管理
type: knowledge
chapter: 第6章 Oracle表空间与对象管理
tags: [Oracle,DBA,表空间,TABLESPACE,永久表空间,临时表空间,撤销表空间,CREATE TABLESPACE,分区表,索引,约束,视图,序列,同义词]
prerequisites: ["数据库原理", "第4章 Oracle数据库启动与关闭", "第5章 用户、权限与角色管理"]
aliases: [MOC - 第6章, 第6章 Oracle表空间与对象管理]
---

# MOC - 第6章 Oracle表空间与对象管理

> [!info] 本章定位
> 本章是Oracle DBA的**存储与对象管理核心章**，解决"数据存在哪里？怎么放最合理？如何创建和管理数据库对象（表/约束/索引/视图/序列/同义词）？大表如何分区提升性能？"这四个数据库物理存储核心问题。前半节详解三类表空间（永久/临时/撤销）的创建维护与DMT vs LMT、ASSM vs MSSM对比；后半节详述建表约束、索引类型适用场景、序列同义词视图、分区表基础与分区剪枝原理。
>
> 存储设计是数据库性能、可用性、可恢复性的基石：合理的表空间布局是IO均衡的前提；合适的索引类型与分区策略是SQL性能优化的基础；理解表空间备份模式与DROP高风险是运维必备。本章与[[MOC - 第7章 Oracle重做日志、归档模式]]（在线重做与归档）、[[MOC - 第8章 Oracle备份与恢复]]（表空间级备份恢复）强关联。

## 学习路线图

```mermaid
flowchart LR
    S1[6.1 三类表空间管理<br/>永久/临时/撤销<br/>CREATE/ALTER/DROP TABLESPACE]
    S2[6.2 数据表与约束<br/>CREATE TABLE完整语法<br/>5类约束+4种状态]
    S3[6.3 索引序列同义词视图<br/>B树/位图/函数/反向键索引<br/>CREATE SEQUENCE/SYNONYM/VIEW]
    S4[6.4 分区表基础<br/>RANGE/LIST/HASH/复合分区<br/>分区维护+剪枝原理]

    S1 --> S2
    S2 --> S3
    S3 --> S4

    S1 -.对象容器.-> S2
    S2 -.表上建对象.-> S3
    S3 -.大表优化.-> S4
```

> [!tip] 路线说明
> 推荐按 6.1 → 6.2 → 6.3 → 6.4 顺序学习。6.1 先掌握表空间三大类（永久/临时/撤销）的创建与维护（含DROP INCLUDING CONTENTS高风险）；6.2 掌握CREATE TABLE全子句+5类约束+约束4种状态+TRUNCATE vs DELETE区别；6.3 对比B树索引与位图索引适用场景（高基数vs低基数）、序列用法、视图WITH CHECK OPTION；6.4 理解分区剪枝Partition Pruning原理、4种分区类型适用场景、6种分区维护操作。

## 知识点导航

| 节 | 主题 | 核心要点 | 入口链接 |
| ---- | ---- | ---- | ---- |
| 6.1 | 永久、临时、撤销表空间 | CREATE TABLESPACE完整语法、DATAFILE/TEMPFILE参数、LMT vs DMT、ASSM vs MSSM、5大默认表空间、DROP TABLESPACE INCLUDING CONTENTS AND DATAFILES危险 | [[6.1 永久表空间、临时表空间、撤销表空间]] |
| 6.2 | 数据表、约束管理 | CREATE TABLE完整语法（PCTFREE/PCTUSED/STORAGE/ORGANIZATION）、5类约束+4种状态+可延迟、TRUNCATE vs DELETE对比、Oracle专有数据类型VARCHAR2/NULL=空串/NUMBER/DATE含时分秒 | [[6.2 数据表、约束管理]] |
| 6.3 | 索引、序列、同义词、视图 | 5类索引（B树/位图/函数/反向键/域）适用场景对比、CREATE INDEX ONLINE REBUILD、序列CYCLE/CACHE、同义词PUBLIC/PRIVATE、视图WITH CHECK OPTION/READ ONLY | [[6.3 索引、序列、同义词、视图]] |
| 6.4 | 分区表基础 | 4种分区类型（RANGE/LIST/HASH/复合）、6种分区维护操作（ADD/DROP/TRUNCATE/SPLIT/MERGE/EXCHANGE）、分区剪枝Partition Pruning原理、分区性能收益 | [[6.4 分区表基础]] |

## 核心考点

> [!warning] 重点掌握
> 1. **CREATE TABLESPACE完整语法**：DATAFILE大小与AUTOEXTEND、EXTENT MANAGEMENT LOCAL（AUTOALLOCATE vs UNIFORM）、SEGMENT SPACE MANAGEMENT AUTO（ASSM）、BLOCKSIZE非标准块大小、LOGGING/NOLOGGING影响。
> 2. **DROP TABLESPACE INCLUDING CONTENTS AND DATAFILES高风险命令**：永久物理删除所有数据文件+表空间+所有对象，生产执行前必须先备份+查DBA_SEGMENTS确认为空，CASCADE CONSTRAINTS子句删除跨表空间外键。
> 3. **临时表空间与临时表空间组**：CREATE TEMPORARY TABLESPACE使用TEMPFILE而非DATAFILE、SWITCH TEMPFILE、数据库级默认临时表空间、临时表空间组（分散大排序IO）。
> 4. **撤销表空间与RETENTION GUARANTEE**：CREATE UNDO TABLESPACE、ALTER SYSTEM SWITCH UNDO TABLESPACE、RETENTION GUARANTEE保证长查询一致性读不报错ORA-01555 Snapshot Too Old、V$UNDOSTAT监控撤销段使用。
> 5. **5类约束+4种状态+可延迟**：PRIMARY KEY/FOREIGN KEY/UNIQUE/NOT NULL/CHECK；约束状态ENABLE NOVALIDATE/DISABLE NOVALIDATE/ENABLE VALIDATE/DISABLE VALIDATE；DEFERRABLE INITIALLY IMMEDIATE vs DEFERRED（事务提交时才检查）。
> 6. **TRUNCATE TABLE vs DELETE FROM 区别对比表**：TRUNCATE是DDL（不可回滚、自动COMMIT、闪回需回收站）、不写RED0日志、重置高水位线HWM；DELETE是DML（可回滚、产生大量UNDO/RED0）、保留高水位线后续FTS仍扫空块。
> 7. **B树索引vs位图索引适用场景**：B树（默认）适合高基数列（主键/唯一键/性别不适合）、OLTP高DML表；位图适合低基数列（性别/状态/省份只有几十个值）、数据仓库低DML，位图索引对DML操作会锁整个位图段导致高并发DML死锁。
> 8. **分区表4种分区类型+6种维护操作**：RANGE分区（按日期/数字连续值）、LIST分区（枚举值省份/状态）、HASH分区（散列均匀IO）、复合分区（RANGE-LIST/RANGE-HASH）；分区剪枝Partition Pruning原理（WHERE条件包含分区键，Oracle直接跳过其他分区扫描，核心性能收益）。

## 自测题

> [!question] 1. CREATE TABLESPACE语句中，EXTENT MANAGEMENT LOCAL UNIFORM SIZE 1M和AUTOALLOCATE有什么区别？生产永久表空间选哪种更好？
> > [!check]- 参考答案
> > Oracle 9i起表空间区管理分**字典管理DMT**（已淘汰）和**本地管理LMT**（默认，生产必选），LMT下区分配方式分两种：
> > - **UNIFORM SIZE 1M**：表空间中每次分配的区（Extent）大小都统一为1M，每个区大小一致。优点：不会产生大量大小不一的碎片，空间管理简单可预测；适合数据量稳定、对象增长速度均匀的表空间。
> > - **AUTOALLOCATE**（AUTOALLOCATE = SYSTEM，默认）：Oracle自动根据段增长的需要分配64K/1M/8M/64M等不同大小的区，对象小时用小区，对象大了自动用大区；优点：空间浪费少（小对象小区不浪费）；缺点：碎片可能略多。
> >
> > 生产环境推荐：**SEGMENT SPACE MANAGEMENT AUTO（ASSM） + EXTENT MANAGEMENT LOCAL AUTOALLOCATE** 组合是19c默认，绝大多数场景最佳；**大表/分区表专用表空间**可选择UNIFORM SIZE 16M/64M更简单，避免大量小区导致$UET等数据字典视图膨胀。

> [!question] 2. 简述TRUNCATE TABLE employees 和 DELETE FROM employees 两条SQL的8个核心区别（执行速度、回滚能力、触发器、触发器触发、闪回能力、对索引影响、属于DML/DDL、空间回收、WHEN子句能力）。
> > [!check]- 参考答案
> > | 对比维度 | DELETE FROM employees | TRUNCATE TABLE employees |
> > | ---- | ---- | ---- |
> > | **语言类型** | DML（数据操作语言），事务级操作 | DDL（数据定义语言），隐式COMMIT前所有未提交事务 |
> > | **是否可回滚** | ✅ COMMIT之前ROLLBACK可撤销 | ❌ 不可回滚！执行完立即永久生效，只能恢复：① 有闪回表FLASHBACK TABLE employees TO BEFORE DROP;（回收站）② 有备份从备份恢复 |
> > | **执行速度** | 慢（逐行删除，每行产生UNDO回滚段+REDO重做日志） | 极快（不处理数据行，只修改数据字典中区分配位图，标记为"已释放"，数据量大小对速度几乎无影响，1亿行表秒级完成） |
> > | **DML触发器** | 会逐行触发DELETE触发器 | ❌ **不会触发DML触发器！** 有审计触发器的表用TRUNCATE会漏审计 |
> > | **闪回能力** | 可通过闪回查询（Flashback Query）查到事务前旧数据；COMMIT后需UNDO_RETENTION内 | 作为DDL，闪回只能依赖FLASHBACK TABLE TO BEFORE DROP（回收站内）或闪回数据库/FRA |
> > | **高水位线HWM** | 保留HWM不变，删除后空块仍在HWM之下，后续全表扫描FTS仍会扫空块浪费IO | 重置HWM到段起点，HWM之后所有空块不再被扫描！后续FTS速度快、索引统计信息也被更新 |
> > | **索引状态** | DELETE后索引叶子块保留，B树会产生叶块碎片（空块需后续COALESCE） | TRUNCATE同时TRUNCATE所有关联索引，索引也重置HWM，最干净 |
> > | **WHERE条件能力** | ✅ DELETE FROM emp WHERE deptno=10; 可按条件删部分行 | ❌ 只能TRUNCATE整表，不能加WHERE条件删部分行，分区表可TRUNCATE PARTITION分区级 |
> >
> > 额外两个常见差异：
> > - **引用约束**：有外键引用本表时TRUNCATE会失败（需先DISABLE外键或用CASCADE子句12c+）；DELETE只要外键ON DELETE CASCADE即可级联删除。
> > - **权限**：DELETE是对象权限（GRANT DELETE ON ...）；TRUNCATE需要DROP ANY TABLE系统权限或表Owner才行（TRUNCATE是强DDL权限）。

> [!question] 3. 为什么OLTP系统高并发订单表的"订单状态status"列（只有10个枚举值）上建了位图索引反而导致大量死锁和DML缓慢？正确应该建什么索引？
> > [!check]- 参考答案
> > **位图索引适用场景错误导致的死锁**：位图索引的存储结构是为每个键值存储一个位图串（每个位代表一行是否是该值）。当DML修改一条记录的status值时，Oracle需要对**整个位图段加锁**（锁住该status值对应的所有行位图），而不是只锁被修改的那一行。
> >
> > 高并发OLTP订单表场景下：两个用户同时修改不同订单行的status（用户A改status=1→2，用户B改status=2→3），但因为位图索引加的是**段级大锁**，A锁住status=1和status=2的位图段，B锁住status=2和status=3的位图段，就会互相等待产生位图索引死锁。
> >
> > **结论**：位图索引只适合**数据仓库/报表库（DML极低、SELECT为主）的低基数列**。
> >
> > **OLTP高并发场景正确做法**：
> > - 若是低基数status列且经常作为WHERE过滤条件：用**B树索引**即可（虽然区分度不高，但不会锁表，适合高并发）；
> > - 若是status只出现在组合WHERE（如WHERE user_id=? AND status=?）：建**复合B树索引(user_id, status)**，user_id是高基数在前，status在后辅助过滤，既满足查询又避免锁表。

> [!question] 4. 分区表Partition Pruning（分区剪枝）的核心原理是什么？举RANGE分区的sales_range表按sale_date分区的具体例子说明分区剪枝带来的性能收益，并说明哪些写法会导致分区剪枝失效（写了分区键也没剪到）。
> > [!check]- 参考答案
> > **分区剪枝（Partition Pruning，也称分区消除）**：Oracle优化器在解析SQL时，判断WHERE条件中包含**分区键列**且条件是**可推导范围/等值**时，直接确定只需扫描满足条件的**一个或少数几个分区**，物理上跳过其余所有分区的数据文件和索引段，完全不访问它们，从而减少扫描数据量，是分区表的**头号性能收益来源**。
> >
> > **RANGE分区例子**：SALES_RANGE表按SALE_DATE列做范围分区，分为P2021（<2022）、P2022（<2023）、P2023（<2024）、P2024（<2025）四个分区，历史+当前共10亿行数据：
> > ```sql
> > SELECT SUM(amount) FROM sales_range WHERE sale_date >= DATE'2024-01-01' AND sale_date < DATE'2024-02-01';
> > ```
> > - 未分区（普通大表）：全表扫描10亿行（~100GB），耗时几十分钟；
> > - **分区剪枝生效**：WHERE条件能确定只要扫P2024分区中1月份的数据，只需扫描1/4分区中约1/12的数据（~2GB），耗时从几十分钟降到几十秒，性能提升上百倍。
> >
> > **常见分区剪枝失效反模式（写了分区键也不剪）**：
> > 1. **对分区键列用了函数**：`WHERE TO_CHAR(sale_date,'YYYY') = '2024'` → 分区键上加函数导致Oracle无法判断分区范围，扫全部分区。替代写法：`WHERE sale_date >= DATE'2024-01-01' AND sale_date < DATE'2025-01-01'`。
> > 2. **分区键参与隐式类型转换**：`WHERE sale_date = '2024-01-01'`（字符串隐式转DATE，受NLS影响剪枝失效）。替代：显式DATE字面量。
> > 3. **分区键列参与运算**：`WHERE sale_date + 7 > DATE'2024-01-01'` → 失效。
> > 4. **OR连接包含非分区条件**：`WHERE sale_date > DATE'2024-01-01' OR channel='ONLINE'` → 因OR条件后半部分无分区键，只能扫全部分区。
> > 5. **本地索引列查询但条件无分区键**：即使查询本地分区索引，WHERE条件不包含分区键也会导致索引全分区扫描（不如全局索引）。
> >
> > 快速验证剪枝：EXPLAIN PLAN FOR SQL语句后查看执行计划的PARTITION START/PARTITION STOP列，值=具体分区号或KEY(SUBQ)=剪枝生效；值=1~4（1到最后分区号）=扫全部分区剪枝失效。

## 章节导航

- 上一级：[[MOC - Oracle数据库管理]]
- 上一章：[[MOC - 第5章 用户、权限与角色管理]]
- 下一章：[[MOC - 第7章 Oracle重做日志、归档模式]]
- 本章习题：[[MOC - 第6章习题]]
