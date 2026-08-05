---
domain: 软件工程
subject: Web开发技术
type: exercise
chapter: 第4章 JavaScript基础
section: 4.1 JS语法、变量、数据类型
tags: [Web开发,习题,HTML,CSS,JavaScript]
prerequisites: []
---

# MOC - 第4章习题

> [!info] 习题说明
> 本章习题覆盖 var/let/const、数据类型、typeof、类型转换、函数（声明/表达式/箭头函数）、作用域、闭包、数组方法（push/pop/map/filter/reduce）、对象、DOM 操作、事件机制等知识点。题目包含编程题，要求编写完整 JS 功能，答案与解析折叠在 `<details>` 中。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 对应笔记 |
| --- | --- | --- | --- |
| 1 | 单选 | var/let/const 区别 | [[4.1 JS语法、变量、数据类型]] |
| 2 | 单选 | typeof 返回值 | [[4.1 JS语法、变量、数据类型]] |
| 3 | 单选 | 数据类型 | [[4.1 JS语法、变量、数据类型]] |
| 4 | 单选 | 类型转换 | [[4.1 JS语法、变量、数据类型]] |
| 5 | 单选 | 箭头函数 | [[4.2 函数、数组、对象]] |
| 6 | 单选 | 作用域 | [[4.2 函数、数组、对象]] |
| 7 | 单选 | 数组 map 方法 | [[4.2 函数、数组、对象]] |
| 8 | 单选 | 数组 filter 方法 | [[4.2 函数、数组、对象]] |
| 9 | 单选 | DOM 获取元素 | [[4.3 DOM操作、事件机制]] |
| 10 | 单选 | 事件委托 | [[4.3 DOM操作、事件机制]] |
| 11 | 多选 | let/const 特点 | [[4.1 JS语法、变量、数据类型]] |
| 12 | 多选 | 数组方法 | [[4.2 函数、数组、对象]] |
| 13 | 多选 | DOM 获取元素方法 | [[4.3 DOM操作、事件机制]] |
| 14 | 多选 | 事件监听方法 | [[4.3 DOM操作、事件机制]] |
| 15 | 多选 | 数组迭代方法 | [[4.2 函数、数组、对象]] |
| 16 | 判断 | let 块级作用域 | [[4.1 JS语法、变量、数据类型]] |
| 17 | 判断 | 闭包定义 | [[4.2 函数、数组、对象]] |
| 18 | 判断 | map 返回新数组 | [[4.2 函数、数组、对象]] |
| 19 | 判断 | 事件冒泡方向 | [[4.3 DOM操作、事件机制]] |
| 20 | 判断 | const 引用类型 | [[4.1 JS语法、变量、数据类型]] |
| 21 | 简答 | var/let/const 区别 | [[4.1 JS语法、变量、数据类型]] |
| 22 | 简答 | 闭包概念与应用 | [[4.2 函数、数组、对象]] |
| 23 | 简答 | DOM 操作方法 | [[4.3 DOM操作、事件机制]] |
| 24 | 简答 | 事件冒泡与捕获 | [[4.3 DOM操作、事件机制]] |
| 25 | 编程 | 待办列表 | [[4.3 DOM操作、事件机制]] |
| 26 | 编程 | 表单验证 | [[4.3 DOM操作、事件机制]] |
| 27 | 编程 | 图片轮播 | [[4.3 DOM操作、事件机制]] |
| 28 | 编程 | 数组数据处理 | [[4.2 函数、数组、对象]] |
| 29 | 综合 | 购物车功能 | [[4.3 DOM操作、事件机制]] |
| 30 | 综合 | 学生成绩管理 | [[4.2 函数、数组、对象]] |

## 一、单选题（每题 2 分，共 10 题）

**1. 下列关于 var、let、const 的说法，正确的是？**

A. var 声明的变量有块级作用域
B. let 声明的变量有变量提升
C. const 声明的常量必须初始化且不能重新赋值
D. let 声明的变量可以重复声明

**2. `typeof null` 返回的结果是？**

A. "null"
B. "undefined"
C. "object"
D. "boolean"

**3. 下列不属于 JavaScript 基本数据类型的是？**

A. number
B. string
C. array
D. boolean

