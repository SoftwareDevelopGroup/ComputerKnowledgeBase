---
domain: 软件工程
subject: Web开发技术
type: exercise
chapter: 第3章 CSS样式技术
section: 3.1 CSS引入方式、选择器
tags: [Web开发,习题,HTML,CSS,JavaScript]
prerequisites: []
---

# MOC - 第3章习题

> [!info] 习题说明
> 本章习题覆盖 CSS 引入方式与优先级、选择器体系（基础/复合/伪类/伪元素）、选择器优先级计算、盒模型（content/padding/border/margin）、box-sizing、浮动与清除浮动、定位（static/relative/absolute/fixed/sticky）、Flex 布局、媒体查询、响应式设计等知识点。题目包含编程题，要求编写完整 CSS 样式，答案与解析折叠在 `<details>` 中。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 对应笔记 |
| --- | --- | --- | --- |
| 1 | 单选 | CSS 引入方式优先级 | [[3.1 CSS引入方式、选择器]] |
| 2 | 单选 | 选择器优先级 | [[3.1 CSS引入方式、选择器]] |
| 3 | 单选 | 伪类选择器 | [[3.1 CSS引入方式、选择器]] |
| 4 | 单选 | 伪元素选择器 | [[3.1 CSS引入方式、选择器]] |
| 5 | 单选 | 盒模型组成 | [[3.2 盒模型、浮动与布局]] |
| 6 | 单选 | box-sizing | [[3.2 盒模型、浮动与布局]] |
| 7 | 单选 | position 定位 | [[3.2 盒模型、浮动与布局]] |
| 8 | 单选 | flex-direction | [[3.3 Flex布局、响应式基础]] |
| 9 | 单选 | justify-content | [[3.3 Flex布局、响应式基础]] |
| 10 | 单选 | 媒体查询 | [[3.3 Flex布局、响应式基础]] |
| 11 | 多选 | CSS 引入方式 | [[3.1 CSS引入方式、选择器]] |
| 12 | 多选 | 复合选择器 | [[3.1 CSS引入方式、选择器]] |
| 13 | 多选 | position 取值 | [[3.2 盒模型、浮动与布局]] |
| 14 | 多选 | Flex 容器属性 | [[3.3 Flex布局、响应式基础]] |
| 15 | 多选 | 清除浮动方法 | [[3.2 盒模型、浮动与布局]] |
| 16 | 判断 | !important 优先级 | [[3.1 CSS引入方式、选择器]] |
| 17 | 判断 | border-box 含义 | [[3.2 盒模型、浮动与布局]] |
| 18 | 判断 | relative 脱离文档流 | [[3.2 盒模型、浮动与布局]] |
| 19 | 判断 | flex 默认主轴方向 | [[3.3 Flex布局、响应式基础]] |
| 20 | 判断 | viewport 作用 | [[3.3 Flex布局、响应式基础]] |
| 21 | 简答 | CSS 引入与优先级 | [[3.1 CSS引入方式、选择器]] |
| 22 | 简答 | 选择器优先级计算 | [[3.1 CSS引入方式、选择器]] |
| 23 | 简答 | 盒模型与 box-sizing | [[3.2 盒模型、浮动与布局]] |
| 24 | 简答 | Flex 水平垂直居中 | [[3.3 Flex布局、响应式基础]] |
| 25 | 编程 | 横向导航栏 | [[3.2 盒模型、浮动与布局]] |
| 26 | 编程 | 卡片布局 | [[3.3 Flex布局、响应式基础]] |
| 27 | 编程 | 响应式两栏布局 | [[3.3 Flex布局、响应式基础]] |
| 28 | 编程 | sticky 页头 | [[3.2 盒模型、浮动与布局]] |
| 29 | 综合 | 商品列表页布局 | [[3.3 Flex布局、响应式基础]] |
| 30 | 综合 | 完整响应式页面 | [[3.3 Flex布局、响应式基础]] |

## 一、单选题（每题 2 分，共 10 题）

**1. 下列 CSS 引入方式中，优先级最高的是？**

A. 外部样式表
B. 内部样式表
C. 行内样式
D. @import

**2. 选择器优先级从高到低排列正确的是？**

A. 类 > ID > 标签 > !important
B. !important > 行内 > ID > 类 > 标签
C. ID > 类 > 标签 > !important
D. 行内 > ID > 类 > 标签 > !important

