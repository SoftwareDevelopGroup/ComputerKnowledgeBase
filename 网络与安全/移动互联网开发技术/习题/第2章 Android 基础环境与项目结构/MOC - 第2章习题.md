---
domain: 网络与安全
subject: 移动互联网开发技术
type: exercise
chapter: 第2章 Android 基础环境与项目结构
tags: [移动开发,习题,Android,四大组件,Manifest]
prerequisites: ["计算机网络A","Java程序设计"]
aliases: [第2章习题, Android环境习题]
---

# MOC - 第2章习题

本章习题覆盖 [[MOC - 第2章|第2章 Android 基础环境与项目结构]] 的全部知识点，共 15 题：选择题 5、填空题 3、简答题 4、代码阅读题 3。每题答案以 `<details>` 折叠，建议先独立作答再展开核对。

> [!info] 使用说明
> - 选题覆盖环境搭建、工程目录、四大组件、Manifest、生命周期五个小节
> - 答案附简要解析，便于复习时定位知识点
> - 末尾附考点统计表与复习建议

## 一、选择题（5 题）

### 1. 下列 Android SDK 工具集中，主要负责“与设备/模拟器通信”的是？

A. SDK Tools
B. Platform Tools
C. Build Tools
D. AndroidX

<details>
<summary>答案与解析</summary>

**答案：B**

**解析**：Platform Tools 包含 `adb`、`fastboot` 等工具，负责与设备/模拟器通信；SDK Tools 是旧版管理工具；Build Tools 负责编译打包（`aapt`、`d8` 等）；AndroidX 是支持库，不属于 SDK 工具集。

