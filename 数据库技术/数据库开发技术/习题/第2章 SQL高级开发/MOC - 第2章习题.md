---
domain: 数据库技术
subject: 数据库开发技术
type: exercise
chapter: 第2章 SQL高级开发
section: 第2章综合习题
tags: [数据库开发,习题,视图,存储过程,触发器,函数,游标]
prerequisites: []
---

第2章习题覆盖视图、存储过程、触发器、自定义函数、游标五大 SQL 高级开发对象，重点考查可编程对象的编写与执行逻辑。配套知识点见 [[MOC - 第2章]]。本章基于 MySQL 8.0（InnoDB），SQL 编程题要求编写完整可运行代码。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | 视图本质 | 概念理解 |
| 单2 | 单选 | WITH CHECK OPTION 作用 | 概念理解 |
| 单3 | 单选 | 存储过程参数模式 | 概念理解 |
| 单4 | 单选 | 触发器触发时机 | 概念理解 |
| 单5 | 单选 | MySQL 触发器粒度 | 概念理解 |
| 单6 | 单选 | 函数与存储过程返回值 | 概念理解 |
| 单7 | 单选 | 游标操作步骤顺序 | 概念理解 |
| 单8 | 单选 | 视图不可更新场景 | 概念理解 |
| 单9 | 单选 | MySQL 函数 DETERMINISTIC | 概念理解 |
| 单10 | 单选 | 游标 NOT FOUND 处理 | 概念理解 |
| 多1 | 多选 | 视图作用 | 概念辨析 |
| 多2 | 多选 | 存储过程优缺点 | 概念辨析 |
| 多3 | 多选 | 触发器应用场景 | 概念辨析 |
| 多4 | 多选 | MySQL 游标特性 | 概念辨析 |
| 多5 | 多选 | 函数 vs 存储过程区别 | 概念辨析 |
| 判1 | 判断 | 视图存储数据 | 概念理解 |
| 判2 | 判断 | MySQL 行级触发 | 概念理解 |
| 判3 | 判断 | 函数内 DML | 概念理解 |
| 判4 | 判断 | 游标必须 CLOSE | 概念理解 |
| 判5 | 判断 | 触发器可显式调用 | 概念理解 |
| 简1 | 简答 | 视图不可更新场景 | 分析说明 |
| 简2 | 简答 | 存储过程参数 IN/OUT/INOUT | 分析说明 |
| 简3 | 简答 | BEFORE 与 AFTER 触发器区别 | 分析说明 |
| 简4 | 简答 | 游标性能注意事项 | 分析说明 |
| SQL1 | SQL编程 | 存储过程（转账） | 综合应用 |
| SQL2 | SQL编程 | 触发器（审计） | 综合应用 |
| SQL3 | SQL编程 | 自定义函数 | 综合应用 |
| SQL4 | SQL编程 | 游标（部门汇总） | 综合应用 |
| 综1 | 综合 | 视图+触发器+函数综合 | 综合应用 |
| 综2 | 综合 | 存储过程事务与游标综合 | 综合应用 |

## 一、单选题（每题 2 分，共 10 题）

**1. 关于视图，下列说法正确的是（　）。**
A. 视图是物化表，存储真实数据
B. 视图是一条命名查询的虚拟表，本身不存储数据（物化视图除外）
C. 视图不能用于权限控制
D. 视图修改后底层表数据不变

**2. `WITH CHECK OPTION` 的作用是（　）。**
A. 检查视图查询性能
B. 限制通过视图执行的 INSERT/UPDATE 必须满足视图 WHERE 条件
C. 检查视图是否可更新
D. 检查基表约束

**3. 存储过程中 `INOUT` 参数的含义是（　）。**
A. 调用方传入只读参数
B. 过程内赋值后返回，调用方不传入初始值
C. 调用方传入初始值，过程可修改后返回
D. 仅用于输出错误码

