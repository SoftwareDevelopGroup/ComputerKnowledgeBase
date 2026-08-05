---
domain: 数据库技术
subject: 数据库开发技术
type: exercise
chapter: 第4章 数据库访问接口
section: 第4章综合习题
tags: [数据库开发,习题,JDBC,ODBC,连接池,参数化查询,SQL注入]
prerequisites: []
---

第4章习题覆盖 ODBC/JDBC 架构与 API、JDBC 六步骤、连接池原理（Druid/HikariCP）、连接池参数配置、参数化查询（PreparedStatement）与 SQL 注入防范，重点考查完整 JDBC 代码编写能力。配套知识点见 [[MOC - 第4章]]。本章基于 JDK 17 + MySQL Connector/J 8.x。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | JDBC 加载驱动 | 概念理解 |
| 单2 | 单选 | JDBC 操作六步骤顺序 | 概念理解 |
| 单3 | 单选 | Statement vs PreparedStatement | 概念理解 |
| 单4 | 单选 | PreparedStatement 防注入原理 | 概念理解 |
| 单5 | 单选 | 连接池 close 语义 | 概念理解 |
| 单6 | 单选 | HikariCP 定位 | 概念理解 |
| 单7 | 单选 | maximumPoolSize 调优 | 概念理解 |
| 单8 | 单选 | maxLifetime 与 wait_timeout | 概念理解 |
| 单9 | 单选 | ODBC DSN 作用 | 概念理解 |
| 单10 | 单选 | 占位符不能用于标识符 | 概念理解 |
| 多1 | 多选 | JDBC 核心 API | 概念辨析 |
| 多2 | 多选 | 连接池优点 | 概念辨析 |
| 多3 | 多选 | PreparedStatement 性能优势前提 | 概念辨析 |
| 多4 | 多选 | 常见连接池 | 概念辨析 |
| 多5 | 多选 | SQL 注入防范措施 | 概念辨析 |
| 判1 | 判断 | try-with-resources 关闭顺序 | 概念理解 |
| 判2 | 判断 | 占位符用于表名 | 概念理解 |
| 判3 | 判断 | 连接归还前须提交事务 | 概念理解 |
| 判4 | 判断 | Statement 防注入 | 概念理解 |
| 判5 | 判断 | CallableStatement 调存储过程 | 概念理解 |
| 简1 | 简答 | JDBC 六步骤 | 分析说明 |
| 简2 | 简答 | Statement vs PreparedStatement | 分析说明 |
| 简3 | 简答 | 连接池工作原理与优点 | 分析说明 |
| 简4 | 简答 | 参数化查询防注入原理 | 分析说明 |
| 编1 | 编程 | JDBC 查询完整代码 | 综合应用 |
| 编2 | 编程 | PreparedStatement 代码 | 综合应用 |
| 编3 | 编程 | HikariCP 连接池代码 | 综合应用 |
| 编4 | 编程 | CallableStatement 调存储过程 | 综合应用 |
| 综1 | 综合 | SQL 注入漏洞修复 | 综合应用 |
| 综2 | 综合 | 连接池参数配置综合 | 综合应用 |

## 一、单选题（每题 2 分，共 10 题）

**1. 在 JDBC 4.0 之前，加载 MySQL 驱动类的语句是（　）。**
A. `DriverManager.load("mysql")`
B. `Class.forName("com.mysql.cj.jdbc.Driver")`
C. `import java.sql.Driver`
D. `System.loadLibrary("mysql")`

**2. JDBC 操作的正确六步骤顺序是（　）。**
A. 建立连接→加载驱动→执行SQL→创建语句→处理结果→释放资源
B. 加载驱动→建立连接→创建语句→执行SQL→处理结果→释放资源
C. 创建语句→加载驱动→建立连接→执行SQL→处理结果→释放资源
D. 加载驱动→建立连接→执行SQL→创建语句→处理结果→释放资源

**3. 关于 Statement 与 PreparedStatement，下列说法正确的是（　）。**
A. Statement 防注入，PreparedStatement 不防
B. PreparedStatement 用占位符+参数绑定，防注入且执行计划可复用
C. 二者都只能执行查询
D. PreparedStatement 用字符串拼接构造 SQL

**4. PreparedStatement 防止 SQL 注入的根本原因是（　）。**
A. 自动过滤特殊字符
B. SQL 文本与参数分别发送，DBMS 把参数值仅作字面量绑定，不解析为 SQL 语法
C. 在客户端加密参数
D. 限制参数长度