**4. `Number("123")` 返回的结果是？**

A. "123"
B. 123
C. NaN
D. undefined

**5. 箭头函数 `() => {}` 的特点是？**

A. 有自己的 this
B. 没有 this，继承外层 this
C. 可以使用 arguments 对象
D. 可以作为构造函数使用

**6. 在函数内部声明的 var 变量，其作用域是？**

A. 块级作用域
B. 函数作用域
C. 全局作用域
D. 模块作用域

**7. `[1,2,3].map(x => x * 2)` 的结果是？**

A. [1,2,3]
B. [2,4,6]
C. 6
D. [6]

**8. `[1,2,3,4].filter(x => x > 2)` 的结果是？**

A. [1,2]
B. [3,4]
C. [2,3,4]
D. 4

**9. 下列方法中，通过 ID 获取元素的是？**

A. `document.getElementsByTagName()`
B. `document.getElementsByClassName()`
C. `document.getElementById()`
D. `document.querySelector(".id")`

**10. 事件委托利用了事件流的哪个特性？**

A. 事件捕获
B. 事件冒泡
C. 事件目标
D. 事件阻止

## 二、多选题（每题 3 分，共 5 题）

**11. 下列属于 let/const 特点的有？**（多选）

A. 块级作用域
B. 不存在变量提升（暂时性死区）
C. 不允许重复声明
D. 必须初始化

**12. 下列属于数组方法的有？**（多选）

A. push
B. pop
C. map
D. reduce

**13. 下列属于 DOM 获取元素方法的有？**（多选）

A. getElementById
B. getElementsByTagName
C. querySelector
D. querySelectorAll

**14. 下列属于事件监听方式的有？**（多选）

A. `element.addEventListener("click", fn)`
B. `element.onclick = fn`
C. `<button onclick="fn()">`
D. `element.on("click", fn)`

**15. 下列属于数组迭代方法的有？**（多选）

A. forEach
B. map
C. filter
D. reduce

## 三、判断题（每题 2 分，共 5 题）

**16. `let` 声明的变量具有块级作用域。**

**17. 闭包是指有权访问另一个函数作用域中变量的函数。**

**18. `map` 方法会修改原数组并返回新数组。**

**19. 事件冒泡的方向是从目标元素向父级元素传播。**

**20. `const` 声明的对象，其属性也不能修改。**

## 四、简答题（每题 5 分，共 4 题）

**21. 说明 var、let、const 三者的区别。**

**22. 什么是闭包？举例说明闭包的应用场景。**

**23. 列举至少五种 DOM 操作方法（获取、创建、插入、删除元素）。**

**24. 说明事件冒泡与事件捕获的区别，以及如何阻止事件传播。**

## 五、编程题（每题 8 分，共 4 题）

**25. 编写一个待办列表（Todo List）功能：包含输入框、添加按钮、列表展示，可添加和删除待办项。要求使用 DOM 操作和事件委托。**

**26. 编写一个表单验证功能：用户名（≥3 字符）、邮箱（合法格式）、密码（≥6 字符），提交时验证，失败时在输入框下方显示错误提示。**

**27. 编写一个图片轮播功能：3 张图片自动切换（每 3 秒），可点击"上一张""下一张"按钮手动切换。**

**28. 给定数组 `[{name:"张三",score:85},{name:"李四",score:92},{name:"王五",score:78},{name:"赵六",score:95}]`，使用 map/filter/reduce 完成：**
- 筛选出 score ≥ 85 的学生
- 提取姓名数组
- 计算平均分

## 六、综合题（每题 12 分，共 2 题）

**29. 综合实现一个购物车功能：**
- 商品列表（名称、单价、库存）
- 点击"加入购物车"将商品加入列表
- 购物车中可调整数量、删除商品
- 实时计算总价
- 使用 DOM 操作与事件委托

请编写完整 HTML+CSS+JS 代码。

**30. 综合实现一个学生成绩管理系统：**
- 输入框：姓名、成绩
- 添加按钮：将学生加入列表
- 列表展示：姓名、成绩、等级（A/B/C/D）
- 统计：总人数、平均分、最高分、最低分
- 筛选：可按等级筛选学生

请编写完整 HTML+CSS+JS 代码。

