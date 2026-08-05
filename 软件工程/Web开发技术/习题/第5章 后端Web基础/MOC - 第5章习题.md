---
domain: 软件工程
subject: Web开发技术
type: exercise
chapter: 第5章 后端Web基础
section: 5.1 客户端与服务端交互模型
tags: [Web开发,习题,HTML,CSS,JavaScript]
prerequisites: []
---

# MOC - 第5章习题

> [!info] 习题说明
> 本章习题覆盖客户端-服务端交互模型、Web 服务器（Apache/Nginx）、GET vs POST、表单提交编码类型、Cookie（属性/应用）、Session（机制/创建销毁）、Cookie vs Session 等知识点。题目分为单选、多选、判断、简答、分析、综合六类，共 30 题，答案与解析折叠在 `<details>` 中。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 对应笔记 |
| --- | --- | --- | --- |
| 1 | 单选 | 客户端-服务端模型 | [[5.1 客户端与服务端交互模型]] |
| 2 | 单选 | Web 服务器 | [[5.1 客户端与服务端交互模型]] |
| 3 | 单选 | Nginx 特点 | [[5.1 客户端与服务端交互模型]] |
| 4 | 单选 | GET 请求特点 | [[5.2 GET-POST请求、表单提交]] |
| 5 | 单选 | POST 请求特点 | [[5.2 GET-POST请求、表单提交]] |
| 6 | 单选 | 表单默认 method | [[5.2 GET-POST请求、表单提交]] |
| 7 | 单选 | 文件上传 enctype | [[5.2 GET-POST请求、表单提交]] |
| 8 | 单选 | Cookie 存储位置 | [[5.3 Cookie、Session基础]] |
| 9 | 单选 | Session 存储位置 | [[5.3 Cookie、Session基础]] |
| 10 | 单选 | Cookie 属性 | [[5.3 Cookie、Session基础]] |
| 11 | 多选 | Web 服务器软件 | [[5.1 客户端与服务端交互模型]] |
| 12 | 多选 | GET 与 POST 区别 | [[5.2 GET-POST请求、表单提交]] |
| 13 | 多选 | enctype 取值 | [[5.2 GET-POST请求、表单提交]] |
| 14 | 多选 | Cookie 属性 | [[5.3 Cookie、Session基础]] |
| 15 | 多选 | Session 与 Cookie 区别 | [[5.3 Cookie、Session基础]] |
| 16 | 判断 | HTTP 无状态 | [[5.3 Cookie、Session基础]] |
| 17 | 判断 | Cookie 大小限制 | [[5.3 Cookie、Session基础]] |
| 18 | 判断 | Session 依赖 Cookie | [[5.3 Cookie、Session基础]] |
| 19 | 判断 | GET 可缓存 | [[5.2 GET-POST请求、表单提交]] |
| 20 | 判断 | Nginx 反向代理 | [[5.1 客户端与服务端交互模型]] |
| 21 | 简答 | 请求-响应模型 | [[5.1 客户端与服务端交互模型]] |
| 22 | 简答 | GET vs POST | [[5.2 GET-POST请求、表单提交]] |
| 23 | 简答 | Cookie 机制 | [[5.3 Cookie、Session基础]] |
| 24 | 简答 | Session 机制 | [[5.3 Cookie、Session基础]] |
| 25 | 分析 | 表单提交场景 | [[5.2 GET-POST请求、表单提交]] |
| 26 | 分析 | 登录状态保持 | [[5.3 Cookie、Session基础]] |
| 27 | 分析 | Cookie vs Session 选型 | [[5.3 Cookie、Session基础]] |
| 28 | 分析 | Session 销毁时机 | [[5.3 Cookie、Session基础]] |
| 29 | 综合 | 电商网站状态管理 | [[5.3 Cookie、Session基础]] |
| 30 | 综合 | 完整登录流程 | [[5.3 Cookie、Session基础]] |

## 一、单选题（每题 2 分，共 10 题）

**1. B/S 架构中，客户端与服务器之间的通信模型是？**

A. 推送模型
B. 请求-响应模型
C. 广播模型
D. 长连接模型

**2. 下列属于常见 Web 服务器软件的是？**

A. MySQL
B. Apache
C. Redis
D. Node.js（运行时）

**3. 关于 Nginx，下列说法正确的是？**

A. 仅支持静态文件服务
B. 擅长高并发反向代理与负载均衡
C. 不能作为反向代理
D. 默认监听 3306 端口

**4. GET 请求的数据位置是？**