**5. 使用连接池后，`Connection.close()` 的语义变为（　）。**
A. 物理关闭连接
B. 把连接归还给池而非物理关闭
C. 提交事务
D. 回滚事务

**6. 关于 HikariCP，下列说法正确的是（　）。**
A. 阿里开源，监控完善
B. 性能最高、代码精简，是 Spring Boot 默认，新项目首选
C. 老牌稳定，仅用于遗留项目
D. 不支持 MySQL

**7. 关于连接池 `maximumPoolSize`，下列说法正确的是（　）。**
A. 越大越好，提升吞吐
B. 超过 DB 或 CPU 承受能力后上下文切换与锁竞争反而降低吞吐，应压测确定拐点
C. 必须等于 CPU 核心数
D. 没有上限

**8. 连接池的 `maxLifetime` 应如何配置（　）。**
A. 大于 DB 端 wait_timeout
B. 必须等于 8 小时
C. 必须小于 DB 端 wait_timeout，避免被 DB 单方面关闭
D. 设为 0 表示永不过期

**9. ODBC 通过什么配置把"驱动+连接参数"配置在系统层（　）。**
A. DSN（Data Source Name）
B. JDBC URL
C. 环境变量
D. classpath

**10. 关于 PreparedStatement 占位符 `?`，下列说法正确的是（　）。**
A. 可用于表名
B. 可用于列名
C. 只能用于值，不能用于标识符（表名/列名）或 SQL 关键字
D. 可用于 ORDER BY 关键字

## 二、多选题（每题 3 分，共 5 题）

**1. 下列属于 JDBC 核心 API 的有（　）。**
A. `DriverManager.getConnection`
B. `conn.prepareStatement(sql)`
C. `rs.next()` / `rs.getXxx(col)`
D. `conn.setAutoCommit(false)` / `commit()`

**2. 连接池的优点包括（　）。**
A. 减少连接创建开销（复用现有连接）
B. 控制连接数量上限防止压垮数据库
C. 资源复用提升吞吐
D. 统一管理超时、保活、监控

**3. PreparedStatement 获得执行计划复用性能优势的前提包括（　）。**
A. 开启服务端预编译（useServerPrepStmts=true）
B. SQL 模板完全相同（含空格）
C. 动态拼接表名/列名
D. 计划缓存有空间且热点 SQL 命中

**4. 下列属于常见 Java 数据库连接池的有（　）。**
A. HikariCP
B. Druid
C. DBCP
D. C3P0

**5. 防范 SQL 注入的措施包括（　）。**
A. 参数化查询（核心防线）
B. 输入验证与白名单校验
C. 最小权限账户
D. 永远使用 root 连接

## 三、判断题（每题 2 分，共 5 题）

**1. try-with-resources 按 ResultSet→Statement→Connection 顺序自动关闭，且 Statement 关闭后 ResultSet 失效。**

**2. PreparedStatement 的占位符 `?` 可用于动态表名或列名。**

**3. 连接归还给池前必须确保事务已 commit 或 rollback，否则下个借用方会继承未提交事务。**

**4. Statement 通过字符串拼接构造 SQL，能有效防止 SQL 注入。**

**5. 调用数据库存储过程应使用 CallableStatement，通过 `{call proc(?,?)}` 语法。**

## 四、简答题（每题 5 分，共 4 题）

**1. 列出 JDBC 操作的六步骤。**

**2. 从 SQL 构造、注入风险、执行计划、适用场景四方面比较 Statement 与 PreparedStatement。**

**3. 说明连接池的工作原理（借出—使用—归还）与四点优点。**

**4. 解释参数化查询防止 SQL 注入的原理。**

## 五、编程题（每题 8 分，共 4 题，要求编写完整可运行的 Java JDBC 代码）

**1. JDBC 查询完整代码。** 表 `product(id BIGINT, name VARCHAR(128), price NUMERIC)`。要求：用 try-with-resources，通过 PreparedStatement 查询 price <= 指定值的商品，遍历输出 id、name、price，并正确处理 SQLException 打印 SQLState、ErrorCode、Message。

**2. PreparedStatement 防注入代码。** 表 `employee(id, name, dept_id)`。要求：对比展示拼接 SQL（不安全）与 PreparedStatement（安全）两种写法，输入 `deptId="1 OR 1=1"` 时说明行为差异，写出安全的完整代码。

