---
domain: 数据库技术
subject: 数据库原理
type: exercise
chapter: 第4章 数据库安全性
section: 4.1 数据库安全概述
tags: [数据库原理,习题,数据库安全性,GRANT,REVOKE,DAC,MAC,视图,审计,加密]
prerequisites: ["[[MOC - 第4章]]"]
---

# MOC - 第4章习题

本习题集覆盖第4章数据库安全性的全部知识点，按"单选 → 多选 → 判断 → 简答 → 分析 → 综合"六类组织共 30 题，所有题目均附答案与解析，用于课后练习与期末复习。建议先独立作答再查看答案。

> [!abstract] 习题范围
> 涵盖 [[4.1 数据库安全概述]]、[[4.2 身份鉴别]]、[[4.3 存取控制]]（GRANT/REVOKE、DAC/MAC）、[[4.4 视图机制、审计]]、[[4.5 数据加密基础]]（加密方式、统计数据库）。

---

## 一、单选题（10题）

**1.** 数据库安全性防范的对象是（ ）。
- A. 合法用户输入不合语义的数据
- B. 非法用户的非法访问与破坏
- C. 系统故障导致的数据丢失
- D. 并发操作引起的数据不一致

<details>
<summary>答案与解析</summary>
<b>答案：B</b>。数据库安全性防止非法访问；A 是完整性问题；C 是恢复技术问题；D 是并发控制问题。详见 [[5.1 完整性约束概念]] 与 [[4.1 数据库安全概述]]。
</details>

**2.** 计算机安全性的 CIA 三元组不包括（ ）。
- A. 保密性
- B. 完整性
- C. 可用性
- D. 可追溯性

<details>
<summary>答案与解析</summary>
<b>答案：D</b>。CIA 三元组为 Confidentiality（保密性）、Integrity（完整性）、Availability（可用性）。可追溯性属于审计目标，非 CIA 三元组。
</details>

**3.** TCSEC 中需要支持强制存取控制 MAC 的最低安全级别是（ ）。
- A. C1
- B. C2
- C. B1
- D. B2

<details>
<summary>答案与解析</summary>
<b>答案：C</b>。C1-C2 仅支持 DAC；B1 及以上必须支持 MAC（敏感度标记）。
</details>

**4.** 在 SQL 中，将表 Student 的 SELECT 权限授予用户 U1，并允许 U1 转授他人，正确的语句是（ ）。
- A. `GRANT SELECT ON Student TO U1 WITH CHECK OPTION;`
- B. `GRANT SELECT ON Student TO U1 WITH GRANT OPTION;`
- C. `GRANT SELECT ON Student TO U1 CASCADE;`
- D. `REVOKE SELECT ON Student FROM U1 WITH GRANT OPTION;`

<details>
<summary>答案与解析</summary>
<b>答案：B</b>。`WITH GRANT OPTION` 允许被授权者转授权限；WITH CHECK OPTION 是视图更新检查；CASCADE 用于 REVOKE 的级联回收。
</details>

**5.** 关于 MAC 的敏感度标记，下列密级由高到低排序正确的是（ ）。
- A. S > TS > C > U
- B. TS > S > C > U
- C. U > C > S > TS
- D. TS > C > S > U

<details>
<summary>答案与解析</summary>
<b>答案：B</b>。MAC 敏感度标记从高到低为 TS（绝密）> S（机密）> C（秘密）> U（普通）。
</details>

**6.** 在强制存取控制 MAC 中，密级为 S 的用户（ ）。
- A. 能读 S 与 C 级数据，不能写 C 级数据
- B. 能读 S 与 C 级数据，能写 C 级数据
- C. 不能读 C 级数据
- D. 只能读写 S 级数据

<details>
<summary>答案与解析</summary>
<b>答案：A</b>。读规则"向下读"：S 级用户可读 S、C 级数据（S≥C）；写规则"向上写"：S 级用户不能写 C 级数据（要求主体密级 ≤ 客体密级，S>C 不满足）。
</details>

**7.** 下列关于视图机制实现安全性的描述，错误的是（ ）。
- A. 可为不同用户定义不同视图
- B. 能实现列级权限隔离
- C. 能实现行级权限隔离
- D. 视图能完全替代 GRANT/REVOKE 的所有功能

