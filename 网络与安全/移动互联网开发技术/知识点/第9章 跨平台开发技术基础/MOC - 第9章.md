---
domain: 网络与安全
subject: 移动互联网开发技术
type: MOC
chapter: 第9章 跨平台开发技术基础
section: MOC
tags: [移动开发,跨平台,WebView,Flutter,React Native,混合开发,选型对比]
prerequisites: ["计算机网络A","Java程序设计","第1章 移动互联网与移动开发概述","第4章 Android UI 界面开发"]
aliases: [第9章, 跨平台开发, Chapter 9, Cross-Platform Development]
---

# MOC - 第9章 跨平台开发技术基础

第 1 章在选型对比中提到"原生开发双端成本高、跨平台方案各有取舍"，但并未深入到框架内部机制。本章正是对那处伏笔的回应：从最轻量的 WebView 混合方案，到当前主流的 Flutter 与 React Native，逐一拆解它们的架构原理、渲染机制、与原生的通信方式，最终回到工程视角的方案选型。本章的目标不是让读者精通三种框架，而是建立"为什么这样设计、什么场景该用它"的判断力。

> [!info] 本章定位
> - **核心对象**：跨平台框架的架构原理、渲染机制、原生通信与方案选型
> - **关键能力**：WebView 混合开发与 JSBridge 通信、Flutter 三层架构与 Widget 体系、RN 的 Bridge 架构与组件映射、四方案对比与选型决策
> - **承前启后**：在第 1 章选型对比基础上深入框架细节；为第 10 章项目实战中的技术选型做铺垫
> - **考试权重**：WebView 通信机制、Flutter 渲染流程、RN 架构、方案选型对比为高频考点
> - **实践提示**：本章代码示例以原理演示为主，实际开发需配合官方文档与最新 API

> [!abstract] 本章核心问题
> 1. WebView 如何作为容器承载 H5 页面？原生与 JS 之间如何双向通信？
> 2. Flutter 的三层架构（Framework / Engine / Embedder）各自承担什么职责？Widget→Element→RenderObject 的渲染链路如何运作？
> 3. React Native 的 JS 线程、Bridge、Native 线程如何协作？组件如何映射到原生控件？
> 4. 原生、Flutter、RN、WebView 四方案在性能、开发效率、一致性、维护成本上如何取舍？
> 5. 给定一个具体业务场景（如电商详情页、即时通讯、系统工具），应如何选择技术方案？

## 本章学习路线

```mermaid
flowchart LR
    S1["9.1 WebView 混合开发<br/>最轻量的跨平台方案"]
    S2["9.2 Flutter 基础框架<br/>自绘引擎 · Dart"]
    S3["9.3 React Native 基础<br/>JS Bridge · 原生映射"]
    S4["9.4 跨平台方案选型对比<br/>原生/Flutter/RN/WebView"]

    S1 -->|"容器化思路"| S2
    S2 -->|"自绘 vs 映射"| S3
    S3 -->|"特性汇总"| S4

    style S1 fill:#f8d7da,stroke:#721c24,stroke-width:2px
    style S2 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style S3 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style S4 fill:#d4edda,stroke:#155724,stroke-width:2px
```

学习路线说明：先从最轻量的 WebView 混合方案入门，理解"原生壳 + H5"的容器化思路（9.1）；再进入当前最主流的 Flutter，剖析自绘引擎与 Widget 体系（9.2）；随后对比 React Native 的"原生组件映射"思路，理解两种跨平台范式的差异（9.3）；最终汇总四方案特性，给出工程化的选型决策方法（9.4）。

## 知识点导航

