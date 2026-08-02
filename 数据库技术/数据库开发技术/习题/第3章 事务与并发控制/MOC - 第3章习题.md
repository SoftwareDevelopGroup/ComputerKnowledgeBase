---
domain: 数据库技术
subject: 数据库开发技术
type: exercise
chapter: 第3章 事务与并发控制
section: 第3章综合习题
tags: [数据库开发,习题,事务,ACID,隔离级别,锁,死锁,并发控制]
prerequisites: []
---

第3章习题覆盖 ACID 特性、事务控制语句、脏读/不可重复读/幻读、四种隔离级别、锁类型与粒度、意向锁、死锁与两阶段锁协议，重点考查并发场景分析与解决方案。配套知识点见 [[MOC - 第3章]]。本章基于 MySQL 8.0 InnoDB。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | 原子性实现机制 | 概念理解 |
| 单2 | 单选 | 持久性实现机制 | 概念理解 |
| 单3 | 单选 | MySQL 默认隔离级别 | 概念理解 |
| 单4 | 单选 | 脏读定义 | 概念理解 |
| 单5 | 单选 | 幻读定义 | 概念理解 |
| 单6 | 单选 | SAVEPOINT 作用 | 概念理解 |
| 单7 | 单选 | InnoDB 行锁基于索引 | 概念理解 |
| 单8 | 单选 | 排他锁加锁语句 | 概念理解 |
| 单9 | 单选 | 死锁产生条件数 | 概念理解 |
| 单10 | 单选 | 两阶段锁协议阶段 | 概念理解 |
| 多1 | 多选 | ACID 四特性 | 概念辨析 |
| 多2 | 多选 | 死锁四条件 | 概念辨析 |
| 多3 | 多选 | 隔离级别与异常对应 | 概念辨析 |
| 多4 | 多选 | 死锁预防策略 | 概念辨析 |
| 多5 | 多选 | 意向锁作用 | 概念辨析 |
| 判1 | 判断 | MySQL InnoDB RR 额外避免幻读 | 概念理解 |
| 判2 | 判断 | 一致性是目标 | 概念理解 |
| 判3 | 判断 | 无索引更新退化为表锁 | 概念理解 |
| 判4 | 判断 | 长事务影响 | 概念理解 |
| 判5 | 判断 | 2PL 保证可串行化 | 概念理解 |
| 简1 | 简答 | ACID 各自实现机制 | 分析说明 |
| 简2 | 简答 | 脏读/不可重复读/幻读区别 | 分析说明 |
| 简3 | 简答 | 四种隔离级别与异常屏蔽 | 分析说明 |
| 简4 | 简答 | 死锁产生条件与预防 | 分析说明 |
| 分1 | 分析 | 脏读场景分析与解决 | 综合应用 |
| 分2 | 分析 | 不可重复读场景分析 | 综合应用 |
| 分3 | 分析 | 死锁场景分析与预防 | 综合应用 |
| 分4 | 分析 | 锁升级与索引缺失分析 | 综合应用 |
| 综1 | 综合 | 转账事务与隔离级别综合 | 综合应用 |
| 综2 | 综合 | 高并发抢购死锁处理综合 | 综合应用 |

## 一、单选题（每题 2 分，共 10 题）

**1. InnoDB 实现事务原子性的机制是（　）。**
A. redo log 刷盘
B. undo log 回滚
C. MVCC 多版本控制
D. Next-Key Lock

**2. InnoDB 实现事务持久性的机制是（　）。**
A. undo log
B. redo log（WAL）提交时强制刷盘
C. 间隙锁
D. 共享锁

**3. MySQL InnoDB 的默认隔离级别是（　）。**
A. READ UNCOMMITTED
B. READ COMMITTED
C. REPEATABLE READ
D. SERIALIZABLE

**4. 脏读是指（　）。**
A. 事务内同一行两次读取结果不同
B. 事务读到了另一事务未提交的修改，且该事务随后回滚
C. 同一查询两次结果集行数不同
D. 事务读到已提交的修改

**5. 幻读关注的现象是（　）。**
A. 已存在行被 UPDATE
B. 结果集行数变化（INSERT/DELETE）
C. 读到未提交数据
D. 事务回滚

**6. `SAVEPOINT sp` 的作用是（　）。**
A. 提交事务
B. 设置保存点，支持部分回滚
C. 设置隔离级别
D. 释放所有锁

**7. 关于 InnoDB 行锁，下列说法正确的是（　）。**
A. 行锁基于数据页
B. 行锁基于索引，无索引更新会退化为对全部扫描行加锁（相当于表锁）
C. 行锁只能加在主键上
D. 行锁不支持 WHERE 条件

