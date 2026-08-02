---
domain: 软件工程
subject: Web开发技术
type: exercise
chapter: 第6章 前后端交互与AJAX
section: 6.1 AJAX基本原理
tags: [Web开发,习题,HTML,CSS,JavaScript]
prerequisites: []
---

# MOC - 第6章习题

> [!info] 习题说明
> 本章习题覆盖 AJAX 原理、XMLHttpRequest（readyState/status）、Fetch API、async/await、JSON 格式、JSON.stringify/parse、RESTful API、HTTP 方法语义、跨域与 CORS 等知识点。题目包含编程题，要求编写 AJAX/Fetch 代码，答案与解析折叠在 `<details>` 中。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 对应笔记 |
| --- | --- | --- | --- |
| 1 | 单选 | AJAX 全称 | [[6.1 AJAX基本原理]] |
| 2 | 单选 | XMLHttpRequest readyState | [[6.1 AJAX基本原理]] |
| 3 | 单选 | readyState=4 含义 | [[6.1 AJAX基本原理]] |
| 4 | 单选 | Fetch API 特点 | [[6.1 AJAX基本原理]] |
| 5 | 单选 | async/await | [[6.1 AJAX基本原理]] |
| 6 | 单选 | JSON 数据类型 | [[6.2 JSON数据格式]] |
| 7 | 单选 | JSON.stringify 作用 | [[6.2 JSON数据格式]] |
| 8 | 单选 | JSON.parse 作用 | [[6.2 JSON数据格式]] |
| 9 | 单选 | RESTful PUT 语义 | [[6.3 接口通信基础]] |
| 10 | 单选 | CORS 跨域 | [[6.3 接口通信基础]] |
| 11 | 多选 | AJAX 优点 | [[6.1 AJAX基本原理]] |
| 12 | 多选 | XMLHttpRequest 常用方法 | [[6.1 AJAX基本原理]] |
| 13 | 多选 | JSON 支持的数据类型 | [[6.2 JSON数据格式]] |
| 14 | 多选 | RESTful HTTP 方法 | [[6.3 接口通信基础]] |
| 15 | 多选 | CORS 响应头 | [[6.3 接口通信基础]] |
| 16 | 判断 | AJAX 同步异步 | [[6.1 AJAX基本原理]] |
| 17 | 判断 | Fetch 默认带 Cookie | [[6.1 AJAX基本原理]] |
| 18 | 判断 | JSON 支持函数 | [[6.2 JSON数据格式]] |
| 19 | 判断 | RESTful 幂等性 | [[6.3 接口通信基础]] |
| 20 | 判断 | 简单请求需预检 | [[6.3 接口通信基础]] |
| 21 | 简答 | AJAX 原理 | [[6.1 AJAX基本原理]] |
| 22 | 简答 | Fetch vs XHR | [[6.1 AJAX基本原理]] |
| 23 | 简答 | JSON 序列化 | [[6.2 JSON数据格式]] |
| 24 | 简答 | RESTful 设计 | [[6.3 接口通信基础]] |
| 25 | 编程 | XMLHttpRequest GET | [[6.1 AJAX基本原理]] |
| 26 | 编程 | Fetch POST JSON | [[6.1 AJAX基本原理]] |
| 27 | 编程 | async/await | [[6.1 AJAX基本原理]] |
| 28 | 编程 | JSON 处理 | [[6.2 JSON数据格式]] |
| 29 | 综合 | 用户列表 CRUD | [[6.3 接口通信基础]] |
| 30 | 综合 | 跨域请求处理 | [[6.3 接口通信基础]] |

## 一、单选题（每题 2 分，共 10 题）

**1. AJAX 的全称是？**

A. Asynchronous JavaScript and XML
B. Advanced JavaScript and XML
C. Asynchronous JSON and XML
D. Active JavaScript and XML

**2. XMLHttpRequest 对象的 readyState 值为 4 表示？**