## 答案与解析

<details>
<summary>点击展开答案与解析</summary>

### 单选题答案

**1. 答案：C**
解析：const 声明的常量必须初始化且不能重新赋值。var 是函数作用域，let 是块级作用域且无变量提升，let/const 都不允许重复声明。

**2. 答案：C**
解析：`typeof null` 返回 "object"（历史遗留 bug）。

**3. 答案：C**
解析：array 属于引用类型（Object），不是基本类型。基本类型有 number、string、boolean、null、undefined、symbol、bigint。

**4. 答案：B**
解析：`Number("123")` 将字符串转为数字 123。

**5. 答案：B**
解析：箭头函数没有自己的 this，继承外层作用域的 this；也没有 arguments 对象，不能作为构造函数。

**6. 答案：B**
解析：var 声明的变量是函数作用域。

**7. 答案：B**
解析：map 对每个元素乘 2，返回新数组 [2,4,6]。

**8. 答案：B**
解析：filter 筛选大于 2 的元素，返回 [3,4]。

**9. 答案：C**
解析：getElementById 通过 ID 获取元素。

**10. 答案：B**
解析：事件委托利用事件冒泡，在父元素上监听子元素的事件。

### 多选题答案

**11. 答案：ABC**
解析：let/const 有块级作用域、暂时性死区、不允许重复声明。D 错误，let 不必初始化，const 才必须初始化。

**12. 答案：ABCD**
解析：push、pop、map、reduce 都是数组方法。

**13. 答案：ABCD**
解析：getElementById、getElementsByTagName、querySelector、querySelectorAll 都是 DOM 获取方法。

**14. 答案：ABC**
解析：addEventListener、onclick 赋值、HTML onclick 属性都是事件监听方式。D 错误，原生 JS 没有 on 方法（jQuery 才有）。

**15. 答案：ABCD**
解析：forEach、map、filter、reduce 都是数组迭代方法。

### 判断题答案

**16. 答案：正确（√）**
解析：let 声明的变量具有块级作用域。

**17. 答案：正确（√）**
解析：闭包是有权访问另一个函数作用域中变量的函数。

**18. 答案：错误（×）**
解析：map 不修改原数组，而是返回新数组。

**19. 答案：正确（√）**
解析：事件冒泡从目标元素向父级元素传播。

**20. 答案：错误（×）**
解析：const 声明的对象不能重新赋值，但其属性可以修改（对象本身是可变的）。

### 简答题参考答案

**21. 参考答案**
| 特性 | var | let | const |
| --- | --- | --- | --- |
| 作用域 | 函数作用域 | 块级作用域 | 块级作用域 |
| 变量提升 | 有（值为 undefined） | 无（暂时性死区） | 无（暂时性死区） |
| 重复声明 | 允许 | 不允许 | 不允许 |
| 重新赋值 | 允许 | 允许 | 不允许 |
| 初始化 | 可不初始化 | 可不初始化 | 必须初始化 |

**22. 参考答案**
闭包是指有权访问另一个函数作用域中变量的函数。常用于：
- 创建私有变量（模块模式）
- 实现计数器
- 保存函数执行上下文
- 防抖节流

示例：
```javascript
function counter() {
    let count = 0;
    return function() {
        return ++count;
    };
}
const c = counter();
console.log(c()); // 1
console.log(c()); // 2
```

**23. 参考答案**
- 获取：getElementById、getElementsByTagName、querySelector、querySelectorAll
- 创建：document.createElement
- 插入：appendChild、insertBefore、append
- 删除：removeChild、remove
- 修改：innerHTML、textContent、setAttribute

**24. 参考答案**
- 事件捕获：从 document 向下传播到目标元素（外→内）
- 事件冒泡：从目标元素向上传播到 document（内→外）

阻止事件传播：`event.stopPropagation()` 阻止冒泡或捕获；`event.stopImmediatePropagation()` 阻止同元素其他监听器。

### 编程题参考答案

