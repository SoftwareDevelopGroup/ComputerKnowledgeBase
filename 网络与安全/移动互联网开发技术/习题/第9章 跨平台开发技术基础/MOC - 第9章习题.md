---
domain: 网络与安全
subject: 移动互联网开发技术
type: exercise
chapter: 第9章 跨平台开发技术基础
tags: [移动开发,习题,跨平台,Flutter,React Native,WebView,选型对比]
prerequisites: ["计算机网络A","Java程序设计"]
aliases: [第9章习题, 跨平台习题, 第9章练习]
---

# MOC - 第9章习题

> [!info] 本章习题说明
> - 配套知识点：[[MOC - 第9章|第9章 跨平台开发技术基础]]
> - 题目数量：**15 题**（选择 5 + 填空 3 + 简答 4 + 分析题 3）
> - 难度梯度：⭐基础 / ⭐⭐中等 / ⭐⭐⭐较难
> - 答案折叠在每题下方的 `<details>` 块中，建议先独立作答再展开对照
> - 分析题含方案选型与代码阅读，需综合运用本章知识

## 一、选择题（5 题）

### 1. ⭐ 关于 WebView 混合开发，下列描述错误的是？

A. WebView 基于 Chromium 内核，可以在应用内渲染 H5 页面
B. `WebSettings` 用于配置内核行为，如启用 JS、设置缓存
C. `WebViewClient` 负责处理浏览器级交互，如进度条与弹窗
D. `addJavascriptInterface` 可将 Java 对象注入 JS，供 JS 直接调用

<details>
<summary>查看答案</summary>

**答案：C**

C 错：`WebViewClient` 负责处理**页面加载事件**（如 URL 拦截、页面开始/结束、SSL 错误）；`WebChromeClient` 才负责浏览器级交互（进度条、alert/confirm/prompt 弹窗、网页图标）。两者职责不可混淆。A、B、D 描述正确。
</details>

---

### 2. ⭐⭐ 关于 `addJavascriptInterface` 的安全风险，下列说法正确的是？

A. Android 4.2+ 已完全修复该漏洞，无任何安全风险
B. 该漏洞是因为 JS 能调用注入对象的所有公有方法，包括 `getClass()` 等系统方法
C. 使用 `@JavascriptInterface` 注解后无需做任何白名单校验
D. 该漏洞仅在加载 HTTPS 页面时存在

<details>
<summary>查看答案</summary>

**答案：B**

- A 错：Android 4.2+ 通过 `@JavascriptInterface` 注解限制了可调用方法，但仍有风险（如注入敏感对象、JS 注入攻击），需配合白名单校验
- B 对：Android 4.2 之前的漏洞正是 JS 能调用 `getClass()` 进而 `Runtime.exec()` 执行任意命令
- C 错：`@JavascriptInterface` 仅限制方法暴露，仍需做 URL 白名单校验、最小化注入方法
- D 错：漏洞与协议无关，HTTP/HTTPS 页面均存在
</details>

---

### 3. ⭐⭐ 关于 Flutter 的渲染机制，下列描述错误的是？

A. Flutter 不使用平台原生控件，而是通过自绘引擎直接绘制 UI
B. Widget 是不可变的配置描述，`setState()` 会创建新的 Widget 树
C. RenderObject 负责实际的测量、布局与绘制
D. Flutter 的 Widget 树直接负责绘制，无需 Element 与 RenderObject

<details>
<summary>查看答案</summary>

**答案：D**

D 错：Flutter 渲染涉及**三棵树协作**：Widget 树（配置）→ Element 树（实例）→ RenderObject 树（渲染）。Widget 只描述 UI 应该长什么样，不负责绘制；Element 是中间层管理生命周期；RenderObject 才真正负责测量、布局、绘制。A、B、C 描述正确。
</details>

---

### 4. ⭐⭐ 关于 React Native 的架构，下列说法正确的是？