<details>
<summary>答案与解析</summary>
<b>答案：D</b>。视图是存取控制的补充手段，无法完全替代 GRANT/REVOKE（如创建表、删除表的权限仍需 GRANT）。
</details>

**8.** 关于审计（Audit）的描述，正确的是（ ）。
- A. 审计是事前预防机制
- B. 审计是事后追溯机制
- C. MySQL 8.0 社区版默认支持 AUDIT 语句
- D. 审计能阻止非法操作的发生

<details>
<summary>答案与解析</summary>
<b>答案：B</b>。审计记录操作日志供事后分析，属事后追溯机制；存取控制才是事前预防。MySQL 8.0 社区版不原生支持 AUDIT 语句，需审计插件。
</details>

**9.** 下列加密算法中，属于非对称加密的是（ ）。
- A. DES
- B. AES
- C. RSA
- D. 3DES

<details>
<summary>答案与解析</summary>
<b>答案：C</b>。RSA 是非对称加密；DES、3DES、AES 都是对称加密。
</details>

**10.** 在统计数据库中，攻击者通过多次统计查询推断出个体数据，这种攻击称为（ ）。
- A. 特洛伊木马攻击
- B. 推断攻击
- C. SQL 注入
- D. 重放攻击

<details>
<summary>答案与解析</summary>
<b>答案：B</b>。统计数据库通过构造多个统计查询推断个体信息属于推断攻击，需通过推断控制防范。
</details>

---

## 二、多选题（5题）

**1.** 下列属于数据库安全保护层面的有（ ）。
- A. 物理环境层
- B. 网络层
- C. 操作系统层
- D. 数据库系统层

<details>
<summary>答案与解析</summary>
<b>答案：ABCD</b>。数据库安全需物理、网络、操作系统、数据库系统、应用多个层面协同保护。
</details>

**2.** 身份鉴别常用的方法包括（ ）。
- A. 口令鉴别
- B. 智能卡鉴别
- C. 生物特征鉴别
- D. 多因素鉴别

<details>
<summary>答案与解析</summary>
<b>答案：ABCD</b>。四种均为常用身份鉴别方法，多因素鉴别是上述方法的组合。
</details>

**3.** 在 SQL 中，以下权限类型属于表级权限的有（ ）。
- A. SELECT
- B. INSERT
- C. CREATE
- D. DELETE

<details>
<summary>答案与解析</summary>
<b>答案：ABD</b>。SELECT、INSERT、UPDATE、DELETE、REFERENCES 等是表/视图级权限；CREATE 是数据库/模式级权限，不属于表级。
</details>

**4.** 关于 MAC 与 DAC 的区别，下列说法正确的有（ ）。
- A. DAC 由对象所有者自主授权，MAC 由系统强制执行
- B. DAC 支持 WITH GRANT OPTION 权限传播，MAC 不支持
- C. DAC 安全等级低于 MAC
- D. MAC 通过敏感度标记决定访问，DAC 通过授权矩阵决定

<details>
<summary>答案与解析</summary>
<b>答案：ABCD</b>。四项均为 DAC 与 MAC 的本质区别。
</details>

**5.** 下列关于数据库加密的描述，正确的有（ ）。
- A. 对称加密速度快但密钥分发难
- B. 非对称加密速度慢但解决了密钥分发问题
- C. 库内加密对应用透明
- D. 实际系统通常采用混合加密

<details>
<summary>答案与解析</summary>
<b>答案：ABCD</b>。四项均正确。混合加密 = 非对称加密协商密钥 + 对称加密数据。
</details>

---

## 三、判断题（5题）

**1.** 数据库安全性是防止合法用户输入不合语义数据的机制。（ ）

<details>
<summary>答案与解析</summary>
<b>答案：错</b>。这是数据库完整性的定义。数据库安全性是防止非法用户的非法访问与破坏。
</details>

**2.** WITH GRANT OPTION 允许被授权用户将所得权限再授予其他用户。（ ）

<details>
<summary>答案与解析</summary>
<b>答案：对</b>。WITH GRANT OPTION 是 DAC 权限传播机制的核心。
</details>