**4. 触发器中 `BEFORE` 时机的典型用途是（　）。**
A. 事件后记录审计日志
B. 事件前校验业务规则或改写 NEW 值
C. 事件后级联更新汇总表
D. 事件后发送通知

**5. 关于 MySQL 触发器，下列说法正确的是（　）。**
A. MySQL 支持语句级与行级两种触发
B. MySQL 仅支持行级触发（FOR EACH ROW）
C. MySQL 触发器可被应用显式调用
D. MySQL 支持同一表同事件多个同类触发器

**6. 关于 MySQL 自定义函数，下列说法正确的是（　）。**
A. 函数可返回多个值
B. 函数可在 SQL 表达式中调用，必须返回一个值
C. 函数内可执行 INSERT/UPDATE/DELETE
D. 函数用 CALL 语句调用

**7. 游标操作的正确顺序是（　）。**
A. OPEN → DECLARE → FETCH → CLOSE
B. DECLARE → OPEN → FETCH → CLOSE
C. DECLARE → FETCH → OPEN → CLOSE
D. OPEN → FETCH → DECLARE → CLOSE

**8. 下列视图通常**不可更新**的是（　）。**
A. 单表简单视图
B. 包含聚合函数（SUM/COUNT）的视图
C. 只含等值过滤的视图
D. WITH CHECK OPTION 的视图

**9. MySQL 中创建函数时 `DETERMINISTIC` 关键字表示（　）。**
A. 函数只能读取数据
B. 相同输入恒定输出；缺省时 MySQL 可能拒绝创建以避免复制不一致
C. 函数执行计划固定
D. 函数只能被一个会话调用

**10. MySQL 存储过程中游标 `FETCH` 到末尾时，应通过什么机制处理（　）。**
A. 自动返回 NULL
B. 声明 CONTINUE HANDLER FOR NOT FOUND 设置标志变量
C. 抛出异常并自动回滚
D. 自动关闭游标

## 二、多选题（每题 3 分，共 5 题）

**1. 视图的主要作用包括（　）。**
A. 简化查询（封装多表 JOIN）
B. 数据安全（行列级权限控制）
C. 逻辑独立性（屏蔽底层表结构调整）
D. 自动生成索引

**2. 存储过程的优点包括（　）。**
A. 预编译，执行计划可复用
B. 减少应用与 DB 之间的往返
C. 封装业务逻辑，统一权限控制
D. 完全可移植，无方言差异

**3. 触发器的典型应用场景有（　）。**
A. 审计日志（记录变更前后值）
B. 数据校验（BEFORE 检查业务规则）
C. 级联操作（维护冗余或派生字段）
D. 软删除（BEFORE DELETE 改写为 UPDATE）

**4. 关于 MySQL 游标的特性，下列正确的有（　）。**
A. 只能在存储过程/函数内使用
B. 默认只读、只进
C. 支持滚动游标（FETCH PRIOR/FIRST/LAST）
D. 必须声明 NOT FOUND 处理器

**5. 函数与存储过程的区别包括（　）。**
A. 函数必须返回一个值，存储过程可 0 或多个 OUT/INOUT
B. 函数在 SQL 表达式中调用，存储过程用 CALL
C. MySQL 中函数一般不允许 DML，存储过程允许
D. 函数可包含事务控制，存储过程不能

## 三、判断题（每题 2 分，共 5 题）

**1. 视图本身存储真实数据，每次访问直接读取视图存储的内容。**

**2. MySQL 仅支持行级触发（FOR EACH ROW），不支持语句级触发。**

**3. MySQL 自定义函数内可直接执行 INSERT/UPDATE/DELETE 修改数据。**

**4. 游标 OPEN 后结果集在服务端占用资源，必须显式 CLOSE 释放。**

**5. 触发器可被应用程序通过 CALL 语句显式调用执行。**

## 四、简答题（每题 5 分，共 4 题）

**1. 列举视图不可更新的常见场景（至少 4 种）。**

**2. 说明存储过程参数 IN、OUT、INOUT 三种模式的方向与用途。**