**3. HikariCP 连接池代码。** 要求：配置 HikariDataSource（maximumPoolSize=20、minimumIdle=5、maxLifetime=30 分钟、connectionTimeout=30 秒、connectionTestQuery=SELECT 1），从池中借出连接执行 `SELECT id, name FROM product WHERE id=?`。

**4. CallableStatement 调用存储过程。** 调用第2章定义的 `transfer(p_from, p_to, p_amount, OUT p_result)`。要求：用 `{call transfer(?,?,?,?)}`，绑定 3 个 IN 参数并注册 1 个 OUT 参数（Types.VARCHAR），执行后取得 OUT 结果。

## 六、综合题（每题 8 分，共 2 题）

**1. SQL 注入漏洞修复。** 某系统登录代码如下（不安全）：**
```java
String name = request.getParameter("name");
String pwd = request.getParameter("pwd");
String sql = "SELECT * FROM user WHERE name = '" + name + "' AND pwd = '" + pwd + "'";
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery(sql);
```
要求：
- **(1)** 说明攻击者用 `name = "admin' --"` 输入时的注入后果；
- **(2)** 给出用 PreparedStatement 修复后的完整安全代码；
- **(3)** 补充一条非代码层面的防范建议（最小权限等）。

**2. 连接池参数配置综合。** 某 Java 应用使用 HikariCP 连接 MySQL 8.0（默认 wait_timeout=28800 秒），出现间歇性 `CommunicationsException`（连接已被 DB 关闭）。要求：**
- **(1)** 分析该异常的可能原因（maxLifetime 配置）；
- **(2)** 给出正确的 maxLifetime 与 connectionTimeout 配置值与理由；
- **(3)** 说明为何 `maximumPoolSize` 不是越大越好，以及应如何确定该值；
- **(4)** 说明连接归还前的事务处理要求。

## 答案与解析

<details>
<summary>单选题答案</summary>

1. **B**。`Class.forName("com.mysql.cj.jdbc.Driver")`；JDBC 4.0+ 通过 SPI 自动注册可省略。
2. **B**。加载驱动→建立连接→创建语句→执行SQL→处理结果→释放资源。
3. **B**。PreparedStatement 用占位符+参数绑定，防注入且执行计划可复用。
4. **B**。SQL 文本与参数分别发送，DBMS 把参数值仅作字面量绑定，不解析为 SQL 语法。
5. **B**。close 把连接归还给池而非物理关闭。
6. **B**。HikariCP 性能最高、代码精简，Spring Boot 默认，新项目首选。
7. **B**。超过承受能力后上下文切换与锁竞争反而降低吞吐，应压测确定拐点（常见 10–30）。
8. **C**。maxLifetime 必须小于 DB 端 wait_timeout，避免被 DB 单方面关闭。
9. **A**。ODBC 通过 DSN 把"驱动+连接参数"配置在系统层。
10. **C**。占位符只能用于值，不能用于标识符（表名/列名）或 SQL 关键字。

</details>

<details>
<summary>多选题答案</summary>

1. **ABCD**。四项均为 JDBC 核心 API。
2. **ABCD**。连接池四优点：减少开销、控制数量、资源复用、统一管理。
3. **ABD**。前提：开启服务端预编译、SQL 模板相同、计划缓存有空间命中；动态拼接表名会破坏复用。
4. **ABCD**。HikariCP、Druid、DBCP、C3P0 均为常见连接池。
5. **ABC**。参数化、输入校验、最小权限均为防范措施；永远用 root 连接是反模式。

</details>

<details>
<summary>判断题答案</summary>

1. **√**。try-with-resources 按 ResultSet→Statement→Connection 声明逆序关闭，Statement 关闭后 ResultSet 失效。
2. **×**。占位符只能用于值，不能用于表名/列名。
3. **√**。归还前须 commit/rollback，否则下个借用方继承未提交事务（脏数据）。
4. **×**。Statement 拼接 SQL，易受注入，不能防注入。
5. **√**。CallableStatement 用 `{call proc(?,?)}` 调存储过程。

</details>

<details>
<summary>简答题答案</summary>

**1. JDBC 六步骤：**
1. 加载驱动（`Class.forName`，新版可省）
2. 建立连接（`DriverManager.getConnection`）
3. 创建语句对象（Statement/PreparedStatement）
4. 执行 SQL（`executeQuery`/`executeUpdate`/`execute`）
5. 处理结果（遍历 ResultSet 或读影响行数）
6. 释放资源（按 ResultSet→Statement→Connection 顺序，推荐 try-with-resources）

