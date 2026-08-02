---
domain: 软件工程
subject: Web开发技术
type: exercise
chapter: 第2章 HTML基础
section: 2.1 HTML文档结构
tags: [Web开发,习题,HTML,CSS,JavaScript]
prerequisites: []
---

# MOC - 第2章习题

> [!info] 习题说明
> 本章习题覆盖 HTML 文档结构、语义化标签、标题段落、列表、超链接、图片、表格（合并单元格）、表单（input 类型/select/textarea）、表单验证属性、audio/video/iframe 等知识点。题目包含编程题，要求编写完整 HTML 页面，答案与解析折叠在 `<details>` 中。

## 知识点覆盖表

| 题号 | 题型 | 知识点 | 对应笔记 |
| --- | --- | --- | --- |
| 1 | 单选 | HTML 文档结构 | [[2.1 HTML文档结构]] |
| 2 | 单选 | DOCTYPE 作用 | [[2.1 HTML文档结构]] |
| 3 | 单选 | 语义化标签 | [[2.1 HTML文档结构]] |
| 4 | 单选 | 超链接 target 属性 | [[2.2 常用标签使用]] |
| 5 | 单选 | 图片标签属性 | [[2.2 常用标签使用]] |
| 6 | 单选 | 表格合并单元格 | [[2.2 常用标签使用]] |
| 7 | 单选 | input 类型 | [[2.3 表单与多媒体标签]] |
| 8 | 单选 | 表单验证属性 | [[2.3 表单与多媒体标签]] |
| 9 | 单选 | select 下拉框 | [[2.3 表单与多媒体标签]] |
| 10 | 单选 | video 标签属性 | [[2.3 表单与多媒体标签]] |
| 11 | 多选 | head 内元素 | [[2.1 HTML文档结构]] |
| 12 | 多选 | 语义化标签 | [[2.1 HTML文档结构]] |
| 13 | 多选 | 表单 input 类型 | [[2.3 表单与多媒体标签]] |
| 14 | 多选 | 表单验证属性 | [[2.3 表单与多媒体标签]] |
| 15 | 多选 | audio/video 属性 | [[2.3 表单与多媒体标签]] |
| 16 | 判断 | html 根元素 | [[2.1 HTML文档结构]] |
| 17 | 判断 | strong vs em | [[2.2 常用标签使用]] |
| 18 | 判断 | colspan 合并方向 | [[2.2 常用标签使用]] |
| 19 | 判断 | textarea 用途 | [[2.3 表单与多媒体标签]] |
| 20 | 判断 | iframe 作用 | [[2.3 表单与多媒体标签]] |
| 21 | 简答 | HTML 文档结构 | [[2.1 HTML文档结构]] |
| 22 | 简答 | 语义化标签 | [[2.1 HTML文档结构]] |
| 23 | 简答 | colspan/rowspan | [[2.2 常用标签使用]] |
| 24 | 简答 | enctype 取值 | [[2.3 表单与多媒体标签]] |
| 25 | 编程 | 个人简历页 | [[2.2 常用标签使用]] |
| 26 | 编程 | 用户注册表单 | [[2.3 表单与多媒体标签]] |
| 27 | 编程 | 课程表页面 | [[2.2 常用标签使用]] |
| 28 | 编程 | 多媒体页面 | [[2.3 表单与多媒体标签]] |
| 29 | 综合 | 表单综合设计 | [[2.3 表单与多媒体标签]] |
| 30 | 综合 | 完整页面结构 | [[2.1 HTML文档结构]] |

## 一、单选题（每题 2 分，共 10 题）

**1. HTML 文档的根元素是？**

A. `<head>`
B. `<body>`
C. `<html>`
D. `<doctype>`

**2. `<!DOCTYPE html>` 的作用是？**

A. 声明文档编码
B. 告诉浏览器使用 HTML5 标准模式解析
C. 引入外部 CSS
D. 定义文档标题

**3. 下列哪个是 HTML5 语义化标签？**

A. `<div>`
B. `<span>`
C. `<article>`
D. `<b>`

**4. 超链接在新标签页打开的 target 属性值是？**

A. `_self`
B. `_blank`
C. `_parent`
D. `_top`

**5. `<img>` 标签必须包含的属性是？**