**3. 比较 BEFORE 与 AFTER 触发器在时机、能否修改 NEW 值、典型用途上的区别。**

**4. 列出游标使用的 4 条性能注意事项。**

## 五、SQL编程题（每题 8 分，共 4 题，要求编写完整可运行的 MySQL 8.0 代码）

**1. 编写存储过程。** 依赖表 `account(id, balance)`、`transfer_log(id, from_id, to_id, amount, created_at)`。要求：实现转账存储过程 `transfer(p_from, p_to, p_amount, OUT p_result)`，在事务内校验余额不足、账户不存在，扣款与入账并记录日志，结果通过 OUT 参数返回（`OK`/`INSUFFICIENT_BALANCE`/`FROM_NOT_FOUND`）。

**2. 编写触发器。** 依赖表 `employee(id, name, salary, dept_id, updated_at)` 与 `employee_audit(id, emp_id, old_salary, new_salary, op_user, op_time)`。要求：创建 `AFTER UPDATE` 行级触发器，仅当 salary 发生变化时记录变更前后的薪资到审计表。

**3. 编写自定义函数。** 要求：创建函数 `fn_dept_avg_salary(p_dept_id)` 返回指定部门平均薪资（NUMERIC(15,2)），部门无员工时返回 0，并在 SQL 中调用示例。

**4. 编写游标存储过程。** 依赖表 `department(id, dept_name)`、`employee(id, name, dept_id, salary)`、`dept_salary_summary(dept_id, total, cnt, avg_sal, snapshot_at)`。要求：使用游标遍历所有部门，为每个部门生成一条薪资汇总记录（total、cnt、avg_sal、snapshot_at）。

## 六、综合题（每题 8 分，共 2 题）

**1. 某电商系统有 `orders(id, customer_id, total_amount, status, placed_at)` 与 `order_item(id, order_id, product_id, quantity, unit_price)`。要求：**
- **(1)** 创建一个只读视图 `v_paid_orders`，展示已支付订单（status='PAID'）的订单号、客户 ID、总金额与下单时间；
- **(2)** 创建一个 `BEFORE INSERT` 触发器，校验订单 `total_amount` 必须为正数，否则用 `SIGNAL SQLSTATE` 抛错；
- **(3)** 创建一个函数 `fn_order_total(p_order_id)` 返回指定订单所有明细金额合计（quantity×unit_price）。

**2. 某库存系统有 `product(id, name, stock)` 与 `stock_log(id, product_id, delta, op_time)`。要求编写存储过程 `stock_out(p_product_id, p_qty, OUT p_result)`：**
- **(1)** 事务内用 `SELECT ... FOR UPDATE` 锁定商品行；
- **(2)** 校验库存充足，不足返回 `OUT_OF_STOCK`；
- **(3)** 扣减库存并写入 stock_log；
- **(4)** 说明该存储过程中 FOR UPDATE 的作用与隔离级别配合。

## 答案与解析

<details>
<summary>单选题答案</summary>

1. **B**。视图是命名查询的虚拟表，本身不存储数据（物化视图除外），每次访问重写为底层查询执行。
2. **B**。WITH CHECK OPTION 限制通过视图的 INSERT/UPDATE 必须满足视图 WHERE 条件，防止"插入后从视图查不到"。
3. **C**。INOUT 双向，调用方传入初始值，过程可修改后返回。
4. **B**。BEFORE 时机用于事件前校验业务规则或改写 NEW 值；AFTER 用于事件后审计/级联。
5. **B**。MySQL 仅支持行级触发（FOR EACH ROW），不支持语句级触发；触发器不可显式调用；不支持同表同事件多个同类触发器（Oracle 支持）。
6. **B**。函数必须返回一个值，可在 SQL 表达式中调用；MySQL 中函数内一般不允许 DML，用 CALL 调用的是存储过程。
7. **B**。DECLARE → OPEN → FETCH → CLOSE。
8. **B**。含聚合函数（SUM/COUNT/AVG）、DISTINCT、GROUP BY、HAVING、UNION、子查询引用基表、多表 JOIN 非键保持表的视图通常不可更新。
9. **B**。DETERMINISTIC 表示相同输入恒定输出；缺省时 MySQL 可能拒绝创建以避免复制不一致。
10. **B**。必须声明 `DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done=1`，否则 FETCH 到末尾会抛出错误。

