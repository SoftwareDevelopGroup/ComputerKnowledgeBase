---
domain: 数据库技术
subject: Oracle数据库管理
type: exercise
chapter: 第5章 用户、权限与角色管理
section: 5.9 习题MOC
tags: [Oracle,习题,DBA,用户,权限,角色,Profile,安全审计,GRANT,REVOKE,CREATE USER]
prerequisites: ["5.1 用户创建、修改、删除", "5.2 系统权限、对象权限", "5.3 角色Role管理与预定义角色", "5.4 资源配置与Profile文件", "5.5 Oracle安全审计基础", "5.6 数据库安全加固与最小权限原则"]
aliases: [MOC - 第5章习题]
---

# MOC - 第5章习题

> [!info] 习题说明
> 本习题集覆盖 [[MOC - 第5章]] 全部知识点，共30题，分六类：单选10、多选5、判断5、简答4、SQL编程4（含CREATE USER完整案例、GRANT/REVOKE链、角色层级、Profile）、综合2（权限合规审计方案设计、安全加固整改案例）。重点考查CREATE USER全子句、DROP USER CASCADE风险、系统权限WITH ADMIN OPTION与对象权限WITH GRANT OPTION回收差异（★考点）、SYSDBA vs SYSOPER对比、三大预定义角色权限范围、Profile口令参数含义、DBA权限最小化案例。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | CREATE USER DEFAULT TABLESPACE | 概念理解 |
| 单2 | 单选 | DROP USER CASCADE影响 | 概念理解 |
| 单3 | 单选 | SYS vs SYSTEM区别 | 概念理解 |
| 单4 | 单选 | WITH ADMIN OPTION vs WITH GRANT OPTION回收差异 | 概念辨析 |
| 单5 | 单选 | SYSDBA可执行SYSOPER不能的操作 | 概念理解 |
| 单6 | 单选 | CONNECT/RESOURCE角色权限（12c+） | 概念理解 |
| 单7 | 单选 | Profile FAILED_LOGIN_ATTEMPTS | 概念理解 |
| 单8 | 单选 | CREATE TABLE权限（自己Schema vs ANY） | 应用分析 |
| 单9 | 单选 | 对象权限列级授予（UPDATE工资列） | 应用分析 |
| 单10 | 单选 | DBA角色 vs SYSDBA管理权限 | 概念辨析 |
| 多1 | 多选 | CREATE USER子句 | 概念辨析 |
| 多2 | 多选 | 对象权限可执行于表的种类 | 概念辨析 |
| 多3 | 多选 | 预定义角色说明 | 概念辨析 |
| 多4 | 多选 | Profile口令安全参数 | 概念辨析 |
| 多5 | 多选 | 统一审计Unified Auditing | 概念辨析 |
| 判1 | 判断 | Oracle 11g+密码大小写敏感 | 概念理解 |
| 判2 | 判断 | WITH ADMIN OPTION系统权限回收级联 | 概念理解 |
| 判3 | 判断 | DBA角色=SYSDBA权限 | 概念理解 |
| 判4 | 判断 | SELECT ANY TABLE可以访问SYS数据字典基表 | 概念理解 |
| 判5 | 判断 | 标准审计写SYS.AUD$无需担心空间 | 概念理解 |
| 简1 | 简答 | SYS/SYSTEM/DBSNMP区别 + SYS必须AS SYSDBA原因 | 分析说明 |
| 简2 | 简答 | WITH ADMIN OPTION/WITH GRANT OPTION授予回收区别表+举例 | 分析说明 |
| 简3 | 简答 | SYSDBA vs SYSOPER权限对比表 | 分析说明 |
| 简4 | 简答 | 最小权限原则定义+5条落地方法 | 分析说明 |
| 编1 | SQL编程 | 创建完整业务用户+授权 | 综合应用 |
| 编2 | SQL编程 | 权限链案例：GRANT/REVOKE链 + 回收结果分析 | 综合应用 |
| 编3 | SQL编程 | 角色层级 + SET ROLE启用密码角色 | 综合应用 |
| 编4 | SQL编程 | 三套Profile模板（DBA/业务/只读）+ 应用用户 | 综合应用 |
| 综1 | 综合 | 合规审计：查出所有违规ANY权限+DBA角色+高危账户 | 综合应用 |
| 综2 | 综合 | 安全整改案例：从裸奔到安全基线完整落地步骤 | 综合应用 |

---

## 一、单选题（每题 2 分，共 10 题）

**1. CREATE USER语句中，如果不显式指定DEFAULT TABLESPACE子句，Oracle 19c默认将用户默认表空间设为（　）。**
A. SYSTEM表空间  
B. TEMP临时表空间  
C. USERS表空间  
D. SYSAUX表空间  

**2. 执行DROP USER hr CASCADE，不会发生的是（　）。**
A. 删除hr用户本身  
B. 删除hr用户Schema下的所有表、索引、视图、序列  
C. 删除引用了hr用户表的其他Schema下的视图  
D. Oracle回收站Flashback Drop不能恢复级联删除的表  

**3. 关于SYS用户与SYSTEM用户，下列说法正确的是（　）。**
A. SYS与SYSTEM都拥有所有数据字典基表，可以直接修改SYS.USER$表  
B. SYS登录必须使用AS SYSDBA身份；SYSTEM默认不能AS SYSDBA，除非显式GRANT SYSDBA  
C. SYS与SYSTEM都推荐日常DBA使用，没有区别  
D. SYS拥有DBA角色，SYSTEM没有DBA角色  

**4. 关于系统权限WITH ADMIN OPTION与对象权限WITH GRANT OPTION的回收，说法正确的是（　）。**
A. 两者回收都自动级联（A→B→C，从A回收，B、C权限一起消失）  
B. 两者回收都不级联（从A回收，B、C权限保留）  
C. 系统权限WITH ADMIN OPTION回收不级联；对象权限WITH GRANT OPTION回收自动级联  
D. 系统权限WITH ADMIN OPTION回收自动级联；对象权限WITH GRANT OPTION回收不级联  