A. RN 的 JS 代码运行在主线程，可直接调用原生控件
B. RN 旧架构的 Bridge 是同步通信，性能优秀
C. RN 的组件映射机制使其 UI 遵循各平台原生设计风格
D. Hermes 是 RN 的渲染引擎，替代了 Skia

<details>
<summary>查看答案</summary>

**答案：C**

- A 错：RN 是**三线程架构**：JS 线程运行业务代码，Native 线程渲染原生控件，JS 与 Native 通过 Bridge 通信，不能直接调用
- B 错：旧架构 Bridge 是**异步**通信（JSON 序列化），是性能瓶颈，新架构 JSI 才支持同步
- C 对：RN 用原生控件渲染，Android 上是 Material 风格，iOS 上是 UIKit 风格，遵循平台设计规范
- D 错：Hermes 是 **JS 引擎**（替代 JSC），不是渲染引擎。RN 用原生控件渲染，无独立渲染引擎
</details>

---

### 5. ⭐⭐ 关于跨平台方案选型，下列描述错误的是？

A. 包体积从大到小：Flutter > RN > 原生 ≈ WebView
B. 热更新支持：RN（CodePush）与 WebView 优于 Flutter 与原生
C. 性能从高到低：原生 > Flutter > RN > WebView
D. Flutter 的双端 UI 一致性最差，因为不自绘

<details>
<summary>查看答案</summary>

**答案：D**

D 错：Flutter 的双端 UI 一致性**最高**，正是因为它**自绘渲染**——同一套 Dart 代码画出的 UI 在 Android/iOS 上像素一致。RN 用原生控件映射，反而双端 UI 有差异。A、B、C 描述正确。
</details>

---

## 二、填空题（3 题）

### 6. ⭐ Flutter 的渲染涉及三棵树：________、________ 和 ________，其中 ________ 是开发者直接编写的不可变配置描述。

<details>
<summary>查看答案</summary>

**答案：Widget Tree、Element Tree、RenderObject Tree、Widget Tree**

- **Widget Tree**：开发者编写的 Widget 组成的树，是不可变的 UI 配置描述
- **Element Tree**：Widget 的实例化对象，管理生命周期，是 Widget 与 RenderObject 的桥梁
- **RenderObject Tree**：负责实际测量、布局、绘制
- `setState()` 会重建 Widget 树，Element 树通过 diff 复用，RenderObject 树只更新变化部分
</details>

---

### 7. ⭐⭐ React Native 的三线程架构包括 ________、________ 和 ________；旧架构通过 ________ 进行异步序列化通信，新架构引入 ________ 实现直接引用通信。

<details>
<summary>查看答案</summary>

**答案：JS 线程、Bridge（通信层）、Native 线程、Bridge、JSI**

- **JS 线程**：运行业务代码（JS/TS），计算 React 组件树
- **Bridge**：JS 与 Native 的通信层，旧架构是异步 JSON 序列化
- **Native 线程**：创建/更新原生控件，渲染到屏幕
- **JSI（JavaScript Interface）**：新架构让 JS 直接持有 C++ 对象引用，无需序列化，性能接近 Flutter
</details>

---

### 8. ⭐⭐ WebView 中 JS 调用 Java 的两种主要机制是 ________ 和 ________；前者通过 `@JavascriptInterface` 注解暴露方法，后者通过拦截 ________ 协议实现。

<details>
<summary>查看答案</summary>

**答案：addJavascriptInterface、URL Scheme 拦截、自定义 URL Scheme（或 jsbridge://）**

- **addJavascriptInterface**：将 Java 对象注入 JS，JS 直接调用 `window.X.method()`，需 `@JavascriptInterface` 注解（Android 4.2+）
- **URL Scheme 拦截**：JS 修改 `location.href` 触发自定义协议（如 `jsbridge://action?params=xxx`），原生在 `shouldOverrideUrlLoading` 中拦截
- 前者调用直接、可获取返回值；后者兼容性好但无法直接返回值（需原生回调 JS）
</details>

---

## 三、简答题（4 题）

### 9. ⭐⭐ 简述 WebView 混合开发中 JSBridge 的作用与异步回调机制。