**3. 下列属于伪类选择器的是？**

A. `::before`
B. `:hover`
C. `::after`
D. `::first-line`

**4. 下列属于伪元素选择器的是？**

A. `:hover`
B. `:first-child`
C. `::before`
D. `:nth-child(n)`

**5. CSS 盒模型由内到外的顺序是？**

A. content → border → padding → margin
B. content → padding → border → margin
C. padding → content → border → margin
D. margin → border → padding → content

**6. `box-sizing: border-box` 表示 width 包含？**

A. 仅 content
B. content + padding
C. content + padding + border
D. content + padding + border + margin

**7. 下列 position 值中，会让元素脱离文档流的是？**

A. static
B. relative
C. absolute
D. sticky

**8. Flex 布局中，设置主轴方向的属性是？**

A. justify-content
B. align-items
C. flex-direction
D. flex-wrap

**9. Flex 中实现主轴两端对齐的 justify-content 值是？**

A. center
B. flex-start
C. space-between
D. space-around

**10. 媒体查询 `@media (max-width: 768px)` 表示？**

A. 屏幕宽度大于 768px 时应用
B. 屏幕宽度小于等于 768px 时应用
C. 屏幕宽度等于 768px 时应用
D. 屏幕宽度不等于 768px 时应用

## 二、多选题（每题 3 分，共 5 题）

**11. 下列属于 CSS 引入方式的有？**（多选）

A. 行内样式
B. 内部样式表
C. 外部样式表
D. @import 导入

**12. 下列属于复合选择器的有？**（多选）

A. 后代选择器（`A B`）
B. 子代选择器（`A > B`）
C. 相邻兄弟选择器（`A + B`）
D. 通用兄弟选择器（`A ~ B`）

**13. 下列属于 position 取值的有？**（多选）

A. static
B. relative
C. absolute
D. sticky

**14. 下列属于 Flex 容器属性的有？**（多选）

A. flex-direction
B. justify-content
C. align-items
D. flex-wrap

**15. 下列属于清除浮动方法的有？**（多选）

A. 父元素设置 `overflow: hidden`
B. 添加额外标签并设置 `clear: both`
C. 使用 clearfix 伪元素
D. 父元素设置 `float: left`

## 三、判断题（每题 2 分，共 5 题）

**16. `!important` 的优先级高于行内样式。**

**17. `box-sizing: border-box` 模式下，width 包含 content + padding + border，但不包含 margin。**

**18. `position: relative` 会让元素脱离文档流。**

**19. Flex 布局默认主轴方向为水平方向（row）。**

**20. 移动端响应式页面需在 head 设置 `<meta name="viewport">` 以控制视口。**

## 四、简答题（每题 5 分，共 4 题）

**21. 列举 CSS 的三种基本引入方式，并说明它们的优先级关系。**

**22. 计算以下选择器的优先级：`#nav .item a:hover` 与 `div.menu a`。**

**23. 说明标准盒模型与 IE 盒模型（border-box）的区别，box-sizing 如何切换？**

**24. 使用 Flex 实现一个元素水平垂直居中，写出关键 CSS。**

## 五、编程题（每题 8 分，共 4 题）

**25. 编写完整 HTML+CSS 实现一个横向导航栏：5 个菜单项横向排列，鼠标悬停时背景变色，去除列表默认样式。**

**26. 编写完整 HTML+CSS 实现一个卡片布局：3 张卡片横向排列（使用 Flex），每张卡片含图片、标题、描述，卡片间有间距，卡片有边框和圆角。**

**27. 编写完整 HTML+CSS 实现一个响应式两栏布局：宽屏时左右两栏并排（左侧固定宽度 200px，右侧自适应），窄屏（≤768px）时上下堆叠。**

**28. 编写完整 HTML+CSS 实现一个 sticky 页头：页面滚动时顶部导航栏固定在视口顶部（使用 `position: sticky`）。**

## 六、综合题（每题 12 分，共 2 题）

**29. 综合设计：某电商网站需要商品列表页布局，要求：**
- 顶部页头（含 Logo 和搜索框）
- 商品列表（4 列网格，每项含图片、名称、价格、加入购物车按钮）
- 卡片有阴影、圆角、悬停上浮效果
- 移动端（≤768px）变为 2 列，超小屏（≤480px）变为 1 列

请编写完整 HTML+CSS 代码。