**5. 下列操作中，必须SYSDBA才能执行、SYSOPER不能执行的是（　）。**
A. STARTUP / SHUTDOWN  
B. ALTER DATABASE ARCHIVELOG  
C. CREATE DATABASE 或 ALTER DATABASE OPEN RESETLOGS  
D. RECOVER DATABASE（完全介质恢复）  

**6. Oracle 12c+版本中，CONNECT角色与RESOURCE角色实际包含的权限，说法正确的是（　）。**
A. CONNECT角色 = CREATE SESSION + CREATE TABLE + CREATE VIEW  
B. CONNECT角色仅包含CREATE SESSION一个权限（瘦身）；RESOURCE包含CREATE TABLE/CREATE PROCEDURE等建对象权限；12c+ RESOURCE不再隐含UNLIMITED TABLESPACE系统权限  
C. RESOURCE角色 = DBA角色的子集，包含CREATE ANY TABLE权限  
D. CONNECT + RESOURCE = DBA角色的全部权限  

**7. Profile中设置FAILED_LOGIN_ATTEMPTS=5，PASSWORD_LOCK_TIME=UNLIMITED，对某业务用户意味着（　）。**
A. 连续登录失败5次后账户锁定，5分钟后自动解锁  
B. 连续登录失败5次后账户锁定，必须DBA手动ALTER USER XX ACCOUNT UNLOCK才能解锁  
C. 连续登录失败5次后账户被冻结删除  
D. 登录失败5次后用户密码重置为默认值  

**8. 某开发用户需要在自己Schema中创建订单表ORDER_MAIN，但不允许他在其他Schema中建表。应授予（　）系统权限最合适。**
A. CREATE ANY TABLE  
B. DBA角色  
C. CREATE TABLE（仅自己Schema内建表）+ 对应表空间QUOTA配额  
D. ALTER ANY TABLE  

**9. 人力资源部HR助理需要能修改员工的姓名、电话、邮箱，但绝对不能修改SALARY工资列。最佳的权限配置方案是（　）。**
A. GRANT UPDATE ON hr.employees TO hr_assistant; （然后希望他不要手滑）  
B. GRANT SELECT ON hr.employees TO hr_assistant; 再单独 GRANT UPDATE (first_name, last_name, email, phone_number) ON hr.employees TO hr_assistant; （列级精确授权）  
C. GRANT UPDATE ANY TABLE TO hr_assistant;  
D. 把SYSTEM密码给他  

**10. 关于DBA角色与SYSDBA管理权限，说法错误的是（　）。**
A. 拥有DBA角色的用户登录时不需要写AS SYSDBA，普通登录即可  
B. 拥有SYSDBA管理权限的用户登录后SHOW USER显示为SYS，拥有SYS的所有数据字典权限  
C. DBA角色可以执行STARTUP/SHUTDOWN/CREATE DATABASE等实例级操作  
D. DBA角色包含200+系统权限（ALTER ANY TABLE、DROP USER等），但不包含SYSDBA级的管理权限  

---

## 二、多选题（每题 3 分，共 5 题，多选少选均不得分）

**1. CREATE USER语句中合法有效的子句包括（　）。**
A. IDENTIFIED BY "StrongPass123##"  
B. DEFAULT TABLESPACE users TEMPORARY TABLESPACE temp  
C. QUOTA 500M ON users, QUOTA UNLIMITED ON indx  
D. PROFILE app_user_profile  
E. PASSWORD EXPIRE ACCOUNT LOCK  

**2. 下列关于表对象权限的授予，正确的有（　）。**
A. GRANT SELECT, INSERT, UPDATE, DELETE ON app.order TO app_user;  
B. GRANT UPDATE (first_name, last_name) ON hr.employees TO hr_assistant;  
C. GRANT REFERENCES (order_id) ON app.order TO billing_user;   -- 允许billing_user建外键引用order表  
D. GRANT INDEX ON app.order TO dev_user;  -- 允许dev_user在app.order表上建索引  
E. GRANT CREATE TABLE ON app TO dev_user;  

**3. 关于Oracle预定义角色，下列说法正确的有（　）。**
A. DBA角色几乎拥有除SYSDBA/SYSOPER之外的所有系统权限，严禁授予普通业务用户  
B. SELECT_CATALOG_ROLE角色拥有查询所有DBA_*数据字典视图的权限，适合二线运维只读查看  
C. EXP_FULL_DATABASE / IMP_FULL_DATABASE角色分别是Data Pump导出导入所需的权限集合  
D. PUBLIC角色是每个用户默认拥有的，授予PUBLIC等于授予所有用户（包括未来新建的）  
E. 12c+的Common Role（C##前缀）是CDB根容器创建，跨所有PDB可见的公用角色  

**4. 属于Oracle Profile中口令安全策略类的参数有（　）。**
A. FAILED_LOGIN_ATTEMPTS、PASSWORD_LOCK_TIME  
B. PASSWORD_LIFE_TIME、PASSWORD_GRACE_TIME  
C. SESSIONS_PER_USER、IDLE_TIME  
D. PASSWORD_REUSE_MAX、PASSWORD_REUSE_TIME  
E. PASSWORD_VERIFY_FUNCTION、INACTIVE_ACCOUNT_TIME  

**5. 关于Oracle 12c+统一审计（Unified Auditing），正确的有（　）。**
A. 统一审计所有来源（标准审计+FGA细粒度+RMAN+SYSDBA操作）汇到一张视图UNIFIED_AUDIT_TRAIL中，不需分散查多张表  
B. 默认预定义策略ORA_SECURECONFIG、ORA_LOGON_FAILURES、ORA_ACCOUNT_MGMT、ORA_DATABASE_PARAMETER默认启用  
C. 统一审计默认不记录SYSDBA的操作，需要手动开启  
D. CREATE AUDIT POLICY可以自定义动作+对象+条件的组合策略，比标准审计AUDIT语句功能更强  
E. 纯统一审计模式性能优于标准审计（SGA缓冲区异步写）  

