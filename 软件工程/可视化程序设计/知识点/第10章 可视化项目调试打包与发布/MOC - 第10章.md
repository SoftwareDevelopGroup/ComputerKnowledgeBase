---
domain: 软件工程
type: MOC
status: 整理中
created: 2026-07-31
course: 可视化程序设计
chapter: 10
tags: ["可视化程序设计","GUI","事件驱动","JavaFX","窗体设计","界面布局","桌面开发","课程复习"]
prerequisites: ["编程与算法/Java程序设计","软件工程/面向对象程序设计"]
source: 《可视化程序设计》本科教材、JavaFX开发手册、GUI桌面开发课程讲义
---

# MOC - 第10章 可视化项目调试打包与发布

> [!info] 本章定位
> 第9章让应用“好看”，第10章让应用“能交付”。功能写完只是起点，还要定位 Bug、优化性能、模块化构建、打包成可安装应用并跨平台部署。本章覆盖三条主线：用 IDE 调试与性能分析解决卡顿与内存问题，用 `module-info`/Maven/Gradle 管理模块与依赖，用 `jlink`/`jpackage` 生成自包含的原生安装包。这是从“本地能跑”到“用户可装”的关键一跃。

## 学习路线图

```mermaid
flowchart LR
    A[10.1 调试技术与性能优化] --> B[10.2 模块化与项目构建]
    B --> C[10.3 打包发布与跨平台部署]
    C --> D[动手: 打包一个可安装的记事本]
    D --> E[结课: 综合项目]
```

## 知识点导航

| 节 | 主题 | 核心要点 | 入口 |
| --- | --- | --- | --- |
| 10.1 | 调试技术与性能优化 | IDE 断点、Scene Graph 分析、FPS 监控、布局/绑定性能、内存泄漏 | [[10.1 调试技术与性能优化]] |
| 10.2 | 模块化与项目构建 | `module-info.java`、Maven `pom.xml` + JavaFX Maven Plugin、Gradle | [[10.2 模块化与项目构建]] |
| 10.3 | 打包发布与跨平台部署 | `jpackage` 安装包、`jlink` 自定义运行时镜像、MSI/DMG/DEB | [[10.3 打包发布与跨平台部署]] |

## 核心考点

> [!warning] 重点掌握
> 1. IDE 调试：断点、条件断点、变量监视、表达式求值，能定位事件处理器与回调中的逻辑错误。
> 2. JavaFX 性能问题三大典型：布局嵌套过深、过度绑定、动画/特效滥用导致 FPS 下降。
> 3. Java 模块系统：`module-info.java` 的 `requires`/`exports`/`opens` 语义，反射场景需 `opens`。
> 4. Maven 构建 JavaFX：`javafx-controls`/`javafx-fxml` 依赖 + `javafx-maven-plugin` 的 `run` 目标。
> 5. `jpackage` 生成原生安装包（MSI/EXE、DMG/PKG、DEB/RPM），`jlink` 生成精简运行时镜像。
> 6. 自包含应用（self-contained）：镜像打包 JRE，用户无需预装 Java。

## 自测题

> [!question] 题1
> JavaFX 界面卡顿，列出至少 3 种可能原因及排查思路。
> > [!check]- 参考答案
> > ①**布局嵌套过深**：`Scenic View` 分析 Scene Graph 层级，扁平化布局、减少 `StackPane`/`AnchorPane` 套娃。
> > ②**过度绑定**：大量 `Bindings` 计算链每次属性变化都重算，用 `InvalidationListener` 惰性监听或减少绑定层级。
> > ③**动画/特效滥用**：`DropShadow` 大半径、列表项特效每帧重算，用 `setCache(true)` 缓存或移除。
> > ④**UI 线程阻塞**：事件处理器内做了 IO/计算，移到 `Task` 后台线程。
> > ⑤**`runLater` 风暴**：后台高频 `Platform.runLater` 塞满事件队列，改批量提交。
> > 排查工具：`Scenic View` 看 Scene Graph、`jconsole`/VisualVM 看 CPU 与线程、`-Dprism.verbose=true` 看 FPS。

> [!question] 题2
> 写出 `module-info.java` 让一个 JavaFX 应用使用 `javafx.controls` 与 `javafx.fxml`，并允许 FXML 反射访问 `com.example.app` 包。
> > [!check]- 参考答案
> > ```java
> > module com.example.app {
> >     requires javafx.controls;
> >     requires javafx.fxml;
> >     requires org.kordamp.ikonli.javafx;   // 若用字体图标
> >
> >     opens com.example.app to javafx.fxml; // FXML 加载需反射访问
> >     exports com.example.app;
> > }
> > ```
> > `requires` 声明依赖模块；`opens ... to javafx.fxml` 允许 FXML 反射实例化控制器类；`exports` 让外部可访问（主类被启动器调用）。

> [!question] 题3
> 用 Maven 构建并运行一个 JavaFX 应用，写出 `pom.xml` 的关键配置和运行命令。
> > [!check]- 参考答案
> > 关键配置：①依赖 `org.openjfx:javafx-controls` 与 `javafx-fxml`，`classifier` 按平台（`win`/`linux`/`mac`）；②插件 `org.openjfx:javafx-maven-plugin`，`<mainClass>com.example.app.App</mainClass>`。
> > 运行命令：`mvn javafx:run`。
> > 打包（含 JavaFX 运行时）：`mvn javafx:jlink` 生成自定义镜像，或配合 `jpackage` 生成安装包。

> [!question] 题4
> `jlink` 和 `jpackage` 各自的作用是什么？为什么说自包含应用对最终用户友好？
> > [!check]- 参考答案
> > `jlink` 根据 `module-info` 把所需 JDK 模块与应用模块裁剪打包成精简的自定义 JRE 镜像，体积小、启动快。
> > `jpackage` 在 `jlink` 镜像（或现有 JRE）基础上生成平台原生安装包：Windows 的 MSI/EXE、macOS 的 DMG/PKG、Linux 的 DEB/RPM，包含图标、快捷方式、卸载器。
> > 自包含应用把 JRE 一起打包，用户无需预装特定版本 Java，避免“装了 Java 但版本不对”的环境问题，双击即装即用，体验接近原生应用。

## 章节导航

- 上一章：[[MOC - 第9章]]
- 上一级：[[MOC - 可视化程序设计]]
- 下一章：结课综合项目