A. 请求体
B. 请求头
C. URL 查询字符串
D. Cookie

**5. POST 请求相比 GET 的优势是？**

A. 速度更快
B. 可被缓存
C. 数据在请求体，相对安全且无长度限制
D. 可被收藏为书签

**6. HTML 表单默认的 method 是？**

A. POST
B. GET
C. PUT
D. DELETE

**7. 表单上传文件时，enctype 必须设置为？**

A. `application/x-www-form-urlencoded`
B. `multipart/form-data`
C. `text/plain`
D. `application/json`

**8. Cookie 默认存储在？**

A. 服务器端
B. 客户端浏览器
C. 数据库
D. CDN

**9. Session 数据默认存储在？**

A. 客户端浏览器
B. 服务器端
C. Cookie 中
D. URL 中

**10. 设置 Cookie 过期时间的属性是？**

A. expires / max-age
B. timeout
C. lifetime
D. duration

## 二、多选题（每题 3 分，共 5 题）

**11. 下列属于 Web 服务器软件的有？**（多选）

A. Apache
B. Nginx
C. IIS
D. Tomcat

**12. 下列属于 GET 与 POST 区别的有？**（多选）

A. 数据位置不同（URL vs 请求体）
B. 长度限制不同
C. 幂等性不同（GET 幂等，POST 不幂等）
D. 编码类型支持范围不同

**13. 下列属于 form enctype 取值的有？**（多选）

A. `application/x-www-form-urlencoded`
B. `multipart/form-data`
C. `text/plain`
D. `application/json`

**14. 下列属于 Cookie 属性的有？**（多选）

A. name / value
B. expires / max-age
C. domain / path
D. httpOnly / secure

**15. 下列属于 Session 与 Cookie 区别的有？**（多选）

A. 存储位置不同（服务器 vs 客户端）
B. 安全性不同（Session 更安全）
C. 大小限制不同（Session 无明显限制，Cookie 约 4KB）
D. 生命周期不同

## 三、判断题（每题 2 分，共 5 题）

**16. HTTP 是无状态协议，服务器默认不记录客户端的多次请求。**

**17. 单个 Cookie 大小一般限制在 4KB 左右。**

**18. Session 机制通常依赖 Cookie 传递 Session ID（也可通过 URL 重写）。**

**19. GET 请求可被浏览器缓存，POST 请求默认不缓存。**

**20. Nginx 可作为反向代理服务器，将请求转发给后端应用服务器。**

## 四、简答题（每题 5 分，共 4 题）

**21. 简述客户端与服务端的请求-响应交互模型。**

**22. 对比 GET 与 POST 请求的特点（至少 4 个维度）。**

**23. 说明 Cookie 的工作机制及常见应用场景。**

**24. 说明 Session 的工作机制，Session 是如何创建与销毁的？**

## 五、分析题（每题 8 分，共 4 题）

**25. 分析以下三种表单提交场景应使用 GET 还是 POST，并说明理由：**
- 搜索商品
- 提交订单
- 用户登录

**26. 用户登录成功后，服务器需要记住登录状态，分析应使用 Cookie 还是 Session，并说明完整流程。**

**27. 对比 Cookie 与 Session，分析在以下场景应选哪个：**
- 记住用户名（下次自动填充）
- 保存登录态
- 购物车数据
- 用户偏好设置（主题色）

**28. 分析 Session 的销毁时机有哪些？如何实现"关闭浏览器即登出"和"7 天自动登录"两种需求？**

## 六、综合题（每题 12 分，共 2 题）

**29. 综合设计：某电商网站需要管理用户状态，涉及以下场景：**
- 用户登录态保持（7 天有效）
- 浏览历史记录（30 天）
- 购物车数据（未登录也可使用）
- 个性化推荐偏好

请分析每个场景应使用 Cookie 还是 Session，并说明数据存储策略、安全性考量和过期时间设计。

**30. 综合分析：描述一次完整的用户登录流程，从用户输入用户名密码到后续访问受保护页面的全过程。要求包含：**
- 表单提交方式与编码类型
- 服务器验证流程
- Session 创建与 Cookie 下发
- 后续请求如何携带 Session ID
- 登出时 Session 与 Cookie 的处理

## 答案与解析

<details>
<summary>点击展开答案与解析</summary>

### 单选题答案

**1. 答案：B**
解析：B/S 架构采用请求-响应模型，客户端发起请求，服务器响应。

**2. 答案：B**
解析：Apache 是 Web 服务器。MySQL 是数据库，Redis 是缓存，Node.js 是运行时。