---

## 三、判断题（每题 2 分，共 5 题，对打√错打×）

**1. Oracle 11g R1起，数据库密码默认区分大小写。老应用从10g升级到19c时，如果SEC_CASE_SENSITIVE_LOGON=TRUE，原来小写存储的密码可能登录不上。（　）**

**2. 系统权限GRANT CREATE TABLE TO a WITH ADMIN OPTION; 然后a→b→c级联授予；SYS执行REVOKE CREATE TABLE FROM a; 此时b和c的CREATE TABLE权限也会被自动级联回收。（　）**

**3. 用户拥有DBA角色 = 用户拥有SYSDBA管理权限，日常说"给他DBA"就是授权AS SYSDBA。（　）**

**4. 某个用户同时拥有SELECT ANY TABLE系统权限 + 07_DICTIONARY_ACCESSIBILITY=FALSE参数（默认FALSE），则该用户不能SELECT * FROM SYS.USER$等数据字典基表，只能看DBA_*视图。（　）**

**5. Oracle标准审计（audit_trail=DB,EXTENDED）开启后，SYS.AUD$表存储在SYSTEM表空间中，DBA不用关心空间，会自动循环覆盖旧数据。（　）**

---

## 四、简答题（每题 5 分，共 4 题）

**1. 简述SYS、SYSTEM、DBSNMP三个Oracle预定义账户的定位、身份区别，并解释为什么SYS登录必须使用AS SYSDBA而SYSTEM不需要。**

**2. 以对比表形式列出系统权限WITH ADMIN OPTION与对象权限WITH GRANT OPTION的以下维度：①授予子句写法 ②回收是否级联 ③谁可以REVOKE ④举例场景（A→B→C链）。**

**3. 列出SYSDBA与SYSOPER在以下操作上的权限对比（打√或×，或简述）：①STARTUP/SHUTDOWN ②CREATE DATABASE ③ALTER DATABASE OPEN RESETLOGS ④完全介质恢复RECOVER DATABASE ⑤任意CREATE/DROP ANY TABLE/USER系统权限 ⑥默认连接身份（SHOW USER），并说明两者的典型适用岗位。**

**4. 什么是信息安全中的"最小权限原则（Least Privilege Principle）"？结合Oracle生产运维，至少列举5条落地实践方法（如权限拆解、定期审计、应用白名单等）。**

---

## 五、SQL编程题（每题 8 分，共 4 题，必须写出完整SQL语句）

### 编1：ERP应用用户创建与最小权限授权
企业新上线ERP系统，应用架构如下：
- Schema所有者：ERP_OWNER（拥有所有表、索引、存储过程，建对象权限）
- 应用连接池账户：ERP_APP（只读+增删改业务表，但不能DDL改结构）
- 报表只读账户：ERP_READ（仅查询核心业务表，不能创建任何对象）

要求：
(1) 写出创建上述三个用户的完整CREATE USER语句（19c规范：强密码、USERS默认表空间、TEMP临时表空间、QUOTA配额、PROFILE分别设为dba_strict_profile/app_security_profile/report_profile、PASSWORD EXPIRE）。
(2) 给三个用户分别授予最小权限集合（禁止给ANY/DBA角色）。
(3) 写SQL验证ERP_OWNER能CREATE TABLE、ERP_APP能INSERT/UPDATE但不能DROP TABLE、ERP_READ只能SELECT。

### 编2：权限授予链与回收效果分析
场景与执行顺序：
```sql
-- 步骤1 SYS执行：
GRANT SELECT ON hr.employees TO b WITH GRANT OPTION;
GRANT CREATE TABLE TO c WITH ADMIN OPTION;
-- 步骤2 B登录执行：
GRANT SELECT ON hr.employees TO d;   -- B→D对象权限
-- 步骤3 C登录执行：
GRANT CREATE TABLE TO e;             -- C→E系统权限
```
请问：
(1) 此刻B/C/D/E四个用户各自拥有哪些权限？逐一列出。
(2) 随后SYS执行：
```sql
REVOKE SELECT ON hr.employees FROM b;
REVOKE CREATE TABLE FROM c;
```
此刻B/C/D/E四个用户的上述权限还有哪些保留、哪些被回收？逐一说明并解释原因（核心是系统与对象回收的级联差异）。

### 编3：角色层级设计与SET ROLE
银行系统需要设计三级角色：
- ROLE_TELLER（柜员）：CREATE SESSION + 查询客户表CUSTOMER + 自己的柜员表TRANSACTION增删改
- ROLE_MANAGER（经理）：继承ROLE_TELLER全部权限 + 授权额度审批表APPROVAL增删改 + IDENTIFIED BY "MgrRole2024!"密码保护（日常默认不启用，审批时临时启用）
- ROLE_AUDITOR（审计）：CREATE SESSION + 所有业务表只读SELECT + DBA_AUDIT_TRAIL查询（即SELECT_CATALOG_ROLE）

要求：
(1) 写出创建三个角色+各角色授权的完整SQL（假设业务表Schema是BANK）。
(2) 某用户user_bank同时被授予三个角色，写出他登录后，① 临时启用ROLE_MANAGER执行一笔审批的SQL（密码正确启用）；② 做完审批切回只启用ROLE_TELLER+ROLE_AUDITOR的SQL；③ 查看当前会话所有已启用角色的视图查询。

### 编4：Profile设计与账户锁测试
要求：
(1) 设计三套Profile（参数名+值即可，不用CREATE完整语法）：
- profile_dba：DBA用，FAILED_LOGIN_ATTEMPTS=50，PASSWORD_LOCK_TIME=1/24（1小时自动解），密码60天一换+7天宽限+30天不登录自动锁。
- profile_app_user：业务严格用，失败5次永久锁（UNLIMITED），90天改密码+5次重用禁止。
- profile_report：报表只读，登录失败8次锁1天，密码365天改，宽限14天。
(2) 分别写ALTER USER把SYS/应用user_app/报表user_report应用对应Profile。
(3) 写出SQL：查哪些账户未来7天密码即将过期（从DBA_USERS取username、expiry_date、profile）。
(4) 描述场景：DBA误把profile_app_user应用在SYS上，SYS被锁了，请写出应急解锁步骤（OS认证思路）。