A. 请求未初始化
B. 服务器连接已建立
C. 请求已接收
D. 请求已完成且响应就绪

**3. XMLHttpRequest 中表示"响应已完成"的 readyState 值是？**

A. 1
B. 2
C. 3
D. 4

**4. 关于 Fetch API，下列说法正确的是？**

A. 基于回调函数
B. 基于 Promise，支持 async/await
C. 不能发送 POST 请求
D. 不支持跨域

**5. `async` 函数的返回值是？**

A. 普通值
B. Promise 对象
C. callback
D. Generator

**6. 下列不属于 JSON 支持的数据类型的是？**

A. string
B. number
C. function
D. boolean

**7. `JSON.stringify({a:1})` 的结果是？**

A. `{a:1}`
B. `'{"a":1}'`
C. `{"a":"1"}`
D. `'[{"a":1}]'`

**8. `JSON.parse('{"name":"张三"}')` 的结果是？**

A. 字符串 `{"name":"张三"}`
B. 对象 `{name: "张三"}`
C. 数组
D. undefined

**9. RESTful API 中，更新资源的 HTTP 方法是？**

A. GET
B. POST
C. PUT
D. HEAD

**10. 解决跨域问题的 CORS 机制主要由谁实现？**

A. 客户端浏览器单独完成
B. 服务器端设置响应头
C. 修改客户端 hosts 文件
D. 使用 iframe

## 二、多选题（每题 3 分，共 5 题）

**11. 下列属于 AJAX 优点的有？**（多选）

A. 异步通信，无需刷新整个页面
B. 减少服务器负担
C. 提升用户体验
D. 可直接访问本地文件系统

**12. 下列属于 XMLHttpRequest 常用方法/属性的有？**（多选）

A. open()
B. send()
C. onreadystatechange
D. responseText

**13. 下列属于 JSON 支持的数据类型的有？**（多选）

A. string
B. number
C. array
D. object

**14. 下列属于 RESTful API 常用 HTTP 方法的有？**（多选）

A. GET（获取资源）
B. POST（创建资源）
C. PUT（更新资源）
D. DELETE（删除资源）

**15. 下列属于 CORS 相关响应头的有？**（多选）

A. Access-Control-Allow-Origin
B. Access-Control-Allow-Methods
C. Access-Control-Allow-Headers
D. Access-Control-Allow-Credentials

## 三、判断题（每题 2 分，共 5 题）

**16. AJAX 的核心是异步通信，默认推荐使用异步请求而非同步请求。**

**17. Fetch API 默认不会携带 Cookie，需设置 `credentials: 'include'`。**

**18. JSON 支持函数、日期、undefined 等类型。**

**19. RESTful API 中，GET、PUT、DELETE 都是幂等的，POST 不是。**

**20. 所有跨域请求都需要先发送 OPTIONS 预检请求。**

## 四、简答题（每题 5 分，共 4 题）

**21. 简述 AJAX 的工作原理。**

**22. 对比 Fetch API 与 XMLHttpRequest 的优缺点。**

**23. 说明 JSON.stringify 和 JSON.parse 的作用，并举例。**

**24. 什么是 RESTful API？列举其设计原则与 HTTP 方法语义。**

## 五、编程题（每题 8 分，共 4 题）

**25. 使用 XMLHttpRequest 发送一个 GET 请求到 `/api/users`，获取用户列表并打印到控制台，处理可能的错误。**

**26. 使用 Fetch API 发送一个 POST 请求到 `/api/users`，请求体为 JSON 数据 `{name:"张三",age:20}`，处理响应并打印结果。**

**27. 使用 async/await 改写以下 Promise 链式调用：**
```javascript
fetch("/api/data")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
```

**28. 给定 JSON 字符串 `'{"users":[{"name":"张三","age":20},{"name":"李四","age":22}]}'`，完成：**
- 解析为 JS 对象
- 提取所有姓名
- 序列化回 JSON 字符串

## 六、综合题（每题 12 分，共 2 题）