**3.** 在 MAC 中，密级为 C 的用户可以读密级为 S 的数据。（ ）

<details>
<summary>答案与解析</summary>
<b>答案：错</b>。读规则要求主体密级 ≥ 客体密级（向下读），C < S 不满足。
</details>

**4.** MySQL 8.0 必须先创建用户再授权，不能在 GRANT 语句中直接创建用户。（ ）

<details>
<summary>答案与解析</summary>
<b>答案：对</b>。MySQL 8.0 移除了 `GRANT ... IDENTIFIED BY` 语法，必须先 `CREATE USER` 再 `GRANT`。
</details>

**5.** 审计能阻止非法操作的发生，是事前预防机制。（ ）

<details>
<summary>答案与解析</summary>
<b>答案：错</b>。审计是事后追溯机制，记录操作日志供分析，不能阻止非法操作。事前预防是身份鉴别与存取控制。
</details>

---

## 四、简答题（4题）

**1.** 简述数据库安全性与数据库完整性的区别与联系。

<details>
<summary>参考答案</summary>
- <b>区别</b>：
  - 目标不同：安全性防止<b>非法用户</b>对数据库的非法访问；完整性防止<b>合法用户</b>输入<b>不合语义</b>的错误数据。
  - 关注对象不同：安全性关注"用户合法性"，完整性关注"数据正确性"。
  - 机制不同：安全性靠身份鉴别、存取控制、视图、审计、加密；完整性靠实体完整性、参照完整性、用户定义完整性、触发器。
  - 触发时机不同：安全性在访问数据库时检查，完整性在数据写入时检查。
- <b>联系</b>：二者都是数据保护机制，目标都是保证数据的<b>正确可用</b>。安全性保证"只有授权用户能访问"，完整性保证"被访问的数据本身正确"。两者协同工作，缺一不可。

详见 [[4.1 数据库安全概述]] 与 [[5.1 完整性约束概念]]。
</details>

**2.** 简述自主存取控制 DAC 与强制存取控制 MAC 的区别。

<details>
<summary>参考答案</summary>
- <b>控制依据</b>：DAC 基于用户身份与授权矩阵；MAC 基于主体/客体的敏感度标记与支配关系。
- <b>授权主体</b>：DAC 由对象所有者自主授权；MAC 由系统统一强制执行。
- <b>权限传播</b>：DAC 支持 WITH GRANT OPTION 转授；MAC 不允许，由系统统一标记。
- <b>安全等级</b>：DAC 在 C1-C2 级；MAC 在 B1 级及以上。
- <b>典型场景</b>：DAC 用于商业 DBMS；MAC 用于军用、政府涉密系统。
- <b>防木马能力</b>：DAC 易被特洛伊木马绕过；MAC 的"向上写"规则能防止信息从高密级流向低密级，可有效防木马。

详见 [[4.3 存取控制]]。
</details>

**3.** 简述视图机制如何实现数据库安全性。

<details>
<summary>参考答案</summary>
视图机制通过为不同用户定义不同视图，将用户可访问的数据限制在视图范围内：
- <b>列级隔离</b>：视图仅暴露允许查看的列，隐藏敏感列。如为教务员建 `v_student_basic(Sno, Sname, Sdept)` 视图，隐藏 Sage、Ssex。
- <b>行级隔离</b>：视图通过 WHERE 子句过滤，仅暴露允许查看的行。如为各院系建 `v_student_cs WHERE Sdept='计算机'`，使各院系只能看本院系学生。
- <b>操作方式</b>：将视图的 SELECT 权限授予用户，而不授予底层基表权限，用户通过视图访问数据，无法看到视图外的数据。

视图是 [[4.3 存取控制]] 的重要补充手段。
</details>

**4.** 简述对称加密与非对称加密的区别，并说明实际系统中如何结合使用。

<details>
<summary>参考答案</summary>
- <b>区别</b>：
  - 对称加密：加密与解密使用同一密钥，速度快，但密钥分发困难。代表算法 AES、DES。
  - 非对称加密：使用公钥/私钥对，公钥加密私钥解密，解决密钥分发问题但速度慢。代表算法 RSA、ECC。