</details>

<details>
<summary>多选题答案</summary>

1. **ABC**。视图作用：简化查询、数据安全（行列权限）、逻辑独立性；不自动生成索引。
2. **ABC**。存储过程优点：预编译执行计划可复用、减少往返、封装业务统一权限；缺点是可移植性差、方言差异大，故 D 错。
3. **ABCD**。四类典型场景：审计日志、数据校验、级联操作、软删除。
4. **ABD**。MySQL 游标只能存储过程内用、只读只进、必须声明 NOT FOUND 处理器；不支持滚动游标（Oracle/SQL Server 支持）。
5. **ABC**。函数必须返回一个值、SQL 表达式调用、MySQL 一般不允许 DML；存储过程可包含事务控制（START TRANSACTION/COMMIT），函数不应包含，故 D 错。

</details>

<details>
<summary>判断题答案</summary>

1. **×**。视图是虚拟表，本身不存储数据（物化视图除外），每次访问重写为底层查询。
2. **√**。MySQL 仅支持行级触发（FOR EACH ROW），不支持语句级触发。
3. **×**。MySQL 函数内禁止 INSERT/UPDATE/DELETE（存储过程可以）。
4. **√**。OPEN 后结果集在服务端占用资源，必须显式 CLOSE，否则连接结束才释放。
5. **×**。触发器由 DBMS 在事件发生时自动调用，应用无法显式调用。

</details>

<details>
<summary>简答题答案</summary>

**1. 视图不可更新场景：**
- 包含聚合函数（SUM/COUNT/AVG）
- 包含 DISTINCT、GROUP BY、HAVING、UNION
- 包含子查询引用基表
- 多表 JOIN 且非键保持表（key-preserved）

**2. 参数模式：**
| 模式 | 方向 | 说明 |
| ---- | ---- | ---- |
| IN | 调用方→过程 | 默认模式，传入只读 |
| OUT | 过程→调用方 | 过程内赋值后返回 |
| INOUT | 双向 | 调用方传入初始值，过程可修改后返回 |

**3. BEFORE vs AFTER：**
- 时机：BEFORE 在事件前，AFTER 在事件后
- 修改 NEW：BEFORE 可修改 NEW，AFTER 不可
- 典型用途：BEFORE 用于校验/改写；AFTER 用于审计/级联/通知

**4. 游标性能注意事项：**
1. 行级游标是反模式，应优先重写为单条集合 SQL；
2. 结果集占用资源，必须显式 CLOSE；
3. 长时间未关闭的游标持有锁或导致 MVCC 版本无法回收；
4. 用 EXPLAIN 分析游标内查询执行计划。

</details>

<details>
<summary>SQL编程题答案（完整可运行 MySQL 8.0 代码）</summary>

**1. 转账存储过程：**

```sql
-- MySQL 8.0 / InnoDB
-- 前置：建表
CREATE TABLE account (
    id      BIGINT PRIMARY KEY,
    balance NUMERIC(15,2) NOT NULL
);
CREATE TABLE transfer_log (
    id         BIGINT AUTO_INCREMENT PRIMARY KEY,
    from_id    BIGINT,
    to_id      BIGINT,
    amount     NUMERIC(15,2),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$
CREATE PROCEDURE transfer(
    IN  p_from   BIGINT,
    IN  p_to     BIGINT,
    IN  p_amount NUMERIC(15,2),
    OUT p_result VARCHAR(32)
)
BEGIN
    DECLARE v_bal NUMERIC(15,2);

    START TRANSACTION;

    SELECT balance INTO v_bal FROM account WHERE id = p_from FOR UPDATE;
    IF v_bal IS NULL THEN
        ROLLBACK; SET p_result = 'FROM_NOT_FOUND';
    ELSEIF v_bal < p_amount THEN
        ROLLBACK; SET p_result = 'INSUFFICIENT_BALANCE';
    ELSE
        UPDATE account SET balance = balance - p_amount WHERE id = p_from;
        UPDATE account SET balance = balance + p_amount WHERE id = p_to;
        INSERT INTO transfer_log(from_id, to_id, amount, created_at)
            VALUES (p_from, p_to, p_amount, NOW());
        COMMIT; SET p_result = 'OK';
    END IF;
END$$
DELIMITER ;

-- 调用
CALL transfer(1, 2, 100.00, @r);
SELECT @r AS result;
```

