---
domain: 数据库技术
subject: 数据库开发技术
type: exercise
chapter: 第6章 数据库性能优化
section: 第6章综合习题
tags: [数据库开发,习题,索引,SQL优化,EXPLAIN,慢查询,B+树]
prerequisites: []
---

第6章习题覆盖 B+树索引结构、聚簇索引 vs 非聚簇索引、复合索引与最左前缀、索引失效场景、EXPLAIN 分析、SQL 优化技巧、慢查询日志与优化，重点考查给定 SQL 的优化方案设计。配套知识点见 [[MOC - 第6章]]。本章基于 MySQL 8.0 InnoDB。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | B+ 树特点 | 概念理解 |
| 单2 | 单选 | 聚簇索引叶子节点 | 概念理解 |
| 单3 | 单选 | 回表概念 | 概念理解 |
| 单4 | 单选 | 最左前缀 | 概念理解 |
| 单5 | 单选 | 覆盖索引 Extra | 概念理解 |
| 单6 | 单选 | EXPLAIN type=ALL 含义 | 概念理解 |
| 单7 | 单选 | LIKE 前缀通配失效 | 概念理解 |
| 单8 | 单选 | 索引选择性 | 概念理解 |
| 单9 | 单选 | CBO 决策依据 | 概念理解 |
| 单10 | 单选 | 深分页优化 | 概念理解 |
| 多1 | 多选 | 索引失效场景 | 概念辨析 |
| 多2 | 多选 | EXPLAIN 关键字段 | 概念辨析 |
| 多3 | 多选 | SQL 优化技巧 | 概念辨析 |
| 多4 | 多选 | 索引设计原则 | 概念辨析 |
| 多5 | 多选 | 慢查询分析工具 | 概念辨析 |
| 判1 | 判断 | 函数导致索引失效 | 概念理解 |
| 判2 | 判断 | 隐式类型转换失效 | 概念理解 |
| 判3 | 判断 | 索引越多越好 | 概念理解 |
| 判4 | 判断 | UNION ALL vs UNION | 概念理解 |
| 判5 | 判断 | 统计信息过期影响 CBO | 概念理解 |
| 简1 | 简答 | 聚簇索引 vs 非聚簇索引 | 分析说明 |
| 简2 | 简答 | 最左前缀原则 | 分析说明 |
| 简3 | 简答 | EXPLAIN 关键字段 | 分析说明 |
| 简4 | 简答 | 慢查询优化流程 | 分析说明 |
| SQL1 | SQL优化 | 函数导致失效优化 | 综合应用 |
| SQL2 | SQL优化 | SELECT * 与 JOIN 优化 | 综合应用 |
| SQL3 | SQL优化 | 子查询与深分页优化 | 综合应用 |
| SQL4 | SQL优化 | GROUP BY filesort 优化 | 综合应用 |
| 综1 | 综合 | 综合索引设计与执行计划 | 综合应用 |
| 综2 | 综合 | 慢查询定位到优化闭环 | 综合应用 |

## 一、单选题（每题 2 分，共 10 题）

**1. 关于 B+ 树索引，下列说法正确的是（　）。**
A. 非叶子节点存数据
B. 非叶子节点只存索引键，所有数据存于叶子节点，叶子节点按主键顺序用双向链表相连
C. 叶子节点无序
D. 不支持范围查询

**2. InnoDB 聚簇索引的叶子节点存储（　）。**
A. 主键值
B. 整行数据
C. 指向数据的指针
D. 哈希值

**3. 通过二级索引查到主键后，再到聚簇索引查整行，称为（　）。**
A. 覆盖索引
B. 回表
C. 索引下推
D. 索引合并

**4. 复合索引 `(a, b, c)`，下列查询能完整使用索引的是（　）。**
A. `WHERE b=?`
B. `WHERE a=? AND c=?`
C. `WHERE a=? AND b=? AND c=?`
D. `WHERE c=?`

**5. EXPLAIN 中表示覆盖索引（无需回表）的 Extra 值是（　）。**
A. `Using where`
B. `Using filesort`
C. `Using index`
D. `Using temporary`