- <b>结合使用</b>（混合加密）：实际系统（如 HTTPS/TLS）先用非对称加密协商一个对称密钥（会话密钥），再用对称密钥加密实际数据。这样既解决了密钥分发问题，又保证了加密速度。

详见 [[4.5 数据加密基础]]。
</details>

---

## 五、分析题（4题）

**1.** 给定表 `Student(Sno, Sname, Ssex, Sage, Sdept)`，DBA 执行以下语句：
```sql
GRANT SELECT ON Student TO U1 WITH GRANT OPTION;
```
随后 U1 登录并执行：
```sql
GRANT SELECT ON Student TO U2;
GRANT SELECT ON Student TO U3;
```
若 DBA 接着执行：
```sql
REVOKE SELECT ON Student FROM U1 CASCADE;
```
分析 U1、U2、U3 各自的权限变化。

<details>
<summary>参考答案</summary>
- <b>U1</b>：失去对 Student 的 SELECT 权限（被回收）。
- <b>U2</b>：失去通过 U1 获得的 SELECT 权限（级联回收）。
- <b>U3</b>：同样失去通过 U1 获得的 SELECT 权限（级联回收）。
- <b>原因</b>：REVOKE 的 CASCADE 选项会连带回收由 U1 转授出去的所有权限，整条传播链失效。
- <b>MySQL 8.0 说明</b>：MySQL 不支持 RESTRICT/CASCADE 关键字，默认行为为级联回收。