**25. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>待办列表</title>
    <style>
        body { font-family: Arial; padding: 20px; max-width: 500px; }
        .input-group { display: flex; gap: 8px; margin-bottom: 16px; }
        input[type="text"] { flex: 1; padding: 8px; }
        button { padding: 8px 16px; cursor: pointer; }
        ul { list-style: none; padding: 0; }
        li {
            display: flex;
            justify-content: space-between;
            padding: 8px;
            border-bottom: 1px solid #eee;
        }
        .del { color: red; cursor: pointer; }
    </style>
</head>
<body>
    <h2>待办列表</h2>
    <div class="input-group">
        <input type="text" id="todoInput" placeholder="输入待办事项">
        <button id="addBtn">添加</button>
    </div>
    <ul id="todoList"></ul>

    <script>
        const input = document.getElementById("todoInput");
        const addBtn = document.getElementById("addBtn");
        const list = document.getElementById("todoList");

        function addTodo() {
            const text = input.value.trim();
            if (!text) return;
            const li = document.createElement("li");
            li.innerHTML = `<span>${text}</span><span class="del">删除</span>`;
            list.appendChild(li);
            input.value = "";
        }

        addBtn.addEventListener("click", addTodo);
        input.addEventListener("keydown", e => {
            if (e.key === "Enter") addTodo();
        });

        // 事件委托：删除
        list.addEventListener("click", e => {
            if (e.target.classList.contains("del")) {
                e.target.parentElement.remove();
            }
        });
    </script>
</body>
</html>
```

**26. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>表单验证</title>
    <style>
        body { font-family: Arial; padding: 20px; max-width: 400px; }
        .form-group { margin-bottom: 12px; }
        label { display: block; margin-bottom: 4px; }
        input { width: 100%; padding: 8px; box-sizing: border-box; }
        .error { color: red; font-size: 12px; margin-top: 4px; }
    </style>
</head>
<body>
    <h2>注册表单</h2>
    <form id="regForm">
        <div class="form-group">
            <label>用户名</label>
            <input type="text" id="username">
            <div class="error" id="usernameError"></div>
        </div>
        <div class="form-group">
            <label>邮箱</label>
            <input type="text" id="email">
            <div class="error" id="emailError"></div>
        </div>
        <div class="form-group">
            <label>密码</label>
            <input type="password" id="password">
            <div class="error" id="passwordError"></div>
        </div>
        <button type="submit">提交</button>
    </form>

    <script>
        const form = document.getElementById("regForm");

        function showError(id, msg) {
            document.getElementById(id).textContent = msg;
        }

        form.addEventListener("submit", e => {
            e.preventDefault();
            const username = document.getElementById("username").value.trim();
            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value;
            let valid = true;

            // 清空错误
            showError("usernameError", "");
            showError("emailError", "");
            showError("passwordError", "");

            if (username.length < 3) {
                showError("usernameError", "用户名至少3个字符");
                valid = false;
            }
            const emailReg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailReg.test(email)) {
                showError("emailError", "邮箱格式不正确");
                valid = false;
            }
            if (password.length < 6) {
                showError("passwordError", "密码至少6个字符");
                valid = false;
            }

            if (valid) {
                alert("提交成功！");
            }
        });
    </script>
</body>
</html>
```

