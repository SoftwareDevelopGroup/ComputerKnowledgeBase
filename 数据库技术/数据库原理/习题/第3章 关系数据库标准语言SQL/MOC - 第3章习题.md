---
domain: 数据库技术
subject: 数据库原理
type: exercise
chapter: 第3章 关系数据库标准语言SQL
section: 3.1 SQL概述
tags: [数据库原理, 习题, SQL查询, 视图]
prerequisites:
  - "[[MOC - 第3章]]"
  - "[[3.1 SQL概述]]"
  - "[[3.2 数据定义]]"
  - "[[3.3 数据查询]]"
  - "[[3.4 数据更新]]"
  - "[[3.5 视图]]"
  - "[[3.6 嵌入式SQL基础]]"
aliases:
  - "第3章习题"
  - "SQL 习题"
---

# MOC - 第3章习题

> [!info] 习题说明
> 本习题集覆盖《数据库系统概论》第3章「关系数据库标准语言 SQL」全部知识点，共 **30 题**，分为单选 10、多选 5、判断 5、简答 4、分析 4、综合 2。
> 分析题与综合题基于 **Student / Course / SC** 三表，要求写出可直接在 MySQL 8.0 中运行的 SQL 语句。
> 答案与解析以 `<details>` 折叠，便于自测后核对。

## 知识点覆盖表

| 题号 | 题型 | 对应知识点 | 对应节 |
| ---- | ---- | ---------- | ------ |
| 单选 1 | 单选 | SQL 特点 | 3.1 |
| 单选 2 | 单选 | SQL 功能动词分类 | 3.1 |
| 单选 3 | 单选 | DROP TABLE RESTRICT/CASCADE | 3.2 |
| 单选 4 | 单选 | WHERE vs HAVING | 3.3 |
| 单选 5 | 单选 | LEFT JOIN 含义 | 3.3 |
| 单选 6 | 单选 | NULL 比较运算 | 3.3 |
| 单选 7 | 单选 | 视图消解 | 3.5 |
| 单选 8 | 单选 | 可更新视图条件 | 3.5 |
| 单选 9 | 单选 | 游标用途 | 3.6 |
| 单选 10 | 单选 | 参照完整性 ON DELETE | 3.2/3.4 |
| 多选 1 | 多选 | SQL 数据定义对象 | 3.2 |
| 多选 2 | 多选 | 聚集函数 | 3.3 |
| 多选 3 | 多选 | LIKE 通配符 | 3.3 |
| 多选 4 | 多选 | 视图作用 | 3.5 |
| 多选 5 | 多选 | 必须使用游标的情形 | 3.6 |
| 判断 1 | 判断 | 视图存储 | 3.5 |
| 判断 2 | 判断 | DELETE vs DROP | 3.4 |
| 判断 3 | 判断 | COUNT(*) 含 NULL | 3.3 |
| 判断 4 | 判断 | ANY/ALL 与聚集 | 3.3 |
| 判断 5 | 判断 | 主变量与指示变量 | 3.6 |
| 简答 1 | 简答 | SQL 五大特点 | 3.1 |
| 简答 2 | 简答 | WHERE/HAVING 区别 | 3.3 |
| 简答 3 | 简答 | 视图消解过程 | 3.5 |
| 简答 4 | 简答 | 相关 vs 不相关子查询 | 3.3 |
| 分析 1 | 分析 | 单表查询与聚集 | 3.3 |
| 分析 2 | 分析 | 多表连接与外连接 | 3.3 |
| 分析 3 | 分析 | 嵌套查询 EXISTS | 3.3 |
| 分析 4 | 分析 | 数据更新与约束 | 3.4 |
| 综合 1 | 综合 | 建表+约束+视图+查询 | 3.2/3.5/3.3 |
| 综合 2 | 综合 | 集合查询+派生表+更新 | 3.3/3.4 |

## 分析题与综合题表结构与示例数据