---

## 六、综合题（每题 12 分，共 2 题，需给出完整方案）

### 综1：合规审计 - 违规权限大排查（红蓝对抗前自查）
某等保三级Oracle 19c生产数据库需在对抗前做一次全库违规权限自查，请设计一套可执行的SQL审计方案：

要求至少覆盖6个审计维度（每维度写出1条有效SQL，能直接在SQL窗口执行得到结果）：
(1) **维度1：业务用户拥有高危ANY系统权限**（ANY权限 = 可跨任意Schema操作，必须严查）。查出所有非SYS/SYSTEM/实名DBA白名单用户拥有的%ANY%系统权限，按权限名分组列出。
(2) **维度2：DBA角色违规授予**。查出所有拥有DBA角色但不在白名单（SYS,SYSTEM,DBA01,DBA02）的用户。
(3) **维度3：SYSDBA/SYSOPER管理权限白名单**。V$PWFILE_USERS中除SYS外的用户有哪些，并给出回收命令。
(4) **维度4：PUBLIC角色授予高危UTL包权限**。检查PUBLIC是否被授予UTL_FILE/UTL_HTTP/UTL_SMTP/UTL_TCP（OS交互/SSRF风险），如果有给出REVOKE命令。
(5) **维度5：僵尸账户/开放账户状态异常**。列出账户状态OPEN但超过180天没登录的账户（超过6个月没用的可能是离职员工留下的僵尸）。
(6) **维度6：对象权限越级授予**。查出普通业务用户（非DBA、非Schema Owner）被授予DROP ANY/ALTER ANY/GRANT ANY对象权限的情况。

(7) 最后给出上述6项审计发现问题后，通用的整改闭环4步流程（发现→复核→整改→验证）。

### 综2：安全整改案例 - 从"裸奔"到合规基线
某初创公司Oracle 19c生产库刚从开发环境搬上生产，存在以下已知裸奔问题：
① **密码全是弱口令**：SYS=Oracle123，SYSTEM=manager，所有业务用户=abc123456；② **权限乱给**：应用连接池账户直接给了DBA角色；③ **没有审计**：audit_trail=NONE，审计全关；④ **Profile全是DEFAULT**：FAILED_LOGIN_ATTEMPTS=10（不严）、PASSWORD_LIFE_TIME=UNLIMITED（永不过期）、PASSWORD_VERIFY_FUNCTION=NULL（无复杂度校验）；⑤ **网络裸奔**：监听1521绑定0.0.0.0全网段开放，SQLNET.ORA没有任何IP限制；⑥ **补丁滞后**：19.3版本，19.20+高危CVE补丁没打。

作为刚入职的DBA，请设计一份分三阶段实施的安全整改方案（P0紧急/P1中危/P2优化），每阶段至少包含：
- 阶段目标（完成时间T+N天）
- 具体整改动作（对应的SQL或配置）
- 风险评估与回滚方案
- 验证方式（怎么确认改到位了）

要求覆盖上述6个裸奔问题，全部落地到P0/P1/P2三阶段中（P0=24小时内完成，P1=7天内完成，P2=30天内完成），并给出等保合规完成后的最终状态说明。

---

## 答案与解析

<details>
<summary>单选题答案与解析</summary>

1. **C**。11g+设置了数据库级默认永久表空间为USERS（CREATE DATABASE时默认，或ALTER DATABASE DEFAULT TABLESPACE users修改）。10g及以前才默认SYSTEM（危险）。
2. **C**。CASCADE删除hr用户Schema**自己拥有的**所有对象，其他Schema依赖hr对象的视图/同义词会**标记为INVALID（失效），但不会被物理删除。D正确：Flashback Drop只能恢复单个DROP TABLE，整用户CASCADE时绕过回收站直接删。
3. **B**。A错误：SYSTEM不拥有数据字典基表（基表全是SYS的），也不建议直接修改SYS.USER$这种基表。C错误：SYS只用于SYSDBA级操作，SYSTEM做日常DBA，职责分离。D错误：SYSTEM默认有DBA角色。
4. **C**。系统权限ADMIN OPTION回收不级联，对象GRANT OPTION回收自动级联（★必考，核心区别）。
5. **C**。CREATE DATABASE、DROP DATABASE、ALTER DATABASE OPEN RESETLOGS、不完全恢复等是SYSDBA专属，SYSOPER只能做完全恢复/启装备份/归档切换。
6. **B**。12c+ CONNECT瘦身（只有CREATE SESSION）；RESOURCE不再隐含UNLIMITED TABLESPACE。
7. **B**。UNLIMITED锁就是永久锁，直到DBA手动解锁（最严）。等保合规通常这么配。
8. **C**。CREATE TABLE只在自己Schema内建；CREATE ANY TABLE=任意Schema，风险太高。必须同时给QUOTA，不然建表时ORA-01536。
9. **B**。列级精控是Oracle对象权限的一大特性，最符合最小权限。A方案授权过宽，他可能UPDATE salary=salary*10自己涨工资。
10. **C**。DBA角色没有STARTUP/SHUTDOWN等实例级操作能力（这些是SYSDBA的）。

</details>

<details>
<summary>多选题答案与解析</summary>

