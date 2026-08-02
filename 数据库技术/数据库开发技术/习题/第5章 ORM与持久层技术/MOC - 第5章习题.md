---
domain: 数据库技术
subject: 数据库开发技术
type: exercise
chapter: 第5章 ORM与持久层技术
section: 第5章综合习题
tags: [数据库开发,习题,ORM,JPA,MyBatis,持久层,对象关系映射]
prerequisites: []
---

第5章习题覆盖 ORM 原理与优缺点、对象关系映射（一对一/一对多/多对多）、延迟加载与急切加载、实体生命周期、MyBatis vs Hibernate、Spring Data JPA，重点考查 JPA/MyBatis 代码编写。配套知识点见 [[MOC - 第5章]]。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 考查层次 |
| ---- | ---- | ---- | ---- |
| 单1 | 单选 | ORM 定义 | 概念理解 |
| 单2 | 单选 | ORM 阻抗失配 | 概念理解 |
| 单3 | 单选 | JPA 实体状态 | 概念理解 |
| 单4 | 单选 | persist vs merge | 概念理解 |
| 单5 | 单选 | 关系拥有方 mappedBy | 概念理解 |
| 单6 | 单选 | 延迟加载触发 | 概念理解 |
| 单7 | 单选 | N+1 问题 | 概念理解 |
| 单8 | 单选 | MyBatis #{} 与 ${} | 概念理解 |
| 单9 | 单选 | CascadeType.ALL | 概念理解 |
| 单10 | 单选 | Spring Data JPA 方法名解析 | 概念理解 |
| 多1 | 多选 | ORM 优点 | 概念辨析 |
| 多2 | 多选 | ORM 缺点 | 概念辨析 |
| 多3 | 多选 | JPA 实体四种状态 | 概念辨析 |
| 多4 | 多选 | 加载策略 | 概念辨析 |
| 多5 | 多选 | MyBatis vs Hibernate | 概念辨析 |
| 判1 | 判断 | ORM 消除 SQL 硬编码 | 概念理解 |
| 判2 | 判断 | FetchType.EAGER 隐式 JOIN | 概念理解 |
| 判3 | 判断 | MyBatis ${} 防注入 | 概念理解 |
| 判4 | 判断 | persist 传已有主键对象 | 概念理解 |
| 判5 | 判断 | 双向关联维护两端 | 概念理解 |
| 简1 | 简答 | ORM 优缺点 | 分析说明 |
| 简2 | 简答 | 四种关联关系映射 | 分析说明 |
| 简3 | 简答 | 实体生命周期四状态 | 分析说明 |
| 简4 | 简答 | MyBatis vs Hibernate 对比 | 分析说明 |
| 编1 | 编程 | JPA 实体一对多映射 | 综合应用 |
| 编2 | 编程 | MyBatis Mapper 动态 SQL | 综合应用 |
| 编3 | 编程 | Spring Data JPA Repository | 综合应用 |
| 编4 | 编程 | JOIN FETCH 解决 N+1 | 综合应用 |
| 综1 | 综合 | N+1 问题诊断与解决 | 综合应用 |
| 综2 | 综合 | 框架选型综合分析 | 综合应用 |

## 一、单选题（每题 2 分，共 10 题）

**1. ORM 的核心思想是（　）。**
A. 用存储过程替代应用层 SQL
B. 在面向对象程序与关系数据库之间建立映射，程序操作对象，ORM 生成并执行 SQL
C. 用 NoSQL 替代关系数据库
D. 用文件存储替代数据库

**2. ORM 解决的"阻抗失配"是指（　）。**
A. 网络协议不匹配
B. 面向对象程序有继承/组合/多态，关系数据库只有表/行/外键，二者模型不匹配
C. Java 与 Python 语法不匹配
D. 主键与外键类型不匹配

**3. JPA 实体 `new Order()` 创建后、调用 `persist()` 前的状态是（　）。**
A. 托管 Persistent
B. 游离 Detached
C. 新建 New/Transient
D. 删除 Removed

**4. 关于 `persist` 与 `merge`，下列说法正确的是（　）。**
A. persist 把游离对象合并为托管，发 UPDATE
B. merge 把新对象置为托管，提交时发 INSERT
C. persist 把新对象置为托管，提交时发 INSERT；传入已有主键对象会抛异常
D. merge 会修改原游离对象使其变托管