> [!example] 三表结构与示例数据（贯穿分析题与综合题）
>
> **Student**(Sno, Sname, Ssex, Sage, Sdept)
>
> | Sno | Sname | Ssex | Sage | Sdept |
> | --- | --- | --- | --- | --- |
> | 2024001 | 李勇 | 男 | 20 | CS |
> | 2024002 | 刘晨 | 女 | 19 | IS |
> | 2024003 | 王敏 | 女 | 18 | MA |
> | 2024004 | 张立 | 男 | 21 | IS |
> | 2024005 | 陈玲 | 女 | 20 | CS |
>
> **Course**(Cno, Cname, Cpno, Ccredit)
>
> | Cno | Cname | Cpno | Ccredit |
> | --- | --- | --- | --- |
> | 1 | 数据库 | 5 | 4 |
> | 2 | 数学 | NULL | 2 |
> | 3 | 信息系统 | 1 | 4 |
> | 4 | 操作系统 | 6 | 3 |
> | 5 | 数据结构 | 7 | 4 |
> | 6 | 数据处理 | NULL | 2 |
> | 7 | PASCAL语言 | 6 | 4 |
>
> **SC**(Sno, Cno, Grade)
>
> | Sno | Cno | Grade |
> | --- | --- | --- |
> | 2024001 | 1 | 92 |
> | 2024001 | 2 | 85 |
> | 2024001 | 3 | 88 |
> | 2024002 | 2 | 90 |
> | 2024002 | 3 | 80 |
> | 2024003 | 1 | 78 |
> | 2024004 | 1 | 95 |
> | 2024004 | 4 | 70 |

---

## 一、单选题（10 题）

1. SQL 语言具有"高度非过程化"的特点，其含义是（ ）
   A. 用户必须指定数据的存取路径
   B. 用户只需提出"做什么"，不必指明"怎么做"
   C. SQL 只能处理过程化问题
   D. SQL 一次只能处理一条记录

2. 下列 SQL 动词中，属于数据操纵语言（DML）的是（ ）
   A. CREATE
   B. DROP
   C. UPDATE
   D. GRANT

3. 执行 `DROP TABLE Student RESTRICT` 时，若 Student 表上存在依赖视图，则结果是（ ）
   A. 删除表及其所有依赖对象
   B. 拒绝删除
   C. 删除表但保留依赖视图
   D. 删除依赖视图

4. 关于 `WHERE` 和 `HAVING`，下列说法正确的是（ ）
   A. 两者都作用于分组后的结果
   B. `WHERE` 可使用聚集函数
   C. `HAVING` 用于对分组结果进行筛选
   D. `WHERE` 在 `GROUP BY` 之后执行

5. `FROM A LEFT JOIN B ON A.id = B.id` 的结果是（ ）
   A. 仅 A 与 B 的交集
   B. A 的全部行，B 无匹配填 NULL
   C. B 的全部行，A 无匹配填 NULL
   D. A 与 B 的并集

6. 在 SQL 中，判断某列是否为 NULL，正确的写法是（ ）
   A. `WHERE Cpno = NULL`
   B. `WHERE Cpno == NULL`
   C. `WHERE Cpno IS NULL`
   D. `WHERE Cpno <> NULL`

7. 关于视图查询的处理过程，下列描述正确的是（ ）
   A. DBMS 直接查询视图的物理存储
   B. DBMS 通过视图消解将查询转换为对基本表的查询
   C. 视图查询不经过优化器
   D. 视图查询不检查权限

8. 下列视图中，**通常不可更新**的是（ ）
   A. 行列子集视图（含主键、单表、无表达式）
   B. 由单表选择部分行和列构成的视图
   C. 含 `GROUP BY` 与 `AVG` 的分组视图
   D. 由单表选择全部行构成的视图

9. 在嵌入式 SQL 中，**必须**使用游标的情形是（ ）
   A. 单行查询的 `SELECT INTO`
   B. 查询结果为多行的 SELECT
   C. 非 CURRENT 形式的 `UPDATE`
   D. `INSERT INTO ... VALUES`