**27. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>图片轮播</title>
    <style>
        .carousel {
            width: 400px;
            margin: 20px auto;
            text-align: center;
        }
        .carousel img {
            width: 400px;
            height: 250px;
            object-fit: cover;
        }
        .controls { margin-top: 10px; }
        button { padding: 8px 16px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="carousel">
        <img id="slide" src="https://picsum.photos/400/250?random=1" alt="轮播图">
        <div class="controls">
            <button id="prev">上一张</button>
            <button id="next">下一张</button>
        </div>
    </div>

    <script>
        const images = [
            "https://picsum.photos/400/250?random=1",
            "https://picsum.photos/400/250?random=2",
            "https://picsum.photos/400/250?random=3"
        ];
        let index = 0;
        const slide = document.getElementById("slide");
        let timer = null;

        function show(i) {
            index = (i + images.length) % images.length;
            slide.src = images[index];
        }

        document.getElementById("prev").addEventListener("click", () => show(index - 1));
        document.getElementById("next").addEventListener("click", () => show(index + 1));

        function startAuto() {
            timer = setInterval(() => show(index + 1), 3000);
        }
        function stopAuto() {
            clearInterval(timer);
        }

        startAuto();
        // 鼠标悬停暂停
        slide.addEventListener("mouseenter", stopAuto);
        slide.addEventListener("mouseleave", startAuto);
    </script>
</body>
</html>
```

**28. 参考答案**
```javascript
const students = [
    {name: "张三", score: 85},
    {name: "李四", score: 92},
    {name: "王五", score: 78},
    {name: "赵六", score: 95}
];

// 筛选 score >= 85
const passed = students.filter(s => s.score >= 85);
console.log("及格学生:", passed);
// [{name:"张三",score:85},{name:"李四",score:92},{name:"赵六",score:95}]

// 提取姓名数组
const names = students.map(s => s.name);
console.log("姓名数组:", names);
// ["张三","李四","王五","赵六"]

// 计算平均分
const avg = students.reduce((sum, s) => sum + s.score, 0) / students.length;
console.log("平均分:", avg);
// 87.5
```

### 综合题参考答案

**29. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>购物车</title>
    <style>
        body { font-family: Arial; padding: 20px; max-width: 800px; }
        .product, .cart-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            border-bottom: 1px solid #eee;
        }
        button { padding: 6px 12px; cursor: pointer; }
        .total { font-size: 18px; font-weight: bold; margin-top: 16px; }
        .qty { display: flex; align-items: center; gap: 8px; }
    </style>
</head>
<body>
    <h2>商品列表</h2>
    <div id="productList"></div>

    <h2>购物车</h2>
    <div id="cartList"></div>
    <div class="total">总价：¥<span id="total">0</span></div>

    <script>
        const products = [
            {id: 1, name: "苹果", price: 5, stock: 10},
            {id: 2, name: "香蕉", price: 3, stock: 20},
            {id: 3, name: "橙子", price: 4, stock: 15}
        ];
        const cart = [];
        const productList = document.getElementById("productList");
        const cartList = document.getElementById("cartList");
        const totalEl = document.getElementById("total");

        // 渲染商品
        products.forEach(p => {
            const div = document.createElement("div");
            div.className = "product";
            div.innerHTML = `
                <span>${p.name} - ¥${p.price} (库存:${p.stock})</span>
                <button data-id="${p.id}">加入购物车</button>
            `;
            productList.appendChild(div);
        });

        // 事件委托：加入购物车
        productList.addEventListener("click", e => {
            if (e.target.tagName === "BUTTON") {
                const id = +e.target.dataset.id;
                const product = products.find(p => p.id === id);
                const item = cart.find(i => i.id === id);
                if (item) {
                    if (item.qty < product.stock) item.qty++;
                    else alert("库存不足");
                } else {
                    cart.push({...product, qty: 1});
                }
                renderCart();
            }
        });

        function renderCart() {
            cartList.innerHTML = "";
            cart.forEach(item => {
                const div = document.createElement("div");
                div.className = "cart-item";
                div.innerHTML = `
                    <span>${item.name} - ¥${item.price}</span>
                    <div class="qty">
                        <button class="dec" data-id="${item.id}">-</button>
                        <span>${item.qty}</span>
                        <button class="inc" data-id="${item.id}">+</button>
                    </div>
                    <button class="remove" data-id="${item.id}">删除</button>
                `;
                cartList.appendChild(div);
            });
            const total = cart.reduce((sum, i) => sum + i.price * i.qty, 0);
            totalEl.textContent = total;
        }

        // 事件委托：购物车操作
        cartList.addEventListener("click", e => {
            const id = +e.target.dataset.id;
            const item = cart.find(i => i.id === id);
            const product = products.find(p => p.id === id);
            if (e.target.classList.contains("inc")) {
                if (item.qty < product.stock) item.qty++;
                else alert("库存不足");
            } else if (e.target.classList.contains("dec")) {
                item.qty--;
                if (item.qty <= 0) {
                    cart.splice(cart.indexOf(item), 1);
                }
            } else if (e.target.classList.contains("remove")) {
                cart.splice(cart.indexOf(item), 1);
            }
            renderCart();
        });
    </script>
</body>
</html>
```

**30. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>学生成绩管理</title>
    <style>
        body { font-family: Arial; padding: 20px; max-width: 800px; }
        .form-group { display: inline-block; margin-right: 10px; }
        input { padding: 6px; }
        button { padding: 6px 12px; cursor: pointer; }
        table { width: 100%; border-collapse: collapse; margin-top: 16px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
        th { background: #f0f0f0; }
        .stats { margin: 16px 0; }
        .filter { margin: 12px 0; }
    </style>
</head>
<body>
    <h2>学生成绩管理</h2>
    <div>
        <div class="form-group">
            姓名：<input type="text" id="name">
        </div>
        <div class="form-group">
            成绩：<input type="number" id="score">
        </div>
        <button id="addBtn">添加</button>
    </div>

    <div class="filter">
        筛选等级：
        <select id="gradeFilter">
            <option value="all">全部</option>
            <option value="A">A (>=90)</option>
            <option value="B">B (80-89)</option>
            <option value="C">C (70-79)</option>
            <option value="D">D (<70)</option>
        </select>
    </div>

    <div class="stats" id="stats"></div>

    <table>
        <thead>
            <tr><th>姓名</th><th>成绩</th><th>等级</th><th>操作</th></tr>
        </thead>
        <tbody id="studentList"></tbody>
    </table>

    <script>
        const students = [];
        const nameInput = document.getElementById("name");
        const scoreInput = document.getElementById("score");
        const addBtn = document.getElementById("addBtn");
        const tbody = document.getElementById("studentList");
        const statsEl = document.getElementById("stats");
        const gradeFilter = document.getElementById("gradeFilter");

        function getGrade(score) {
            if (score >= 90) return "A";
            if (score >= 80) return "B";
            if (score >= 70) return "C";
            return "D";
        }

        function render() {
            const filter = gradeFilter.value;
            tbody.innerHTML = "";
            students.filter(s => filter === "all" || s.grade === filter)
                .forEach((s, idx) => {
                    const tr = document.createElement("tr");
                    tr.innerHTML = `
                        <td>${s.name}</td>
                        <td>${s.score}</td>
                        <td>${s.grade}</td>
                        <td><button class="del" data-idx="${students.indexOf(s)}">删除</button></td>
                    `;
                    tbody.appendChild(tr);
                });

            if (students.length === 0) {
                statsEl.textContent = "暂无数据";
                return;
            }
            const scores = students.map(s => s.score);
            const total = scores.reduce((a, b) => a + b, 0);
            statsEl.innerHTML = `
                总人数：${students.length} |
                平均分：${(total / students.length).toFixed(1)} |
                最高分：${Math.max(...scores)} |
                最低分：${Math.min(...scores)}
            `;
        }

        addBtn.addEventListener("click", () => {
            const name = nameInput.value.trim();
            const score = +scoreInput.value;
            if (!name || isNaN(score)) {
                alert("请输入有效数据");
                return;
            }
            students.push({name, score, grade: getGrade(score)});
            nameInput.value = "";
            scoreInput.value = "";
            render();
        });

        gradeFilter.addEventListener("change", render);

        // 事件委托：删除
        tbody.addEventListener("click", e => {
            if (e.target.classList.contains("del")) {
                students.splice(+e.target.dataset.idx, 1);
                render();
            }
        });

        render();
    </script>
</body>
</html>
```

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| --- | --- | --- | --- |
| 单选题 | 10 | 20 | 基础概念识别（变量类型、typeof、函数、作用域、数组、DOM、事件） |
| 多选题 | 5 | 15 | 综合属性辨析（let/const、数组方法、DOM 获取、事件监听、迭代方法） |
| 判断题 | 5 | 10 | 易混点辨析（作用域、闭包、map、冒泡、const 引用） |
| 简答题 | 4 | 20 | 核心知识复述（变量区别、闭包、DOM、事件流） |
| 编程题 | 4 | 32 | 实战编码（待办列表、表单验证、轮播、数组处理） |
| 综合题 | 2 | 24 | 综合应用（购物车、成绩管理） |
| 合计 | 30 | 121 | 覆盖第4章全部核心考点 |

## 章节导航

- 上一级：[[MOC - Web开发技术]]
- 本章知识点：[[MOC - 第4章]]
- 上一章习题：[[MOC - 第3章习题]]
- 下一章习题：[[MOC - 第5章习题]]