知识点：[[2.1 Android SDK、开发工具环境搭建#2.1.1 Android SDK 组成|2.1.1 SDK 组成]]
</details>

### 2. 关于 `minSdkVersion`、`targetSdkVersion`、`compileSdkVersion` 三个字段，下列说法正确的是？

A. 三者必须相等
B. `minSdkVersion` 决定编译期能调用的 API
C. `targetSdkVersion` 决定系统是否启用新行为
D. `compileSdkVersion` 决定能安装的最低设备

<details>
<summary>答案与解析</summary>

**答案：C**

**解析**：
- `minSdkVersion`：最低支持版本，决定能安装的设备范围（A 错、D 错）
- `targetSdkVersion`：目标版本，告知系统“我已适配”，系统据此决定是否启用新行为（C 正确）
- `compileSdkVersion`：编译版本，决定编译期能调用哪些 API（B 错）
- 三者不必相等，通常 `compileSdk ≥ target ≥ min`

知识点：[[2.1 Android SDK、开发工具环境搭建#2.1.3 SDK 版本与 API Level 对应关系|2.1.3 SDK 版本字段]]
</details>

### 3. 下列 Android 四大组件中，**没有界面**且适合执行长期后台任务的是？

A. Activity
B. Service
C. BroadcastReceiver
D. ContentProvider

<details>
<summary>答案与解析</summary>

**答案：B**

**解析**：Service 没有界面，专为后台长期任务设计（如音乐播放、下载）。Activity 有界面；BroadcastReceiver 仅在 `onReceive` 短暂执行；ContentProvider 提供数据接口，不执行后台任务。

知识点：[[2.3 Android 四大组件概述#2.3.6 四大组件对比|2.3.6 四大组件对比]]
</details>

### 4. 在 `AndroidManifest.xml` 中，`<uses-permission>` 标签必须放在哪里？

A. `<application>` 内部
B. `<manifest>` 内、`<application>` 之外
C. `<activity>` 内部
D. 任意位置

<details>
<summary>答案与解析</summary>

**答案：B**

**解析**：`<uses-permission>` 是应用级权限声明，必须放在 `<manifest>` 根标签内、`<application>` 标签之外。`<application>` 内部只能放组件声明。

知识点：[[2.4 AndroidManifest 清单文件作用#2.4.6 权限声明|2.4.6 权限声明]]
</details>

### 5. 关于 Android 进程优先级，下列顺序**正确**（从高到低）的是？

A. 前台 → 可见 → 后台 → 服务 → 空
B. 前台 → 服务 → 可见 → 后台 → 空
C. 前台 → 可见 → 服务 → 后台 → 空
D. 可见 → 前台 → 服务 → 后台 → 空

<details>
<summary>答案与解析</summary>

**答案：C**

**解析**：进程优先级从高到低为：前台进程 → 可见进程 → 服务进程 → 后台进程 → 空进程。系统回收时从低到高（空 → 后台 → 服务 → 可见 → 前台）。

知识点：[[2.5 应用生命周期基础概念#2.5.2 进程优先级五级模型|2.5.2 进程优先级]]
</details>

## 二、填空题（3 题）

### 6. Android SDK 三件套是指 SDK Tools、______ 和 ______。

<details>
<summary>答案与解析</summary>

**答案**：Platform Tools；Build Tools

**解析**：
- **Platform Tools**：与设备通信（`adb`）
- **Build Tools**：编译打包（`aapt`、`d8`、`zipalign`）

知识点：[[2.1 Android SDK、开发工具环境搭建#2.1.1 Android SDK 组成|2.1.1 SDK 组成]]
</details>

### 7. Android 工程中，布局文件放在 `res/______` 目录，字符串等简单值放在 `res/______` 目录，启动图标放在 `res/______` 目录。

<details>
<summary>答案与解析</summary>

**答案**：layout；values；mipmap

**解析**：
- `layout/`：布局 XML
- `values/`：字符串、颜色、样式等简单值
- `mipmap/`：启动图标（按密度分文件夹）

知识点：[[2.2 Android 工程目录结构解析#2.2.3 资源目录|2.2.3 资源目录]]
</details>

### 8. Android 应用启动时，系统通过 ______ fork 新进程，新进程的入口类是 ______。

<details>
<summary>答案与解析</summary>

**答案**：Zygote；ActivityThread

**解析**：
- **Zygote**：进程孵化器，负责 fork 新的应用进程
- **ActivityThread**：应用主线程入口类，管理主线程 MessageQueue 与组件生命周期调度

知识点：[[2.5 应用生命周期基础概念#2.5.3 应用启动流程|2.5.3 应用启动流程]]
</details>

## 三、简答题（4 题）

### 9. 简述 Android 四大组件的职责，并各举一个典型场景。

<details>
<summary>参考答案</summary>

| 组件 | 职责 | 典型场景 |
| ---- | ---- | -------- |
| Activity | 提供用户可交互界面 | 登录页、列表页 |
| Service | 后台长期运行，无界面 | 音乐播放、文件下载 |
| BroadcastReceiver | 接收系统或应用广播 | 开机启动、网络变化 |
| ContentProvider | 跨应用数据共享 | 通讯录、相册访问 |

要点：四者都需在 Manifest 声明（动态广播除外），由系统调度生命周期。

知识点：[[2.3 Android 四大组件概述|2.3 四大组件概述]]
</details>

### 10. 说明 `minSdkVersion`、`targetSdkVersion`、`compileSdkVersion` 的区别，并解释为什么通常 `compileSdk ≥ target ≥ min`。

<details>
<summary>参考答案</summary>

- **minSdkVersion**：最低支持版本，应用商店据此过滤设备，低于此值的设备无法安装。
- **targetSdkVersion**：目标版本，告知系统“我已针对该版本适配”，系统据此决定是否启用新行为（如运行时权限、后台限制）。
- **compileSdkVersion**：编译版本，决定编译期能调用哪些 API，必须 ≥ targetSdk 才能使用 target 版本引入的新 API。

**为何 `compileSdk ≥ target ≥ min`**：
- `compileSdk ≥ target`：要用 target 版本的新 API 进行适配，编译版本必须能识别这些 API。
- `target ≥ min`：目标版本应不低于最低支持版本，否则逻辑矛盾（适配的版本比支持的还低）。

知识点：[[2.1 Android SDK、开发工具环境搭建#2.1.3 SDK 版本与 API Level 对应关系|2.1.3 SDK 版本字段]]
</details>

### 11. 简述 AndroidManifest.xml 的主要作用，并列举至少 4 类必备内容。

<details>
<summary>参考答案</summary>

**作用**：向系统声明应用的结构、组件、权限、属性与运行需求，是系统安装、运行、调度应用的依据。

**必备内容**（任选 4 类）：
1. **四大组件声明**：`<activity>` / `<service>` / `<receiver>` / `<provider>`
2. **权限声明**：`<uses-permission>`
3. **应用属性**：`<application>` 的 icon / label / theme 等
4. **启动入口**：通过 `<intent-filter>` 的 `MAIN` + `LAUNCHER` 指定入口 Activity
5. **SDK 版本**：旧式 `<uses-sdk>` 或新式 build.gradle 配置
6. **硬件特性**：`<uses-feature>`

知识点：[[2.4 AndroidManifest 清单文件作用#2.4.1 Manifest 的作用|2.4.1 Manifest 作用]]
</details>

### 12. 区分“应用级生命周期”与“Activity 生命周期”，并说明二者关系。

<details>
<summary>参考答案</summary>

**区别**：
- **应用级生命周期**：描述**进程**的存亡，由系统按内存压力与进程优先级决定，开发者只能通过组件状态间接影响。
- **Activity 生命周期**：描述**单个页面**的状态转换，由用户操作触发，开发者可在 7 个回调中直接响应。

**关系**：
- 一个进程内可包含多个 Activity，进程存活不代表所有 Activity 都在前台。
- Activity 销毁不意味着进程被杀——进程可能作为空进程缓存。
- 进程被回收时，其内所有 Activity 也会被销毁。
- `Application.onCreate()` 是进程级最早回调，先于首个 Activity 的 `onCreate()`。

知识点：[[2.5 应用生命周期基础概念#2.5.5 应用级 vs 页面级生命周期|2.5.5 应用级 vs 页面级]]
</details>

## 四、代码阅读题（3 题）

### 13. 阅读以下模块级 `build.gradle` 片段，回答问题。

```gradle
android {
    namespace 'com.example.myapp'
    compileSdk 34

    defaultConfig {
        applicationId "com.example.myapp"
        minSdk 24
        targetSdk 34
        versionCode 2
        versionName "1.1"
    }
}
```

**问题**：
1. 该应用支持的最低 Android 版本 API Level 是多少？
2. 应用在应用商店中的唯一标识是什么？
3. `namespace` 与 `applicationId` 在此是否相同？二者职责有何区别？

<details>
<summary>参考答案</summary>

1. **最低 API Level = 24**（对应 Android 7.0 Nougat），由 `minSdk 24` 决定。
2. **应用唯一标识 = `com.example.myapp`**，由 `applicationId` 决定，应用商店据此区分应用。
3. **二者相同**（均为 `com.example.myapp`），但职责不同：
   - `namespace`：决定 R 类、BuildConfig 的生成包路径（AGP 7.0+ 引入）
   - `applicationId`：决定应用在系统与应用商店中的唯一标识
   - 两者可以不同——例如多渠道打包时 `applicationId` 可加后缀，而 `namespace` 保持不变。

知识点：[[2.1 Android SDK、开发工具环境搭建#2.1.6 Gradle 构建系统基础|2.1.6 Gradle 配置]]、[[2.2 Android 工程目录结构解析#2.2.2 源代码目录|2.2.2 包名与 namespace]]
</details>

### 14. 阅读以下 `AndroidManifest.xml` 片段，指出**至少 3 处问题**。

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <application
        android:label="@string/app_name">

        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <service android:name=".PlaybackService" android:exported="true" />

        <uses-permission android:name="android.permission.INTERNET" />
    </application>
</manifest>
```

<details>
<summary>参考答案</summary>

**问题清单**（任选 3 处）：

1. **`<uses-permission>` 位置错误**：必须放在 `<manifest>` 内、`<application>` 之外，而此处放在了 `<application>` 内部。
2. **MainActivity 缺少 `exported` 属性**：Android 12（API 31+）起，带 `<intent-filter>` 的组件必须显式声明 `exported`，否则安装失败。入口 Activity 应为 `android:exported="true"`。
3. **`<application>` 缺少 `android:icon` 与 `android:theme`**：虽非严格必填，但缺少会导致使用系统默认值，影响体验。
4. **`<service>` 的 `exported="true"` 不合理**：若该 Service 仅本应用使用，应设为 `false`，避免被外部应用启动（安全风险）。

知识点：[[2.4 AndroidManifest 清单文件作用#2.4.6 权限声明|2.4.6 权限声明]]、[[2.4 AndroidManifest 清单文件作用#2.4.5 四大组件声明|2.4.5 组件声明与 exported]]
</details>

### 15. 阅读以下代码片段，回答问题。

```java
public class MyApp extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        // 初始化埋点 SDK（耗时 200ms）
        Analytics.init(this);
        // 初始化推送 SDK（耗时 500ms）
        Push.init(this);
    }
}
```

**问题**：
1. `MyApp.onCreate()` 何时被调用？在首个 Activity 的 `onCreate()` 之前还是之后？
2. 上述初始化方式可能带来什么问题？
3. 给出一种改进思路。

<details>
<summary>参考答案</summary>

1. **调用时机**：`Application.onCreate()` 在**进程创建后**、首个 Activity 的 `onCreate()` **之前**调用，且整个进程生命周期内只调用一次。

2. **可能的问题**：
   - 两个 SDK 初始化共耗时约 700ms，直接拖慢应用启动，用户会感到“白屏”或“点击图标后延迟”。
   - 所有初始化都在主线程串行执行，阻塞主线程。
   - 即使首屏不需要这些 SDK，也必须等待它们初始化完成。

3. **改进思路**（任选一种）：
   - **延迟初始化**：将非首屏必需的 SDK 改为按需初始化，例如首屏渲染完成后再初始化推送。
   - **子线程初始化**：将 SDK 初始化放到子线程（注意线程安全与主线程依赖）。
   - **使用启动框架**：如 AndroidX App Startup 或第三方启动优化框架，按依赖关系并行初始化。

知识点：[[2.5 应用生命周期基础概念#2.5.5 应用级 vs 页面级生命周期|2.5.5 Application.onCreate]]、[[2.5 应用生命周期基础概念#2.5.6 工程实践要点|2.5.6 ANR 与耗时操作]]
</details>

## 考点统计

| 题号 | 类型 | 对应小节 | 核心考点 |
| ---- | ---- | -------- | -------- |
| 1 | 选择 | 2.1 | SDK 三件套职责 |
| 2 | 选择 | 2.1 | 三种 SDK 版本字段 |
| 3 | 选择 | 2.3 | 四大组件定位 |
| 4 | 选择 | 2.4 | `<uses-permission>` 位置 |
| 5 | 选择 | 2.5 | 进程优先级顺序 |
| 6 | 填空 | 2.1 | SDK 三件套名称 |
| 7 | 填空 | 2.2 | res 子目录职责 |
| 8 | 填空 | 2.5 | Zygote 与 ActivityThread |
| 9 | 简答 | 2.3 | 四大组件职责与场景 |
| 10 | 简答 | 2.1 | 三种 SDK 版本字段区别 |
| 11 | 简答 | 2.4 | Manifest 作用与内容 |
| 12 | 简答 | 2.5 | 应用级 vs Activity 生命周期 |
| 13 | 代码阅读 | 2.1 / 2.2 | build.gradle 配置解读 |
| 14 | 代码阅读 | 2.4 | Manifest 错误排查 |
| 15 | 代码阅读 | 2.5 | Application 初始化与启动优化 |

## 复习建议

> [!tip] 分层复习
> - **第一遍（识记）**：能复述 SDK 三件套、四大组件、五级进程优先级的名称与顺序——覆盖选择与填空。
> - **第二遍（理解）**：能解释三种 SDK 版本字段的区别、Manifest 各部分的作用、应用级与 Activity 生命周期的关系——覆盖简答。
> - **第三遍（应用）**：能读懂 build.gradle 与 Manifest，发现配置错误并提出改进——覆盖代码阅读。
> - **重点突破**：`exported` 属性（Android 12+ 强制）、`namespace` vs `applicationId`、前台 Service 与进程保活是近年高频考点。

---

## 章节导航

- 上级：[[MOC - 第2章|第2章 MOC]]
- 上一章习题：[[MOC - 第1章习题|第1章习题]]
- 下一章习题：[[MOC - 第3章习题|第3章习题]]
- 课程总览：[[MOC - 移动互联网开发技术|移动互联网开发技术 MOC]]
