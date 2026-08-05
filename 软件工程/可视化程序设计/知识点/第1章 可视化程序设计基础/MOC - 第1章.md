---
domain: 软件工程
type: MOC
status: 整理中
created: 2026-07-31
course: 可视化程序设计
chapter: 1
tags: ["可视化程序设计","GUI","事件驱动","JavaFX","窗体设计","界面布局","桌面开发","课程复习"]
prerequisites: ["编程与算法/Java程序设计","软件工程/面向对象程序设计"]
source: 《可视化程序设计》本科教材、JavaFX开发手册、GUI桌面开发课程讲义
---

# MOC - 第1章 可视化程序设计基础

> [!info] 本章定位
> 第1章是整门课程的地基。它回答三个问题：可视化程序设计“是什么”、GUI 程序“靠什么机制运行”、一个 JavaFX 程序“从启动到关闭经历了什么”。掌握本章后，才能进入组件、布局与事件处理的细节学习。

## 学习路线图

```mermaid
flowchart LR
    A[1.1 概念与开发模式] --> B[1.2 事件驱动编程原理]
    B --> C[1.3 GUI框架与窗体生命周期]
    C --> D[动手: Hello World 应用]
    D --> E[[MOC - 第2章]]
```

## 知识点导航

| 节 | 主题 | 核心要点 | 入口 |
| --- | --- | --- | --- |
| 1.1 | 可视化程序设计概念与开发模式 | 定义、RAD、命令式 vs 可视化、主流 GUI 框架对比 | [[1.1 可视化程序设计概念与开发模式]] |
| 1.2 | 事件驱动编程基本原理 | 事件源/事件对象/监听器、事件循环、EDT、JavaFX 事件模型 | [[1.2 事件驱动编程基本原理]] |
| 1.3 | GUI框架、窗体与程序生命周期 | Application/Stage/Scene、Scene Graph、窗体生命周期 | [[1.3 GUI框架、窗体与程序生命周期]] |

## 核心考点

> [!warning] 重点掌握
> 1. 可视化程序设计的定义与 RAD 理念，能区分命令式与可视化两种开发范式。
> 2. 事件驱动模型三要素（事件源、事件对象、事件监听器）与事件分发线程 EDT 的作用。
> 3. JavaFX 应用的组成：`Application` 类、`start()` 方法、`Stage`、`Scene`、Scene Graph 节点树。
> 4. 窗体生命周期各阶段及对应的回调时机。
> 5. JavaFX 与 Swing、Qt、WPF 等框架的对比要点。

## 自测题

> [!question] 题1
> 简述可视化程序设计与命令行式程序设计在开发流程上的核心差异。
> > [!check]- 参考答案
> > 可视化程序设计以界面为起点，通过拖拽组件、配置属性先构建 UI 再编写交互逻辑；命令式程序设计以代码逻辑为起点，通过文本输入输出驱动流程。前者强调“所见即所得”与快速反馈，后者强调算法与控制流。

> [!question] 题2
> 事件驱动编程模型的三个核心要素是什么？在 JavaFX 中分别对应哪些类型？
> > [!check]- 参考答案
> > 三要素：事件源、事件对象、事件监听器。JavaFX 中事件源通常是 `Node`/`Scene`/`Window`，事件对象为 `javafx.event.Event` 及其子类（如 `ActionEvent`、`MouseEvent`），监听器为 `EventHandler<T extends Event>` 接口实现。

> [!question] 题3
> 什么是事件分发线程（EDT）？为什么不能在 EDT 中执行耗时操作？
> > [!check]- 参考答案
> > EDT 是负责事件分发与界面绘制的单一线程（JavaFX 中为 JavaFX Application Thread）。在 EDT 中执行耗时操作会阻塞事件循环，导致界面卡顿或无响应。耗时任务应放到后台线程，结果再通过 `Platform.runLater()` 切回 EDT 更新界面。

> [!question] 题4
> 描述一个 JavaFX 应用从启动到关闭的生命周期，并指出 `launch()`、`init()`、`start()`、`stop()` 的调用顺序。
> > [!check]- 参考答案
> > 顺序：`main()` 调用 `launch()` → JavaFX 运行时创建 `Application` 实例并调用 `init()`（可重写，用于初始化）→ 在 EDT 上调用 `start(Stage)` 显示主窗体 → 用户关闭窗体后调用 `stop()` 释放资源。`init()` 与 `stop()` 在 JavaFX Application Thread 之外执行，`start()` 在 EDT 上执行。

## 章节导航

- 上一级：[[MOC - 可视化程序设计]]
- 下一章：[[MOC - 第2章]]