A. alt 和 title
B. src 和 alt
C. width 和 height
D. href 和 alt

**6. 表格中实现"跨 2 列合并"的属性是？**

A. `colspan="2"`
B. `rowspan="2"`
C. `cols="2"`
D. `rows="2"`

**7. 用于输入邮箱且自带格式校验的 input 类型是？**

A. `type="text"`
B. `type="email"`
C. `type="mail"`
D. `type="url"`

**8. 表单中限制输入必填的属性是？**

A. `required`
B. `required="true"`
C. `must`
D. `mandatory`

**9. 下拉框 `<select>` 中定义选项的标签是？**

A. `<option>`
B. `<item>`
C. `<li>`
D. `<choice>`

**10. `<video>` 标签中设置自动播放的属性是？**

A. `play`
B. `autoplay`
C. `auto`
D. `start`

## 二、多选题（每题 3 分，共 5 题）

**11. 下列属于 `<head>` 内常见元素的有？**（多选）

A. `<title>`
B. `<meta>`
C. `<link>`
D. `<script>`

**12. 下列属于 HTML5 语义化标签的有？**（多选）

A. `<header>`
B. `<nav>`
C. `<section>`
D. `<div>`

**13. 下列属于 input 类型的有？**（多选）

A. `text`
B. `password`
C. `checkbox`
D. `radio`

**14. 下列属于表单验证属性的有？**（多选）

A. `required`
B. `pattern`
C. `minlength`
D. `maxlength`

**15. 下列属于 audio/video 标签属性的有？**（多选）

A. `controls`
B. `autoplay`
C. `loop`
D. `muted`

## 三、判断题（每题 2 分，共 5 题）

**16. 每个 HTML 文档只能有一个 `<html>` 根元素。**

**17. `<strong>` 表示重要性强调（加粗），`<em>` 表示语气强调（斜体），二者语义不同。**

**18. `colspan` 用于跨行合并，`rowspan` 用于跨列合并。**

**19. `<textarea>` 用于输入多行文本，`<input type="text">` 用于输入单行文本。**

**20. `<iframe>` 用于在当前页面内嵌套另一个网页。**

## 四、简答题（每题 5 分，共 4 题）

**21. 简述 HTML 文档的标准结构，并说明 `<!DOCTYPE html>` 的作用。**

**22. 列举至少五个 HTML5 语义化标签并说明其语义。**

**23. 说明表格中 colspan 和 rowspan 属性的作用，并各举一例。**

**24. 表单提交时 GET 与 POST 方法的区别是什么？enctype 有哪些常见取值？**

## 五、编程题（每题 8 分，共 4 题）

**25. 编写一个完整的个人简历 HTML 页面，要求包含：姓名（标题）、基本信息（段落）、技能列表（无序列表）、学习经历（有序列表）、自我评价（段落）。**

**26. 编写一个用户注册表单 HTML 页面，要求包含：用户名（文本）、邮箱（email 类型）、密码（password）、确认密码、性别（单选）、爱好（多选）、城市（下拉框）、个人简介（文本域）、同意协议（复选框）、提交与重置按钮，并使用 required、pattern 等验证属性。**

**27. 编写一个课程表 HTML 页面，使用 table 标签，要求包含表头（星期一至星期五），至少 4 节课，并使用 colspan 或 rowspan 合并单元格（如午休行跨 5 列）。**

**28. 编写一个多媒体展示 HTML 页面，要求包含：一段音频（audio，带 controls）、一段视频（video，带 controls 和 poster）、一个 iframe 嵌入外部网页（如 example.com）。**

## 六、综合题（每题 12 分，共 2 题）

**29. 综合设计：某在线书店需要一个图书信息录入表单，要求：**
- 书名（文本，必填）
- ISBN（文本，必填，使用 pattern 校验 13 位数字）
- 类别（下拉框：文学/科技/教育/艺术）
- 价格（number 类型，最小值 0，必填）
- 是否上架（单选：是/否）
- 封面图片（文件上传）
- 内容简介（文本域，最多 500 字）
- 提交按钮

请编写完整 HTML 代码，并说明使用了哪些表单验证手段。

