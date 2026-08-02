---
domain: 数据库技术
subject: 数据库开发技术
type: exercise
chapter: 第7章 数据库安全与部署
section: 第7章综合习题
tags: [数据库开发,习题,SQL注入,权限管理,备份恢复,主从复制,安全部署]
prerequisites: []
---

第7章习题覆盖 SQL 注入类型与防范、PreparedStatement 防护、用户管理（CREATE USER）、权限管理（GRANT/REVOKE）、角色管理、备份类型（全量/增量/差异）、mysqldump、binlog 与 PITR、主从复制，重点考查安全与部署综合分析能力。配套知识点见 [[MOC - 第7章]]。本章基于 MySQL 8.0。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | SQL 注入本质 | 概念理解 |
| 单2 | 单选 | 联合查询注入 | 概念理解 |
| 单3 | 单选 | 时间盲注 | 概念理解 |
| 单4 | 单选 | 参数化防注入原理 | 概念理解 |
| 单5 | 单选 | MySQL 账户命名 | 概念理解 |
| 单6 | 单选 | CREATE USER 推荐 | 概念理解 |
| 单7 | 单选 | GRANT OPTION 风险 | 概念理解 |
| 单8 | 单选 | 最小权限原则 | 概念理解 |
| 单9 | 单选 | 增量 vs 差异备份 | 概念理解 |
| 单10 | 单选 | --single-transaction 原理 | 概念理解 |
| 多1 | 多选 | SQL 注入类型 | 概念辨析 |
| 多2 | 多选 | SQL 注入防范措施 | 概念辨析 |
| 多3 | 多选 | 权限层级 | 概念辨析 |
| 多4 | 多选 | 备份类型 | 概念辨析 |
| 多5 | 多选 | 主从复制组件 | 概念辨析 |
| 判1 | 判断 | 黑名单防注入可靠 | 概念理解 |
| 判2 | 判断 | ${} 有注入风险 | 概念理解 |
| 判3 | 判断 | root 连接应用 | 概念理解 |
| 判4 | 判断 | 主从复制替代备份 | 概念理解 |
| 判5 | 判断 | 未演练备份等于没备份 | 概念理解 |
| 简1 | 简答 | SQL 注入四种类型 | 分析说明 |
| 简2 | 简答 | 最小权限原则落地 | 分析说明 |
| 简3 | 简答 | 备份类型与方式 | 分析说明 |
| 简4 | 简答 | PITR 恢复步骤 | 分析说明 |
| 分1 | 分析 | 注入攻击分析 | 综合应用 |
| 分2 | 分析 | 权限配置分析 | 综合应用 |
| 分3 | 分析 | 误删恢复分析 | 综合应用 |
| 分4 | 分析 | 主从复制延迟分析 | 综合应用 |
| 综1 | 综合 | 注入漏洞多层防御 | 综合应用 |
| 综2 | 综合 | 备份恢复策略设计 | 综合应用 |

## 一、单选题（每题 2 分，共 10 题）

**1. SQL 注入的本质是（　）。**
A. 数据库未开启加密
B. 应用把用户输入直接拼接进 SQL 文本，DBMS 无法区分数据与代码
C. 网络传输被窃听
D. 密码强度不够

**2. 利用 `UNION` 把攻击者查询结果拼到原查询返回中，直接读取其他表的注入类型是（　）。**
A. 布尔盲注
B. 联合查询注入（Union-based）
C. 时间盲注
D. 堆叠注入

**3. 攻击者用 `SLEEP()` 等延时函数，通过响应时间判断条件真假的注入类型是（　）。**
A. 联合查询注入
B. 布尔盲注
C. 时间盲注（Time-based Blind）
D. 堆叠注入

**4. 参数化查询防止 SQL 注入的原理是（　）。**
A. 自动过滤特殊字符
B. SQL 文本与参数分别发送，DBMS 把参数值仅作字面量绑定，不解析为 SQL 语法
C. 加密传输参数
D. 限制 SQL 长度