**8. 下列语句对命中行加排他锁（X 锁）的是（　）。**
A. `SELECT * FROM t WHERE id=1 FOR SHARE`
B. `SELECT * FROM t WHERE id=1 FOR UPDATE`
C. `SELECT * FROM t WHERE id=1`
D. `BEGIN`

**9. 死锁产生必须同时满足的条件个数是（　）。**
A. 2 个
B. 3 个
C. 4 个
D. 5 个

**10. 两阶段锁协议（2PL）的两个阶段是（　）。**
A. 加锁阶段与解锁阶段（扩展阶段只加锁，收缩阶段只放锁）
B. 读阶段与写阶段
C. 提交阶段与回滚阶段
D. 解析阶段与执行阶段

## 二、多选题（每题 3 分，共 5 题）

**1. 下列属于事务 ACID 特性的有（　）。**
A. 原子性 Atomicity
B. 一致性 Consistency
C. 隔离性 Isolation
D. 持久性 Durability

**2. 死锁产生的四个必要条件包括（　）。**
A. 互斥
B. 占有并等待
C. 不剥夺
D. 循环等待

**3. 关于隔离级别与异常，下列对应正确的有（　）。**
A. READ UNCOMMITTED 可能脏读
B. READ COMMITTED 避免脏读
C. REPEATABLE READ 避免不可重复读
D. SERIALIZABLE 避免幻读

**4. 死锁的预防策略包括（　）。**
A. 一次性加锁（事务开始申请全部锁）
B. 固定加锁顺序（所有事务按相同顺序加锁）
C. 缩短事务
D. 永不使用事务

**5. 意向锁（IS/IX）的作用包括（　）。**
A. 快速判断表中是否有行级锁，避免逐行检查
B. 加行级 S 锁前先加表级 IS
C. 加行级 X 锁前先加表级 IX
D. 替代行锁实现隔离

## 三、判断题（每题 2 分，共 5 题）

**1. MySQL InnoDB 在 REPEATABLE READ 级别下通过 Next-Key Lock 额外避免了幻读，这与 SQL 标准 RR（允许幻读）不同。**

**2. 一致性是 ACID 的目标，原子性、隔离性、持久性是手段。**

**3. InnoDB 的行锁基于索引，若 UPDATE 的 WHERE 未命中索引，会退化为对全部扫描行加锁，相当于表锁。**

**4. 长事务在 MVCC 下会阻止 undo log 回收，导致表空间膨胀。**

**5. 严格 2PL（X 锁持有到事务结束）保证可串行化且避免级联回滚。**

## 四、简答题（每题 5 分，共 4 题）

**1. 说明 ACID 四个特性各自的实现机制。**

**2. 区分脏读、不可重复读、幻读三种并发问题。**

**3. 列出四种 SQL 隔离级别及其对三种异常的屏蔽情况。**

**4. 说明死锁产生的四个条件与至少三种预防策略。**

## 五、分析题（每题 6 分，共 4 题，要求分析并发场景并给出解决方案）

**1. 脏读场景分析：** 事务 T1 执行 `UPDATE account SET balance = balance - 100 WHERE id = 1`（未提交），事务 T2 在此期间读取 `balance`。在 READ UNCOMMITTED 下会发生什么？给出解决方案（隔离级别与实现机制）。

**2. 不可重复读场景分析：** 事务 T2 两次读取 `balance`，期间事务 T1 提交了 `UPDATE`。描述在 READ COMMITTED 与 REPEATABLE READ 下的差异，并说明 InnoDB 在 RR 下如何通过 MVCC 实现。

**3. 死锁场景分析：** 连接 T1 先 UPDATE id=1 再 UPDATE id=2；连接 T2 先 UPDATE id=2 再 UPDATE id=1。分析死锁形成过程，给出两种预防方案。

**4. 锁升级分析：** 某 `UPDATE employee SET salary = salary + 100 WHERE dept_id = 5` 中 `dept_id` 无索引。分析该语句在 InnoDB 下的锁行为与对并发的影响，给出修复方案。

## 六、综合题（每题 8 分，共 2 题）

**1. 转账事务综合：** 账户表 `account(id, balance)`，要求实现 A→B 转账 100 元。**
- **(1)** 写出完整的事务 SQL（含 START TRANSACTION/COMMIT/ROLLBACK）；
- **(2)** 说明应使用什么隔离级别，并解释为何不能用 READ UNCOMMITTED；
- **(3)** 若需防止并发超扣，应在查询余额时使用什么语句？说明其锁类型。