**5. 双向一对多关联中，`@OneToMany` 侧用 `mappedBy` 指向多的一方，说明（　）。**
A. "一"的一方是关系拥有方，维护外键
B. "多"的一方（外键所在）是关系拥有方，"一"的一方只读不维护
C. 双方都维护外键
D. 无外键

**6. 关于延迟加载（Lazy），下列说法正确的是（　）。**
A. 查询主实体时立即查出关联
B. 访问关联属性时才发 SQL 查询
C. 关联数据一定不会被查询
D. 与急切加载无区别

**7. N+1 查询问题是指（　）。**
A. 查询 N 条主实体触发 1 条 SQL
B. 遍历 N 条主实体并访问其关联属性，触发 N 次额外查询（共 N+1 条 SQL）
C. 执行 N+1 次事务
D. 连接池配置 N+1 个连接

**8. 关于 MyBatis 的 `#{}` 与 `${}`，下列说法正确的是（　）。**
A. `${}` 参数化占位符，防注入
B. `#{}` 字符串拼接，有注入风险
C. `#{}` 参数化占位符生成 `?` 并绑定，防注入，应优先使用；`${}` 字符串拼接有风险
D. 二者完全相同

**9. `@OneToMany(cascade = CascadeType.ALL)` 表示（　）。**
A. 不级联任何操作
B. 对主实体的 persist/merge/remove/refresh/detach 全部级联到关联实体
C. 仅级联查询
D. 仅级联删除

**10. Spring Data JPA 中 `User findByName(String name)` 方法名会被解析为（　）。**
A. `SELECT * FROM user WHERE id = ?`
B. `SELECT * FROM user WHERE name = ?`
C. `DELETE FROM user WHERE name = ?`
D. 需手写实现类

## 二、多选题（每题 3 分，共 5 题）

**1. ORM 的优点包括（　）。**
A. 消除 SQL 硬编码
B. 面向对象操作数据库
C. 提高开发效率（CRUD 自动）
D. 数据库可移植性（切换 Dialect）

**2. ORM 的缺点包括（　）。**
A. 性能开销（对象-关系转换、脏检查）
B. 复杂查询困难（多表统计、窗口函数常退回原生 SQL）
C. 学习曲线（映射、级联、抓取、缓存）
D. 完全取代原生 SQL 适用所有场景

**3. JPA 实体的四种状态包括（　）。**
A. 新建 New/Transient
B. 托管 Persistent/Managed
C. 游离 Detached
D. 删除 Removed

**4. 关于加载策略，下列说法正确的有（　）。**
A. 急切加载 Eager 查询主实体时立即查出关联
B. 延迟加载 Lazy 访问关联属性时才发 SQL
C. FetchType.EAGER 会隐式 JOIN，列表查询时拉入大量数据
D. 应优先用 LAZY

**5. MyBatis 相对 Hibernate 的特点包括（　）。**
A. 开发者手写 SQL，SQL 优化直接可控
B. 动态 SQL 强（`<if>`/`<choose>`/`<foreach>`）
C. 学习成本低（会 SQL 即可）
D. 数据库可移植性高于 Hibernate

## 三、判断题（每题 2 分，共 5 题）

**1. ORM 消除了 SQL 硬编码，业务代码中不再需要手写 SQL。**

**2. `FetchType.EAGER` 会隐式 JOIN，列表查询时拉入大量数据，应优先用 LAZY。**

**3. MyBatis 的 `${}` 是参数化占位符，能防止 SQL 注入。**

**4. `persist()` 传入已有主键的对象会抛异常。**

**5. 双向关联必须同时维护两端，否则内存中数据不一致。**

## 四、简答题（每题 5 分，共 4 题）

**1. 说明 ORM 的优点与缺点，并指出 ORM 不适用的场景。**

**2. 列出四种关联关系映射（一对一/一对多/多对一/多对多）及对应 JPA 注解。**

**3. 说明 JPA 实体生命周期的四种状态及其典型产生方式。**

**4. 从 SQL 编写、SQL 优化、学习成本、动态 SQL、适用场景五方面比较 MyBatis 与 Hibernate/JPA。**

## 五、编程题（每题 8 分，共 4 题，要求编写完整可运行代码）

**1. JPA 实体一对多映射。** 表 `orders(id, customer_id)` 与 `order_item(id, order_id, product_id)`。要求：编写 Order 与 OrderItem 两个 JPA 实体，建立双向一对多关联（`@OneToMany(mappedBy="order", cascade=ALL, fetch=LAZY)` 与 `@ManyToOne`），并提供 `addItem` 方法同时维护两端。