1. **ABCDE**。5个都是CREATE USER合法子句，生产创建用户建议子句显式全写，避免默认行为不明确。
2. **ABCD**。E错误：对象权限不能授CREATE TABLE（那是系统权限）。表对象权限是SELECT/INSERT/UPDATE/DELETE/ALTER/INDEX/REFERENCES/FLASHBACK共8个。
3. **ABCDE**。5个全对，DBA角色尤其要强调严禁给普通用户。
4. **ABDE**。C错：SESSIONS_PER_USER/IDLE_TIME是会话资源类（不是口令安全），需要resource_limit=TRUE才生效。
5. **ABDE**。C错：统一审计默认记录SYSDBA操作，且几乎无法关闭，这是合规要求（区别于标准审计需手动开audit_sys_operations=TRUE）。

</details>

<details>
<summary>判断题答案与解析</summary>

1. **√**。11g默认SEC_CASE_SENSITIVE_LOGON=TRUE，密码大小写敏感。升级老库的常见坑。
2. **×**。系统权限WITH ADMIN OPTION回收**不级联**。题中：SYS从C回收CREATE TABLE → C没了，但是E还有（必须显式REVOKE CREATE TABLE FROM e;）。
3. **×**。完全两回事！DBA是一个角色（200+系统权限），普通登录即可；SYSDBA是管理权限，登录时必须AS SYSDBA，能做STARTUP/CREATE DATABASE等DBA角色做不了的事。生产一定要区分开，不能混为一谈。
4. **√**。07_DICTIONARY_ACCESSIBILITY=FALSE（默认值）保证即使拥有SELECT ANY TABLE也看不到SYS的基表（只看得到DBA视图），防止篡改数据字典。参数设TRUE才是危险行为。
5. **×**。AUD$默认在SYSTEM表空间，不清理会膨胀撑爆SYSTEM导致数据库HANG！生产必须：① 迁移到独立AUDIT_TS表空间（DBMS_AUDIT_MGMT）；② 配置自动清理任务（保留6个月）；③ 每月检查表空间使用率。

</details>

<details>
<summary>简答题参考答案</summary>

**1. SYS/SYSTEM/DBSNMP区别：**
| 账户 | 定位 | 拥有什么 | 登录方式 |
| ---- | ---- | ---- | ---- |
| SYS | 超级用户，数据库创造者 | 所有数据字典基表（TAB$/USER$）+所有系统包 | **必须AS SYSDBA**登录（11g+强制）。原因：SYS做的是实例级操作（STARTUP/CREATE DATABASE/RESETLOGS），必须通过密码文件或OS认证验证身份，登录后SHOW USER=SYS，操作会单独记录到AUDIT_SYS审计链。 |
| SYSTEM | 日常DBA管理账户 | DBA角色（200+系统权限），不拥有SYS基表 | 默认普通登录（AS SYSDBA需显式GRANT SYSDBA给SYSTEM才会有） |
| DBSNMP | OEM代理监控账户（12c+） | OEM Agent连接数据库、采集性能指标用的专用账户 | 普通Oracle密码验证，生产保持锁定/合理密码，OEM使用时启用 |

> 总结：SYS管"数据库能不能起来、能不能存在"；SYSTEM管"数据库起来后日常对象、用户、权限管理"；DBSNMP是OEM监控专用。

**2. WITH ADMIN OPTION vs WITH GRANT OPTION对比表：**
| 维度 | 系统权限WITH ADMIN OPTION | 对象权限WITH GRANT OPTION |
| ---- | ---- | ---- |
| 授予子句写法 | GRANT CREATE TABLE TO b **WITH ADMIN OPTION**; | GRANT SELECT ON hr.emp TO b **WITH GRANT OPTION**; |
| 回收是否级联 | ❌ **不级联**。A→B→C：SYS从A回收，B和C权限**保留** | ✅ **自动级联**。A→B→C：A/SYS从B回收，C的权限**自动一起消失** |
| 谁能回收 | 任何拥有GRANT ANY PRIVILEGE的DBA都能从任何用户回收系统权限 | 通常是授予者本人回收（或DBA强制回收） |
| 举例说明结果 | A=SYS, B=dev1, C=dev2<br/>SYS→B(CREATE TABLE, ADMIN)；B→C；SYS从B回收 → C还能建表！需显式REVOKE FROM c; | A=HR，B=HR_MGR，C=HR_ASST<br/>HR→B(SELECT emp, GRANT)；B→C；HR从B回收 → C的SELECT也自动被干掉了 |

**3. SYSDBA vs SYSOPER权限对比表：**
| 操作 | SYSDBA | SYSOPER |
| ---- | ---- | ---- |
| ① STARTUP / SHUTDOWN | ✅ | ✅ |
| ② CREATE DATABASE / DROP DATABASE | ✅ | ❌ |
| ③ ALTER DATABASE OPEN RESETLOGS（不完全恢复后重置日志）| ✅ | ❌ |
| ④ 完全介质恢复 RECOVER DATABASE | ✅ | ✅ |
| ⑤ 不完全恢复（UNTIL TIME / CHANGE / CANCEL）| ✅ | ❌ |
| ⑥ CREATE ANY / DROP ANY TABLE/USER等系统权限 | ✅ 隐含全部 | ❌ |
| ⑦ SYS用户Schema对象（SELECT * FROM SYS.USER$）| ✅ | ❌ |
| ⑧ ALTER SYSTEM 所有参数 | ✅ | 部分（仅归档/切换日志等少数）|
| ⑨ SHOW USER默认身份 | **SYS** | PUBLIC |
| **典型岗位** | 核心DBA/数据库架构师（做版本升级/不完全恢复/建库删库） | 二线运维/NOC值班（启停/备份/归档切换/完全恢复）|

> 权限分离原则：日常启停备份交给SYSOPER即可，SYSDBA只在真正需要时用。