| 序号 | 知识点 | 核心内容 | 重点等级 |
| ---- | ------ | -------- | -------- |
| 9.1 | [[9.1 WebView 混合开发\|WebView 混合开发]] | WebView 控件、WebSettings、WebViewClient、WebChromeClient、addJavascriptInterface、evaluateJavascript、JSBridge、URL Scheme、缓存与预加载、JS 注入安全 | ⭐⭐⭐⭐ |
| 9.2 | [[9.2 Flutter 基础框架简介\|Flutter 基础框架]] | Flutter 特点、三层架构（Framework/Engine/Embedder）、StatelessWidget/StatefulWidget、Hot Reload、Widget→Element→RenderObject 渲染链、MethodChannel/EventChannel | ⭐⭐⭐⭐⭐ |
| 9.3 | [[9.3 React Native 基础概念\|React Native 基础]] | RN 特点、JS 线程/Bridge/Native 线程架构、组件映射原生、Native Module、与 Flutter 对比 | ⭐⭐⭐⭐ |
| 9.4 | [[9.4 跨平台方案选型对比\|方案选型对比]] | 四方案八维度对比、选型决策树、微信/抖音/淘宝/美团案例、混合架构实践 | ⭐⭐⭐⭐ |

## 核心考点速览

> [!warning] 高频考点（7 点）
> 1. **WebView 通信机制**：addJavascriptInterface（Java→JS 注入）与 evaluateJavascript（JS→Java 调用）的区别与安全风险（**必考**）
> 2. **JSBridge 原理**：URL Scheme 拦截 vs 注入对象两种实现方式，以及各自的适用场景
> 3. **Flutter 三层架构**：Framework（Dart）/ Engine（C++/Skia）/ Embedder 各层职责（**必考**）
> 4. **Flutter 渲染链路**：Widget→Element→RenderObject 三棵树的关系与各自职责
> 5. **Flutter 两种 Widget**：StatelessWidget 与 StatefulWidget 的区别与使用场景
> 6. **RN 三线程架构**：JS 线程、Bridge、Native 线程的协作方式与通信开销
> 7. **四方案选型**：原生/Flutter/RN/WebView 在性能、一致性、开发效率、热更新、包体积上的取舍（**必考**）

## 关键概念速查

### 四方案核心特征

| 方案 | 语言 | 渲染方式 | 原生通信 | 热更新 |
| ---- | ---- | -------- | -------- | ------ |
| 原生开发 | Kotlin/Swift | 系统原生控件 | 直接调用 | 不支持 |
| Flutter | Dart | 自绘引擎（Skia/Impeller） | MethodChannel/EventChannel | 不原生支持 |
| React Native | JS/TS | 原生组件映射 | Native Module / Bridge | 支持（CodePush） |
| WebView 混合 | HTML/CSS/JS | 浏览器内核 | JSBridge | 支持（H5 替换） |

### 三种跨平台范式对比

| 范式 | 代表 | 渲染核心 | 一致性 | 性能 |
| ---- | ---- | -------- | ------ | ---- |
| 自绘渲染 | Flutter | Skia/Impeller 直接绘制 | 极高（双端像素一致） | 接近原生 |
| 原生映射 | React Native | JS 驱动原生控件 | 中等（遵循平台风格） | 中等 |
| 浏览器渲染 | WebView 混合 | 浏览器内核 | 较低（受内核版本影响） | 较弱 |

## 跨章关联

- **理论基础**：[[1.3 原生开发、跨平台开发方案对比|1.3 选型对比]] — 本章是对第 1 章选型内容的深入
- **UI 基础**：[[MOC - 第4章|第4章 UI 界面开发]] — 原生控件知识是理解 RN 组件映射的前提
- **安全关联**：[[8.4 权限最小化、恶意调用防范|8.4 权限最小化]] — WebView 的 JS 注入安全与本节关联
- **网络通信**：[[6.4 OkHttp 等网络框架基础|6.4 OkHttp]] — WebView 加载远程页面涉及 HTTP/HTTPS
- **工程闭环**：[[MOC - 第10章|第10章 打包发布与实战]] — 选型决策最终落地于项目实战

## 章节导航

- 上级：[[MOC - 移动互联网开发技术|移动互联网开发技术总览]]
- 上一章：[[MOC - 第8章|第8章 移动应用安全]]
- 下一章：[[MOC - 第10章|第10章 应用打包、发布与项目实战]]
- 习题：[[MOC - 第9章习题|第9章习题]]
