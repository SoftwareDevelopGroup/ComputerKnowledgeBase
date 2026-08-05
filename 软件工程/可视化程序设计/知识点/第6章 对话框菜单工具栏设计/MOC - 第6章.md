---
domain: 软件工程
type: MOC
status: 整理中
created: 2026-07-31
course: 可视化程序设计
chapter: 6
tags: ["可视化程序设计","GUI","事件驱动","JavaFX","窗体设计","界面布局","桌面开发","课程复习"]
prerequisites: ["编程与算法/Java程序设计","软件工程/面向对象程序设计"]
source: 《可视化程序设计》本科教材、JavaFX开发手册、GUI桌面开发课程讲义
---

# MOC - 第6章 对话框、菜单、工具栏设计

> [!info] 本章定位
> 第5章丰富了界面表现力，第6章补齐桌面应用的“标准交互骨架”。对话框解决“临时、模态的确认与输入”，菜单栏解决“功能入口的分级组织”，工具栏与状态栏解决“常用操作与运行时反馈”。本章覆盖 JavaFX `Dialog` 体系、菜单层次与快捷键、工具栏与系统托盘，让应用具备完整的桌面级交互规范。

## 学习路线图

```mermaid
flowchart LR
    A[6.1 对话框与弹窗] --> B[6.2 菜单栏与上下文菜单]
    B --> C[6.3 工具栏与状态栏]
    C --> D[动手: 完整主框架]
    D --> E[[MOC - 第7章]]
```

## 知识点导航

| 节 | 主题 | 核心要点 | 入口 |
| --- | --- | --- | --- |
| 6.1 | 对话框设计与弹窗交互 | `Dialog`/`Alert`、预定义对话框、`DialogPane`+`ButtonType`、模态、`TextInputDialog`/`ChoiceDialog` | [[6.1 对话框设计与弹窗交互]] |
| 6.2 | 菜单栏与上下文菜单 | `MenuBar`/`Menu`/`MenuItem`、`CheckMenuItem`/`RadioMenuItem`、`ContextMenu`、`accelerator` | [[6.2 菜单栏与上下文菜单]] |
| 6.3 | 工具栏与状态栏设计 | `ToolBar`、状态栏实现、`Tooltip`、`SystemTray` | [[6.3 工具栏与状态栏设计]] |

## 核心考点

> [!warning] 重点掌握
> 1. `Alert` 预定义类型（Confirmation/Information/Warning/Error）与 `showAndWait()` 的阻塞行为。
> 2. 自定义对话框：`DialogPane` + `ButtonType` + `setResultConverter` 的结果转换机制。
> 3. 模态（`Modality.APPLICATION_MODAL`/`WINDOW_MODAL`/`NONE`）的区别与适用场景。
> 4. `MenuBar`→`Menu`→`MenuItem` 三级层次，`CheckMenuItem`/`RadioMenuItem` 的状态保持。
> 5. `ContextMenu` 与控件 `setContextMenu` 的绑定方式，`accelerator` 快捷键设置。
> 6. `ToolBar` 溢出特性与状态栏（`HBox`+`Label`）的实现思路。

## 自测题

> [!question] 题1
> `Alert` 的 `show()` 与 `showAndWait()` 有何区别？模态对话框为什么要用 `showAndWait`？
> > [!check]- 参考答案
> > `show()` 立即返回，对话框非阻塞显示，调用方继续执行；`showAndWait()` 阻塞当前调用线程直到对话框关闭，并返回 `Optional<Result>`。模态对话框需要阻塞主窗口交互并在关闭后根据用户选择执行后续逻辑，因此用 `showAndWait` 便于顺序化处理结果。注意 `showAndWait` 必须在 JavaFX Application Thread 调用。

> [!question] 题2
> 如何自定义一个返回用户输入文本的对话框？描述 `DialogPane`、`ButtonType` 与 `setResultConverter` 三者协作。
> > [!check]- 参考答案
> > 创建 `Dialog<String>`，`setHeaderText` 设置提示，构造 `DialogPane` 并放入 `TextField`，`getDialogPane().setContent(field)`，添加 `ButtonType.OK`/`CANCEL`。关键是用 `setResultConverter(button -> button == ButtonType.OK ? field.getText() : null)`：当用户点击 OK 时把文本框内容作为对话框返回值，CANCEL 返回 null。`showAndWait` 返回 `Optional<String>` 即用户输入。

> [!question] 题3
> `CheckMenuItem` 与 `RadioMenuItem` 的区别是什么？`RadioMenuItem` 如何实现互斥选择？
> > [!check]- 参考答案
> > `CheckMenuItem` 是独立开关，可多选，状态由 `selected` 属性表示。`RadioMenuItem` 是单选项，必须加入同一个 `ToggleGroup` 才能互斥：同一组内任一时刻只有一个被选中，选中新的会自动取消旧的。`RadioMenuItem` 常用于“视图模式”“字号”等互斥选项。

> [!question] 题4
> 简述 JavaFX 状态栏的实现思路，为什么不直接提供 `StatusBar` 控件？
> > [!check]- 参考答案
> > JavaFX 没有内置 `StatusBar`，标准做法是用 `HBox`（或 `BorderPane` 的 `bottom` 区）横向排列若干 `Label`，左侧放状态文本、右侧放进度指示或时间。用 `HBox.setHgrow(label, Priority.ALWAYS)` 让状态文本占满剩余空间。这种“组合而非内置”的设计遵循 JavaFX 用基础面板拼装控件的统一思路，状态栏需求差异大，组合实现更灵活。

## 章节导航

- 上一章：[[MOC - 第5章]]
- 上一级：[[MOC - 可视化程序设计]]
- 下一章：[[MOC - 第7章]]