**4. 最小权限原则定义+落地：**
- **定义**：任何用户/程序/进程只能拥有完成其预定业务功能所必需的**最少权限**，绝不额外多给一分。核心是"需要才给、用完就收、定期审计"。
- **落地5条**（任选5条或更多）：
  1. **权限拆解（核心）**：用户申请DBA→DBA反问3问（具体做什么操作？只操作哪些具体对象？持续多久？）→拆成具体系统权限+具体对象权限，不给ANY大权限。
  2. **RESOURCE替代DBA**：开发用户给CONNECT+RESOURCE+特定QUOTA；应用账户只给具体表的增删改查，绝不给CREATE/DROP ANY权限。
  3. **IP白名单+SQLNET**：数据库只允许应用服务器段IP登录，开发IP不能直接上生产，VPN+堡垒机双重验证。
  4. **临时权限到期回收**：项目上线窗口临时给的DROP ANY TABLE权限，上线后24小时内必须回收，写在Change流程里。
  5. **季度权限审计**：跑综1的6个维度SQL，3个月一次大审计+1个月一次小审计，没用到的权限一律收回。
  6. **应用连接账户Schema Owner分离**：Owner只存对象不登录；App账户只DML不DDL；防止应用SQL注入后拿到Owner删表。
  7. **Profile + 审计**：FAILED_LOGIN_ATTEMPTS暴力破解防护+登录失败审计+高危操作审计，溯源追责。
  8. **DBA双权互备**：生产SYSDBA密码双人员掌握，一次操作两人在场（4A系统双人审批）。

</details>

<details>
<summary>SQL编程题参考答案</summary>

**编1：ERP应用用户创建**
```sql
-- (1) 创建三个用户
CREATE USER erp_owner
  IDENTIFIED BY "ErpOwner2024##"
  DEFAULT TABLESPACE users
  TEMPORARY TABLESPACE temp
  QUOTA UNLIMITED ON users
  QUOTA UNLIMITED ON indx
  PROFILE dba_strict_profile
  PASSWORD EXPIRE
  ACCOUNT UNLOCK;

CREATE USER erp_app
  IDENTIFIED BY "ErpApp2024##"
  DEFAULT TABLESPACE users
  TEMPORARY TABLESPACE temp
  QUOTA 0 ON users                       -- 应用池账户不能建对象
  PROFILE app_security_profile
  ACCOUNT UNLOCK;

CREATE USER erp_read
  IDENTIFIED BY "ErpRead2024##"
  DEFAULT TABLESPACE users
  TEMPORARY TABLESPACE temp
  QUOTA 0 ON users
  PROFILE report_profile
  PASSWORD EXPIRE
  ACCOUNT UNLOCK;

-- (2) 最小权限授予
-- ERP_OWNER：建自己Schema对象的权限
GRANT CREATE SESSION TO erp_owner;
GRANT CREATE TABLE, CREATE VIEW, CREATE SEQUENCE, CREATE PROCEDURE,
      CREATE TRIGGER, CREATE TYPE, CREATE SYNONYM TO erp_owner;
-- ERP_OWNER建完表后（假设已经建好了）：
-- ERP_APP：业务DML（具体表授权）
GRANT SELECT, INSERT, UPDATE, DELETE ON erp_owner.sales_order TO erp_app;
GRANT SELECT, INSERT, UPDATE, DELETE ON erp_owner.order_item  TO erp_app;
GRANT SELECT, INSERT, UPDATE, DELETE ON erp_owner.customer    TO erp_app;
-- ERP_READ：只读
GRANT SELECT ON erp_owner.sales_order TO erp_read;
GRANT SELECT ON erp_owner.order_item  TO erp_read;
GRANT SELECT ON erp_owner.customer    TO erp_read;

-- (3) 验证
-- 用ERP_OWNER登录：CREATE TABLE test_t(id INT); -- ✅ 成功
-- 用ERP_APP登录：INSERT INTO erp_owner.customer ... -- ✅；DROP TABLE erp_owner.customer -- ❌ ORA-01031权限不足
-- 用ERP_READ登录：SELECT * FROM erp_owner.customer; -- ✅；INSERT -- ❌ 权限不足
```

**编2：权限链与回收结果**
(1) 回收前（SYS执行完步骤1~3后）各用户权限：
- B：对象权限SELECT ON HR.EMPLOYEES（WITH GRANT OPTION：可以转授）
- C：系统权限CREATE TABLE（WITH ADMIN OPTION：可以转授）
- D：对象权限SELECT ON HR.EMPLOYEES（B授予D的，无转授）
- E：系统权限CREATE TABLE（C授予E的）

(2) SYS执行两次REVOKE后的最终状态：
- B：SELECT ON HR.EMPLOYEES ❌**被回收了**（从B直接回收）
- C：CREATE TABLE ❌**被回收了**（从C直接回收）
- D：SELECT ON HR.EMPLOYEES ❌**也被回收了！**（对象权限WITH GRANT OPTION回收自动级联，B→D链一起断）
- E：CREATE TABLE ✅**仍然保留！**（系统权限WITH ADMIN OPTION回收不级联，SYS从C收不会影响E，必须显式REVOKE CREATE TABLE FROM e;才会没）

**编3：银行角色设计**
```sql
-- (1) 创建角色+授权
-- 柜员角色
CREATE ROLE role_teller NOT IDENTIFIED;
GRANT CREATE SESSION TO role_teller;
GRANT SELECT, INSERT, UPDATE, DELETE ON bank.transaction TO role_teller;
GRANT SELECT ON bank.customer TO role_teller;
-- 经理角色（密码保护）
CREATE ROLE role_manager IDENTIFIED BY "MgrRole2024!";
GRANT role_teller TO role_manager;                 -- 继承柜员全部权限
GRANT SELECT, INSERT, UPDATE, DELETE ON bank.approval TO role_manager;
-- 审计角色
CREATE ROLE role_auditor NOT IDENTIFIED;
GRANT CREATE SESSION TO role_auditor;
GRANT SELECT_CATALOG_ROLE TO role_auditor;          -- DBA_AUDIT_TRAIL等字典视图
-- 自动所有业务表SELECT（假设所有表都是BANK下的，写循环授权）
BEGIN
  FOR rec IN (SELECT table_name FROM dba_tables WHERE owner='BANK') LOOP
    EXECUTE IMMEDIATE 'GRANT SELECT ON bank.' || rec.table_name || ' TO role_auditor';
  END LOOP;
END;
/

-- 授予用户
GRANT role_teller, role_manager, role_auditor TO user_bank;
ALTER USER user_bank DEFAULT ROLE role_teller, role_auditor;  -- 默认不启用密码角色

-- (2) SET ROLE启用密码角色
-- ① 登录后默认role_teller+role_auditor启用，经理审批时临时启用带密码的role_manager：
SET ROLE role_teller IDENTIFIED BY "MgrRole2024!", role_auditor, role_manager IDENTIFIED BY "MgrRole2024!";
-- ② 做完审批切回只读
SET ROLE role_teller, role_auditor;
-- ③ 查看会话当前启用角色
SELECT * FROM session_roles ORDER BY 1;
```