**30. 综合设计：编写一个完整的"个人博客首页"HTML 页面，要求：**
- 使用语义化标签（header/nav/main/article/section/aside/footer）
- header 包含网站标题和导航
- main 包含至少两篇文章（article），每篇含标题、发布时间、正文
- aside 包含"关于我"和"友情链接"
- footer 包含版权信息
- 至少使用一种列表和一种图片

请编写完整 HTML 代码，并说明各语义化标签的作用。

## 答案与解析

<details>
<summary>点击展开答案与解析</summary>

### 单选题答案

**1. 答案：C**
解析：`<html>` 是 HTML 文档的根元素，包含 `<head>` 和 `<body>`。

**2. 答案：B**
解析：`<!DOCTYPE html>` 告诉浏览器使用 HTML5 标准模式解析，不写会触发怪异模式。

**3. 答案：C**
解析：`<article>` 是 HTML5 语义化标签。`<div>`、`<span>` 是无语义容器，`<b>` 仅是文本格式化标签。

**4. 答案：B**
解析：`target="_blank"` 在新标签页打开；`_self` 在当前页打开。

**5. 答案：B**
解析：`<img>` 必须包含 src（图片路径）和 alt（替代文本，用于无障碍和图片加载失败时显示）。

**6. 答案：A**
解析：`colspan="2"` 实现跨 2 列合并；`rowspan` 用于跨行。

**7. 答案：B**
解析：`type="email"` 自带邮箱格式校验。

**8. 答案：A**
解析：`required` 是布尔属性，存在即表示必填。

**9. 答案：A**
解析：`<option>` 标签定义下拉框选项。

**10. 答案：B**
解析：`autoplay` 属性设置自动播放。

### 多选题答案

**11. 答案：ABCD**
解析：title、meta、link、script 都是 head 内常见元素。

**12. 答案：ABC**
解析：header、nav、section 是语义化标签。`<div>` 是无语义容器。

**13. 答案：ABCD**
解析：text、password、checkbox、radio 都是 input 类型。

**14. 答案：ABCD**
解析：required、pattern、minlength、maxlength 都是表单验证属性。

**15. 答案：ABCD**
解析：controls（控制条）、autoplay（自动播放）、loop（循环）、muted（静音）都是 audio/video 属性。

### 判断题答案

**16. 答案：正确（√）**
解析：HTML 文档只有一个 `<html>` 根元素。

**17. 答案：正确（√）**
解析：`<strong>` 表示重要性（加粗），`<em>` 表示语气强调（斜体），语义不同。

**18. 答案：错误（×）**
解析：相反。`colspan` 用于跨列合并，`rowspan` 用于跨行合并。

**19. 答案：正确（√）**
解析：textarea 用于多行文本，input text 用于单行文本。

**20. 答案：正确（√）**
解析：iframe 用于在页面内嵌套另一个网页。

### 简答题参考答案

**21. 参考答案**
标准结构包含 `<!DOCTYPE html>`、`<html>`（根元素）、`<head>`（头部含元信息）、`<body>`（主体内容）。`<!DOCTYPE html>` 告诉浏览器使用 HTML5 标准模式解析，不写会触发怪异模式，导致渲染不一致。

**22. 参考答案**
- header：页头/标题区
- nav：导航栏
- main：主要内容
- article：独立文章内容
- section：内容分区块
- aside：侧边栏/附属信息
- footer：页脚

语义化标签提升可读性与可访问性，利于 SEO 与屏幕阅读器。

**23. 参考答案**
colspan（跨列合并）让单元格横向占据多列，如 `<td colspan="2">` 占两列宽度；rowspan（跨行合并）让单元格纵向占据多行，如 `<td rowspan="3">` 占三行高度。合并后需删除被合并的对应单元格。

**24. 参考答案**
GET 将表单数据拼接在 URL 后以查询字符串提交，可见且有长度限制，适合查询；POST 将数据放在请求体中，相对安全且无长度限制，适合提交敏感或大量数据。enctype 常见取值：`application/x-www-form-urlencoded`（默认）、`multipart/form-data`（文件上传）、`text/plain`（纯文本，少用）。

### 编程题参考答案

