---
domain: 数据库技术
subject: 数据库原理
type: exercise
chapter: 第5章 数据库完整性
section: 5.1 完整性约束概念
tags: [数据库原理,习题,数据库完整性,实体完整性,参照完整性,用户定义完整性,触发器]
prerequisites: ["[[MOC - 第5章]]"]
---

# MOC - 第5章习题

本习题集覆盖第5章数据库完整性的全部知识点，按"单选 → 多选 → 判断 → 简答 → 分析 → 综合"六类组织共 30 题，所有题目均附答案与解析，用于课后练习与期末复习。建议先独立作答再查看答案。

> [!abstract] 习题范围
> 涵盖 [[5.1 完整性约束概念]]、[[5.2 实体完整性]]、[[5.3 参照完整性]]（违约处理）、[[5.4 用户定义完整性]]（NOT NULL/UNIQUE/CHECK）、[[5.5 触发器实现完整性]]（含 SQL 编程题）。

---

## 一、单选题（10题）

**1.** 数据库完整性防范的对象是（ ）。
- A. 非法用户的非法访问
- B. 合法用户输入不合语义的数据
- C. 系统故障导致的数据丢失
- D. 并发操作引起的数据不一致

<details>
<summary>答案与解析</summary>
<b>答案：B</b>。数据库完整性防止合法用户输入不合语义的错误数据；A 是安全性问题；C 是恢复技术问题；D 是并发控制问题。详见 [[5.1 完整性约束概念]] 与 [[4.1 数据库安全概述]]。
</details>

**2.** 实体完整性规则要求（ ）。
- A. 主码取值唯一
- B. 主码取值非空
- C. 主码取值唯一且非空
- D. 外码必须在被参照表中存在

<details>
<summary>答案与解析</summary>
<b>答案：C</b>。实体完整性规则：主码取值唯一且非空。D 是参照完整性规则。
</details>

**3.** 关于参照完整性的违约处理，下列描述错误的是（ ）。
- A. NO ACTION 表示拒绝违约操作
- B. CASCADE 表示级联操作相关数据
- C. SET NULL 表示将相关数据置为 NULL
- D. SET DEFAULT 表示删除违约的记录

<details>
<summary>答案与解析</summary>
<b>答案：D</b>。SET DEFAULT 表示将相关外码置为默认值，不是删除记录。
</details>

**4.** 在 `SC(Sno, Cno, Grade)` 表中，`(Sno, Cno)` 是主码，则下列描述正确的是（ ）。
- A. Sno 可以取 NULL
- B. Cno 可以取 NULL
- C. Sno 和 Cno 都不能取 NULL
- D. (Sno, Cno) 整体不能取 NULL，但单独列可以

<details>
<summary>答案与解析</summary>
<b>答案：C</b>。主码的任何组成部分都不能取 NULL（实体完整性规则：所有主属性非空）。
</details>

**5.** 下列约束中，不属于用户定义完整性的是（ ）。
- A. NOT NULL
- B. UNIQUE
- C. CHECK
- D. FOREIGN KEY

<details>
<summary>答案与解析</summary>
<b>答案：D</b>。FOREIGN KEY 属于参照完整性；NOT NULL、UNIQUE、CHECK 是用户定义完整性的实现机制。
</details>

**6.** CHECK 约束的局限性在于（ ）。
- A. 只能定义在列上，不能定义在表上
- B. 不能跨元组或跨表查询
- C. 只能检查非空，不能检查范围
- D. MySQL 完全不支持 CHECK

<details>
<summary>答案与解析</summary>
<b>答案：B</b>。CHECK 不能跨元组或跨表查询，复杂规则需用触发器。MySQL 8.0.16+ 已支持 CHECK。
</details>

**7.** 触发器的"事件-条件-动作"模型中，"事件"指的是（ ）。
- A. 触发时机（BEFORE/AFTER）
- B. 触发操作类型（INSERT/UPDATE/DELETE）
- C. 时机与操作类型的组合
- D. 触发条件表达式