**编4：Profile设计**
```sql
-- (1) 三套Profile参数
-- profile_dba：
FAILED_LOGIN_ATTEMPTS = 50, PASSWORD_LOCK_TIME = 1/24, PASSWORD_LIFE_TIME = 60,
PASSWORD_GRACE_TIME = 7, PASSWORD_REUSE_TIME = 365, PASSWORD_REUSE_MAX = 10,
PASSWORD_VERIFY_FUNCTION = VERIFY_FUNCTION_11G, INACTIVE_ACCOUNT_TIME = 30;
-- profile_app_user：
FAILED_LOGIN_ATTEMPTS = 5, PASSWORD_LOCK_TIME = UNLIMITED, PASSWORD_LIFE_TIME = 90,
PASSWORD_GRACE_TIME = 7, PASSWORD_REUSE_MAX = 5,
PASSWORD_VERIFY_FUNCTION = VERIFY_FUNCTION_11G;
-- profile_report：
FAILED_LOGIN_ATTEMPTS = 8, PASSWORD_LOCK_TIME = 1, PASSWORD_LIFE_TIME = 365,
PASSWORD_GRACE_TIME = 14, PASSWORD_VERIFY_FUNCTION = DEFAULT;

-- (2) 应用Profile
ALTER USER sys       PROFILE profile_dba;
ALTER USER user_app  PROFILE profile_app_user;
ALTER USER user_report PROFILE profile_report;

-- (3) 7天内过期账户
SELECT username, account_status, TRUNC(expiry_date - SYSDATE) days_left, profile
  FROM dba_users
 WHERE expiry_date IS NOT NULL AND account_status = 'OPEN'
   AND expiry_date BETWEEN SYSDATE AND SYSDATE + 7
 ORDER BY expiry_date;

-- (4) 应急解锁SYS（SYS被锁）
-- OS层面：确保Oracle用户属于dba组（Linux）/ORA_DBA组（Windows）
-- SQLNET.ORA：SQLNET.AUTHENTICATION_SERVICES=(ALL) -- Linux / (NTS) -- Windows
-- $ sqlplus / as sysdba    -- 走OS认证登录成功（不需要数据库验证密码，所以不会被锁）
-- SQL> ALTER USER sys ACCOUNT UNLOCK IDENTIFIED BY "新的强密码";
-- SQL> ALTER USER sys PROFILE profile_dba;  -- 确保SYS回到宽松Profile，不再被误锁
```

</details>

<details>
<summary>综合题参考答案（核心要点+关键SQL）</summary>

**综1：合规审计6维度SQL**
```sql
-- 维度1：业务用户高危ANY系统权限
SELECT sp.grantee, sp.privilege, sp.admin_option
  FROM dba_sys_privs sp
 WHERE sp.privilege LIKE '%ANY%'
   AND sp.grantee IN (SELECT username FROM dba_users
                       WHERE account_status='OPEN'
                         AND username NOT IN ('SYS','SYSTEM','DBA01','DBA02'))
 ORDER BY sp.privilege, sp.grantee;

-- 维度2：DBA角色违规（非白名单用户）
SELECT rp.grantee, rp.granted_role, rp.admin_option
  FROM dba_role_privs rp
 WHERE rp.granted_role = 'DBA'
   AND rp.grantee NOT IN ('SYS','SYSTEM','DBA01','DBA02');

-- 维度3：SYSDBA/SYSOPER管理权限白名单
SELECT username, sysdba, sysoper FROM v$pwfile_users;
-- 若有白名单外用户，回收：REVOKE sysdba FROM former_dba;

-- 维度4：PUBLIC高危UTL包
SELECT tp.owner, tp.table_name, tp.privilege
  FROM dba_tab_privs tp
 WHERE tp.grantee = 'PUBLIC'
   AND tp.table_name IN ('UTL_FILE','UTL_HTTP','UTL_SMTP','UTL_TCP','UTL_INADDR');
-- REVOKE示例：REVOKE EXECUTE ON utl_http FROM PUBLIC; -- 执行前评估应用是否真的需要

-- 维度5：僵尸账户180天没登录
SELECT username, account_status, created, last_login, TRUNC(SYSDATE - last_login) days_since_login
  FROM dba_users
 WHERE account_status = 'OPEN'
   AND last_login IS NOT NULL
   AND SYSDATE - last_login > 180
 ORDER BY days_since_login DESC;

-- 维度6：对象权限越级
SELECT tp.grantee, tp.owner schema_owner, tp.table_name, tp.privilege, tp.grantable
  FROM dba_tab_privs tp
 WHERE tp.privilege IN ('ALTER','DROP ANY','INDEX')      -- 越权类
   AND tp.grantee NOT IN (SELECT rp.granted_role FROM dba_roles)  -- 非角色
   AND tp.grantee NOT IN ('SYS','SYSTEM');
```

整改闭环4步：①发现（上述SQL跑一次存到审计表+截图）→②复核（通知业务/安全部门二次确认，避免误杀）→③整改（REVOKE/ALTER USER/加白名单，生产变更流程）→④验证（次日再跑一遍相同SQL确认问题消失+回归业务测试验证无影响）。最后归档留痕（等保检查要审计记录）。