**25. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>个人简历</title>
</head>
<body>
    <h1>张三</h1>
    <p>性别：男 | 年龄：22 | 邮箱：zhangsan@example.com | 电话：13800000000</p>

    <h2>技能列表</h2>
    <ul>
        <li>HTML5 / CSS3</li>
        <li>JavaScript / ES6+</li>
        <li>Vue.js / React</li>
        <li>Node.js</li>
    </ul>

    <h2>学习经历</h2>
    <ol>
        <li>2018-2021 XX大学 计算机科学与技术 本科</li>
        <li>2021-2024 XX大学 软件工程 硕士</li>
    </ol>

    <h2>自我评价</h2>
    <p>热爱 Web 开发，具备扎实的前端基础与良好的工程习惯，善于团队协作与持续学习。</p>
</body>
</html>
```

**26. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>用户注册</title>
</head>
<body>
    <h1>用户注册</h1>
    <form action="/register" method="post">
        <p>
            用户名：<input type="text" name="username" required minlength="3" maxlength="20">
        </p>
        <p>
            邮箱：<input type="email" name="email" required>
        </p>
        <p>
            密码：<input type="password" name="password" required minlength="6">
        </p>
        <p>
            确认密码：<input type="password" name="confirm" required minlength="6">
        </p>
        <p>
            性别：
            <label><input type="radio" name="gender" value="male" checked> 男</label>
            <label><input type="radio" name="gender" value="female"> 女</label>
        </p>
        <p>
            爱好：
            <label><input type="checkbox" name="hobby" value="reading"> 阅读</label>
            <label><input type="checkbox" name="hobby" value="music"> 音乐</label>
            <label><input type="checkbox" name="hobby" value="sports"> 运动</label>
        </p>
        <p>
            城市：
            <select name="city">
                <option value="beijing">北京</option>
                <option value="shanghai">上海</option>
                <option value="guangzhou">广州</option>
            </select>
        </p>
        <p>
            个人简介：<br>
            <textarea name="intro" rows="5" cols="40" maxlength="200"></textarea>
        </p>
        <p>
            <label><input type="checkbox" name="agree" value="yes" required> 同意《用户协议》</label>
        </p>
        <p>
            <input type="submit" value="注册">
            <input type="reset" value="重置">
        </p>
    </form>
</body>
</html>
```

**27. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>课程表</title>
</head>
<body>
    <h1>课程表</h1>
    <table border="1" cellpadding="8">
        <thead>
            <tr>
                <th>节次</th>
                <th>星期一</th>
                <th>星期二</th>
                <th>星期三</th>
                <th>星期四</th>
                <th>星期五</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>第1节</td>
                <td>语文</td>
                <td>数学</td>
                <td>英语</td>
                <td>物理</td>
                <td>化学</td>
            </tr>
            <tr>
                <td>第2节</td>
                <td>数学</td>
                <td>语文</td>
                <td>物理</td>
                <td>英语</td>
                <td>生物</td>
            </tr>
            <tr>
                <td colspan="6" style="text-align:center; background:#eee;">午休</td>
            </tr>
            <tr>
                <td>第3节</td>
                <td>英语</td>
                <td>化学</td>
                <td>数学</td>
                <td>语文</td>
                <td>物理</td>
            </tr>
            <tr>
                <td rowspan="2">第4节</td>
                <td>物理</td>
                <td>生物</td>
                <td>语文</td>
                <td>数学</td>
                <td>英语</td>
            </tr>
            <tr>
                <td>自习</td>
                <td>自习</td>
                <td>自习</td>
                <td>自习</td>
                <td>自习</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```

**28. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>多媒体展示</title>
</head>
<body>
    <h1>多媒体展示</h1>

    <h2>音频</h2>
    <audio controls>
        <source src="audio/song.mp3" type="audio/mpeg">
        您的浏览器不支持 audio 标签。
    </audio>

    <h2>视频</h2>
    <video controls poster="images/poster.jpg" width="480">
        <source src="video/demo.mp4" type="video/mp4">
        您的浏览器不支持 video 标签。
    </video>

    <h2>嵌入网页</h2>
    <iframe src="https://example.com" width="600" height="400" title="外部网页"></iframe>
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
    <title>图书信息录入</title>
</head>
<body>
    <h1>图书信息录入</h1>
    <form action="/book/add" method="post" enctype="multipart/form-data">
        <p>
            书名：<input type="text" name="title" required>
        </p>
        <p>
            ISBN：<input type="text" name="isbn" required pattern="\d{13}" title="请输入13位数字">
        </p>
        <p>
            类别：
            <select name="category">
                <option value="literature">文学</option>
                <option value="tech">科技</option>
                <option value="edu">教育</option>
                <option value="art">艺术</option>
            </select>
        </p>
        <p>
            价格：<input type="number" name="price" min="0" step="0.01" required>
        </p>
        <p>
            是否上架：
            <label><input type="radio" name="onsale" value="yes" checked> 是</label>
            <label><input type="radio" name="onsale" value="no"> 否</label>
        </p>
        <p>
            封面图片：<input type="file" name="cover" accept="image/*">
        </p>
        <p>
            内容简介：<br>
            <textarea name="desc" rows="5" cols="50" maxlength="500"></textarea>
        </p>
        <p>
            <input type="submit" value="提交">
        </p>
    </form>
</body>
</html>
```
使用的验证手段：
- `required`：书名、ISBN、价格为必填
- `pattern="\d{13}"`：ISBN 校验 13 位数字
- `min="0"`：价格最小值 0
- `type="number"`：价格只能输入数字
- `type="file" accept="image/*"`：限制只能上传图片
- `maxlength="500"`：内容简介最多 500 字
- `enctype="multipart/form-data"`：支持文件上传