<details>
<summary>答案与解析</summary>
<b>答案：C</b>。事件由"时机（BEFORE/AFTER）+ 操作类型（INSERT/UPDATE/DELETE）"组成，如 BEFORE INSERT。
</details>

**8.** 在 BEFORE UPDATE 触发器中，访问更新前的旧值应使用（ ）。
- A. NEW.列名
- B. OLD.列名
- C. CURRENT.列名
- D. ROW.列名

<details>
<summary>答案与解析</summary>
<b>答案：B</b>。OLD 表示更新前的旧值，NEW 表示更新后的新值。
</details>

**9.** 关于触发器与约束的对比，正确的是（ ）。
- A. 约束性能低于触发器
- B. 约束能表达跨表约束，触发器不能
- C. 触发器能表达动态约束，约束不能
- D. 触发器可移植性高于约束

<details>
<summary>答案与解析</summary>
<b>答案：C</b>。触发器能表达动态约束（新旧值比较），CHECK 约束只能检查静态值；约束性能高于触发器，可移植性也更高。
</details>

**10.** 在参照完整性中，外码取值的合法情况是（ ）。
- A. 必须为 NULL
- B. 必须在被参照表中存在
- C. 要么为 NULL，要么在被参照表中存在
- D. 可以是任意值

<details>
<summary>答案与解析</summary>
<b>答案：C</b>。参照完整性规则：外码要么为 NULL，要么在被参照表中存在（前提是外码列允许 NULL）。
</details>

---

## 二、多选题（5题）

**1.** 完整性约束条件按作用对象可分为（ ）。
- A. 列级约束
- B. 元组级约束
- C. 关系级约束
- D. 数据库级约束

<details>
<summary>答案与解析</summary>
<b>答案：ABC</b>。按作用对象分列级、元组级、关系级三类。教材中无数据库级约束分类。
</details>

**2.** DBMS 的完整性控制机制包括（ ）。
- A. 定义功能
- B. 检查功能
- C. 违约处理
- D. 备份恢复

<details>
<summary>答案与解析</summary>
<b>答案：ABC</b>。完整性控制机制包括定义、检查、违约处理三方面。备份恢复属于恢复技术，不属于完整性控制。
</details>

**3.** 参照完整性的违约处理策略包括（ ）。
- A. NO ACTION / RESTRICT
- B. CASCADE
- C. SET NULL
- D. SET DEFAULT

<details>
<summary>答案与解析</summary>
<b>答案：ABCD</b>。四种策略均为参照完整性违约处理方式。
</details>

**4.** 下列属于用户定义完整性实现机制的有（ ）。
- A. NOT NULL
- B. UNIQUE
- C. CHECK
- D. CONSTRAINT 命名约束

<details>
<summary>答案与解析</summary>
<b>答案：ABCD</b>。NOT NULL、UNIQUE、CHECK 是用户定义完整性的实现机制；CONSTRAINT 用于为约束命名，便于管理。
</details>

**5.** 触发器相比声明式约束的优势包括（ ）。
- A. 能实现跨表约束
- B. 能实现动态约束
- C. 能实现审计日志
- D. 能实现复杂条件级联

<details>
<summary>答案与解析</summary>
<b>答案：ABCD</b>。触发器灵活强大，能实现跨表约束、动态约束、审计日志、复杂级联等场景。
</details>

---

## 三、判断题（5题）

**1.** 实体完整性要求主码的任何组成部分都不能取 NULL。（ ）

<details>
<summary>答案与解析</summary>
<b>答案：对</b>。实体完整性规则要求所有主属性（包含在任一候选码中的属性）都不能取 NULL，不仅是主码列。
</details>

**2.** UNIQUE 约束的列不允许出现多个 NULL 值。（ ）

<details>
<summary>答案与解析</summary>
<b>答案：错</b>。UNIQUE 允许有多个 NULL（NULL 不参与唯一性比较），这是它与 PRIMARY KEY 的重要区别。
</details>

**3.** CASCADE 策略在删除被参照表记录时，会连带删除参照表中引用该主码的记录。（ ）

<details>
<summary>答案与解析</summary>
<b>答案：对</b>。CASCADE 表示级联操作，删除/更新被参照表主码时，参照表对应记录执行相同操作。
</details>