**2. 高并发抢购死锁综合：** 抢购场景下，多个并发事务同时对同一商品先查询库存再扣减，出现大量死锁（错误码 1213）与超卖。要求：**
- **(1)** 分析死锁与超卖的根因；
- **(2)** 给出基于 `SELECT ... FOR UPDATE` 的解决方案（含完整存储过程）；
- **(3)** 说明应用层应如何处理 1213 错误码；
- **(4)** 给出至少两条死锁预防建议（加锁顺序、事务长度等）。

## 答案与解析

<details>
<summary>单选题答案</summary>

1. **B**。原子性由 undo log 回滚实现，记录修改前数据，回滚时反向恢复。
2. **B**。持久性由 redo log（WAL）实现，提交时强制刷盘，崩溃后重放恢复。
3. **C**。MySQL InnoDB 默认 REPEATABLE READ，并通过 Next-Key Lock 额外避免幻读。
4. **B**。脏读是读到未提交的修改，且该事务随后回滚，读到"从未存在过"的数据。
5. **B**。幻读关注结果集行数变化（INSERT/DELETE）；不可重复读关注已存在行被 UPDATE。
6. **B**。SAVEPOINT 设置保存点，支持 `ROLLBACK TO sp` 部分回滚。
7. **B**。InnoDB 行锁基于索引，无索引更新退化为全部扫描行加锁，相当于表锁。
8. **B**。`FOR UPDATE` 加排他锁（X 锁）；`FOR SHARE` 加共享锁。
9. **C**。死锁四条件：互斥、占有并等待、不剥夺、循环等待，必须同时满足。
10. **A**。2PL 分扩展阶段（只加锁）与收缩阶段（只放锁）。

</details>

<details>
<summary>多选题答案</summary>

1. **ABCD**。ACID 即原子性、一致性、隔离性、持久性。
2. **ABCD**。死锁四条件全部必要。
3. **ABCD**。RU 可能脏读；RC 避免脏读；RR 避免不可重复读；SERIALIZABLE 避免幻读。
4. **ABC**。一次性加锁、固定加锁顺序、缩短事务均为预防策略；永不使用事务不可行。
5. **ABC**。意向锁用于快速判断表是否有行锁，加行 S 前加 IS，加行 X 前加 IX；不替代行锁。

</details>

<details>
<summary>判断题答案</summary>

1. **√**。InnoDB 在 RR 下用 Next-Key Lock（行锁+间隙锁）额外避免幻读，超出 SQL 标准 RR。
2. **√**。原子性、隔离性、持久性是手段，一致性是目标。
3. **√**。行锁基于索引，无索引 WHERE 退化为全扫描行加锁，相当于表锁。
4. **√**。长事务阻止 undo log 回收，导致表空间膨胀。
5. **√**。严格 2PL（X 锁持有到事务结束）保证可串行化且避免级联回滚。

</details>

<details>
<summary>简答题答案</summary>

**1. ACID 实现机制：**
- 原子性：undo log 回滚
- 一致性：业务约束 + 原子性 + 隔离性 + 持久性协作
- 隔离性：锁 + MVCC
- 持久性：redo log（WAL）提交时强制刷盘

**2. 三种并发问题：**
- 脏读：读到未提交修改，回滚后数据"从未存在"
- 不可重复读：同一行两次读取结果不同（UPDATE）
- 幻读：同一查询两次结果集行数不同（INSERT/DELETE）

**3. 隔离级别与异常屏蔽：**
| 级别 | 脏读 | 不可重复读 | 幻读 |
| ---- | ---- | ---- | ---- |
| READ UNCOMMITTED | 可能 | 可能 | 可能 |
| READ COMMITTED | 避免 | 可能 | 可能 |
| REPEATABLE READ | 避免 | 避免 | 可能（InnoDB 额外避免） |
| SERIALIZABLE | 避免 | 避免 | 避免 |

**4. 死锁四条件：互斥、占有并等待、不剥夺、循环等待。预防策略：**
- 一次性加锁（事务开始申请全部锁）
- 固定加锁顺序（所有事务按相同顺序加锁）
- 缩短事务，减少锁持有时间
- 应用捕获 1213 后重试

</details>

<details>
<summary>分析题答案</summary>

**1. 脏读分析：** READ UNCOMMITTED 下 T2 读到 T1 未提交的 `balance-100` 中间值；若 T1 回滚，T2 基于错误余额做决策。**解决方案**：提升到 READ COMMITTED 及以上，InnoDB 通过语句级 MVCC（每条 SQL 读最新已提交快照）避免脏读。生产环境至少 RC，推荐默认 RR。

**2. 不可重复读分析：** READ COMMITTED 下 T2 两次读取同一行结果不同（T1 提交了 UPDATE）；REPEATABLE READ 下 T2 两次读取一致。**InnoDB 在 RR 下通过事务级 MVCC**：事务首个读建立快照，事务内所有读基于该快照，故两次读取一致；T1 的 UPDATE 对 T2 不可见。