**5. MySQL 账户由什么唯一标识（　）。**
A. 仅用户名
B. 用户名 + 主机（user@host）
C. 仅主机
D. 端口号

**6. MySQL 8.0 推荐的创建用户方式是（　）。**
A. 用 GRANT 隐式创建
B. 用 CREATE USER 显式创建
C. 直接修改 mysql.user 表
D. 用 INSERT 语句

**7. 关于 `GRANT OPTION`，下列说法正确的是（　）。**
A. 允许被授权者把自身权限再授予他人，等于扩散权限，普通应用账户不应拥有
B. 只授予查询权限
C. 自动创建用户
D. 无风险

**8. 最小权限原则是指（　）。**
A. 账户只授予完成其职责所必需的最小权限，且仅授予必需时长
B. 所有账户都授予 ALL
C. 只用 root 账户
D. 不授予任何权限

**9. 关于增量备份与差异备份，下列说法正确的是（　）。**
A. 差异备份只备份自上次任意备份以来的变化
B. 增量备份只备份自上次全量以来的变化
C. 增量备份空间小速度快，但恢复需链式回放；差异恢复只需全量+最近一次差异
D. 二者完全相同

**10. `mysqldump --single-transaction` 实现一致性备份的原理是（　）。**
A. 锁全表
B. 利用 InnoDB MVCC 取一致性快照，备份期间不锁表
C. 关闭数据库
D. 删除索引

## 二、多选题（每题 3 分，共 5 题）

**1. SQL 注入的主要类型包括（　）。**
A. 联合查询注入（Union-based）
B. 布尔盲注（Boolean-based Blind）
C. 时间盲注（Time-based Blind）
D. 堆叠注入（Stacked Queries）

**2. 防范 SQL 注入的措施包括（　）。**
A. 参数化查询（核心防线）
B. 输入验证与白名单校验
C. 最小权限账户
D. WAF（Web 应用防火墙）作为补充防线

**3. MySQL 权限层级包括（　）。**
A. 全局级 `*.*`
B. 数据库级 `db.*`
C. 表级 `db.table`
D. 列级 `db.table(col)`

**4. 备份类型包括（　）。**
A. 全量备份 Full
B. 增量备份 Incremental
C. 差异备份 Differential
D. 只读备份

**5. MySQL 主从复制的组件包括（　）。**
A. 主库 binlog
B. 从库 IO 线程拉取到 relay log
C. 从库 SQL 线程重放
D. 从库只读查询

## 三、判断题（每题 2 分，共 5 题）

**1. 依赖黑名单/正则过滤可以有效防止所有 SQL 注入，是可靠的安全措施。**

**2. MyBatis 的 `${}` 是字符串拼接，有注入风险，应优先使用 `#{}`。**

**3. 应用程序应使用 root 账户连接数据库以获得最大便利。**

**4. 主从复制可以替代备份，从库能保留所有历史数据。**

**5. 未演练的备份等于没有备份，必须定期在隔离环境执行真实恢复演练。**

## 四、简答题（每题 5 分，共 4 题）

**1. 说明 SQL 注入的四种主要类型及其原理。**

**2. 列出最小权限原则的 5 条落地要点。**

**3. 比较全量、增量、差异备份的含义与特点。**

**4. 描述基于 binlog 的时间点恢复（PITR）步骤。**

## 五、分析题（每题 6 分，共 4 题）

**1. 注入攻击分析。** 某登录接口拼接 SQL：`SELECT * FROM user WHERE name = '{输入}'`。攻击者输入 `admin' --`。分析注入后果，并给出基于 PreparedStatement 的修复方案。

**2. 权限配置分析。** 某应用使用 `root` 账户连接数据库，且授予应用账户 `ALL PRIVILEGES ON *.*` 与 `GRANT OPTION`。指出三处问题，并给出符合最小权限原则的改进方案（含 CREATE USER 与 GRANT 语句）。