<details>
<summary>查看答案</summary>

**JSBridge 的作用**：
JSBridge 是混合开发中"原生与 H5 双向通信"的工程化封装。它统一了通信协议、处理了异步回调、屏蔽了平台差异，是大型混合应用的核心基础设施。微信小程序的 `wx.*` API 本质上就是 JSBridge。

**异步回调机制**：
JS→Java 的调用通常是异步的（原生能力如网络、相机都需要时间）。JSBridge 通过"callbackId + 回调表"机制实现异步回调：

1. JS 调用 `JSBridge.call(action, params, callback)`，传入回调函数
2. JSBridge 给回调分配唯一 callbackId，存入回调表
3. 通过 `addJavascriptInterface` 或 URL Scheme 调用原生，传入 callbackId
4. 原生执行完毕后，用 `evaluateJavascript` 调用 `bridge.invokeCallback(callbackId, result)`
5. JSBridge 从回调表取出对应 callback 执行，并删除该条目

**意义**：这种机制让 JS 调用原生能力像调用异步函数一样自然，开发者无需关心底层通信细节。
</details>

---

### 10. ⭐⭐ 简述 Flutter 的三层架构（Framework/Engine/Embedder）各自职责，并说明为什么 Flutter 不使用平台原生控件。

<details>
<summary>查看答案</summary>

**三层架构职责**：

| 层次 | 语言 | 职责 |
| ---- | ---- | ---- |
| Framework 层 | Dart | 开发者直接接触，提供 Widget、动画、手势、绘制 API；含 Material/Cupertino 组件库 |
| Engine 层 | C/C++ | 提供 Dart 运行时（AOT/JIT）与图形渲染能力（Skia/Impeller），是跨平台核心 |
| Embedder 层 | 平台特定 | 将 Engine 嵌入具体平台，处理渲染上下文创建、输入事件、生命周期管理 |

**Flutter 不使用原生控件的原因**：

1. **双端一致性**：原生控件在 Android 与 iOS 上外观与行为不同，自绘可实现像素级一致
2. **性能可控**：自绘引擎直接调用 GPU，不依赖平台控件实现差异
3. **跨平台扩展**：同一套渲染逻辑可扩展到 Web、桌面、嵌入式
4. **设计自由度**：可实现任意自定义 UI，不受原生控件 API 限制

**代价**：包体积增大（需打包 Engine），UI 不完全遵循平台设计规范（需用 Material/Cupertino 双风格模拟），原生能力需通过 MethodChannel 桥接。
</details>

---

### 11. ⭐⭐ 对比 Flutter 与 React Native 在渲染机制、UI 一致性、性能、热更新四个维度的差异。

<details>
<summary>查看答案</summary>

| 维度 | Flutter | React Native |
| ---- | ------- | ------------ |
| **渲染机制** | 自绘引擎（Skia/Impeller）直接绘制，绕过原生控件 | JS 驱动原生控件渲染（View→android.view.View，Text→UILabel） |
| **UI 一致性** | 极高，双端像素一致（同一套 Dart 代码画出） | 中等，遵循各平台设计风格（Android Material / iOS UIKit） |
| **性能** | 接近原生，Dart AOT 编译为机器码，无 Bridge 开销 | 中等，旧架构 Bridge 异步序列化有开销；新架构 JSI 改善 |
| **热更新** | 不原生支持（受应用商店政策限制，需自研） | 支持，通过 CodePush 等方案可热更新 JS 代码 |

**本质差异**：
- Flutter 选择"绕过原生、自绘 UI"，换取一致性与性能，代价是不用真原生控件
- RN 选择"调用原生控件、JS 写逻辑"，换取原生体验与热更新，代价是 Bridge 通信开销

**选型倾向**：
- 重视 UI 一致性与性能 → Flutter
- 重视热更新与前端技能复用 → RN
</details>

---

### 12. ⭐⭐⭐ 简述跨平台方案选型决策树的核心判断逻辑，并说明大型 APP 为什么普遍采用混合架构而非单一方案。