详见 [[4.3 存取控制#2.5 权限传播与级联回收]]。
</details>

**2.** 在 MAC 系统中，主体 Alice 的敏感度标记为 (S, {财务, 人事})，客体文件 F1 标记为 (C, {财务})，文件 F2 标记为 (S, {财务, 人事, 研发})。分析 Alice 对 F1、F2 的读、写权限。

<details>
<summary>参考答案</summary>
- <b>F1 (C, {财务})</b>：
  - 读：Alice 密级 S ≥ F1 密级 C ✓；Alice 范畴 {财务,人事} ⊇ {财务} ✓。可读。
  - 写：要求主体密级 ≤ 客体密级。Alice S > F1 C，不满足。不可写。
- <b>F2 (S, {财务, 人事, 研发})</b>：
  - 读：Alice 密级 S = F2 密级 S ✓；但 Alice 范畴 {财务,人事} ⊉ {财务,人事,研发}（缺研发）。不可读。
  - 写：Alice 密级 S = F2 密级 S ✓；Alice 范畴 {财务,人事} ⊆ {财务,人事,研发} ✓。可写。
- <b>结论</b>：Alice 能读 F1，能写 F2，不能写 F1，不能读 F2。

详见 [[4.3 存取控制#3.5 MAC 示例]]。
</details>

**3.** 设计一个视图方案：人事经理能查看员工全部信息，普通员工只能查看本人信息（假设有 `Employee(EmpID, Name, Dept, Salary)` 表，并以 `CURRENT_USER` 表示当前登录用户）。

<details>
<summary>参考答案</summary>
```sql
-- MySQL 8.0，假设已建表 Employee(EmpID, Name, Dept, Salary)
-- 1. 人事经理视图（全部信息）
CREATE VIEW v_emp_all AS
SELECT * FROM Employee;

-- 2. 普通员工视图（仅本人信息）
-- 假设用户名与 EmpID 一致，使用 CURRENT_USER 函数
CREATE VIEW v_emp_self AS
SELECT * FROM Employee WHERE EmpID = REPLACE(CURRENT_USER(), '@localhost', '');

-- 3. 创建用户并分别授权
CREATE USER 'mgr'@'localhost' IDENTIFIED BY 'Mgr@2024';
CREATE USER '202400001'@'localhost' IDENTIFIED BY 'Emp@2024';

GRANT SELECT ON v_emp_all  TO 'mgr'@'localhost';
GRANT SELECT ON v_emp_self TO '202400001'@'localhost';

-- 4. 普通员工登录后
-- SELECT * FROM v_emp_self;  -- 仅看到本人记录
-- SELECT * FROM v_emp_all;  -- 报错：无权限
```
该方案利用视图实现<b>行级权限隔离</b>：不同用户通过不同视图看到不同范围的数据。
</details>

**4.** 统计数据库允许查询"计算机系平均工资"但不允许查"张三的工资"。假设攻击者已知张三是计算机系唯一男性，请设计一种推断攻击，并给出对应的推断控制方法。

<details>
<summary>参考答案</summary>
- <b>推断攻击</b>：
  - 查询1：`SELECT AVG(Salary) FROM Employee WHERE Dept='计算机' AND Sex='男';` —— 返回值即张三工资（因只有张三满足条件）。
  - 攻击者通过一次"看似合法"的统计查询，因查询集合过小（仅1人），直接得到个体数据。
- <b>改进的推断攻击</b>（即使查询集合限制为 ≥2）：
  - 查询1：`SELECT AVG(Salary) FROM Employee WHERE Dept='计算机' AND Sex='男';` —— 返回 m1（包含张三）
  - 查询2：`SELECT AVG(Salary) FROM Employee WHERE Dept='计算机' AND Sex='男' AND EmpID<>'张三';` —— 返回 m2（不包含张三）
  - 若两次集合大小差为 1，则张三工资 = 2×m1 - m2。
- <b>推断控制方法</b>：
  1. 限制查询集合大小（如要求影响行数 ≥ N）；
  2. 限制查询历史（同一用户连续查询的交集不能过小）；
  3. 数据扰动（在统计结果上加随机噪声）。

详见 [[4.5 数据加密基础#四、统计数据库安全]]。
</details>

---

## 六、综合题（2题）

**1.** 某高校教务系统数据库有如下表：
```sql
-- MySQL 8.0，使用 scdb 数据库
USE scdb;
CREATE TABLE Student (Sno CHAR(9) PRIMARY KEY, Sname VARCHAR(20), Ssex CHAR(2), Sage INT, Sdept VARCHAR(20));
CREATE TABLE Course (Cno CHAR(4) PRIMARY KEY, Cname VARCHAR(40), Cpno CHAR(4), Ccredit INT);
CREATE TABLE SC (Sno CHAR(9), Cno CHAR(4), Grade INT, PRIMARY KEY(Sno, Cno));
```
要求：
(1) 创建用户 `u_cs`（计算机系教学秘书）和 `u_student`（普通学生），口令分别为 `Cs@2024`、`Stu@2024`。
(2) 授权 `u_cs` 仅能查看计算机系学生全部信息与选课成绩。
(3) 授权 `u_student` 仅能查看本人基本信息与本人成绩（假设用户名与 Sno 一致）。
(4) 写出回收 `u_cs` 所有权限的 SQL。

<details>
<summary>参考答案</summary>
```sql
-- (1) 创建用户
CREATE USER 'u_cs'@'localhost'      IDENTIFIED BY 'Cs@2024';
CREATE USER 'u_student'@'localhost'  IDENTIFIED BY 'Stu@2024';

-- (2) 为 u_cs 创建视图并授权（仅计算机系学生）
CREATE VIEW v_student_cs AS
SELECT * FROM Student WHERE Sdept = '计算机';
CREATE VIEW v_sc_cs AS
SELECT SC.Sno, SC.Cno, SC.Grade
FROM SC JOIN Student ON SC.Sno = Student.Sno
WHERE Student.Sdept = '计算机';

GRANT SELECT ON v_student_cs TO 'u_cs'@'localhost';
GRANT SELECT ON v_sc_cs     TO 'u_cs'@'localhost';

-- (3) 为 u_student 创建视图并授权（仅本人信息）
-- 假设用户名 'u_student' 对应某具体 Sno，例如 '202400001'
CREATE VIEW v_student_self AS
SELECT * FROM Student WHERE Sno = '202400001';
CREATE VIEW v_sc_self AS
SELECT * FROM SC WHERE Sno = '202400001';

GRANT SELECT ON v_student_self TO 'u_student'@'localhost';
GRANT SELECT ON v_sc_self      TO 'u_student'@'localhost';

-- (4) 回收 u_cs 所有权限
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'u_cs'@'localhost';
-- 或逐对象回收：
REVOKE SELECT ON v_student_cs FROM 'u_cs'@'localhost';
REVOKE SELECT ON v_sc_cs      FROM 'u_cs'@'localhost';
```
<b>设计要点</b>：
- 使用<b>视图</b>实现行级隔离，而非直接授权基表；
- 不授予底层基表 Student、SC 的权限，确保 u_cs 看不到非计算机系学生，u_student 看不到他人信息；
- 回收权限时需回收对应视图的权限。
</details>

**2.** 综合分析：某银行系统需要满足以下安全需求，请分别选用第4章中的何种机制实现，并说明理由。
(a) 客户登录时验证身份，防止冒用；
(b) 普通柜员只能查询本网点客户信息，不能修改账户余额；
(c) 任何对账户表的修改都要可追溯；
(d) 即使数据库备份磁盘被盗，攻击者也无法读取账户数据；
(e) 防止内部员工通过多次"统计查询"推断出某 VIP 客户的资产。

<details>
<summary>参考答案</summary>
- <b>(a) 身份鉴别</b>：使用口令 + 短信验证码的双因素鉴别（[[4.2 身份鉴别]]），确认客户身份。
- <b>(b) 存取控制 + 视图机制</b>：
  - 使用 [[4.3 存取控制]] 的 GRANT 仅授予柜员 SELECT 权限，不授 UPDATE；
  - 进一步用视图（[[4.4 视图机制、审计]]）按网点过滤，实现行级隔离，柜员仅能看本网点客户。
- <b>(c) 审计</b>：开启对账户表的 INSERT/UPDATE/DELETE 审计（[[4.4 视图机制、审计#二、审计]]），记录操作用户、时间、SQL、影响行数，事后可追溯。
- <b>(d) 数据加密</b>：对账户数据使用库内加密（TDE）存储（[[4.5 数据加密基础#三、数据库加密方式]]），即使磁盘被盗也无法解密；备份时同样加密。
- <b>(e) 统计数据库推断控制</b>：对统计查询限制集合大小、限制查询历史，或对统计结果加噪声（[[4.5 数据加密基础#四、统计数据库安全]]），防止推断攻击。
- <b>整体设计</b>：采用纵深防御，从身份鉴别 → 存取控制 → 视图 → 审计 → 加密 → 统计推断控制，构成完整安全防护链。
</details>

---

## 考点统计表

| 题型 | 题数 | 覆盖知识点 | 分值占比（参考） |
| ---- | ---- | ---- | ---- |
| 单选题 | 10 | 安全概述、TCSEC、GRANT/REVOKE、MAC 敏感度标记、视图、审计、加密、统计数据库 | 20% |
| 多选题 | 5 | 安全保护层面、身份鉴别方法、表级权限、DAC/MAC 区别、加密特性 | 15% |
| 判断题 | 5 | 安全性 vs 完整性、WITH GRANT OPTION、MAC 读规则、MySQL 8.0 用户创建、审计性质 | 10% |
| 简答题 | 4 | 安全 vs 完整性、DAC vs MAC、视图机制、对称 vs 非对称加密 | 25% |
| 分析题 | 4 | 级联回收分析、MAC 支配关系、视图设计、推断攻击 | 20% |
| 综合题 | 2 | 综合授权与视图设计、综合安全机制选型 | 10% |
| **合计** | **30** | 第4章全部知识点 | **100%** |

| 知识点 | 涉及题号 | 出现频次 |
| ---- | ---- | ---- |
| 数据库安全概述（CIA、TCSEC） | 单1、单2、单3、多1 | 4 |
| 身份鉴别 | 多2、判断4、综2(a) | 3 |
| GRANT/REVOKE、DAC | 单4、单7、多3、判断2、判断4、分析1、综1 | 7 |
| MAC（敏感度标记、支配关系） | 单5、单6、多4、判断3、分析2、综2 | 6 |
| 视图机制 | 单7、简3、分析3、综1 | 4 |
| 审计 | 单8、判断5、综2(c) | 3 |
| 数据加密 | 单9、多5、简4、综2(d) | 4 |
| 统计数据库 | 单10、分析4、综2(e) | 3 |
| 安全 vs 完整性 | 单1、判断1、简1 | 3 |

## 章节导航

- 上一级：[[MOC - 数据库原理]]
- 本章知识点：[[MOC - 第4章]]
- 上一章习题：[[MOC - 第3章习题]]
- 下一章习题：[[MOC - 第5章习题]]