**2. MyBatis Mapper 动态 SQL。** 表 `user(id, name, age)`。要求：编写 UserMapper.xml 中 `search` 方法，使用 `<where>` + `<if>` 实现按 name（LIKE）与 minAge 动态过滤，并编写对应 Mapper 接口。

**3. Spring Data JPA Repository。** 表 `user(id, name, age)`。要求：编写 UserRepository 接口继承 JpaRepository，包含：①方法名查询 `findByName`；②`findByAgeGreaterThanEqualAndNameLike`；③`@Query` 自定义查询按年龄区间；④分页查询 `findByNameLike(Pageable)`。

**4. JOIN FETCH 解决 N+1。** 针对 Order 与 OrderItem 的一对多关联。要求：写出会触发 N+1 的反模式代码，再用 `JOIN FETCH` 改写为一次查完的正例代码。

## 六、综合题（每题 8 分，共 2 题）

**1. N+1 问题诊断与解决。** 某系统用 JPA 查询订单列表后遍历访问 `order.getItems().size()`，日志显示 1 条主查询 + N 条 `SELECT * FROM order_item WHERE order_id=?`。要求：**
- **(1)** 说明这是何种问题及根因；
- **(2)** 给出基于 JOIN FETCH 的解决方案代码；
- **(3)** 给出在 MyBatis 中的对应解决方案（`<collection>` 嵌套结果映射）；
- **(4)** 说明为何 `FetchType.EAGER` 不能解决该问题。

**2. 框架选型综合分析。** 某项目同时有：①核心业务 CRUD（领域模型清晰）；②复杂报表统计（多表 JOIN、窗口函数）；③对 SQL 性能要求极高的热点查询。要求：**
- **(1)** 分别为三类需求推荐合适的持久层技术（Spring Data JPA / MyBatis / 原生 JDBC）并说明理由；
- **(2)** 说明大型项目常混合使用的原因；
- **(3)** 指出全自动 ORM（Hibernate）生成的 SQL 为何需用执行计划验证。

## 答案与解析

<details>
<summary>单选题答案</summary>

1. **B**。ORM 在面向对象程序与关系数据库间建立映射，程序操作对象，ORM 生成并执行 SQL。
2. **B**。阻抗失配指 OO 有继承/组合/多态，关系库只有表/行/外键，二者模型不匹配。
3. **C**。`new Order()` 后 persist 前是新建 New/Transient 状态。
4. **C**。persist 把新对象置托管发 INSERT，传已有主键对象会抛异常；merge 把游离对象状态复制到托管对象，原游离对象仍游离。
5. **B**。外键所在的一方是关系拥有方；一对多中外键在"多"的一方，故 `@ManyToOne` 侧拥有，`@OneToMany` 用 mappedBy。
6. **B**。延迟加载访问关联属性时才发 SQL。
7. **B**。N+1 是遍历 N 条主实体访问关联触发 N 次额外查询（共 N+1 条 SQL）。
8. **C**。`#{}` 参数化防注入优先用；`${}` 拼接有风险。
9. **B**。CascadeType.ALL 级联 persist/merge/remove/refresh/detach 全部。
10. **B**。`findByName` 解析为 `SELECT * FROM user WHERE name = ?`。

</details>

<details>
<summary>多选题答案</summary>

1. **ABCD**。ORM 四优点：消除 SQL 硬编码、面向对象操作、提高开发效率、数据库可移植性。
2. **ABC**。缺点：性能开销、复杂查询困难、学习曲线；并非适用所有场景。
3. **ABCD**。四种状态：新建、托管、游离、删除。
4. **ABCD**。Eager 立即查、Lazy 访问才查、EAGER 隐式 JOIN 拉大量数据、应优先 LAZY。
5. **ABC**。MyBatis 手写 SQL 可控、动态 SQL 强、学习成本低；但数据库可移植性低于 Hibernate，故 D 错。

</details>

<details>
<summary>判断题答案</summary>

1. **×**。ORM 消除大部分 SQL 硬编码，但复杂查询、报表仍需退回原生 SQL；并非完全不需要。
2. **√**。EAGER 隐式 JOIN 拉入大量数据，应优先 LAZY。
3. **×**。`#{}` 防注入；`${}` 是字符串拼接，有注入风险。
4. **√**。persist 传已有主键对象会抛异常，应用 merge。
5. **√**。双向关联必须同时维护两端，否则内存不一致。

</details>

<details>
<summary>简答题答案</summary>