<details>
<summary>查看答案</summary>

**选型决策树的核心判断逻辑**：

1. **是否需要深度系统能力**（传感器/后台服务/AR）？→ 是 → **原生开发**
2. **是否为内容展示型应用**（活动页/资讯/营销）？→ 是 → **WebView 混合**
3. **是否要求双端 UI 高度一致**（复杂动画/自定义绘制）？→ 是 → **Flutter**
4. **团队是否以 Web 为主**？→ 是 → **React Native**
5. **以上都不满足**？→ 按性能与复杂度选 **Flutter 或原生**

**核心逻辑**：选型不是"哪个方案最好"，而是"哪个方案最适合当前业务"。从"硬性约束"（系统能力）到"软性偏好"（团队技能）逐层筛选。

**大型 APP 采用混合架构的原因**：

1. **业务模块差异大**：不同模块有不同需求（活动页要快、核心页要性能），单一方案无法兼顾
2. **性能与动态化矛盾**：性能好的方案（原生/Flutter）不支持热更新；支持热更新的（RN/WebView）性能弱
3. **演进路径**：业务随时间演进，需预留模块替换空间，混合架构可逐步迁移
4. **风险分散**：单一方案风险集中（如 RN 架构升级可能导致全 App 受影响），混合架构可降级
5. **团队技能利用**：不同团队擅长的技术栈不同，混合架构可最大化复用

**典型实践**：
- 主框架用原生（保证基础体验）
- 业务模块按一致性需求选 Flutter/RN
- 活动页用 WebView/小程序（快速迭代）
- 核心性能模块用原生（视频/动画/相机）

如微信（原生+小程序+部分 Flutter）、淘宝（原生+Weex+H5）、美团（原生+Flutter+H5）。
</details>

---

## 四、分析题（3 题）

### 13. ⭐⭐ 方案选型分析

某创业团队要开发一款"在线教育 APP"，包含以下模块，请为每个模块选择最合适的技术方案并说明理由：

| 模块 | 特点 | 选型 | 理由 |
| ---- | ---- | ---- | ---- |
| 视频播放页 | 性能敏感，需硬件解码 | ? | ? |
| 课程列表页 | 内容展示，需频繁更新 | ? | ? |
| 直播间 | 实时交互，弹幕动画 | ? | ? |
| 营销活动页 | 限时活动，运营频繁改 | ? | ? |
| 用户个人中心 | 表单交互，双端一致 | ? | ? |

<details>
<summary>查看答案</summary>

| 模块 | 特点 | 选型 | 理由 |
| ---- | ---- | ---- | ---- |
| 视频播放页 | 性能敏感，需硬件解码 | **原生** | 视频编解码需调用 MediaCodec/AVFoundation，性能要求极高，跨平台方案无法胜任 |
| 课程列表页 | 内容展示，需频繁更新 | **Flutter** 或 **RN** | 列表性能要求中等，需双端一致；若团队前端为主选 RN，否则选 Flutter 性能更优 |
| 直播间 | 实时交互，弹幕动画 | **原生** 或 **Flutter** | 弹幕动画性能敏感，原生最优；Flutter 自绘动画性能接近原生且双端一致 |
| 营销活动页 | 限时活动，运营频繁改 | **WebView 混合** | 活动页生命周期短、需热更新、多端复用，H5 开发最快、运营可随时替换 |
| 用户个人中心 | 表单交互，双端一致 | **Flutter** | 表单交互性能要求中等，双端 UI 一致性重要，Flutter 一套代码双端一致 |

**整体架构建议**：
- **主框架**：原生（承载导航、视频播放等核心模块）
- **业务模块**：Flutter（课程列表、个人中心）
- **活动页**：WebView 容器（营销活动）
- **直播间**：原生（性能敏感）

**考核要点**：
- 能根据模块特性（性能要求、更新频率、一致性需求）选择方案
- 理解"大型 APP 普遍采用混合架构"的工程逻辑
- 不盲目选单一方案，而是按模块分层选型
</details>