10. 若 SC 表对 Student 的外键定义为 `ON DELETE SET NULL`，则删除 Student 中某学生时，SC 表中其选课记录的 Sno 字段会被（ ）
    A. 同步删除
    B. 设为 NULL
    C. 保持不变
    D. 设为默认值 0

---

## 二、多选题（5 题）

1. SQL 数据定义功能（DDL）可以定义的对象包括（ ）
   A. 模式
   B. 基本表
   C. 视图
   D. 索引
   E. 用户

2. 下列属于 SQL 聚集函数的有（ ）
   A. `COUNT`
   B. `SUM`
   C. `AVG`
   D. `MAX`
   E. `MIN`
   F. `GROUP`

3. 在 SQL `LIKE` 模式匹配中，下列符号含义正确的有（ ）
   A. `%` 匹配任意长度的字符串
   B. `_` 匹配单个字符
   C. `*` 匹配任意长度字符串
   D. `?` 匹配单个字符
   E. 可用 `ESCAPE` 转义 `%` 或 `_`

4. 视图的作用包括（ ）
   A. 简化用户操作
   B. 使用户能以多种角度看待同一数据
   C. 提供逻辑数据独立性
   D. 提供安全保护机制
   E. 加速所有查询的物理执行

5. 在嵌入式 SQL 中，**必须**使用游标的情形包括（ ）
   A. 查询结果为多行的 SELECT
   B. `CURRENT OF <游标>` 形式的 `UPDATE`
   C. `CURRENT OF <游标>` 形式的 `DELETE`
   D. 查询结果为单行的 `SELECT INTO`
   E. `INSERT INTO ... VALUES`

---

## 三、判断题（5 题）

1. 视图是一张虚表，数据库中既不存放视图的定义，也不存放其数据。（ ）

2. `DELETE FROM Student` 与 `DROP TABLE Student` 都会删除 Student 表中的所有数据，效果相同。（ ）

3. `COUNT(*)` 统计时不忽略 NULL 值的行，而 `COUNT(列名)` 忽略该列 NULL 值。（ ）

4. `> ALL` 子查询等价于 `> (SELECT MAX(...) ...)`，`> ANY` 等价于 `> (SELECT MIN(...) ...)`。（ ）

5. 在嵌入式 SQL 中，指示变量取值为 `-1` 表示该列值被截断。（ ）

---

## 四、简答题（4 题）

1. 简述 SQL 语言的五个主要特点。

2. 简述 SQL 中 `WHERE` 子句与 `HAVING` 子句的区别。

3. 什么是视图消解？简述 DBMS 处理视图查询的过程。

4. 什么是相关子查询与不相关子查询？二者在执行方式上有何不同？

---

## 五、分析题（4 题，基于 Student/Course/SC 三表）

### 分析题 1（单表查询与聚集函数）

针对 Student 表，写出满足下列要求的 SQL 语句：

1. 查询全体学生的姓名、所在系。
2. 查询各系的学生人数及平均年龄，按平均年龄降序排列。
3. 查询年龄不小于 20 岁的男生姓名与年龄。

### 分析题 2（多表连接与外连接）

针对 Student/Course/SC 三表：

1. 查询每个学生的学号、姓名、选修课程名及成绩。
2. 查询所有学生的选课情况（含未选课学生），列出学号、姓名、课程号、成绩。
3. 查询选修了"数据库"课程且成绩在 85 分以上的学生姓名。

### 分析题 3（嵌套查询与 EXISTS）

1. 查询与"刘晨"在同一个系学习的学生学号与姓名。
2. 查询选修了课程号为 1 的所有学生姓名（使用 `EXISTS`）。
3. 查询选修了全部课程的学生的学号与姓名（用 `NOT EXISTS` 双重否定实现）。

### 分析题 4（数据更新与约束）