**6. EXPLAIN 中 `type=ALL` 表示（　）。**
A. 主键等值查询
B. 索引范围扫描
C. 全表扫描，需优化
D. 覆盖索引

**7. 下列 LIKE 写法能走索引的是（　）。**
A. `name LIKE '%张'`
B. `name LIKE '%张%'`
C. `name LIKE '_张%'`
D. `name LIKE '张%'`

**8. 关于索引选择性，下列说法正确的是（　）。**
A. 区分度越低越适合建索引
B. `count(distinct col)/count(*)` 接近 1 的列适合建索引
C. 性别列单独建索引意义很大
D. 选择性与索引无关

**9. CBO（基于成本优化器）的决策依据是（　）。**
A. 预定义规则
B. 统计信息（行数、唯一值、数据分布）估算成本
C. SQL 长度
D. 表名

**10. `LIMIT 1000000, 20` 深分页性能问题，下列优化方案正确的是（　）。**
A. 增大 LIMIT
B. 延迟关联（先走覆盖索引取主键，再 JOIN 取整行）
C. 删除索引
D. 改用 SELECT *

## 二、多选题（每题 3 分，共 5 题）

**1. 下列会导致索引失效的有（　）。**
A. 对索引列使用函数 `WHERE YEAR(created_at)=2024`
B. 隐式类型转换（字符串列传数字）
C. LIKE 前缀通配 `'%张'`
D. OR 条件中一侧无索引

**2. 下列属于 EXPLAIN 关键字段的有（　）。**
A. `type`（访问类型）
B. `key`（实际使用的索引）
C. `rows`（预估扫描行数）
D. `Extra`（附加信息，如 Using index/filesort/temporary）

**3. 常见 SQL 优化技巧包括（　）。**
A. 避免 SELECT *
B. 小表驱动大表（JOIN）
C. IN 子查询改写为 JOIN
D. 深分页用延迟关联或游标分页

**4. 索引设计原则包括（　）。**
A. 选择性高的列优先
B. 避免过度索引（写入与存储成本）
C. 高频查询列尽量放入复合索引形成覆盖索引
D. 主键尽量短

**5. 慢查询分析工具包括（　）。**
A. `mysqldumpslow`
B. `pt-query-digest`
C. EXPLAIN
D. `SELECT *`

## 三、判断题（每题 2 分，共 5 题）

**1. 对索引列使用函数（如 `WHERE YEAR(created_at)=2024`）会导致索引失效。**

**2. 字符串列传入数字（如 `WHERE phone=13800138000` 而 phone 是 VARCHAR）会因隐式类型转换导致索引失效。**

**3. 索引越多越好，应尽可能为每个列都建索引。**

**4. `UNION` 会对结果去重（内部排序），确认无重复或允许重复时用 `UNION ALL` 省去排序开销。**

**5. CBO 依赖统计信息，大量数据增删后未更新统计信息可能导致优化器选错索引，可定期 `ANALYZE TABLE` 刷新。**

## 四、简答题（每题 5 分，共 4 题）

**1. 比较聚簇索引与二级索引（非聚簇）在数据存储、每表数量、查询效率上的区别。**

**2. 说明复合索引的最左前缀原则，并举例哪些查询能/不能使用索引 `(a,b,c)`。**

**3. 列出 EXPLAIN 的关键字段（type、key、rows、Extra）及优化目标。**

**4. 描述慢查询优化的闭环流程（定位→分析→优化→验证）。**

## 五、SQL优化题（每题 8 分，共 4 题，要求分析给定 SQL 的问题并给出优化方案）

**1. 函数导致失效。** 表 `orders(id, created_at, status, amount)`，`created_at` 上有索引。
```sql
SELECT * FROM orders WHERE YEAR(created_at) = 2024 AND status = 1;
```
分析问题并改写为走索引的 SQL。