**29. 综合实现一个用户列表 CRUD 页面：**
- 页面加载时通过 Fetch 获取用户列表并渲染
- 提供"添加用户"表单（姓名、邮箱），提交后通过 POST 创建用户
- 每个用户有"删除"按钮，点击通过 DELETE 删除
- 所有请求使用 async/await，处理加载状态与错误

请编写完整 HTML+JS 代码（可使用模拟接口或假定接口存在）。

**30. 综合分析跨域问题：**
- 假设前端页面运行在 `http://localhost:3000`，需访问 `http://localhost:8080/api/data` 的接口
- 说明为什么会跨域、同源策略的限制
- 说明 CORS 的工作机制（简单请求 vs 预检请求）
- 给出服务器端需配置的响应头示例
- 编写前端 Fetch 请求代码（携带 Cookie）

## 答案与解析

<details>
<summary>点击展开答案与解析</summary>

### 单选题答案

**1. 答案：A**
解析：AJAX 全称 Asynchronous JavaScript and XML（异步 JavaScript 和 XML）。

**2. 答案：D**
解析：readyState=4 表示请求已完成且响应就绪。0 未初始化，1 已打开连接，2 已接收请求头，3 已接收部分响应。

**3. 答案：D**
解析：readyState=4 表示响应已完成。

**4. 答案：B**
解析：Fetch 基于 Promise，支持 async/await，可发送各种请求，跨域需服务器配合。

**5. 答案：B**
解析：async 函数始终返回 Promise 对象。

**6. 答案：C**
解析：JSON 不支持 function、undefined、Date 等。支持 string、number、boolean、null、object、array。

**7. 答案：B**
解析：`JSON.stringify({a:1})` 返回字符串 `'{"a":1}'`（键名加双引号）。

**8. 答案：B**
解析：`JSON.parse` 将 JSON 字符串解析为 JS 对象 `{name: "张三"}`。

**9. 答案：C**
解析：PUT 用于更新资源。

**10. 答案：B**
解析：CORS 由服务器端设置响应头实现，浏览器据此判断是否允许跨域。

### 多选题答案

**11. 答案：ABC**
解析：AJAX 优点是异步、减少负担、提升体验。D 错误，AJAX 不能访问本地文件系统（受同源策略限制）。

**12. 答案：ABCD**
解析：open、send、onreadystatechange、responseText 都是 XHR 常用方法/属性。

**13. 答案：ABCD**
解析：string、number、array、object 都是 JSON 支持的类型。

**14. 答案：ABCD**
解析：GET、POST、PUT、DELETE 都是 RESTful 常用方法。

**15. 答案：ABCD**
解析：四个都是 CORS 相关响应头。

### 判断题答案

**16. 答案：正确（√）**
解析：AJAX 推荐异步请求，同步请求会阻塞 UI。

**17. 答案：正确（√）**
解析：Fetch 默认不带 Cookie，需 `credentials: 'include'`。

**18. 答案：错误（×）**
解析：JSON 不支持函数、日期、undefined。

**19. 答案：正确（√）**
解析：GET、PUT、DELETE 幂等，POST 不幂等。

**20. 答案：错误（×）**
解析：简单请求（GET/POST + 简单头）无需预检，只有非简单请求（如 PUT、自定义头）才需 OPTIONS 预检。

### 简答题参考答案

**21. 参考答案**
AJAX 通过浏览器内置的 XMLHttpRequest 对象（或 Fetch API）异步向服务器发送请求并接收响应，无需刷新整个页面。流程：创建 XHR 对象 → open 设置方法和 URL → send 发送请求 → 监听 onreadystatechange → readyState=4 且 status=200 时处理响应数据。AJAX 实现了页面局部更新，提升用户体验。