**3. 误删恢复分析。** 某运维人员在 2024-06-01 15:00 误执行 `DROP TABLE orders`。已知有全量备份（含 `--master-data=2`）与 binlog。给出恢复到误删前一刻（14:59）的步骤。

**4. 主从复制延迟分析。** 某从库 `SHOW REPLICA STATUS` 显示 `Seconds_Behind_Master` 持续增大，读业务读到旧数据。分析延迟的可能原因，并给出至少 3 条缓解建议。

## 六、综合题（每题 8 分，共 2 题）

**1. 注入漏洞多层防御。** 某电商系统商品查询接口存在拼接 SQL 漏洞，且使用 root 连接。要求设计多层防御：**
- **(1)** 写出 PreparedStatement 修复代码；
- **(2)** 对动态 ORDER BY 字段给出白名单校验代码；
- **(3)** 设计符合最小权限的应用账户（CREATE USER + GRANT，仅业务库 CRUD）；
- **(4)** 补充非代码层面的两道防线（WAF、备份）。

**2. 备份恢复策略设计。** 某金融系统数据库约 500GB，要求 RPO（数据丢失容忍）≤ 5 分钟，RTO（恢复时间目标）≤ 2 小时。要求：**
- **(1)** 设计备份策略（全量/增量频率、binlog、保留周期、存储位置）；
- **(2)** 写出 mysqldump 一致性全量备份命令（含 --single-transaction、--master-data=2）；
- **(3)** 写出主库创建复制账户的最小权限语句；
- **(4)** 说明为何主从复制不能替代备份，以及定期演练的必要性。

## 答案与解析

<details>
<summary>单选题答案</summary>

1. **B**。SQL 注入本质是"数据与代码未分离"，应用拼接用户输入，DBMS 无法区分 SQL 语法与字面量。
2. **B**。联合查询注入利用 UNION 把攻击者查询拼到原查询返回中。
3. **C**。时间盲注用 SLEEP() 通过响应时间判断条件真假。
4. **B**。参数化查询 SQL 文本与参数分别发送，参数值仅作字面量绑定。
5. **B**。MySQL 账户由 user@host 唯一标识。
6. **B**。MySQL 8.0 推荐用 CREATE USER 显式创建，而非 GRANT 隐式。
7. **A**。GRANT OPTION 允许被授权者再授权，扩散权限，普通应用账户不应拥有。
8. **A**。最小权限原则：账户只授予完成职责必需的最小权限，且仅授予必需时长。
9. **C**。增量备份空间小但恢复需链式回放；差异恢复只需全量+最近一次差异。
10. **B**。--single-transaction 利用 InnoDB MVCC 取一致性快照，不锁表（仅 InnoDB 有效）。

</details>

<details>
<summary>多选题答案</summary>

1. **ABCD**。四种注入类型：联合查询、布尔盲注、时间盲注、堆叠注入。
2. **ABCD**。参数化、输入校验、最小权限、WAF 均为防范措施。
3. **ABCD**。四级权限：全局、数据库、表、列。
4. **ABC**。全量、增量、差异；"只读备份"非备份类型。
5. **ABCD**。主库 binlog、从库 IO 线程拉 relay log、SQL 线程重放、从库只读查询均为复制组件。

</details>

<details>
<summary>判断题答案</summary>

1. **×**。黑名单/正则过滤难以覆盖所有注入向量（编码、注释、二次注入），不可靠，应永远用参数化查询。
2. **√**。`#{}` 参数化防注入优先用；`${}` 拼接有风险，仅用于标识符且须白名单。
3. **×**。root 拥有 ALL，被注入等于数据库沦陷，应用不应使用 root 连接。
4. **×**。主从复制不能替代备份：误删表会通过 binlog 同步到从库，从库也被删。
5. **√**。未演练的备份可能因格式/版本/权限/损坏无法恢复，必须定期演练。