**1. ORM 优缺点与不适用场景：**
优点：消除 SQL 硬编码、面向对象操作、提高开发效率、数据库可移植性。
缺点：性能开销、复杂查询困难、学习曲线。
不适用场景：报表、ETL、超大规模批量写入、高性能热点查询——应使用原生 SQL 或专用工具。

**2. 四种关联映射：**
| 关系 | 注解 | 外键位置 |
| ---- | ---- | ---- |
| 一对一 | `@OneToOne` | 任意一方 |
| 一对多 | `@OneToMany`（mappedBy） | 多的一方 |
| 多对一 | `@ManyToOne` | 多的一方（拥有方） |
| 多对多 | `@ManyToMany` + `@JoinTable` | 中间表 |

**3. 实体四状态：**
| 状态 | 说明 | 产生方式 |
| ---- | ---- | ---- |
| 新建 New | 内存对象，无主键，未关联持久化上下文 | `new Order()` |
| 托管 Persistent | 在持久化上下文中，修改自动同步 | `persist()`/`find()`/`merge()` 返回值 |
| 游离 Detached | 曾托管但已脱离，有主键不再被跟踪 | `detach()`/事务提交后/`clear()` |
| 删除 Removed | 标记删除，提交时 DELETE | `remove(托管对象)` |

**4. MyBatis vs Hibernate：**
| 维度 | MyBatis | Hibernate/JPA |
| ---- | ---- | ---- |
| SQL 编写 | 开发者手写 | 框架自动生成 |
| SQL 优化 | 直接可控 | 需理解框架行为 |
| 学习成本 | 低 | 高 |
| 动态 SQL | 强（`<if>`/`<choose>`/`<foreach>`） | 弱（Criteria 冗长） |
| 适用 | 复杂查询、报表、SQL 控制要求高 | 业务模型清晰、CRUD 为主、领域驱动 |

</details>

<details>
<summary>编程题答案（完整可运行代码）</summary>

**1. JPA 实体一对多映射：**

```java
// JPA 实体
import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "orders")
public class Order {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<OrderItem> items = new ArrayList<>();

    // 双向关联维护：同时设置两端
    public void addItem(OrderItem item) {
        items.add(item);
        item.setOrder(this);
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public List<OrderItem> getItems() { return items; }
    public void setItems(List<OrderItem> items) { this.items = items; }
}

@Entity
@Table(name = "order_item")
public class OrderItem {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "order_id")  // 外键列
    private Order order;

    @ManyToOne
    @JoinColumn(name = "product_id")
    private Product product;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Order getOrder() { return order; }
    public void setOrder(Order order) { this.order = order; }
    public Product getProduct() { return product; }
    public void setProduct(Product product) { this.product = product; }
}
```

**2. MyBatis Mapper 动态 SQL：**

```xml
<!-- UserMapper.xml -->
<mapper namespace="com.example.mapper.UserMapper">
    <select id="search" resultType="User">
        SELECT id, name, age FROM user
        <where>
            <if test="name != null">AND name LIKE CONCAT('%', #{name}, '%')</if>
            <if test="minAge != null">AND age &gt;= #{minAge}</if>
        </where>
        ORDER BY id
    </select>
</mapper>
```

```java
// Mapper 接口
package com.example.mapper;
import com.example.entity.User;
import org.apache.ibatis.annotations.Param;
import java.util.List;

public interface UserMapper {
    List<User> search(@Param("name") String name, @Param("minAge") Integer minAge);
}
```

**3. Spring Data JPA Repository：**

```java
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import java.util.List;

public interface UserRepository extends JpaRepository<User, Long> {
    // 方法名即查询
    User findByName(String name);

    // 自动解析为 age >= ? AND name LIKE ?
    List<User> findByAgeGreaterThanEqualAndNameLike(Integer age, String pattern);

    // 自定义查询
    @Query("SELECT u FROM User u WHERE u.age BETWEEN :a AND :b")
    List<User> findByAgeRange(@Param("a") int a, @Param("b") int b);

    // 分页
    Page<User> findByNameLike(String name, Pageable pageable);
}
```

**4. JOIN FETCH 解决 N+1：**