针对 Student/Course/SC 三表：

1. 向 Student 表插入一名新学生：学号 2024008，姓名 周八，性别 男，年龄 22，系别 IS。
2. 将所有学生的年龄加 1。
3. 删除选课成绩小于 60 分的选课记录（先插入一条 Grade=55 的记录用以验证）。
4. 写出第 1 小题在违反主键约束时的预期错误信息（假设学号 2024008 已存在）。

---

## 六、综合题（2 题，完整 SQL 编程）

### 综合题 1（建表 + 约束 + 视图 + 查询）

某教务系统需要管理学生、课程与选课信息。请完成：

1. 用 `CREATE TABLE` 定义三张表，并满足下列约束：
   - Student(Sno CHAR(7), Sname VARCHAR(20), Ssex CHAR(2), Sage INT, Sdept VARCHAR(20))，Sno 主键，Ssex 取值仅限 '男'/'女'；
   - Course(Cno CHAR(2), Cname VARCHAR(40), Cpno CHAR(2), Ccredit SMALLINT)，Cno 主键，Cpno 引用本表 Cno，删除时置 NULL；
   - SC(Sno, Cno, Grade)，(Sno, Cno) 复合主键，Sno 与 Cno 分别外键引用 Student 和 Course，删除主表时级联删除。
2. 创建一个视图 `CS_Student_Grade`，包含 CS 系学生的学号、姓名、课程名、成绩。
3. 通过该视图查询 CS 系学生的姓名、课程名与成绩，结果按成绩降序排列。

### 综合题 2（集合查询 + 派生表 + 更新）

针对 Student/Course/SC 三表：

1. 用 `UNION` 查询"计算机系(CS)学生"与"年龄不超过 19 岁的学生"的并集，列出学号、姓名、所在系。
2. 查询每名学生的学号、姓名、平均成绩（用派生表先求平均成绩再与 Student 连接）。
3. 将每名学生的选课成绩提升 5 分（注意上限不超过 100）。

---

## 答案与解析

### 单选题答案

<details>
<summary>点击展开：单选题 1–10 答案与解析</summary>