**综2：三阶段安全整改方案（要点）**

**P0阶段（24小时内必须完成，高危阻断）**
| 动作 | 整改内容 | 风险/回滚 | 验证 |
| ---- | ---- | ---- | ---- |
| ① 立即改弱密码 | `ALTER USER sys IDENTIFIED BY "<随机32位强密码>";` 全库改SYS/SYSTEM/业务用户密码，保存到4A系统 | 风险：应用配置文件旧密码连接报错ORA-1017<br/>回滚：`ALTER USER ... IDENTIFIED BY 旧密码` | 逐台应用服务器配置改新密码；`sqlplus sys/新密码 as sysdba` 登录成功 |
| ② 立即紧急回收应用DBA | `REVOKE dba FROM app_user;` → 最小授予：`GRANT CREATE SESSION, SELECT/INSERT/UPDATE/DELETE ON app_owner.* TO app_user;` （循环授权） | 风险：应用用到了DBA里的CREATE ANY TABLE（违规）会报错<br/>回滚：`GRANT dba TO app_user;`（紧急恢复后后续整改） | 应用冒烟测试通过；维度1+维度2SQL验证不再出现app_user在违规列表 |
| ⑤ 立即关闭公网监听IP | listener.ora: ADDRESS=(PROTOCOL=TCP)(HOST=内网应用段IP)(PORT=1521) → 不要0.0.0.0；加SQLNET.ORA TCP.VALIDNODE_CHECKING=YES + TCP.INVITED_NODES=(应用服务器IP列表) | 风险：误配会导致业务连不上库<br/>回滚：改回0.0.0.0 | `tnsping`从应用服务器通；从外网/开发PC机tnsping不通 |

**P1阶段（7天完成，中危整改）**
| 动作 | 整改内容 |
| ---- | ---- |
| ③ 立即开启统一审计 | `ALTER SYSTEM SET audit_trail=NONE scope=spfile;`（19c混合模式，统一审计默认已启）→ 确认预定义策略：`SELECT * FROM audit_unified_enabled_policies;` → 自定义2个策略：CREATE AUDIT POLICY drop_audit ACTIONS DROP TABLE, TRUNCATE TABLE; AUDIT POLICY drop_audit; / AUDIT ROLE dba;（所有拥有DBA的人操作全记） |
| ④ Profile严格化 | 执行编4的三套Profile（dba/app_user/report）→ 应用DEFAULT Profile ALTER PROFILE default LIMIT FAILED_LOGIN_ATTEMPTS=5 PASSWORD_LOCK_TIME=UNLIMITED PASSWORD_VERIFY_FUNCTION=VERIFY_FUNCTION_11G; → 执行@$ORACLE_HOME/rdbms/admin/utlpwdmg.sql装复杂度函数 |
| ⑥ 补丁窗口打RU | 提前2天在测试环境验证19.20+ RU不影响业务 → 生产低峰期滚动打补丁（RAC滚动，单实例重启）：`opatch apply 12345678` → 运行`$ORACLE_HOME/rdbms/admin/catbundle.sql`应用SQL补丁 |

验证：维度3审计6项全绿；Profile SQL查询FAILED_LOGIN_ATTEMPTS=5对非DBA；opatch lsinventory显示RU已安装。

**P2阶段（30天内完成，优化加固）**
- TCPS TLS传输加密（sqlnet.ora加密，防止抓包）
- 堡垒机+4A系统：所有DBA通过堡垒机登录，全程录像；密码自动改密
- 细粒度审计FGA：SELECT SALARY列审计、DELETE核心业务表审计
- Flashback Data Archive核心表、动态数据脱敏Redaction
- 季度自动化审计：把综1的6个维度SQL写成脚本+定时邮件报告

**最终合规状态：** 等保2.0三级60+项控制项全部通过；统一审计保留≥6个月；高危ANY权限/DBA角色0违规；密码90天换+复杂度强制+5次错锁定；IP白名单应用段限定；Oracle季度RU保持在N-2范围内。

</details>

---

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | CREATE USER默认表空间、DROP USER CASCADE、SYS/SYSTEM区别、ADMIN vs GRANT回收差异、SYSDBA专属操作、12c+角色变化、Profile锁定效果、CREATE TABLE权限、列级授权、DBA vs SYSDBA |
| 多选 | 5 | 15 | CREATE USER子句、表对象权限9种、预定义角色5类、Profile口令参数、统一审计5条特性 |
| 判断 | 5 | 10 | 密码大小写敏感、WITH ADMIN不级联、DBA≠SYSDBA、07_DICTIONARY_ACCESSIBILITY保护、SYS.AUD$空间陷阱 |
| 简答 | 4 | 20 | 3个预定义账户+AS SYSDBA原因、WITH ADMIN/GRANT对比表、SYSDBA/SYSOPER 9项对比、最小权限5条落地 |
| 编程 | 4 | 32 | ERP三用户最小权限创建授权、权限级联回收结果分析（★必考）、银行3级角色+SET ROLE密码角色、3套Profile参数+SYS被锁应急步骤 |
| 综合 | 2 | 24 | 6个维度合规审计SQL+整改闭环、P0/P1/P2三阶段安全整改落地（6个裸奔问题全覆盖） |
| **合计** | 30 | 121 | 覆盖第5章全部考点，重ADMIN vs GRANT回收差异（★必考）+最小权限原则落地+安全加固方案 |

## 章节导航

- 上级MOC：[[MOC - Oracle数据库管理]]
- 本章知识点：[[MOC - 第5章]]（[[5.1 用户创建、修改、删除]]、[[5.2 系统权限、对象权限]]、[[5.3 角色Role管理与预定义角色]]、[[5.4 资源配置与Profile文件]]、[[5.5 Oracle安全审计基础]]、[[5.6 数据库安全加固与最小权限原则]]）
- 上一章习题：[[MOC - 第4章习题]]
- 下一章习题：[[MOC - 第6章习题]]