---

### 14. ⭐⭐⭐ 代码阅读与分析

下列代码是某 APP 的 WebView 混合开发实现，请分析存在的问题并给出改进方案：

```java
// 代码片段 1:WebView 配置
public class WebActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        WebView webView = new WebView(this);
        setContentView(webView);

        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);                    // ①
        settings.setAllowFileAccess(true);                      // ②
        settings.setSavePassword(true);                         // ③

        webView.addJavascriptInterface(this, "AndroidNative");  // ④
        webView.setWebViewClient(new WebViewClient());
        webView.loadUrl(getIntent().getStringExtra("url"));     // ⑤
    }

    @JavascriptInterface
    public String readFile(String path) {                       // ⑥
        try {
            return new String(Files.readAllBytes(Paths.get(path)));
        } catch (Exception e) {
            return null;
        }
    }

    @JavascriptInterface
    public void execCmd(String cmd) {                           // ⑦
        Runtime.getRuntime().exec(cmd);
    }
}
```

<details>
<summary>查看答案</summary>

**问题分析与改进**：

| 编号 | 问题 | 风险 | 改进方案 |
| ---- | ---- | ---- | -------- |
| ① | 启用 JS 未做白名单 | 加载任意 URL 均可执行 JS | 加载前校验 URL 域名白名单 |
| ② | `setAllowFileAccess(true)` | `file://` 协议下 JS 可读取本地文件 | 改为 `false`，禁用 File 域 |
| ③ | `setSavePassword(true)` | 密码明文保存到数据库 | 改为 `false`（该 API 已废弃但仍需禁用） |
| ④ | 注入 `this`（Activity 对象） | 暴露 Activity 所有 `@JavascriptInterface` 方法，过度暴露 | 注入专用最小化对象，非 Activity |
| ⑤ | 直接加载 Intent 传入的 URL | 未校验，可被外部传入恶意 URL | 校验 URL 白名单，拒绝非预期域名 |
| ⑥ | `readFile` 可读任意路径 | 恶意 JS 可读取应用沙箱敏感数据 | 移除该方法，或限制可读目录白名单 |
| ⑦ | `execCmd` 可执行任意命令 | **严重漏洞**，恶意 JS 可执行任意系统命令 | **必须移除**，绝不应暴露命令执行能力 |

**改进后代码**：

```java
public class WebActivity extends Activity {
    private static final Set<String> ALLOWED_HOSTS = Set.of("m.example.com", "h5.example.com");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        WebView webView = new WebView(this);
        setContentView(webView);

        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setAllowFileAccess(false);          // ② 禁用 File 域
        settings.setSavePassword(false);             // ③ 禁用密码保存

        // ④ 注入最小化专用对象,而非 Activity
        webView.addJavascriptInterface(new JsBridge(this), "JsBridge");

        webView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView v, WebResourceRequest req) {
                // ⑤ 校验 URL 白名单
                String host = req.getUrl().getHost();
                if (!ALLOWED_HOSTS.contains(host)) {
                    return true;  // 拒绝非白名单
                }
                v.loadUrl(req.getUrl().toString());
                return true;
            }
        });

        String url = getIntent().getStringExtra("url");
        // ⑤ 加载前再校验
        if (ALLOWED_HOSTS.contains(Uri.parse(url).getHost())) {
            webView.loadUrl(url);
        }
    }
}

// ④ 最小化注入对象,仅暴露必要方法,不暴露文件读取/命令执行
public class JsBridge {
    private Context context;
    public JsBridge(Context context) { this.context = context; }

    @JavascriptInterface
    public void share(String title, String url) {
        // 仅暴露业务必要方法
    }

    @JavascriptInterface
    public String getToken() {
        // 返回受限的 Token,非任意文件
        return TokenManager.get();
    }
    // ⑥ ⑦ 移除 readFile 和 execCmd
}
```