**2. SELECT * 与 JOIN 优化。** 表 `employee(id, name, dept_id, salary)`、`department(id, dept_name)`，`dept_id` 有索引。
```sql
SELECT * FROM employee e, department d WHERE e.dept_id = d.id AND d.id IN (1,2,3);
```
分析问题并给出优化后的 SQL（指定列、小表驱动大表）。

**3. 子查询与深分页优化。** 表 `orders(id, user_id, created_at)`，`user_id` 与 `created_at` 有索引。
```sql
SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE status = 1);
-- 以及深分页
SELECT id, name FROM orders ORDER BY created_at DESC LIMIT 1000000, 20;
```
分别给出优化方案。

**4. GROUP BY filesort 优化。** 表 `employee(id, dept_id, salary, created_at)`，`dept_id` 有索引。
```sql
SELECT dept_id, AVG(salary) AS avg_sal FROM employee GROUP BY dept_id ORDER BY avg_sal DESC LIMIT 10;
```
EXPLAIN 显示 `type=ALL, Extra: Using temporary; Using filesort`。分析问题并给出优化方案。

## 六、综合题（每题 8 分，共 2 题）

**1. 综合索引设计与执行计划。** 表 `employee(id BIGINT PK, name VARCHAR(50), dept_id BIGINT, age INT, salary DECIMAL, created_at DATETIME)`，常见查询：**
- 查询 1：`WHERE dept_id=? AND age>? ORDER BY age`
- 查询 2：`WHERE name=?`（按姓名查员工）
- 查询 3：`SELECT dept_id, age FROM employee WHERE dept_id=?`
要求：
- **(1)** 为三类查询设计合适的索引（写出 CREATE INDEX 语句）；
- **(2)** 说明查询 3 如何形成覆盖索引；
- **(3)** 写出查询 1 的 EXPLAIN 语句及期望的 type、key、Extra。

**2. 慢查询定位到优化闭环。** 某系统响应变慢，`mysqldumpslow` 显示高频慢查询 `SELECT * FROM orders WHERE user_id=? ORDER BY created_at DESC LIMIT ?`，总耗时最高。要求：**
- **(1)** 写出开启慢查询日志的 SQL（含 long_query_time=1、log_queries_not_using_indexes）；
- **(2)** 用 EXPLAIN 分析该 SQL，说明 `Using filesort` 的成因；
- **(3)** 给出建立复合索引的优化方案并验证；
- **(4)** 说明优化后必须复测的原因。

## 答案与解析

<details>
<summary>单选题答案</summary>

1. **B**。B+ 树非叶子节点只存索引键，数据存于叶子节点，叶子按主键顺序双向链表相连，支持范围查询。
2. **B**。聚簇索引叶子节点存整行数据；二级索引叶子存主键值。
3. **B**。二级索引查到主键再到聚簇索引查整行称为回表。
4. **C**。`a=? AND b=? AND c=?` 完整命中复合索引；其余缺最左列或不连续。
5. **C**。`Using index` 表示覆盖索引，无需回表。
6. **C**。type=ALL 表示全表扫描，需优化。
7. **D**。`LIKE '张%'` 走索引；前导 `%` 或 `_` 失效。
8. **B**。区分度 `count(distinct col)/count(*)` 接近 1 的列适合建索引；性别等低选择性列单独建索引意义不大。
9. **B**。CBO 基于统计信息估算成本；RBO 基于规则。
10. **B**。延迟关联（先走覆盖索引取主键再 JOIN）或游标分页（记上一页最大 id）优化深分页。

</details>

<details>
<summary>多选题答案</summary>

1. **ABCD**。函数、隐式类型转换、LIKE 前导通配、OR 一侧无索引均致失效。
2. **ABCD**。type、key、rows、Extra 均为 EXPLAIN 关键字段。
3. **ABCD**。避免 SELECT *、小表驱动大表、IN 子查询改 JOIN、深分页延迟关联均为优化技巧。
4. **ABCD**。选择性高优先、避免过度索引、覆盖索引、主键尽量短均为设计原则。
5. **ABC**。mysqldumpslow、pt-query-digest、EXPLAIN 均为分析工具；`SELECT *` 不是工具。