</details>

<details>
<summary>简答题答案</summary>

**1. SQL 注入四种类型：**
- 联合查询注入：用 UNION 拼接攻击者查询读取其他表。
- 布尔盲注：根据查询真假返回不同内容，用 AND 1=1/1=2 逐字符猜解。
- 时间盲注：无回显差异，用 SLEEP() 通过响应时间判断真假。
- 堆叠注入：用 `;` 一次执行多条 SQL，直接 INSERT/UPDATE/DELETE。

**2. 最小权限落地 5 条：**
1. 应用账户与 DBA 账户分离，DDL 用独立 DBA 账户审计执行；
2. 读写分离账户，读副本只授 SELECT；
3. 限定主机（`'app'@'10.0.0.5'` 而非 `'%'`）；
4. 定期审计 `SHOW GRANTS` 检查并回收冗余权限；
5. 不用 root 连应用。

**3. 备份类型：**
| 类型 | 含义 | 特点 |
| ---- | ---- | ---- |
| 全量 | 完整复制所有数据 | 恢复最简单，耗时空间大 |
| 增量 | 自上次任意备份以来的变化 | 空间小快，恢复需链式回放 |
| 差异 | 自上次全量以来的变化 | 恢复需全量+最近一次差异，介于二者 |

**4. PITR 步骤：**
1. 恢复最近全量备份（备份注释含 binlog 位点）；
2. 用 `mysqlbinlog --start-position=<位点> --stop-datetime=<误操作前>` 重放 binlog；
3. 验证数据后恢复服务。
关键：`--stop-datetime` 必须精确到误操作前；binlog 未被清理；建议先测试库演练。

</details>

<details>
<summary>分析题答案</summary>

**1. 注入攻击分析：** 输入 `admin' --`，拼接后 SQL 为 `SELECT * FROM user WHERE name = 'admin' --'`，`--` 后注释掉密码校验，绕过认证以 admin 登录。
**修复：**
```java
String sql = "SELECT id, name FROM user WHERE name = ?";
try (PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setString(1, request.getParameter("name"));
    try (ResultSet rs = ps.executeQuery()) { /* ... */ }
}
```
参数值仅作字面量，`'`、`--` 不改变 SQL 结构。

**2. 权限配置分析：** 三处问题：①用 root 连接应用——被注入等于数据库沦陷；②应用账户 `ALL PRIVILEGES ON *.*`——权限过大；③`GRANT OPTION`——可扩散权限。
**改进：**
```sql
-- 创建应用账户，限定主机
CREATE USER 'app_user'@'10.0.%.%' IDENTIFIED BY 'StrongPass!2024';
-- 仅授予业务库表的 CRUD
GRANT SELECT, INSERT, UPDATE, DELETE ON shopdb.* TO 'app_user'@'10.0.%.%';
-- 不授予 GRANT OPTION、不授予 ALL、不用 root
```

**3. 误删恢复分析：** 步骤：
1. 恢复最近全量备份：`mysql -uroot -p shopdb < shopdb_full.sql`（备份注释含位点 `MASTER_LOG_FILE='mysql-bin.000010', MASTER_LOG_POS=154`）；
2. 用 mysqlbinlog 重放到误删前：
```bash
mysqlbinlog --start-position=154 --stop-datetime='2024-06-01 14:59:00' \
    /var/log/mysql/mysql-bin.000010 /var/log/mysql/mysql-bin.000011 \
    | mysql -uroot -p shopdb
```
3. 验证 orders 表数据后恢复服务。
关键：`--stop-datetime` 精确到误删前；先测试库演练确认位点。

**4. 主从复制延迟分析：** 原因：①大事务/长事务，binlog 顺序传输单线程重放；②网络抖动；③从库 SQL 线程单线程重放（MySQL 8.0 可开多线程复制）。
**缓解建议：**
1. 避免大事务，拆分批量操作；
2. 开启从库多线程复制（`slave_parallel_workers`）；
3. 读业务对延迟容忍度评估，关键读走主库；
4. 监控 `Seconds_Behind_Master` 告警。