**30. 综合设计：编写一个完整的响应式个人主页，要求：**
- 顶部 sticky 导航栏
- 主体分为左侧个人信息栏（头像、姓名、简介）和右侧内容栏（文章列表）
- 宽屏两栏并排，窄屏（≤768px）上下堆叠
- 使用 Flex 布局和媒体查询
- 包含盒模型、圆角、阴影等样式

请编写完整 HTML+CSS 代码。

## 答案与解析

<details>
<summary>点击展开答案与解析</summary>

### 单选题答案

**1. 答案：C**
解析：行内样式（style 属性）优先级最高，其次是 ID、类、标签。@import 优先级最低。

**2. 答案：B**
解析：优先级顺序为 `!important > 行内 > ID > 类 > 标签`。

**3. 答案：B**
解析：`:hover` 是伪类（单冒号）。`::before`、`::after`、`::first-line` 是伪元素（双冒号）。

**4. 答案：C**
解析：`::before` 是伪元素。`:hover`、`:first-child`、`:nth-child(n)` 都是伪类。

**5. 答案：B**
解析：盒模型由内到外为 content → padding → border → margin。

**6. 答案：C**
解析：border-box 模式下 width 包含 content + padding + border，不包含 margin。

**7. 答案：C**
解析：absolute 会脱离文档流。static 是默认定位，relative 不脱离文档流，sticky 在阈值内保持。fixed 也脱离文档流但选项中只有 absolute。

**8. 答案：C**
解析：flex-direction 设置主轴方向（row/column）。

**9. 答案：C**
解析：space-between 实现两端对齐，首尾贴边，中间间距均匀。

**10. 答案：B**
解析：`max-width: 768px` 表示屏幕宽度小于等于 768px 时应用样式。

### 多选题答案

**11. 答案：ABCD**
解析：行内、内部、外部、@import 都是 CSS 引入方式。

**12. 答案：ABCD**
解析：后代、子代、相邻兄弟、通用兄弟都是复合选择器。

**13. 答案：ABCD**
解析：static、relative、absolute、sticky（以及 fixed）都是 position 取值。

**14. 答案：ABCD**
解析：flex-direction、justify-content、align-items、flex-wrap 都是 Flex 容器属性。

**15. 答案：ABC**
解析：overflow:hidden、额外标签 clear:both、clearfix 伪元素都是清除浮动的方法。D 错误，父元素 float 不能清除子元素浮动。

### 判断题答案

**16. 答案：正确（√）**
解析：`!important` 优先级最高，高于行内样式。

**17. 答案：正确（√）**
解析：border-box 的 width 包含 content + padding + border，不含 margin。

**18. 答案：错误（×）**
解析：relative 不脱离文档流，元素仍占据原位置，只是相对原位置偏移。absolute 和 fixed 才脱离文档流。

**19. 答案：正确（√）**
解析：Flex 默认 flex-direction: row，主轴为水平方向。

**20. 答案：正确（√）**
解析：移动端需设置 `<meta name="viewport" content="width=device-width, initial-scale=1.0">` 控制视口。

### 简答题参考答案

**21. 参考答案**
三种引入方式：行内样式（style 属性）、内部样式表（`<style>` 标签）、外部样式表（`<link>` 引入 .css 文件）。优先级：行内样式 > 内部样式表 = 外部样式表（后者取决于书写顺序，后写的覆盖先写的）。注意 @import 引入的外部样式优先级低于 link。所有这些都低于 `!important`。

**22. 参考答案**
优先级按 (ID, 类, 标签) 三元组计算：
- `#nav .item a:hover` = (1, 2, 1)（1 个 ID + 2 个类/伪类 + 1 个标签）
- `div.menu a` = (0, 1, 2)（1 个类 + 2 个标签）

比较：先比 ID 数，(1,2,1) > (0,1,2)，故 `#nav .item a:hover` 优先级更高。

**23. 参考答案**
- 标准盒模型（content-box）：width/height 只包含 content，实际占用宽度 = content + padding + border + margin。
- IE 盒模型（border-box）：width/height 包含 content + padding + border，实际占用宽度 = width + margin。

通过 `box-sizing: content-box`（默认）或 `box-sizing: border-box` 切换。实际开发常全局设置 border-box 以简化尺寸计算。

**24. 参考答案**
```css
.parent {
    display: flex;
    justify-content: center;
    align-items: center;
}
```
也可在父容器设 `display: flex`，子元素设 `margin: auto`。