**4.** CHECK 约束可以在条件中查询本表其他元组的聚合值。（ ）

<details>
<summary>答案与解析</summary>
<b>答案：错</b>。CHECK 不能跨元组或跨表查询，不能用聚合函数或子查询，复杂规则需用触发器。
</details>

**5.** MySQL 触发器支持语句级触发（FOR EACH STATEMENT）。（ ）

<details>
<summary>答案与解析</summary>
<b>答案：错</b>。MySQL 仅支持行级触发器（FOR EACH ROW），不支持语句级触发器。
</details>

---

## 四、简答题（4题）

**1.** 简述数据库完整性约束条件的分类（按作用对象与按时间维度），并各举一例。

<details>
<summary>参考答案</summary>
- <b>按作用对象</b>：
  - 列级约束：约束单个列，如 `Sage INT CHECK (Sage>0)`；
  - 元组级约束：约束元组内多列关系，如 `CHECK (EndDate >= StartDate)`；
  - 关系级约束：约束整个关系或多表关系，如主码唯一、外码参照。
- <b>按时间维度</b>：
  - 静态约束：与时间无关，反映数据固有性质，如 `Sage>0`（任何时刻年龄为正）；
  - 动态约束：涉及状态变迁，如"工资只能升不能降"（新工资 ≥ 旧工资），需用触发器实现。

详见 [[5.1 完整性约束概念]]。
</details>

**2.** 简述参照完整性的双向检查机制，并说明四种违约处理策略。

<details>
<summary>参考答案</summary>
- <b>双向检查</b>：
  - 参照表侧：INSERT 或 UPDATE 外码时，检查外码值是否在被参照表中存在（或为 NULL）；
  - 被参照表侧：DELETE 或 UPDATE 主码时，检查是否有参照表元组引用该主码，若有则按违约策略处理。
- <b>四种违约处理策略</b>：
  - NO ACTION / RESTRICT：拒绝违约操作；
  - CASCADE：级联，参照表对应记录执行相同操作；
  - SET NULL：参照表对应外码置 NULL（要求外码列允许 NULL）；
  - SET DEFAULT：参照表对应外码置默认值。

详见 [[5.3 参照完整性]]。
</details>

**3.** 简述触发器的"事件-条件-动作"模型及 BEFORE 与 AFTER 触发器的区别。

<details>
<summary>参考答案</summary>
- <b>ECA 模型</b>：
  - 事件（Event）：触发触发器的操作，由"时机 + 类型"组成，如 BEFORE INSERT；
  - 条件（Condition）：触发时需满足的条件；
  - 动作（Action）：满足条件时执行的 SQL 语句块。
- <b>BEFORE vs AFTER</b>：
  - BEFORE 触发器在数据写入前执行，可修改 NEW 值，常用于约束检查与数据预处理；
  - AFTER 触发器在数据写入后执行，无法修改已写入数据，常用于审计、级联、日志。

详见 [[5.5 触发器实现完整性]]。
</details>

**4.** 简述触发器与声明式约束的对比，并说明何时应优先使用触发器。

<details>
<summary>参考答案</summary>
- <b>对比</b>：
  - 定义方式：约束是 DDL 声明，触发器是过程式代码；
  - 表达能力：约束简单固定，触发器灵活强大；
  - 性能：约束高（DBMS 内部优化），触发器低（每行触发执行）；
  - 可移植性：约束高（SQL 标准），触发器低（各 DBMS 语法差异大）；
  - 调试难度：约束容易，触发器困难。
- <b>优先使用触发器的场景</b>：
  - 跨表约束（CHECK 无法跨表）；
  - 动态约束（新旧值比较，CHECK 无法实现）；
  - 复杂条件级联（外码 CASCADE 不够灵活时）；
  - 审计日志记录；
  - 能用约束表达的应优先用约束，不要用触发器。