**考核要点**：
- 能识别 WebView 安全配置问题（File 域、密码保存、白名单）
- 能识别 `addJavascriptInterface` 的过度暴露风险
- 能识别致命漏洞（`execCmd` 命令执行）
- 改进方案遵循"最小权限原则"：白名单校验、最小化注入、移除敏感方法
- 关联 [[8.4 权限最小化、恶意调用防范|8.4 权限最小化]] 的安全实践
</details>

---

### 15. ⭐⭐⭐ 综合分析：跨平台方案技术演进

某公司技术负责人在技术选型会上面临以下问题，请基于本章知识给出分析与建议：

**背景**：
- 团队现状：5 名 Android 原生开发 + 2 名 iOS 原生开发 + 3 名前端开发
- 业务场景：电商 APP，含商品详情、活动页、用户中心、直播
- 痛点：双端开发慢、活动页发版来不及、用户中心双端 UI 不一致

**问题**：
1. 是否应该全面迁移到 Flutter？为什么？
2. 活动页应该选什么方案？
3. 用户中心选 Flutter 还是 RN？说明理由
4. 直播模块选什么方案？
5. 给出整体混合架构建议

<details>
<summary>查看答案</summary>

**1. 是否全面迁移到 Flutter？**

**不建议全面迁移**。理由：
- 团队以原生开发为主（7 人），全面迁移会让原有技能闲置
- 直播、视频等性能敏感模块 Flutter 仍需原生桥接，不如直接原生
- 全面迁移成本高、风险大，应渐进式引入
- **建议**：保留原生主框架，按模块逐步引入 Flutter/RN

**2. 活动页方案**：**WebView 混合**
- 活动页生命周期短，运营频繁改，需热更新
- H5 开发最快，前端团队（3 人）可直接承担
- 多端复用（APP/小程序/浏览器）
- 配合离线包提升性能

**3. 用户中心：Flutter vs RN**

**建议选 Flutter**。理由：
- 用户中心是表单交互型，需双端 UI 一致（解决痛点）
- Flutter 自绘引擎双端像素一致，正好解决"双端 UI 不一致"痛点
- 性能要求中等，Flutter 完全胜任
- 虽然前端团队可上 RN，但 RN 双端 UI 不一致（用原生控件），不解决核心痛点
- **若团队强烈倾向 RN**：可用 RN + 自定义组件统一双端 UI，但成本高于 Flutter

**4. 直播模块**：**原生开发**
- 直播涉及视频编解码、推流、弹幕动画，性能敏感
- 需调用 MediaCodec/AVFoundation 等系统能力
- 跨平台方案（Flutter/RN）的视频能力仍依赖原生桥接
- 原生开发性能最优，且团队有 7 名原生开发可承担

**5. 整体混合架构建议**：

```
电商 APP 混合架构:
├── 原生主框架（导航、首页、直播、视频播放）
│   └── 7 名原生开发负责
├── Flutter 模块（用户中心、商品详情、订单流程）
│   └── 解决双端一致性问题,逐步由原生开发学习 Dart
├── WebView 容器（活动页、营销页、图文详情）
│   └── 3 名前端开发负责,支持热更新
└── 统一路由与通信层
    └── 模块间通过统一路由跳转,标准化通信协议
```

**关键实施建议**：
1. **渐进式迁移**：先从活动页（WebView）和用户中心（Flutter）入手，验证方案
2. **培训计划**：原生开发学习 Dart，前端学习 WebView 容器
3. **性能监控**：各方案启动时间、帧率、内存需统一监控
4. **降级方案**：跨端模块出问题时应能降级到原生或 H5
5. **避免重复**：通用能力（网络、存储、登录）下沉到原生层，各方案共享

**考核要点**：
- 能基于团队结构与业务需求做综合判断，而非盲目选热门方案
- 理解"混合架构"是大型 APP 的主流实践
- 能区分各方案的适用场景（活动页→WebView，一致性→Flutter，性能→原生）
- 提出渐进式迁移与培训计划，体现工程思维
</details>

---

## 考点统计与复习建议

### 考点分布统计表