### 编程题参考答案

**25. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>横向导航栏</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        .nav {
            list-style: none;
            display: flex;
            background: #333;
        }
        .nav li a {
            display: block;
            padding: 14px 20px;
            color: #fff;
            text-decoration: none;
        }
        .nav li a:hover {
            background: #555;
        }
    </style>
</head>
<body>
    <ul class="nav">
        <li><a href="#">首页</a></li>
        <li><a href="#">产品</a></li>
        <li><a href="#">服务</a></li>
        <li><a href="#">关于</a></li>
        <li><a href="#">联系</a></li>
    </ul>
</body>
</html>
```

**26. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>卡片布局</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { padding: 20px; }
        .card-container {
            display: flex;
            gap: 20px;
        }
        .card {
            flex: 1;
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
        }
        .card img {
            width: 100%;
            height: 160px;
            object-fit: cover;
        }
        .card-body {
            padding: 16px;
        }
        .card-body h3 {
            margin-bottom: 8px;
        }
        .card-body p {
            color: #666;
            line-height: 1.5;
        }
    </style>
</head>
<body>
    <div class="card-container">
        <div class="card">
            <img src="https://via.placeholder.com/300x160" alt="卡片1">
            <div class="card-body">
                <h3>卡片标题1</h3>
                <p>这是卡片1的描述内容。</p>
            </div>
        </div>
        <div class="card">
            <img src="https://via.placeholder.com/300x160" alt="卡片2">
            <div class="card-body">
                <h3>卡片标题2</h3>
                <p>这是卡片2的描述内容。</p>
            </div>
        </div>
        <div class="card">
            <img src="https://via.placeholder.com/300x160" alt="卡片3">
            <div class="card-body">
                <h3>卡片标题3</h3>
                <p>这是卡片3的描述内容。</p>
            </div>
        </div>
    </div>
</body>
</html>
```