</details>

<details>
<summary>判断题答案</summary>

1. **√**。对索引列使用函数导致失效，应改范围查询。
2. **√**。字符串列传数字隐式转换致失效，应传字符串。
3. **×**。索引越多写入与存储成本越高，写多读少表索引过多拖慢 DML。
4. **√**。UNION 去重内部排序，无需去重用 UNION ALL 省排序开销。
5. **√**。统计信息过期导致 CBO 选错索引，定期 ANALYZE TABLE 刷新。

</details>

<details>
<summary>简答题答案</summary>

**1. 聚簇索引 vs 二级索引：**
| 维度 | 聚簇索引 | 二级索引（非聚簇） |
| ---- | ---- | ---- |
| 数据存储 | 叶子存整行数据 | 叶子存主键值 |
| 每表数量 | 仅 1 个 | 可多个 |
| 查询效率 | 直接取数据 | 非覆盖索引需回表（两次 IO） |

**2. 最左前缀：** 复合索引 `(a,b,c)` 按 a、b、c 顺序排序，查询必须从最左列开始连续使用。
- 使用：`a=?`、`a=? AND b=?`、`a=? AND b=? AND c=?`
- 不使用：`b=?`（缺 a）
- 部分使用：`a=? AND c=?`（仅 a）
- 范围后失效：`a>? AND b=?`（a 用范围，b 无法用）

**3. EXPLAIN 关键字段：**
| 字段 | 含义 | 优化目标 |
| ---- | ---- | ---- |
| type | 访问类型 | const > eq_ref > ref > range > index > ALL |
| key | 实际使用索引 | 非 NULL 且符合预期 |
| rows | 预估扫描行数 | 越小越好 |
| Extra | 附加信息 | Using index 为佳；filesort/temporary 需警惕 |

**4. 慢查询优化流程：**
1. 定位：开启慢日志/采样
2. 分析：EXPLAIN + 索引检查
3. 判断：是否走索引？扫描行数过大？有 filesort/temporary？
4. 优化：加索引/改写条件/缩小范围/调整 ORDER BY/GROUP BY
5. 验证：EXPLAIN 对比/压测，效果不佳则回到分析

</details>

<details>
<summary>SQL优化题答案</summary>

**1. 函数导致失效：**
问题：`YEAR(created_at)=2024` 对索引列使用函数导致索引失效，退化为全表扫描。
优化：改为范围查询，走索引。
```sql
SELECT * FROM orders
WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01' AND status = 1;
```

**2. SELECT * 与 JOIN 优化：**
问题：`SELECT *` 读取所有列无法利用覆盖索引，网络与内存开销大；老式隐式 JOIN 可读性差。
优化：指定列、用显式 JOIN、小表（department）驱动大表（employee），被驱动表关联列建索引。
```sql
SELECT e.id, e.name, e.salary, d.dept_name
FROM department d
STRAIGHT_JOIN employee e ON e.dept_id = d.id
WHERE d.id IN (1, 2, 3);
-- 确保 employee.dept_id 有索引
```

**3. 子查询与深分页优化：**
子查询优化：IN 子查询改写为 JOIN。
```sql
-- 反例：IN 子查询
SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE status = 1);
-- 正例：改写为 JOIN
SELECT o.*
FROM orders o
INNER JOIN users u ON o.user_id = u.id
WHERE u.status = 1;
```
深分页优化：延迟关联或游标分页。
```sql
-- 方案一：延迟关联
SELECT o.*
FROM orders o
INNER JOIN (
    SELECT id FROM orders ORDER BY created_at DESC LIMIT 1000000, 20
) t ON o.id = t.id;

-- 方案二：游标分页（记上一页最大 id）
SELECT id, name FROM orders
WHERE id < :last_id
ORDER BY id DESC LIMIT 20;
```