**22. 参考答案**
Fetch 优点：基于 Promise，支持 async/await，API 更简洁现代，流式响应。
Fetch 缺点：不会因 HTTP 错误状态码（如 404、500）reject，需手动检查 res.ok；默认不带 Cookie。
XHR 优点：兼容性好（支持老浏览器），可监听进度事件，可中止请求。
XHR 缺点：回调地狱，API 繁琐，不基于 Promise。

**23. 参考答案**
- `JSON.stringify(obj)`：将 JS 对象序列化为 JSON 字符串。例：`JSON.stringify({a:1})` → `'{"a":1}'`。
- `JSON.parse(str)`：将 JSON 字符串解析为 JS 对象。例：`JSON.parse('{"a":1}')` → `{a:1}`。

**24. 参考答案**
RESTful API 是一种基于 HTTP 协议、以资源为中心的 API 设计风格。
设计原则：
- 用 URL 表示资源，如 `/api/users/123`。
- 用 HTTP 方法表示操作：GET 获取、POST 创建、PUT 更新、DELETE 删除。
- 使用 HTTP 状态码表示结果（200/201/400/404/500）。
- 无状态，每个请求自包含。
- 数据格式用 JSON。

### 编程题参考答案

**25. 参考答案**
```javascript
const xhr = new XMLHttpRequest();
xhr.open("GET", "/api/users", true);
xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
        if (xhr.status === 200) {
            const users = JSON.parse(xhr.responseText);
            console.log(users);
        } else {
            console.error("请求失败，状态码：" + xhr.status);
        }
    }
};
xhr.onerror = function() {
    console.error("网络错误");
};
xhr.send();
```

**26. 参考答案**
```javascript
fetch("/api/users", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({name: "张三", age: 20})
})
    .then(res => {
        if (!res.ok) {
            throw new Error("HTTP " + res.status);
        }
        return res.json();
    })
    .then(data => console.log("创建成功:", data))
    .catch(err => console.error("请求失败:", err));
```

**27. 参考答案**
```javascript
async function getData() {
    try {
        const res = await fetch("/api/data");
        if (!res.ok) {
            throw new Error("HTTP " + res.status);
        }
        const data = await res.json();
        console.log(data);
    } catch (err) {
        console.error(err);
    }
}

getData();
```

**28. 参考答案**
```javascript
const jsonStr = '{"users":[{"name":"张三","age":20},{"name":"李四","age":22}]}';

// 1. 解析为 JS 对象
const data = JSON.parse(jsonStr);
console.log(data);

// 2. 提取所有姓名
const names = data.users.map(u => u.name);
console.log(names); // ["张三", "李四"]

// 3. 序列化回 JSON 字符串
const newJsonStr = JSON.stringify(data);
console.log(newJsonStr);
```

### 综合题参考答案