**2. 薪资审计触发器：**

```sql
-- MySQL 8.0
CREATE TABLE employee_audit (
    id         BIGINT AUTO_INCREMENT PRIMARY KEY,
    emp_id     BIGINT       NOT NULL,
    old_salary NUMERIC(15,2),
    new_salary NUMERIC(15,2),
    op_user    VARCHAR(64)  NOT NULL DEFAULT CURRENT_USER(),
    op_time    DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$
CREATE TRIGGER trg_employee_salary_audit
AFTER UPDATE ON employee
FOR EACH ROW
BEGIN
    IF OLD.salary <> NEW.salary THEN
        INSERT INTO employee_audit(emp_id, old_salary, new_salary)
        VALUES (NEW.id, OLD.salary, NEW.salary);
    END IF;
END$$
DELIMITER ;

-- 触发测试
UPDATE employee SET salary = salary + 500 WHERE id = 1;
SELECT * FROM employee_audit WHERE emp_id = 1;
```

**3. 部门平均薪资函数：**

```sql
-- MySQL 8.0
DELIMITER $$
CREATE FUNCTION fn_dept_avg_salary(p_dept_id BIGINT)
RETURNS NUMERIC(15,2)
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE v_avg NUMERIC(15,2);
    SELECT AVG(salary) INTO v_avg
    FROM employee
    WHERE dept_id = p_dept_id;
    RETURN IFNULL(v_avg, 0);
END$$
DELIMITER ;

-- 在 SQL 中调用
SELECT dept_id, fn_dept_avg_salary(dept_id) AS avg_salary
FROM department
ORDER BY avg_salary DESC;
```

**4. 部门薪资汇总游标存储过程：**

```sql
-- MySQL 8.0
CREATE TABLE dept_salary_summary (
    dept_id     BIGINT PRIMARY KEY,
    total       NUMERIC(15,2),
    cnt         INT,
    avg_sal     NUMERIC(15,2),
    snapshot_at DATETIME
);

DELIMITER $$
CREATE PROCEDURE sp_build_dept_summary()
BEGIN
    DECLARE v_done      INT DEFAULT 0;
    DECLARE v_dept_id   BIGINT;
    DECLARE v_dept_name VARCHAR(64);

    DECLARE cur_dept CURSOR FOR
        SELECT id, dept_name FROM department ORDER BY id;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = 1;

    OPEN cur_dept;

    read_loop: LOOP
        FETCH cur_dept INTO v_dept_id, v_dept_name;
        IF v_done = 1 THEN
            LEAVE read_loop;
        END IF;

        INSERT INTO dept_salary_summary(dept_id, total, cnt, avg_sal, snapshot_at)
        SELECT v_dept_id, SUM(salary), COUNT(*), AVG(salary), NOW()
        FROM employee
        WHERE dept_id = v_dept_id;
    END LOOP;

    CLOSE cur_dept;
END$$
DELIMITER ;

CALL sp_build_dept_summary();
SELECT * FROM dept_salary_summary;
```

</details>

<details>
<summary>综合题答案</summary>

**1. 电商订单综合（视图+触发器+函数）：**