| 题号 | 题型 | 涉及考点 | 难度 | 对应小节 |
| ---- | ---- | -------- | ---- | -------- |
| 1 | 选择 | WebView 三大组件职责 | ⭐ | [[9.1 WebView 混合开发\|9.1]] |
| 2 | 选择 | addJavascriptInterface 安全 | ⭐⭐ | [[9.1 WebView 混合开发\|9.1]] |
| 3 | 选择 | Flutter 渲染三棵树 | ⭐⭐ | [[9.2 Flutter 基础框架简介\|9.2]] |
| 4 | 选择 | RN 三线程架构 | ⭐⭐ | [[9.3 React Native 基础概念\|9.3]] |
| 5 | 选择 | 四方案特性对比 | ⭐⭐ | [[9.4 跨平台方案选型对比\|9.4]] |
| 6 | 填空 | Flutter 渲染三棵树 | ⭐ | [[9.2 Flutter 基础框架简介\|9.2]] |
| 7 | 填空 | RN 三线程与 JSI | ⭐⭐ | [[9.3 React Native 基础概念\|9.3]] |
| 8 | 填空 | WebView JS→Java 通信 | ⭐⭐ | [[9.1 WebView 混合开发\|9.1]] |
| 9 | 简答 | JSBridge 异步回调 | ⭐⭐ | [[9.1 WebView 混合开发\|9.1]] |
| 10 | 简答 | Flutter 三层架构 | ⭐⭐ | [[9.2 Flutter 基础框架简介\|9.2]] |
| 11 | 简答 | Flutter vs RN 四维度 | ⭐⭐ | [[9.2 Flutter 基础框架简介\|9.2]] / [[9.3 React Native 基础概念\|9.3]] |
| 12 | 简答 | 选型决策树与混合架构 | ⭐⭐⭐ | [[9.4 跨平台方案选型对比\|9.4]] |
| 13 | 分析 | 模块化方案选型 | ⭐⭐ | [[9.4 跨平台方案选型对比\|9.4]] |
| 14 | 分析 | WebView 代码漏洞分析 | ⭐⭐⭐ | [[9.1 WebView 混合开发\|9.1]] |
| 15 | 分析 | 综合选型与混合架构 | ⭐⭐⭐ | [[9.4 跨平台方案选型对比\|9.4]] |

### 复习建议

> [!tip] 高效复习路线
> 1. **第一优先（必考）**：Flutter 渲染三棵树（Widget/Element/RenderObject）与三层架构（见第 3、6、10 题），能默画架构图
> 2. **第二优先**：WebView 通信机制（addJavascriptInterface/evaluateJavascript/URL Scheme）与安全风险（见第 1、2、8、9、14 题）
> 3. **第三优先**：RN 三线程架构与 JSI 新架构（见第 4、7 题），理解 Bridge 瓶颈
> 4. **第四优先**：四方案八维度对比与选型决策树（见第 5、11、12 题），能画决策树
> 5. **综合应用**：方案选型分析题（第 13、15 题）需结合团队结构与业务需求综合判断
> 6. **代码分析**：第 14 题覆盖 WebView 安全配置，需关联 [[8.4 权限最小化、恶意调用防范|8.4 权限最小化]]

> [!warning] 常见错误提醒
> - 混淆 `WebViewClient` 与 `WebChromeClient` 职责（见第 1 题）
> - 误以为 Flutter 用原生控件渲染（Flutter 是自绘）
> - 误以为 RN 是同步通信（旧架构 Bridge 是异步）
> - 误以为 `addJavascriptInterface` 加 `@JavascriptInterface` 就绝对安全
> - 选型题中"哪个火用哪个"或"全部用跨平台"，应基于业务需求判断

## 章节导航

- 上级：[[MOC - 第9章|第9章 跨平台开发技术基础]]
- 上一章习题：[[MOC - 第8章习题|第8章习题]]
- 下一章习题：[[MOC - 第10章习题|第10章习题]]
- 课程总览：[[MOC - 移动互联网开发技术|移动互联网开发技术]]