**3. 答案：B**
解析：Nginx 擅长高并发反向代理与负载均衡，默认监听 80 端口。

**4. 答案：C**
解析：GET 请求的数据放在 URL 查询字符串中。

**5. 答案：C**
解析：POST 数据在请求体，相对安全且无长度限制。

**6. 答案：B**
解析：表单默认 method 是 GET。

**7. 答案：B**
解析：文件上传必须用 `multipart/form-data`。

**8. 答案：B**
解析：Cookie 默认存储在客户端浏览器。

**9. 答案：B**
解析：Session 数据存储在服务器端。

**10. 答案：A**
解析：expires 或 max-age 设置 Cookie 过期时间。

### 多选题答案

**11. 答案：ABCD**
解析：Apache、Nginx、IIS、Tomcat 都是 Web 服务器软件。

**12. 答案：ABCD**
解析：数据位置、长度限制、幂等性、编码类型支持都是 GET 与 POST 的区别。

**13. 答案：ABC**
解析：`application/json` 不是 form 的 enctype 取值（AJAX 才用）。A、B、C 都是 enctype 取值。

**14. 答案：ABCD**
解析：name/value、expires/max-age、domain/path、httpOnly/secure 都是 Cookie 属性。

**15. 答案：ABCD**
解析：存储位置、安全性、大小限制、生命周期都是 Session 与 Cookie 的区别。

### 判断题答案

**16. 答案：正确（√）**
解析：HTTP 是无状态协议，需借助 Cookie/Session 维持状态。

**17. 答案：正确（√）**
解析：单个 Cookie 一般限制 4KB 左右。

**18. 答案：正确（√）**
解析：Session 通常通过 Cookie 传递 Session ID，禁用 Cookie 时可用 URL 重写。

**19. 答案：正确（√）**
解析：GET 可缓存，POST 默认不缓存。

**20. 答案：正确（√）**
解析：Nginx 常作为反向代理转发请求给后端。

### 简答题参考答案

**21. 参考答案**
客户端（浏览器）发起 HTTP 请求，经 DNS 解析、TCP 连接到达服务器；服务器接收请求后处理（路由、查询、业务逻辑），返回 HTTP 响应（状态码、响应头、响应体）；浏览器接收响应后解析渲染。整个过程是无状态的，每次请求独立，服务器默认不记忆客户端。

**22. 参考答案**
| 维度 | GET | POST |
| --- | --- | --- |
| 数据位置 | URL 查询字符串 | 请求体 |
| 长度限制 | 受 URL 长度限制（约 2KB） | 理论上无限制 |
| 安全性 | 数据暴露在 URL | 相对安全 |
| 幂等性 | 幂等 | 不幂等 |
| 缓存 | 可缓存 | 默认不缓存 |
| 书签 | 可收藏 | 不可收藏 |

**23. 参考答案**
Cookie 工作机制：服务器通过 Set-Cookie 响应头下发 Cookie，浏览器存储后，后续请求自动通过 Cookie 请求头携带给同域服务器。
常见应用：用户登录态、购物车、用户偏好设置、浏览历史、广告追踪。

**24. 参考答案**
Session 机制：服务器为每个客户端创建一个 Session 对象，分配唯一 Session ID，通过 Cookie（或 URL 重写）传给客户端；后续请求携带 Session ID，服务器据此找到对应 Session 数据。
- 创建：客户端首次访问或调用创建 Session 的 API 时创建。
- 销毁：调用 invalidate、超时自动销毁、服务器重启。
- Session 数据存储在服务器端，较安全。

### 分析题参考答案

**25. 参考答案**
- 搜索商品：用 GET。搜索是查询操作，幂等，参数可收藏分享，数据量小。
- 提交订单：用 POST。订单是写操作，不幂等，数据量大，需保密，不能缓存。
- 用户登录：用 POST。密码等敏感数据不能暴露在 URL，必须放请求体，且不缓存。

**26. 参考答案**
应使用 Session（搭配 Cookie 传递 Session ID）。
完整流程：
1. 用户提交用户名密码（POST）。
2. 服务器验证账号密码。
3. 验证通过后，服务器创建 Session，存储用户 ID 等信息，生成唯一 Session ID。
4. 服务器通过 Set-Cookie 响应头将 Session ID 下发给浏览器。
5. 浏览器存储该 Cookie。
6. 后续请求浏览器自动携带 Cookie（含 Session ID），服务器据此识别用户。
7. 登出时服务器销毁 Session，清除 Cookie。