</details>

<details>
<summary>综合题答案</summary>

**1. 注入漏洞多层防御：**

**(1)** PreparedStatement 修复：
```java
String sql = "SELECT id, name, price FROM product WHERE name = ?";
try (PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setString(1, request.getParameter("name"));
    try (ResultSet rs = ps.executeQuery()) { /* ... */ }
}
```

**(2)** 动态 ORDER BY 白名单校验：
```java
Set<String> allowed = Set.of("id", "name", "created_at");
String orderBy = request.getParameter("orderBy");
if (!allowed.contains(orderBy)) {
    throw new IllegalArgumentException("非法排序字段");
}
String sql = "SELECT id, name FROM product ORDER BY " + orderBy + " LIMIT ?";
try (PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setInt(1, 10);
    // ...
}
```

**(3)** 最小权限应用账户：
```sql
CREATE USER 'app_user'@'10.0.%.%' IDENTIFIED BY 'StrongPass!2024';
GRANT SELECT, INSERT, UPDATE, DELETE ON shopdb.* TO 'app_user'@'10.0.%.%';
-- 不授予 ALL、GRANT OPTION、DROP、CREATE
```

**(4)** 非代码防线：
- WAF：在 HTTP 层拦截 `UNION SELECT`、`OR 1=1` 等注入特征，作为补充；
- 备份：定期全量+binlog，被注入后可恢复兜底；密码用 bcrypt 加盐哈希存储。

**2. 备份恢复策略设计：**

**(1)** 备份策略：
- 全量备份：每日凌晨一次（500GB 可用 xtrabackup 物理备份提速）；
- 增量：binlog 持续记录（满足 RPO≤5 分钟）；
- 保留：全量 4 周，binlog 7~30 天，长期归档按合规；
- 存储：本地 + 异地（云对象存储），防单点；
- 演练：每季度真实恢复演练。

**(2)** mysqldump 一致性全量备份：
```bash
mysqldump -uroot -p --single-transaction --master-data=2 --routines --triggers shopdb > shopdb_full.sql
# --single-transaction: InnoDB MVCC 一致性快照不锁表
# --master-data=2: 注释记录 binlog 位点用于 PITR
```

**(3)** 主库创建复制账户（最小权限 REPLICATION SLAVE）：
```sql
CREATE USER 'repl'@'10.0.0.2' IDENTIFIED BY 'ReplPass!2024';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'10.0.0.2';
```

**(4)** 主从复制不能替代备份：误删表会通过 binlog 同步到从库，从库也被删，无法恢复误删数据。定期演练必要性：备份可能因格式、版本、权限、损坏无法恢复，必须定期在隔离环境执行真实恢复演练并验证数据完整性，确保 RTO≤2 小时可达成。

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | 注入本质/类型、参数化、账户、最小权限、备份类型、--single-transaction |
| 多选 | 5 | 15 | 注入类型、防范措施、权限层级、备份类型、复制组件 |
| 判断 | 5 | 10 | 黑名单、${}、root、复制替代备份、演练 |
| 简答 | 4 | 20 | 注入类型、最小权限、备份类型、PITR |
| 分析 | 4 | 24 | 注入攻击、权限配置、误删恢复、复制延迟 |
| 综合 | 2 | 16 | 多层防御、备份策略设计 |
| 合计 | 30 | 105 | 覆盖第7章安全与部署全部主题 |

## 导航

- 上级 MOC：[[MOC - 数据库开发技术]]、[[MOC - 第7章]]
- 本章知识点：[[7.1 SQL注入防范]]、[[7.2 用户权限管理]]、[[7.3 备份恢复策略]]
- 上一章习题：[[MOC - 第6章习题]]