详见 [[5.5 触发器实现完整性#五、触发器与约束的对比]]。
</details>

---

## 五、分析题（4题）

**1.** 给定以下表定义：
```sql
-- MySQL 8.0
CREATE TABLE Student (Sno CHAR(9) PRIMARY KEY, Sname VARCHAR(20) NOT NULL, Sdept VARCHAR(20));
CREATE TABLE SC (
    Sno CHAR(9),
    Cno CHAR(4),
    Grade INT CHECK (Grade BETWEEN 0 AND 100),
    PRIMARY KEY (Sno, Cno),
    FOREIGN KEY (Sno) REFERENCES Student(Sno) ON DELETE SET NULL
);
```
分析以下操作的结果：
(a) `INSERT INTO SC VALUES ('202499999', 'C001', 85);`
(b) `INSERT INTO SC VALUES (NULL, 'C001', 85);`
(c) `INSERT INTO SC VALUES ('202400001', 'C001', 120);`
(d) 删除 Student 表中 Sno='202400001' 的记录（假设 SC 表有引用该记录的元组）。

<details>
<summary>参考答案</summary>
- (a) 失败。Sno='202499999' 在 Student 表中不存在，违反参照完整性。MySQL 报错 1452。
- (b) 失败。Sno 是主码 (Sno, Cno) 的组成部分，主属性不能为 NULL，违反实体完整性。MySQL 报错 1048。
- (c) 失败。Grade=120 不满足 CHECK (Grade BETWEEN 0 AND 100)，违反用户定义完整性。MySQL 报错 3819。
- (d) SET NULL 策略下，Student 中该记录被删除；SC 表中引用 Sno='202400001' 的元组的 Sno 列应被置 NULL。但由于 Sno 是 SC 表主码组成部分（主属性），不能为 NULL，所以实际上 MySQL 会拒绝该删除操作（外码约束与实体完整性冲突）。这是 SET NULL 与实体完整性冲突的典型场景，设计时应避免在外码同时是主属性时使用 SET NULL。

详见 [[5.2 实体完整性]]、[[5.3 参照完整性]]、[[5.4 用户定义完整性]]。
</details>

**2.** 分析以下触发器的作用，并说明它实现的是哪类完整性约束（按作用对象与时间维度分类）：
```sql
DELIMITER //
CREATE TRIGGER trg_salary_check
BEFORE UPDATE ON Employee
FOR EACH ROW
BEGIN
    IF NEW.Salary < OLD.Salary THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '工资只能升不能降';
    END IF;
END //
DELIMITER ;
```

<details>
<summary>参考答案</summary>
- <b>作用</b>：在更新 Employee 表前，检查新工资是否小于旧工资，若是则拒绝操作。
- <b>分类</b>：
  - 按作用对象：列级约束（约束 Salary 列）；
  - 按时间维度：动态约束（涉及新旧值比较，约束状态变迁）。
- <b>说明</b>：该约束 CHECK 无法实现（CHECK 只能检查当前值，不能引用旧值），需用 BEFORE UPDATE 触发器实现。详见 [[5.5 触发器实现完整性#4.3 示例 2：BEFORE 触发器——工资只能升不能降（动态约束）]]。
</details>

**3.** 设计一个触发器，实现"员工工资不得低于本部门最低工资"的约束。已知表：
```sql
CREATE TABLE Department (DeptName VARCHAR(20) PRIMARY KEY, MinSalary DECIMAL(10,2) NOT NULL);
CREATE TABLE Employee (EmpID CHAR(9) PRIMARY KEY, Name VARCHAR(20), Dept VARCHAR(20), Salary DECIMAL(10,2));
```
要求：在 INSERT 和 UPDATE Salary 时都进行检查。说明为何 CHECK 约束无法实现此规则。

<details>
<summary>参考答案</summary>
```sql
-- MySQL 8.0，使用 scdb 数据库
USE scdb;

-- 插入时检查
DELIMITER //
CREATE TRIGGER trg_salary_dept_min_insert
BEFORE INSERT ON Employee
FOR EACH ROW
BEGIN
    DECLARE v_min DECIMAL(10,2);
    SELECT MinSalary INTO v_min FROM Department WHERE DeptName = NEW.Dept;
    IF NEW.Salary < v_min THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '工资不得低于本部门最低工资';
    END IF;
END //

-- 更新时检查
DELIMITER //
CREATE TRIGGER trg_salary_dept_min_update
BEFORE UPDATE ON Employee
FOR EACH ROW
BEGIN
    DECLARE v_min DECIMAL(10,2);
    SELECT MinSalary INTO v_min FROM Department WHERE DeptName = NEW.Dept;
    IF NEW.Salary < v_min THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '工资不得低于本部门最低工资';
    END IF;
END //
DELIMITER ;
```
- <b>为何 CHECK 无法实现</b>：CHECK 约束<b>不能跨表查询</b>，不能在 Employee 表的 CHECK 中查询 Department 表的 MinSalary。这种跨表约束必须用触发器实现。

详见 [[5.5 触发器实现完整性#4.2 示例 1：BEFORE 触发器——工资不得低于本部门最低工资]]。
</details>

**4.** 某订单系统有 `Order(OrderID, CustID, OrderDate, TotalAmount)` 和 `OrderItem(OrderID, ProductID, Quantity, Price)` 两表，OrderItem.OrderID 外码参照 Order.OrderID。需求：删除订单时，同时删除其所有订单明细，并在 OrderItem 上记录删除日志到 `DeleteLog` 表。设计触发器或外码策略实现。

<details>
<summary>参考答案</summary>
- <b>方案一</b>：使用外码 CASCADE 自动级联删除（简洁，但无法记录日志）
```sql
CREATE TABLE OrderItem (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    Price DECIMAL(10,2),
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID) ON DELETE CASCADE
);
```
- <b>方案二</b>：使用 AFTER DELETE 触发器记录日志（CASCADE 删除明细后自动记录日志）
```sql
-- 先用 CASCADE 让 MySQL 自动删除 OrderItem
CREATE TABLE OrderItem (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    Price DECIMAL(10,2),
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID) ON DELETE CASCADE
);

-- 在 OrderItem 上加 AFTER DELETE 触发器记录日志
DELIMITER //
CREATE TRIGGER trg_orderitem_delete_log
AFTER DELETE ON OrderItem
FOR EACH ROW
BEGIN
    INSERT INTO DeleteLog(OrderID, ProductID, Quantity, Price, DeleteTime, Operator)
    VALUES (OLD.OrderID, OLD.ProductID, OLD.Quantity, OLD.Price, NOW(), CURRENT_USER());
END //
DELIMITER ;
```
- <b>方案二优势</b>：CASCADE 自动级联删除保证参照完整性，AFTER DELETE 触发器实现审计日志。两者配合实现"删除 + 审计"的复合需求，是触发器与约束协同的典型应用。

详见 [[5.3 参照完整性]]、[[5.5 触发器实现完整性]]。
</details>

---

## 六、综合题（2题）

**1.** 某图书管理系统的数据库有如下表：
```sql
-- MySQL 8.0，使用 scdb 数据库
USE scdb;
CREATE TABLE Reader (ReaderID CHAR(10) PRIMARY KEY, Name VARCHAR(20) NOT NULL, Type VARCHAR(10) CHECK (Type IN ('学生','教师','职工')));
CREATE TABLE Book (BookID CHAR(10) PRIMARY KEY, Title VARCHAR(100) NOT NULL, TotalCopies INT DEFAULT 1);
CREATE TABLE Borrow (
    BorrowID INT AUTO_INCREMENT PRIMARY KEY,
    ReaderID CHAR(10),
    BookID CHAR(10),
    BorrowDate DATE NOT NULL,
    ReturnDate DATE,
    CONSTRAINT chk_date CHECK (ReturnDate IS NULL OR ReturnDate >= BorrowDate),
    FOREIGN KEY (ReaderID) REFERENCES Reader(ReaderID) ON DELETE CASCADE,
    FOREIGN KEY (BookID) REFERENCES Book(BookID) ON DELETE RESTRICT
);
```
要求：
(1) 解释每条完整性约束的作用；
(2) 分析删除读者时 Borrow 表的处理；
(3) 分析删除图书时 Borrow 表的处理；
(4) 编写触发器实现"借书时检查图书库存大于 0，库存为 0 则拒绝借出"，假设 Book 表新增 `AvailableCopies INT` 列。

<details>
<summary>参考答案</summary>
- <b>(1) 约束作用</b>：
  - Reader 表：`PRIMARY KEY (ReaderID)` 实体完整性，读者号唯一非空；`NOT NULL Name` 用户定义完整性，姓名非空；`CHECK (Type IN ...)` 用户定义完整性，类型取值约束。
  - Book 表：`PRIMARY KEY (BookID)` 实体完整性；`NOT NULL Title` 用户定义完整性；`DEFAULT TotalCopies 1` 默认值。
  - Borrow 表：
    - `PRIMARY KEY (BorrowID)` 实体完整性；
    - `CHECK (ReturnDate IS NULL OR ReturnDate >= BorrowDate)` 元组级用户定义完整性，归还日期不早于借出日期；
    - `FOREIGN KEY (ReaderID) ON DELETE CASCADE` 参照完整性，删读者时级联删借阅记录；
    - `FOREIGN KEY (BookID) ON DELETE RESTRICT` 参照完整性，有借阅记录的图书不允许删除。
- <b>(2) 删除读者</b>：CASCADE 策略，Reader 中删除读者后，Borrow 表中该读者的所有借阅记录被级联删除。
- <b>(3) 删除图书</b>：RESTRICT 策略，若 Borrow 表中有引用该 BookID 的记录，则拒绝删除图书；需先删除或迁移相关借阅记录才能删除图书。
- <b>(4) 触发器实现库存检查</b>：
```sql
-- 假设已为 Book 表新增 AvailableCopies 列
-- ALTER TABLE Book ADD COLUMN AvailableCopies INT DEFAULT 0;

DELIMITER //
CREATE TRIGGER trg_check_available_before_borrow
BEFORE INSERT ON Borrow
FOR EACH ROW
BEGIN
    DECLARE v_avail INT;
    SELECT AvailableCopies INTO v_avail FROM Book WHERE BookID = NEW.BookID;
    IF v_avail <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '该图书库存为 0，不可借出';
    END IF;
    -- 借出后库存减 1
    UPDATE Book SET AvailableCopies = AvailableCopies - 1 WHERE BookID = NEW.BookID;
END //
DELIMITER ;

-- 配合还书触发器，归还后库存加 1
DELIMITER //
CREATE TRIGGER trg_return_add_stock
AFTER UPDATE ON Borrow
FOR EACH ROW
BEGIN
    IF OLD.ReturnDate IS NULL AND NEW.ReturnDate IS NOT NULL THEN
        UPDATE Book SET AvailableCopies = AvailableCopies + 1 WHERE BookID = NEW.BookID;
    END IF;
END //
DELIMITER ;
```
- <b>设计要点</b>：
  - BEFORE INSERT 触发器实现库存检查，保证借出时库存足够；
  - 触发器内同时更新 Book 表的库存，是跨表级联的典型应用；
  - AFTER UPDATE 触发器在归还时增加库存，保证数据一致；
  - 该约束涉及跨表（Borrow 表的借出动作影响 Book 表库存），CHECK 无法实现，必须用触发器。

详见 [[5.1 完整性约束概念]] 至 [[5.5 触发器实现完整性]]。
</details>

**2.** 综合分析：某人力资源系统需要保证以下完整性约束，请为每个需求选择合适的实现机制（实体完整性、参照完整性、用户定义完整性 CHECK、触发器），并说明理由。
(a) 员工号 EmpID 唯一且非空；
(b) 员工所属部门必须在 Department 表中存在；
(c) 员工年龄在 18-65 之间；
(d) 员工合同结束日期不早于开始日期；
(e) 员工工资不得低于本部门最低工资；
(f) 删除部门时，该部门所有员工自动转移到"未分配"部门；
(g) 任何对员工表的修改都需记录到审计日志。

<details>
<summary>参考答案</summary>
- <b>(a) EmpID 唯一且非空</b>：实体完整性，`PRIMARY KEY (EmpID)`。最简单高效。
- <b>(b) 部门必须存在</b>：参照完整性，`FOREIGN KEY (Dept) REFERENCES Department(DeptName)`。标准外码约束，CHECK 无法跨表查询。
- <b>(c) 年龄 18-65</b>：用户定义完整性，`CHECK (Age BETWEEN 18 AND 65)`。简单列级范围约束，CHECK 完全胜任。
- <b>(d) 结束日期 ≥ 开始日期</b>：用户定义完整性，元组级 `CHECK (EndDate IS NULL OR EndDate >= StartDate)`。元组内列间关系，CHECK 可表达。
- <b>(e) 工资 ≥ 部门最低工资</b>：触发器。需跨表查询 Department 表的 MinSalary，CHECK 无法跨表，必须用 BEFORE INSERT/UPDATE 触发器实现。
- <b>(f) 删部门时员工转移到"未分配"</b>：参照完整性 + 触发器。外码 `ON DELETE SET DEFAULT`（若 Dept 默认值为"未分配"）可部分实现；但若需复杂逻辑（如设置默认值为"未分配"且该值必须在 Department 表中存在），用 AFTER DELETE 触发器更灵活。
- <b>(g) 修改审计日志</b>：触发器。审计需在数据修改后自动记录到日志表，CHECK 与外码都无法实现，必须用 AFTER INSERT/UPDATE/DELETE 触发器记录到审计表。
- <b>整体原则</b>：
  - 能用约束的优先用约束（性能高、可移植性好）；
  - 跨表、动态、审计等复杂规则才用触发器；
  - 实体完整性用 PRIMARY KEY；
  - 参照完整性用 FOREIGN KEY；
  - 简单列/元组范围约束用 CHECK；
  - 跨表约束、状态变迁、审计日志用触发器。

详见 [[5.1 完整性约束概念]] 至 [[5.5 触发器实现完整性]]。
</details>

---

## 考点统计表

| 题型 | 题数 | 覆盖知识点 | 分值占比（参考） |
| ---- | ---- | ---- | ---- |
| 单选题 | 10 | 完整性概念、实体完整性、参照完整性违约处理、用户定义完整性、CHECK 局限性、触发器 ECA 模型、NEW/OLD | 20% |
| 多选题 | 5 | 约束分类、控制机制、违约处理策略、用户定义机制、触发器优势 | 15% |
| 判断题 | 5 | 实体完整性 NULL 规则、UNIQUE 与 NULL、CASCADE 语义、CHECK 局限性、MySQL 触发器粒度 | 10% |
| 简答题 | 4 | 约束分类、参照完整性双向检查与策略、触发器 ECA 与 BEFORE/AFTER、触发器 vs 约束 | 25% |
| 分析题 | 4 | 综合约束分析、触发器分类、跨表触发器设计、级联删除与审计 | 20% |
| 综合题 | 2 | 综合约束设计、机制选型 | 10% |
| **合计** | **30** | 第5章全部知识点 | **100%** |

| 知识点 | 涉及题号 | 出现频次 |
| ---- | ---- | ---- |
| 完整性概念与分类 | 单1、多1、多2、简1、综2 | 5 |
| 实体完整性 | 单2、单4、判断1、分析1 | 4 |
| 参照完整性（违约处理） | 单3、单10、多3、判断3、简2、分析1、综1 | 7 |
| 用户定义完整性（NOT NULL/UNIQUE/CHECK） | 单5、单6、判断2、判断4、多4、分析1、综1、综2 | 8 |
| 触发器（ECA、NEW/OLD、BEFORE/AFTER） | 单7、单8、单9、判断5、多5、简3、简4、分析2、分析3、分析4、综1 | 11 |
| 触发器 vs 约束 | 单9、简4、综2 | 3 |
| 跨表/动态约束 | 分析3、综1 | 2 |

## 章节导航

- 上一级：[[MOC - 数据库原理]]
- 本章知识点：[[MOC - 第5章]]
- 上一章习题：[[MOC - 第4章习题]]
- 下一章习题：[[MOC - 第6章习题]]