**2. Statement vs PreparedStatement：**
| 维度 | Statement | PreparedStatement |
| ---- | ---- | ---- |
| SQL 构造 | 字符串拼接 | 占位符+参数绑定 |
| 注入风险 | 易受攻击 | 防注入 |
| 执行计划 | 每次重新解析 | 模板可复用 |
| 适用 | DDL、无用户输入的固定语句 | 带用户输入或重复执行的语句 |

**3. 连接池原理与优点：**
原理（借出—使用—归还）：①应用从池借出 Connection；②执行 SQL 与事务；③调用 close() 归还（非物理关闭），池标记空闲；④池定期校验、保活、回收。
优点：①减少连接创建开销；②控制连接数量上限；③资源复用提升吞吐；④统一管理超时、保活、监控。

**4. 参数化查询防注入原理：**
SQL 文本与参数分别发送给 DBMS。DBMS 先解析 SQL 模板（`?` 标记为参数占位），再把参数值作为字面量绑定，参数值只作数据处理，永远不被解析为 SQL 语法。故参数值含 `'`、`;`、`--` 也不会改变 SQL 结构。

</details>

<details>
<summary>编程题答案（完整可运行 Java 代码）</summary>

**1. JDBC 查询完整代码：**

```java
// JDK 17 + MySQL Connector/J 8.x
// pom.xml: mysql-connector-j 8.x
import java.sql.*;

public class JdbcQueryDemo {
    public static void main(String[] args) {
        String url = "jdbc:mysql://127.0.0.1:3306/demo?useSSL=false&serverTimezone=UTC&useServerPrepStmts=true";
        try (Connection conn = DriverManager.getConnection(url, "demo_user", "demo_pwd");
             PreparedStatement ps = conn.prepareStatement(
                 "SELECT id, name, price FROM product WHERE price <= ? ORDER BY price LIMIT 10")) {
            ps.setBigDecimal(1, new java.math.BigDecimal("100.00"));
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    System.out.printf("id=%d name=%s price=%s%n",
                        rs.getLong("id"),
                        rs.getString("name"),
                        rs.getBigDecimal("price"));
                }
            }
        } catch (SQLException e) {
            System.err.printf("SQLState=%s ErrorCode=%d Msg=%s%n",
                e.getSQLState(), e.getErrorCode(), e.getMessage());
        }
    }
}
```

**2. PreparedStatement 防注入代码：**

```java
import java.sql.*;

public class InjectionDemo {
    // 拼接 SQL（不安全）：输入 "1 OR 1=1" → 全表泄露
    // SELECT id, name FROM employee WHERE dept_id = 1 OR 1=1

    // 安全：参数化查询
    public static void safeQuery(Connection conn, String deptIdInput) throws SQLException {
        // 类型校验：非数字直接拒绝
        long deptId = Long.parseLong(deptIdInput); // "1 OR 1=1" 会抛 NumberFormatException
        try (PreparedStatement ps = conn.prepareStatement(
                "SELECT id, name FROM employee WHERE dept_id = ?")) {
            ps.setLong(1, deptId);  // 任意输入只作字面量绑定
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    System.out.printf("id=%d name=%s%n", rs.getLong("id"), rs.getString("name"));
                }
            }
        }
    }
}
```
输入 `"1 OR 1=1"`：拼接 SQL 会变成 `WHERE dept_id = 1 OR 1=1` 返回全表；PreparedStatement 中 `Long.parseLong` 拒绝非法输入，即使绕过校验，`1 OR 1=1` 也只作为字面量比较，无注入。

**3. HikariCP 连接池代码：**

```java
// JDK 17 + HikariCP 5.x
// pom.xml: com.zaxxer:HikariCP, mysql-connector-j
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import java.sql.*;

public class PoolDemo {
    public static void main(String[] args) {
        HikariConfig cfg = new HikariConfig();
        cfg.setJdbcUrl("jdbc:mysql://127.0.0.1:3306/demo?useSSL=false&serverTimezone=UTC");
        cfg.setUsername("demo_user");
        cfg.setPassword("demo_pwd");
        cfg.setMaximumPoolSize(20);
        cfg.setMinimumIdle(5);
        cfg.setMaxLifetime(1800000L);        // 30 分钟，小于 MySQL wait_timeout
        cfg.setConnectionTimeout(30000L);    // 30 秒
        cfg.setConnectionTestQuery("SELECT 1");

        try (HikariDataSource ds = new HikariDataSource(cfg);
             Connection conn = ds.getConnection();
             PreparedStatement ps = conn.prepareStatement(
                 "SELECT id, name FROM product WHERE id = ?")) {
            ps.setLong(1, 1L);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    System.out.printf("id=%d name=%s%n", rs.getLong("id"), rs.getString("name"));
                }
            }
        } catch (SQLException e) {
            System.err.printf("SQLState=%s ErrorCode=%d%n", e.getSQLState(), e.getErrorCode());
        }
    }
}
```