**27. 参考答案**
- 记住用户名：用 Cookie。数据不敏感，长期保存在客户端，下次自动填充。
- 保存登录态：用 Session。安全要求高，数据存服务器，Cookie 仅存 Session ID。
- 购物车数据：未登录用 Cookie（客户端暂存），登录后迁移到 Session/数据库。
- 用户偏好设置（主题色）：用 Cookie。非敏感，长期有效，客户端读取快。

**28. 参考答案**
Session 销毁时机：
1. 显式调用 invalidate()/destroy()（用户登出）。
2. 超时自动销毁（默认 30 分钟无活动）。
3. 服务器重启或应用重新部署。

- 关闭浏览器即登出：将 Cookie 的 max-age 设为会话级（不设置 expires，浏览器关闭即清除），Session ID 丢失，下次访问需重新登录。
- 7 天自动登录：将 Cookie 的 max-age 设为 7 天，服务器端 Session 超时设为 7 天，或将用户标识加密存入持久化 Cookie，下次访问时重新生成 Session。

### 综合题参考答案

**29. 参考答案**
| 场景 | 选择 | 存储策略 | 安全性 | 过期时间 |
| --- | --- | --- | --- | ---|
| 登录态 | Session + Cookie | 服务器存用户 ID，Cookie 存 Session ID | 高，设 httpOnly、secure | 7 天 |
| 浏览历史 | Cookie | 客户端存商品 ID 列表 | 低，非敏感 | 30 天 |
| 购物车（未登录） | Cookie | 客户端存商品 ID+数量 | 中，登录后迁移到服务器 | 会话级或 7 天 |
| 推荐偏好 | Cookie | 客户端存偏好设置 | 低，非敏感 | 长期（如 1 年） |

设计考量：
- 登录态优先用 Session 保证安全，Cookie 仅存 Session ID 且设 httpOnly 防 XSS、secure 强制 HTTPS。
- 非敏感数据（浏览历史、偏好）用 Cookie 减轻服务器压力。
- 购物车需支持未登录场景，先用 Cookie 暂存，登录后合并到服务器端。
- 过期时间根据业务需求设置，登录态不宜过长（7 天），偏好可长期。

**30. 参考答案**
完整登录流程：
1. 用户在登录页输入用户名密码，表单 method="post"，enctype="application/x-www-form-urlencoded"（默认）。
2. 浏览器发送 POST 请求，请求体含 username 和 password。
3. 服务器接收请求，查询数据库验证用户名密码。
4. 验证通过：
   - 服务器创建 Session 对象，存储用户 ID、角色等信息。
   - 生成唯一 Session ID。
   - 通过 Set-Cookie 响应头下发 Session ID：`Set-Cookie: sessionid=abc123; HttpOnly; Secure; Path=/`。
   - 返回登录成功响应（重定向到首页或返回 JSON）。
5. 验证失败：返回错误提示，不创建 Session。
6. 后续访问受保护页面：
   - 浏览器自动携带 Cookie：`Cookie: sessionid=abc123`。
   - 服务器根据 Session ID 查找 Session，验证用户身份与权限。
   - 有效则返回页面内容；无效或过期则重定向到登录页。
7. 登出处理：
   - 服务器调用 Session.invalidate() 销毁 Session 数据。
   - 服务器下发清除 Cookie 的响应：`Set-Cookie: sessionid=; Max-Age=0`。
   - 浏览器删除 Cookie，后续请求不再携带 Session ID。

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| --- | --- | --- | --- |
| 单选题 | 10 | 20 | 基础概念识别（交互模型、服务器、GET/POST、Cookie/Session） |
| 多选题 | 5 | 15 | 综合属性辨析（服务器、GET/POST、enctype、Cookie 属性、Cookie/Session） |
| 判断题 | 5 | 10 | 易混点辨析（无状态、Cookie 大小、Session 依赖、缓存、Nginx） |
| 简答题 | 4 | 20 | 核心知识复述（交互模型、GET/POST、Cookie、Session） |
| 分析题 | 4 | 32 | 原理分析（表单场景、登录态、选型、销毁时机） |
| 综合题 | 2 | 24 | 综合应用（电商状态管理、完整登录流程） |
| 合计 | 30 | 121 | 覆盖第5章全部核心考点 |

## 章节导航

- 上一级：[[MOC - Web开发技术]]
- 本章知识点：[[MOC - 第5章]]
- 上一章习题：[[MOC - 第4章习题]]
- 下一章习题：[[MOC - 第6章习题]]