**4. GROUP BY filesort 优化：**
问题：`GROUP BY dept_id` 后 `ORDER BY avg_sal`（聚合结果）无法走索引，产生 `Using temporary; Using filesort`，且全表扫描。
优化：先过滤缩小范围走 idx_dept，再分组排序。
```sql
-- 先加复合索引
CREATE INDEX idx_dept_salary ON employee(dept_id, salary);

-- 优化 SQL：缩小范围走索引
EXPLAIN
SELECT dept_id, AVG(salary) AS avg_sal
FROM employee
WHERE dept_id IN (1,2,3,4,5)   -- 缩小范围，走 idx_dept_salary
GROUP BY dept_id
ORDER BY avg_sal DESC
LIMIT 10;
-- 期望: type=range, key=idx_dept_salary, rows 显著下降
```

</details>

<details>
<summary>综合题答案</summary>

**1. 综合索引设计与执行计划：**

**(1)** 索引设计：
```sql
-- 查询1: WHERE dept_id=? AND age>? ORDER BY age → 复合索引(dept_id, age)
CREATE INDEX idx_dept_age ON employee(dept_id, age);

-- 查询2: WHERE name=? → 单列索引
CREATE INDEX idx_name ON employee(name);

-- 查询3: SELECT dept_id, age FROM employee WHERE dept_id=? → 复合索引(dept_id, age) 可复用
-- 已由 idx_dept_age 覆盖，无需重复建
```

**(2)** 查询 3 覆盖索引：`SELECT dept_id, age FROM employee WHERE dept_id=?`，查询的列（dept_id、age）全部包含在 `idx_dept_age(dept_id, age)` 中，无需回表聚簇索引，EXPLAIN Extra 显示 `Using index`。

**(3)** 查询 1 EXPLAIN：
```sql
EXPLAIN SELECT * FROM employee WHERE dept_id = 1 AND age > 20 ORDER BY age;
```
期望：`type=range`（dept_id 等值 + age 范围），`key=idx_dept_age`，Extra 不应出现 `Using filesort`（ORDER BY age 与索引顺序一致）。

**2. 慢查询定位到优化闭环：**

**(1)** 开启慢查询日志：
```sql
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;
SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';
SET GLOBAL log_queries_not_using_indexes = ON;
```

**(2)** EXPLAIN 分析：
```sql
EXPLAIN SELECT * FROM orders WHERE user_id = 1001 ORDER BY created_at DESC LIMIT 20;
-- type=ref, key=idx_user, Extra: Using filesort
```
`Using filesort` 成因：`user_id` 有索引但 `ORDER BY created_at` 未走索引，需额外排序。

**(3)** 建立复合索引优化：
```sql
CREATE INDEX idx_user_created ON orders(user_id, created_at);
-- 验证
EXPLAIN SELECT * FROM orders WHERE user_id = 1001 ORDER BY created_at DESC LIMIT 20;
-- Extra 中 filesort 消失，rows 下降
```

**(4)** 复测原因：优化可能"优化一项拖累另一项"——新索引加速该查询但增加写入开销，或影响其他查询计划。必须用真实数据量复测验证，避免引入新问题。

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | B+树、聚簇索引、回表、最左前缀、覆盖索引、失效、CBO、深分页 |
| 多选 | 5 | 15 | 失效场景、EXPLAIN字段、优化技巧、设计原则、工具 |
| 判断 | 5 | 10 | 函数失效、隐式转换、索引数量、UNION ALL、统计信息 |
| 简答 | 4 | 20 | 聚簇vs二级、最左前缀、EXPLAIN、优化流程 |
| SQL优化 | 4 | 32 | 函数失效、JOIN、子查询深分页、GROUP BY |
| 综合 | 2 | 16 | 索引设计、慢查询闭环 |
| 合计 | 30 | 113 | 覆盖第6章性能优化全部主题 |

## 导航

- 上级 MOC：[[MOC - 数据库开发技术]]、[[MOC - 第6章]]
- 本章知识点：[[6.1 索引设计与优化]]、[[6.2 SQL语句调优]]、[[6.3 慢查询分析基础]]
- 上一章习题：[[MOC - 第5章习题]]
- 下一章习题：[[MOC - 第7章习题]]