**29. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>用户列表 CRUD</title>
    <style>
        body { font-family: Arial; padding: 20px; max-width: 700px; }
        .form-group { display: flex; gap: 8px; margin-bottom: 16px; }
        input { padding: 8px; flex: 1; }
        button { padding: 8px 16px; cursor: pointer; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        .loading { color: #999; }
        .error { color: red; }
    </style>
</head>
<body>
    <h2>用户列表</h2>
    <div class="form-group">
        <input type="text" id="name" placeholder="姓名">
        <input type="email" id="email" placeholder="邮箱">
        <button id="addBtn">添加</button>
    </div>
    <div id="status"></div>
    <table>
        <thead>
            <tr><th>ID</th><th>姓名</th><th>邮箱</th><th>操作</th></tr>
        </thead>
        <tbody id="userList"></tbody>
    </table>

    <script>
        const API = "/api/users";
        const tbody = document.getElementById("userList");
        const statusEl = document.getElementById("status");

        function showStatus(msg, isError) {
            statusEl.textContent = msg;
            statusEl.className = isError ? "error" : "loading";
        }

        async function loadUsers() {
            showStatus("加载中...");
            try {
                const res = await fetch(API);
                if (!res.ok) throw new Error("HTTP " + res.status);
                const users = await res.json();
                tbody.innerHTML = "";
                users.forEach(u => {
                    const tr = document.createElement("tr");
                    tr.innerHTML = `
                        <td>${u.id}</td>
                        <td>${u.name}</td>
                        <td>${u.email}</td>
                        <td><button class="del" data-id="${u.id}">删除</button></td>
                    `;
                    tbody.appendChild(tr);
                });
                showStatus("");
            } catch (err) {
                showStatus("加载失败: " + err.message, true);
            }
        }

        document.getElementById("addBtn").addEventListener("click", async () => {
            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            if (!name || !email) {
                showStatus("请填写完整", true);
                return;
            }
            try {
                const res = await fetch(API, {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({name, email})
                });
                if (!res.ok) throw new Error("HTTP " + res.status);
                document.getElementById("name").value = "";
                document.getElementById("email").value = "";
                await loadUsers();
            } catch (err) {
                showStatus("添加失败: " + err.message, true);
            }
        });

        // 事件委托：删除
        tbody.addEventListener("click", async e => {
            if (e.target.classList.contains("del")) {
                const id = e.target.dataset.id;
                if (!confirm("确认删除？")) return;
                try {
                    const res = await fetch(`${API}/${id}`, {method: "DELETE"});
                    if (!res.ok) throw new Error("HTTP " + res.status);
                    await loadUsers();
                } catch (err) {
                    showStatus("删除失败: " + err.message, true);
                }
            }
        });

        loadUsers();
    </script>
</body>
</html>
```

**30. 参考答案**
跨域原因：前端 `http://localhost:3000` 与接口 `http://localhost:8080` 端口不同，属于不同源（协议、域名、端口任一不同即跨域）。同源策略限制：浏览器禁止 JS 跨域读取响应、跨域访问 DOM、跨域发送 Cookie。

CORS 机制：
- 简单请求：GET/HEAD/POST（仅简单 Content-Type），浏览器直接发送，服务器返回 `Access-Control-Allow-Origin` 即可。
- 预检请求：非简单请求（如 PUT、自定义头、application/json），浏览器先发 OPTIONS 请求询问服务器是否允许，服务器返回允许的方法与头后，再发送真实请求。

服务器响应头示例（Node.js Express）：
```javascript
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "http://localhost:3000");
    res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
    res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");
    res.header("Access-Control-Allow-Credentials", "true");
    if (req.method === "OPTIONS") {
        return res.sendStatus(200);
    }
    next();
});
```

前端 Fetch 请求（携带 Cookie）：
```javascript
fetch("http://localhost:8080/api/data", {
    method: "GET",
    credentials: "include"  // 携带 Cookie
})
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
```
注意：携带 Cookie 时，`Access-Control-Allow-Origin` 不能为 `*`，必须指定具体域名，且需设置 `Access-Control-Allow-Credentials: true`。

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| --- | --- | --- | --- |
| 单选题 | 10 | 20 | 基础概念识别（AJAX、XHR、Fetch、async、JSON、RESTful、CORS） |
| 多选题 | 5 | 15 | 综合属性辨析（AJAX 优点、XHR 方法、JSON 类型、RESTful、CORS 头） |
| 判断题 | 5 | 10 | 易混点辨析（异步、Fetch Cookie、JSON 类型、幂等、预检） |
| 简答题 | 4 | 20 | 核心知识复述（AJAX 原理、Fetch vs XHR、JSON 序列化、RESTful） |
| 编程题 | 4 | 32 | 实战编码（XHR GET、Fetch POST、async/await、JSON 处理） |
| 综合题 | 2 | 24 | 综合应用（用户列表 CRUD、跨域处理） |
| 合计 | 30 | 121 | 覆盖第6章全部核心考点 |

## 章节导航

- 上一级：[[MOC - Web开发技术]]
- 本章知识点：[[MOC - 第6章]]
- 上一章习题：[[MOC - 第5章习题]]
- 下一章习题：[[MOC - 第7章习题]]