**1. B**。"高度非过程化"指用户只需提出"做什么"，DBMS 自动决定"怎么做"。参见 [[3.1 SQL概述#SQL 的特点]]。

**2. C**。`CREATE`、`DROP`、`ALTER` 属 DDL；`GRANT`/`REVOKE` 属 DCL；`INSERT`/`UPDATE`/`DELETE` 属 DML。参见 [[3.1 SQL概述#SQL 的功能动词]]。

**3. B**。`RESTRICT` 表示若存在依赖对象则拒绝删除；`CASCADE` 才会级联删除。参见 [[3.2 数据定义#删除基本表]]。

**4. C**。`WHERE` 作用于元组、分组前、不能用聚集函数；`HAVING` 作用于分组、分组后、可用聚集函数。参见 [[3.3 数据查询#GROUP BY 与 HAVING]]。

**5. B**。左外连接保留左表全部行，右表无匹配填 NULL。参见 [[3.3 数据查询#外连接]]。

**6. C**。NULL 判断必须用 `IS NULL` / `IS NOT NULL`。参见 [[3.3 数据查询#字符匹配（LIKE）]]后警告。

**7. B**。视图消解将视图查询重写为对基本表的等价查询。参见 [[3.5 视图#查询视图与视图消解]]。

**8. C**。分组视图（含 `GROUP BY` 与 `AVG`）通常不可更新，因为一行对应一组无法映射回基本表。参见 [[3.5 视图#更新视图]]。

**9. B**。多行查询结果必须用游标逐行处理。参见 [[3.6 嵌入式SQL基础#游标（CURSOR）]]。

**10. B**。`ON DELETE SET NULL` 将外键置空。参见 [[3.2 数据定义#FOREIGN KEY（外键）]]。

</details>

### 多选题答案

<details>
<summary>点击展开：多选题 1–5 答案与解析</summary>

**1. ABCD**。SQL DDL 可定义模式、基本表、视图、索引。用户由 DCL 管理。参见 [[3.2 数据定义#SQL 数据定义的对象与动词]]。

**2. ABCDE**。SQL 聚集函数有 COUNT、SUM、AVG、MAX、MIN。`GROUP` 不是函数。参见 [[3.3 数据查询#聚集函数]]。

**3. ABE**。`%` 匹配任意长度，`_` 匹配单字符，`ESCAPE` 转义。`*`/`?` 不是 SQL 通配符（属正则）。参见 [[3.3 数据查询#字符匹配（LIKE）]]。

**4. ABCD**。视图作用含简化操作、多角度、逻辑独立性、安全保护。视图本身不必然加速物理执行。参见 [[3.5 视图#视图的作用]]。

**5. ABC**。多行 SELECT 与 `CURRENT OF` 形式更新/删除需用游标；单行 `SELECT INTO` 与 `INSERT` 不需游标。参见 [[3.6 嵌入式SQL基础#不需游标 vs 必须使用游标]]。

</details>

### 判断题答案

<details>
<summary>点击展开：判断题 1–5 答案与解析</summary>

**1. ✗**。视图是虚表，但数据库中**存放视图的定义**（不存放数据）。参见 [[3.5 视图#视图的概念]]。

**2. ✗**。`DELETE FROM Student` 仅删数据，保留表结构；`DROP TABLE Student` 删除表结构与数据。两者不同。参见 [[3.4 数据更新#删除数据（DELETE）]]。

**3. ✓**。`COUNT(*)` 统计所有行（含 NULL），`COUNT(列名)` 忽略该列 NULL。参见 [[3.3 数据查询#聚集函数]]。

**4. ✓**。`> ALL` ⟺ `> MAX(...)`，`> ANY` ⟺ `> MIN(...)`。参见 [[3.3 数据查询#带有 ANY 或 ALL 的子查询]]。

**5. ✗**。指示变量 `-1` 表示列值为 NULL；`>0` 才表示截断。参见 [[3.6 嵌入式SQL基础#指示变量]]。

</details>

### 简答题答案

<details>
<summary>点击展开：简答题 1–4 参考答案</summary>

**1. SQL 的五个主要特点**：
1. 综合统一：集 DDL、DML、DCL 于一体，可独立完成数据库生命周期全部活动；
2. 高度非过程化：用户只需提出"做什么"，存取路径由 DBMS 自动选择；
3. 面向集合的操作方式：操作对象和结果都是元组的集合；
4. 以同一种语法结构提供多种使用方式：交互式与嵌入式语法一致；
5. 语言简洁，易学易用：核心动词仅 9 个，接近自然语言。

参见 [[3.1 SQL概述#SQL 的特点]]。

**2. WHERE 与 HAVING 的区别**：

| 方面 | WHERE | HAVING |
| ---- | ----- | ------ |
| 作用对象 | 元组（行） | 分组（GROUP BY 结果） |
| 执行时机 | 分组前 | 分组后 |
| 能否用聚集函数 | 不能 | 能 |
| 是否可与 GROUP BY 配合 | 可单独使用 | 必须配合 GROUP BY |

参见 [[3.3 数据查询#GROUP BY 与 HAVING]]。

**3. 视图消解过程**：
1. DBMS 检查查询涉及的视图、基本表是否存在；
2. 从数据字典取出视图定义；
3. 把视图定义中的子查询与用户查询合并，重写为对基本表的等价查询；
4. 查询优化器对重写后的查询优化并执行，返回结果。
视图消解后，查询等价于直接对基本表的查询，因此视图本身不存储数据。参见 [[3.5 视图#查询视图与视图消解]]。

**4. 相关子查询与不相关子查询**：
- **不相关子查询**：子查询不引用外层查询的列，独立执行一次，把结果作为外层查询的输入。常见于 `IN`、`ANY`/`ALL`。
- **相关子查询**：子查询引用外层查询的列，对外层每个候选元组都要执行一次子查询。典型如 `EXISTS`。
二者执行次数不同：不相关子查询执行 1 次，相关子查询执行 N 次（N 为外层元组数）。参见 [[3.3 数据查询#相关子查询 vs 不相关子查询]]。

</details>

### 分析题答案

<details>
<summary>点击展开：分析题 1–4 SQL 参考答案</summary>

#### 分析题 1（单表查询与聚集函数）

```sql
-- (1) 查询全体学生的姓名、所在系
SELECT Sname, Sdept FROM Student;

-- (2) 查询各系的学生人数及平均年龄, 按平均年龄降序
SELECT Sdept, COUNT(*) AS StudentNum, AVG(Sage) AS AvgAge
FROM Student
GROUP BY Sdept
ORDER BY AvgAge DESC;

-- (3) 查询年龄不小于 20 岁的男生姓名与年龄
SELECT Sname, Sage
FROM Student
WHERE Sage >= 20 AND Ssex = '男';
```

#### 分析题 2（多表连接与外连接）

```sql
-- (1) 每个学生的学号、姓名、选修课程名及成绩
SELECT Student.Sno, Sname, Cname, Grade
FROM Student
    JOIN SC     ON Student.Sno = SC.Sno
    JOIN Course ON SC.Cno = Course.Cno;

-- (2) 所有学生的选课情况(含未选课学生, 用左外连接)
SELECT Student.Sno, Sname, Cno, Grade
FROM Student LEFT JOIN SC ON Student.Sno = SC.Sno;
-- 未选课学生(如2024005)的 Cno/Grade 为 NULL

-- (3) 选修"数据库"且成绩在85分以上的学生姓名
SELECT Sname
FROM Student JOIN SC ON Student.Sno = SC.Sno
            JOIN Course ON SC.Cno = Course.Cno
WHERE Cname = '数据库' AND Grade >= 85;
-- 结果: 李勇(92), 张立(95)
```

#### 分析题 3（嵌套查询与 EXISTS）

```sql
-- (1) 与"刘晨"同系学生(用 IN 子查询)
SELECT Sno, Sname
FROM Student
WHERE Sdept IN (SELECT Sdept FROM Student WHERE Sname = '刘晨');
-- 结果: 2024002 刘晨, 2024004 张立

-- (2) 选修1号课的学生姓名(用 EXISTS)
SELECT Sname
FROM Student
WHERE EXISTS (
    SELECT * FROM SC
    WHERE Sno = Student.Sno AND Cno = '1'
);
-- 结果: 李勇, 王敏, 张立

-- (3) 选修全部课程的学生(用 NOT EXISTS 双重否定)
SELECT Sno, Sname
FROM Student
WHERE NOT EXISTS (
    SELECT * FROM Course
    WHERE NOT EXISTS (
        SELECT * FROM SC
        WHERE Sno = Student.Sno AND Cno = Course.Cno
    )
);
-- 含义: 不存在一门课该学生没选。实际数据中无学生选全部7门课, 结果为空
```

#### 分析题 4（数据更新与约束）

```sql
-- (1) 插入新学生 2024008
INSERT INTO Student VALUES ('2024008', '周八', '男', 22, 'IS');

-- (2) 所有学生年龄加1
UPDATE Student SET Sage = Sage + 1;

-- (3) 删除成绩小于60的选课记录(先插入一条Grade=55验证)
INSERT INTO SC VALUES ('2024001', '4', 55);
DELETE FROM SC WHERE Grade < 60;
-- 删除刚插入的 55 分记录

-- (4) 违反主键约束时(2024008已存在)的错误信息(MySQL):
-- Error 1062 (23000): Duplicate entry '2024008' for key 'PRIMARY'
```

</details>

### 综合题答案

<details>
<summary>点击展开：综合题 1–2 SQL 参考答案</summary>

#### 综合题 1（建表 + 约束 + 视图 + 查询）

```sql
-- (1) 定义三张表
CREATE TABLE Student (
    Sno   CHAR(7)     PRIMARY KEY,
    Sname VARCHAR(20) NOT NULL,
    Ssex  CHAR(2)     CHECK (Ssex IN ('男','女')),
    Sage  INT,
    Sdept VARCHAR(20)
);

CREATE TABLE Course (
    Cno     CHAR(2)     PRIMARY KEY,
    Cname   VARCHAR(40) NOT NULL,
    Cpno    CHAR(2),
    Ccredit SMALLINT    CHECK (Ccredit > 0),
    FOREIGN KEY (Cpno) REFERENCES Course(Cno)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE SC (
    Sno   CHAR(7)     NOT NULL,
    Cno   CHAR(2)     NOT NULL,
    Grade DECIMAL(4,1) CHECK (Grade BETWEEN 0 AND 100),
    PRIMARY KEY (Sno, Cno),
    FOREIGN KEY (Sno) REFERENCES Student(Sno)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Cno) REFERENCES Course(Cno)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- (2) 创建 CS_Student_Grade 视图
CREATE VIEW CS_Student_Grade(Sno, Sname, Cname, Grade)
AS
SELECT Student.Sno, Sname, Cname, Grade
FROM Student
    JOIN SC     ON Student.Sno = SC.Sno
    JOIN Course ON SC.Cno = Course.Cno
WHERE Sdept = 'CS';

-- (3) 通过视图查询并按成绩降序
SELECT Sname, Cname, Grade
FROM CS_Student_Grade
ORDER BY Grade DESC;
```

#### 综合题 2（集合查询 + 派生表 + 更新）

```sql
-- (1) CS 系学生 ∪ 年龄≤19的学生
SELECT Sno, Sname, Sdept FROM Student WHERE Sdept = 'CS'
UNION
SELECT Sno, Sname, Sdept FROM Student WHERE Sage <= 19;

-- (2) 每名学生的学号、姓名、平均成绩(派生表)
SELECT Student.Sno, Sname, AvgG
FROM Student
    JOIN (
        SELECT Sno, AVG(Grade) AS AvgG
        FROM SC
        GROUP BY Sno
    ) AS T ON Student.Sno = T.Sno;

-- (3) 选课成绩提升5分, 不超过100(MySQL: LEAST 函数)
UPDATE SC
SET Grade = LEAST(Grade + 5, 100);
```

</details>

## 考点统计表

| 知识点 | 题号 | 出现次数 |
| ------ | ---- | -------- |
| SQL 特点与功能动词 | 单选1、单选2、简答1 | 3 |
| 数据定义（建表/约束/删除） | 单选3、单选10、多选1、分析4、综合1 | 5 |
| 单表查询 | 分析1 | 1 |
| 连接查询 | 单选5、分析2 | 2 |
| 嵌套查询 | 简答4、分析3 | 2 |
| 集合查询 | 综合2 | 1 |
| 聚集函数与 GROUP BY/HAVING | 单选4、多选2、分析1、简答2 | 4 |
| LIKE 通配符 | 多选3 | 1 |
| NULL 处理 | 单选6、判断3 | 2 |
| 数据更新 | 分析4、综合2 | 2 |
| 视图 | 单选7、单选8、判断1、多选4、简答3、综合1 | 6 |
| 嵌入式 SQL | 单选9、多选5、判断5 | 3 |
| DELETE/DROP 区别 | 判断2 | 1 |
| ANY/ALL 等价转换 | 判断4 | 1 |

## 章节导航

> [!nav] 导航
> 上一级：[[MOC - 数据库原理]] · 本章知识点：[[MOC - 第3章]] · 上一章习题：[[MOC - 第2章习题]] · 下一章习题：[[MOC - 第4章习题]]