```java
import jakarta.persistence.EntityManager;
import java.util.List;

public class NPlusOneDemo {
    // 反模式：N+1
    public void bad(EntityManager em) {
        List<Order> orders = em.createQuery("SELECT o FROM Order o", Order.class).getResultList();
        for (Order o : orders) {
            o.getItems().size();  // 每次触发一条 SELECT * FROM order_item WHERE order_id=?
        }
    }

    // 正例：JOIN FETCH 一次查完
    public void good(EntityManager em) {
        List<Order> orders = em.createQuery(
                "SELECT DISTINCT o FROM Order o LEFT JOIN FETCH o.items", Order.class)
            .getResultList();
        for (Order o : orders) {
            o.getItems().size();  // 关联已加载，不再额外查询
        }
    }
}
```

</details>

<details>
<summary>综合题答案</summary>

**1. N+1 问题诊断与解决：**

**(1)** 这是 N+1 查询问题。根因：延迟加载（FetchType.LAZY）下，查询 N 条主实体为 1 条 SQL，遍历访问每个 order 的 items 关联属性时，每条触发 1 次额外查询，共 N+1 条 SQL。

**(2) JOIN FETCH 解决：**
```java
List<Order> orders = em.createQuery(
        "SELECT DISTINCT o FROM Order o LEFT JOIN FETCH o.items", Order.class)
    .getResultList();
```
一次 JOIN 查出主实体与关联，避免 N 次额外查询。

**(3) MyBatis 解决：** 用 `<collection>` 嵌套结果映射，一条 JOIN SQL 配合 ResultMap 一次填充主对象与集合：
```xml
<resultMap id="orderMap" type="Order">
    <id property="id" column="o_id"/>
    <result property="name" column="o_name"/>
    <collection property="items" ofType="OrderItem">
        <id property="id" column="i_id"/>
        <result property="qty" column="i_qty"/>
    </collection>
</resultMap>
<select id="findOrdersWithItems" resultMap="orderMap">
    SELECT o.id o_id, o.name o_name, i.id i_id, i.quantity i_qty
    FROM orders o LEFT JOIN order_item i ON i.order_id = o.id
</select>
```

**(4)** `FetchType.EAGER` 不能解决 N+1：EAGER 会隐式 JOIN 或在列表查询时为每条主实体单独查关联，且列表场景拉入大量数据，性能更差。正确做法是保持 LAZY 并用 JOIN FETCH 显式指定需要关联的场景。

**2. 框架选型综合：**

**(1)**
- ①核心业务 CRUD（领域模型清晰）→ Spring Data JPA：方法名约定自动实现，开发效率高，适合领域驱动。
- ②复杂报表统计（多表 JOIN、窗口函数）→ MyBatis：手写 SQL 直接可控，动态 SQL 强，适合复杂查询。
- ③SQL 性能要求极高的热点查询 → 原生 JDBC + PreparedStatement：直接优化 SQL 与执行计划，无框架开销。

**(2)** 大型项目混合使用原因：不同需求对自动化与可控性要求不同。核心业务用 JPA 提效，报表用 MyBatis 控 SQL，热点用 JDBC 极致优化。单一框架无法同时满足开发效率与性能可控。

**(3)** 全自动 ORM（Hibernate）根据映射注解与 JPQL 自动生成 SQL，生成的不一定最优（如不必要的 JOIN、未命中索引的写法、N+1）。必须通过 EXPLAIN 检查执行计划（type、key、rows、Extra），发现全表扫描或 filesort 时通过索引或 JPQL 重写优化。不理解 SQL 与数据库原理使用 ORM 易写出低效代码（抽象泄漏）。

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| ---- | ---- | ---- | ---- |
| 单选 | 10 | 20 | ORM 定义、阻抗失配、实体状态、mappedBy、N+1、#{} vs ${} |
| 多选 | 5 | 15 | ORM 优劣、实体状态、加载策略、MyBatis vs Hibernate |
| 判断 | 5 | 10 | 消除SQL、EAGER、${}、persist、双向维护 |
| 简答 | 4 | 20 | ORM 优劣、关联映射、实体状态、框架对比 |
| 编程 | 4 | 32 | JPA 一对多、MyBatis 动态SQL、Spring Data JPA、JOIN FETCH |
| 综合 | 2 | 16 | N+1 诊断解决、框架选型 |
| 合计 | 30 | 113 | 覆盖第5章 ORM 全部主题 |

## 导航

- 上级 MOC：[[MOC - 数据库开发技术]]、[[MOC - 第5章]]
- 本章知识点：[[5.1 ORM思想原理]]、[[5.2 对象与关系映射]]、[[5.3 常见持久层框架简介]]
- 上一章习题：[[MOC - 第4章习题]]
- 下一章习题：[[MOC - 第6章习题]]