**4. CallableStatement 调用存储过程：**

```java
import java.sql.*;

public class CallableDemo {
    public static void callTransfer(Connection conn, long from, long to, java.math.BigDecimal amount)
            throws SQLException {
        try (CallableStatement cs = conn.prepareCall("{call transfer(?,?,?,?)}")) {
            cs.setLong(1, from);                 // IN p_from
            cs.setLong(2, to);                   // IN p_to
            cs.setBigDecimal(3, amount);         // IN p_amount
            cs.registerOutParameter(4, Types.VARCHAR);  // OUT p_result
            cs.execute();
            String result = cs.getString(4);     // 取得 OUT 参数
            System.out.println("transfer result = " + result);
        }
    }
}
```

</details>

<details>
<summary>综合题答案</summary>

**1. SQL 注入漏洞修复：**

**(1) 注入后果：** 输入 `name = "admin' --"`，拼接后 SQL 为：
```sql
SELECT * FROM user WHERE name = 'admin' --' AND pwd = '...'
```
`--` 后面被注释，密码校验被绕过，攻击者以 admin 身份登录。

**(2) 修复代码（PreparedStatement）：**
```java
String sql = "SELECT id, name FROM user WHERE name = ? AND pwd = ?";
try (PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setString(1, request.getParameter("name"));
    ps.setString(2, request.getParameter("pwd"));
    try (ResultSet rs = ps.executeQuery()) {
        if (rs.next()) {
            // 登录成功
        }
    }
}
```
参数值仅作字面量绑定，`'`、`--` 不改变 SQL 结构。

**(3) 非代码防范：** 应用使用的数据库账户只授予业务所需最小权限（仅 SELECT user 表），不使用 root 连接；密码用 bcrypt 加盐哈希存储，即使被注入拖库也无法获得明文。

**2. 连接池参数配置综合：**

**(1) 原因：** HikariCP 的 `maxLifetime` 配置大于 MySQL 的 `wait_timeout`（默认 28800 秒），导致池中连接在 DB 端已被关闭，应用仍借用该连接，抛 `CommunicationsException`。

**(2) 正确配置：** `maxLifetime` 必须小于 DB 端 `wait_timeout`，例如设为 `1800000L`（30 分钟），留出安全余量；`connectionTimeout` 设为 `30000L`（30 秒），超时抛异常而非无限等待，防止线程阻塞。

**(3) maximumPoolSize：** 不是越大越好——超过 DB 或 CPU 承受能力后，上下文切换与锁竞争反而降低吞吐。应通过压测确定拐点，常见最优值在 10–30 区间，而非数百。起步经验值可为 `(核心数×2 + 磁盘数)`。

**(4) 事务处理要求：** 连接归还前必须确保事务已 `commit` 或 `rollback`，否则下个借用方继承未提交事务导致脏数据；Statement/ResultSet 必须在 Connection 归还前关闭。

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | 驱动加载、六步骤、连接池、占位符、防注入 |
| 多选 | 5 | 15 | JDBC API、连接池优点、预编译前提、连接池、防范 |
| 判断 | 5 | 10 | 关闭顺序、占位符、事务归还、Statement、CallableStatement |
| 简答 | 4 | 20 | 六步骤、Statement对比、连接池原理、防注入原理 |
| 编程 | 4 | 32 | JDBC查询、PreparedStatement、HikariCP、CallableStatement |
| 综合 | 2 | 16 | 注入修复、连接池配置 |
| 合计 | 30 | 113 | 覆盖第4章访问接口全部主题 |

## 导航

- 上级 MOC：[[MOC - 数据库开发技术]]、[[MOC - 第4章]]
- 本章知识点：[[4.1 ODBC、JDBC原理]]、[[4.2 数据库连接池]]、[[4.3 参数化查询]]
- 上一章习题：[[MOC - 第3章习题]]
- 下一章习题：[[MOC - 第5章习题]]