```sql
-- (1) 只读视图：已支付订单
CREATE OR REPLACE VIEW v_paid_orders AS
SELECT id AS order_id, customer_id, total_amount, placed_at
FROM orders
WHERE status = 'PAID';

-- (2) BEFORE INSERT 触发器：校验 total_amount 为正
DELIMITER $$
CREATE TRIGGER trg_orders_check_amount
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF NEW.total_amount <= 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'total_amount must be positive';
    END IF;
END$$
DELIMITER ;

-- (3) 订单明细金额合计函数
DELIMITER $$
CREATE FUNCTION fn_order_total(p_order_id BIGINT)
RETURNS NUMERIC(15,2)
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE v_total NUMERIC(15,2);
    SELECT SUM(quantity * unit_price) INTO v_total
    FROM order_item
    WHERE order_id = p_order_id;
    RETURN IFNULL(v_total, 0);
END$$
DELIMITER ;

-- 调用示例
SELECT id, fn_order_total(id) AS item_total
FROM orders WHERE status = 'PAID';
```

**2. 库存扣减存储过程：**

```sql
-- MySQL 8.0
CREATE TABLE product (
    id    BIGINT PRIMARY KEY,
    name  VARCHAR(128),
    stock INT NOT NULL DEFAULT 0
);
CREATE TABLE stock_log (
    id         BIGINT AUTO_INCREMENT PRIMARY KEY,
    product_id BIGINT,
    delta      INT,
    op_time    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$
CREATE PROCEDURE stock_out(
    IN  p_product_id BIGINT,
    IN  p_qty        INT,
    OUT p_result     VARCHAR(32)
)
BEGIN
    DECLARE v_stock INT;

    START TRANSACTION;

    -- 锁定商品行，防止并发超卖
    SELECT stock INTO v_stock FROM product WHERE id = p_product_id FOR UPDATE;

    IF v_stock IS NULL THEN
        ROLLBACK; SET p_result = 'PRODUCT_NOT_FOUND';
    ELSEIF v_stock < p_qty THEN
        ROLLBACK; SET p_result = 'OUT_OF_STOCK';
    ELSE
        UPDATE product SET stock = stock - p_qty WHERE id = p_product_id;
        INSERT INTO stock_log(product_id, delta, op_time)
            VALUES (p_product_id, -p_qty, NOW());
        COMMIT; SET p_result = 'OK';
    END IF;
END$$
DELIMITER ;

-- 调用
CALL stock_out(1, 5, @r);
SELECT @r;
```

**FOR UPDATE 作用与隔离级别配合：** `SELECT ... FOR UPDATE` 对命中行加排他锁（X 锁），其他事务的读写均阻塞，从而防止并发下的"超卖"（两个事务同时读到 stock=10 各扣 8，最终 -6）。在 REPEATABLE READ 下 InnoDB 还会加 Next-Key Lock 防止范围内插入新行；在 READ COMMITTED 下仅行锁。FOR UPDATE 必须在事务内使用，且 WHERE 应走索引（否则退化为表锁）。

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | 视图、参数、触发器、函数、游标概念 |
| 多选 | 5 | 15 | 视图作用、存储过程优劣、触发器场景、游标特性 |
| 判断 | 5 | 10 | 视图存储、行级触发、函数 DML、游标关闭、显式调用 |
| 简答 | 4 | 20 | 不可更新、参数模式、BEFORE/AFTER、游标性能 |
| SQL编程 | 4 | 32 | 存储过程、触发器、函数、游标完整代码 |
| 综合 | 2 | 16 | 视图+触发器+函数综合、事务+锁综合 |
| 合计 | 30 | 113 | 覆盖第2章五大可编程对象 |

## 导航

- 上级 MOC：[[MOC - 数据库开发技术]]、[[MOC - 第2章]]
- 本章知识点：[[2.1 视图、存储过程]]、[[2.2 触发器、函数]]、[[2.3 游标使用基础]]
- 上一章习题：[[MOC - 第1章习题]]
- 下一章习题：[[MOC - 第3章习题]]