**30. 参考答案**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>个人博客</title>
</head>
<body>
    <header>
        <h1>我的技术博客</h1>
        <nav>
            <a href="/">首页</a> |
            <a href="/about">关于</a> |
            <a href="/contact">联系</a>
        </nav>
    </header>

    <main>
        <article>
            <h2>HTML 语义化标签详解</h2>
            <p><time datetime="2024-01-15">2024年1月15日</time></p>
            <p>语义化标签让页面结构更清晰，利于 SEO 和无障碍访问。</p>
            <img src="images/html5.png" alt="HTML5 标签示意图">
        </article>

        <article>
            <h2>CSS Flex 布局入门</h2>
            <p><time datetime="2024-01-20">2024年1月20日</time></p>
            <p>Flex 布局是现代 CSS 最强大的布局方式之一。</p>
        </article>
    </main>

    <aside>
        <section>
            <h3>关于我</h3>
            <p>Web 开发者，热爱前端技术。</p>
        </section>
        <section>
            <h3>友情链接</h3>
            <ul>
                <li><a href="https://developer.mozilla.org">MDN</a></li>
                <li><a href="https://www.w3.org">W3C</a></li>
            </ul>
        </section>
    </aside>

    <footer>
        <p>&copy; 2024 我的技术博客 | 版权所有</p>
    </footer>
</body>
</html>
```
各语义化标签作用：
- `<header>`：页面头部，含网站标题和导航
- `<nav>`：导航栏，包含主要导航链接
- `<main>`：页面主要内容区
- `<article>`：独立的文章内容，可单独分发
- `<section>`：内容分区块，用于组织相关内容
- `<aside>`：侧边栏，含附属信息（关于我、友情链接）
- `<footer>`：页脚，含版权信息

</details>

## 考点统计表

| 题型 | 题数 | 分值 | 考查重点 |
| --- | --- | --- | --- |
| 单选题 | 10 | 20 | 基础标签与属性识别 |
| 多选题 | 5 | 15 | 综合属性辨析（head、语义化、input、验证、媒体） |
| 判断题 | 5 | 10 | 易混点辨析（根元素、strong/em、合并方向、textarea、iframe） |
| 简答题 | 4 | 20 | 核心知识复述（结构、语义化、合并、enctype） |
| 编程题 | 4 | 32 | 实战编码（简历页、注册表单、课程表、多媒体） |
| 综合题 | 2 | 24 | 综合应用（图书录入表单、博客首页） |
| 合计 | 30 | 121 | 覆盖第2章全部核心考点 |

## 章节导航

- 上一级：[[MOC - Web开发技术]]
- 本章知识点：[[MOC - 第2章]]
- 上一章习题：[[MOC - 第1章习题]]
- 下一章习题：[[MOC - 第3章习题]]