**3. 死锁分析：** T1 持 id=1 的 X 锁请求 id=2；T2 持 id=2 的 X 锁请求 id=1 → 循环等待。InnoDB 死锁检测发现环后回滚代价较小事务。**预防方案**：①固定加锁顺序——T1/T2 都先锁 id 小的行；②一次性加锁——事务开始申请全部所需锁。

**4. 锁升级分析：** `dept_id` 无索引时，InnoDB 的行锁基于索引，UPDATE 的 WHERE 未命中索引会退化为对全部扫描行加 X 锁，相当于表锁，严重阻塞并发。**修复方案**：在 `dept_id` 上建索引 `CREATE INDEX idx_dept ON employee(dept_id);`，使锁只加在命中行。

</details>

<details>
<summary>综合题答案</summary>

**1. 转账事务综合：**

**(1)** 完整事务 SQL：
```sql
-- MySQL 8.0 / InnoDB
START TRANSACTION;
UPDATE account SET balance = balance - 100 WHERE id = 1;  -- A 扣款
UPDATE account SET balance = balance + 100 WHERE id = 2;  -- B 入账
COMMIT;
-- 若第二步失败：ROLLBACK;
```

**(2)** 应使用 REPEATABLE READ（MySQL 默认）。不能用 READ UNCOMMITTED：会导致脏读，事务可能读到另一事务未提交的余额中间值并基于其做决策，回滚后数据错误。

**(3)** 防止并发超扣应使用：
```sql
SELECT balance FROM account WHERE id = 1 FOR UPDATE;
```
`FOR UPDATE` 加排他锁（X 锁），其他事务的读写均阻塞，保证校验余额与扣减在同一事务内原子完成。

**2. 高并发抢购死锁综合：**

**(1) 根因：** 多个并发事务先查后改、无锁保护导致：①超卖——两事务同时读到库存=10 各扣 8；②死锁——不同事务以不同顺序锁商品行，形成循环等待。

**(2) 解决方案（存储过程，FOR UPDATE 锁定）：**
```sql
-- MySQL 8.0
DELIMITER $$
CREATE PROCEDURE seckill(
    IN  p_product_id BIGINT,
    IN  p_qty        INT,
    OUT p_result     VARCHAR(32)
)
BEGIN
    DECLARE v_stock INT;
    START TRANSACTION;
    -- 锁定商品行，防止并发超卖与死锁（统一入口）
    SELECT stock INTO v_stock FROM product WHERE id = p_product_id FOR UPDATE;
    IF v_stock IS NULL THEN
        ROLLBACK; SET p_result = 'NOT_FOUND';
    ELSEIF v_stock < p_qty THEN
        ROLLBACK; SET p_result = 'OUT_OF_STOCK';
    ELSE
        UPDATE product SET stock = stock - p_qty WHERE id = p_product_id;
        INSERT INTO stock_log(product_id, delta) VALUES (p_product_id, -p_qty);
        COMMIT; SET p_result = 'OK';
    END IF;
END$$
DELIMITER ;
```

**(3) 应用层处理 1213：** 捕获 `SQLException`，若 `getErrorCode()==1213`（死锁）或 `1205`（锁等待超时），在合理次数内**重试**整个事务，而非直接报错。

**(4) 死锁预防建议：**
- 固定加锁顺序：所有事务按相同顺序（如 id 升序）加锁；
- 缩短事务：减少锁持有时间，避免长事务；
- 一次性加锁：事务开始申请全部锁；
- 确保 WHERE 走索引，避免锁升级为表锁。

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | ACID 机制、隔离级别、锁类型、死锁、2PL |
| 多选 | 5 | 15 | ACID、死锁条件、隔离级别对应、预防、意向锁 |
| 判断 | 5 | 10 | InnoDB RR 防幻读、一致性目标、锁退化、长事务、2PL |
| 简答 | 4 | 20 | ACID 机制、三种异常、隔离级别、死锁 |
| 分析 | 4 | 24 | 脏读/不可重复读/死锁/锁升级场景 |
| 综合 | 2 | 16 | 转账事务、抢购死锁处理 |
| 合计 | 30 | 105 | 覆盖第3章事务与并发全部主题 |

## 导航

- 上级 MOC：[[MOC - 数据库开发技术]]、[[MOC - 第3章]]
- 本章知识点：[[3.1 事务ACID特性]]、[[3.2 并发问题与隔离级别]]、[[3.3 锁机制基础]]
- 上一章习题：[[MOC - 第2章习题]]
- 下一章习题：[[MOC - 第4章习题]]