**27. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>响应式两栏布局</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        .container {
            display: flex;
            padding: 20px;
            gap: 20px;
        }
        .sidebar {
            width: 200px;
            flex-shrink: 0;
            background: #f0f0f0;
            padding: 16px;
        }
        .main {
            flex: 1;
            background: #fafafa;
            padding: 16px;
        }
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
            }
            .sidebar {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <aside class="sidebar">
            <h3>侧边栏</h3>
            <p>菜单项1</p>
            <p>菜单项2</p>
        </aside>
        <main class="main">
            <h3>主内容</h3>
            <p>这里是主内容区域，宽屏时自适应剩余空间。</p>
        </main>
    </div>
</body>
</html>
```

**28. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Sticky 页头</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        .header {
            position: sticky;
            top: 0;
            background: #333;
            color: #fff;
            padding: 16px 20px;
            z-index: 100;
        }
        .header nav a {
            color: #fff;
            margin-right: 20px;
            text-decoration: none;
        }
        .content {
            padding: 20px;
            line-height: 2;
        }
    </style>
</head>
<body>
    <header class="header">
        <nav>
            <a href="#">首页</a>
            <a href="#">产品</a>
            <a href="#">关于</a>
        </nav>
    </header>
    <div class="content">
        <p>滚动页面时，顶部导航栏会固定在视口顶部。</p>
        <p>向下滚动查看效果...</p>
        <p>内容1</p><p>内容2</p><p>内容3</p>
        <p>内容4</p><p>内容5</p><p>内容6</p>
        <p>内容7</p><p>内容8</p><p>内容9</p>
        <p>内容10</p><p>内容11</p><p>内容12</p>
    </div>
</body>
</html>
```

### 综合题参考答案

**29. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>商品列表页</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #f5f5f5; }
        .header {
            display: flex;
            align-items: center;
            padding: 16px 24px;
            background: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .logo { font-size: 24px; font-weight: bold; margin-right: 40px; }
        .search {
            flex: 1;
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .product-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            padding: 24px;
        }
        .product-card {
            background: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.15);
        }
        .product-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .product-info { padding: 16px; }
        .product-name { font-size: 16px; margin-bottom: 8px; }
        .product-price { color: #e74c3c; font-size: 18px; font-weight: bold; margin-bottom: 12px; }
        .btn {
            display: block;
            width: 100%;
            padding: 8px;
            background: #e74c3c;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        @media (max-width: 768px) {
            .product-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 480px) {
            .product-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="logo">Shop</div>
        <input class="search" type="text" placeholder="搜索商品...">
    </header>
    <div class="product-grid">
        <div class="product-card">
            <img src="https://via.placeholder.com/300x200" alt="商品1">
            <div class="product-info">
                <div class="product-name">商品名称1</div>
                <div class="product-price">¥99</div>
                <button class="btn">加入购物车</button>
            </div>
        </div>
        <div class="product-card">
            <img src="https://via.placeholder.com/300x200" alt="商品2">
            <div class="product-info">
                <div class="product-name">商品名称2</div>
                <div class="product-price">¥199</div>
                <button class="btn">加入购物车</button>
            </div>
        </div>
        <div class="product-card">
            <img src="https://via.placeholder.com/300x200" alt="商品3">
            <div class="product-info">
                <div class="product-name">商品名称3</div>
                <div class="product-price">¥299</div>
                <button class="btn">加入购物车</button>
            </div>
        </div>
        <div class="product-card">
            <img src="https://via.placeholder.com/300x200" alt="商品4">
            <div class="product-info">
                <div class="product-name">商品名称4</div>
                <div class="product-price">¥399</div>
                <button class="btn">加入购物车</button>
            </div>
        </div>
    </div>
</body>
</html>
```

**30. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>响应式个人主页</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #f5f5f5; }
        .navbar {
            position: sticky;
            top: 0;
            display: flex;
            background: #2c3e50;
            padding: 14px 24px;
            z-index: 100;
        }
        .navbar a {
            color: #fff;
            text-decoration: none;
            margin-right: 24px;
        }
        .container {
            display: flex;
            gap: 24px;
            padding: 24px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .sidebar {
            flex: 0 0 280px;
            background: #fff;
            border-radius: 8px;
            padding: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            text-align: center;
        }
        .avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            margin: 0 auto 16px;
            background: #ecf0f1;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
        }
        .sidebar h2 { margin-bottom: 8px; }
        .sidebar p { color: #666; line-height: 1.6; }
        .content {
            flex: 1;
            background: #fff;
            border-radius: 8px;
            padding: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .article {
            padding: 16px 0;
            border-bottom: 1px solid #eee;
        }
        .article:last-child { border-bottom: none; }
        .article h3 { margin-bottom: 8px; }
        .article p { color: #555; line-height: 1.6; }
        @media (max-width: 768px) {
            .container { flex-direction: column; }
            .sidebar { flex: 0 0 auto; }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <a href="#">首页</a>
        <a href="#">文章</a>
        <a href="#">项目</a>
        <a href="#">联系</a>
    </nav>
    <div class="container">
        <aside class="sidebar">
            <div class="avatar">👤</div>
            <h2>张三</h2>
            <p>Web 开发工程师，热爱前端技术与开源社区。</p>
        </aside>
        <main class="content">
            <div class="article">
                <h3>文章标题1</h3>
                <p>这是文章1的摘要内容，介绍 Web 开发的相关知识。</p>
            </div>
            <div class="article">
                <h3>文章标题2</h3>
                <p>这是文章2的摘要内容，分享 CSS 布局技巧。</p>
            </div>
            <div class="article">
                <h3>文章标题3</h3>
                <p>这是文章3的摘要内容，探讨 JavaScript 最佳实践。</p>
            </div>
        </main>
    </div>
</body>
</html>
```

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| --- | --- | --- | --- |
| 单选题 | 10 | 20 | 基础概念识别（引入、选择器、盒模型、定位、Flex、媒体查询） |
| 多选题 | 5 | 15 | 综合属性辨析（引入方式、复合选择器、定位、Flex、清除浮动） |
| 判断题 | 5 | 10 | 易混点辨析（!important、border-box、relative、Flex 主轴、viewport） |
| 简答题 | 4 | 20 | 核心知识复述（引入优先级、优先级计算、盒模型、Flex 居中） |
| 编程题 | 4 | 32 | 实战编码（导航栏、卡片、响应式两栏、sticky 页头） |
| 综合题 | 2 | 24 | 综合应用（商品列表页、响应式主页） |
| 合计 | 30 | 121 | 覆盖第3章全部核心考点 |

## 章节导航

- 上一级：[[MOC - Web开发技术]]
- 本章知识点：[[MOC - 第3章]]
- 上一章习题：[[MOC - 第2章习题]]
- 下一章习题：[[MOC - 第4章习题]]
