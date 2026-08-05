---
domain: 网络与安全
subject: 移动互联网开发技术
type: exercise
chapter: 第7章 后台服务与消息通知
tags: [移动开发,习题,Service,广播,通知,任务调度]
prerequisites: ["计算机网络A","Java程序设计"]
aliases: [第7章习题, 后台服务习题, 第7章练习]
---

# MOC - 第7章习题

> [!info] 本章习题说明
> - 配套知识点：[[MOC - 第7章|第7章 后台服务与消息通知]]
> - 题目数量：**15 题**（选择 5 + 填空 3 + 简答 4 + 代码设计 3）
> - 难度梯度：⭐基础 / ⭐⭐中等 / ⭐⭐⭐较难
> - 答案折叠在每题下方的 `<details>` 块中，建议先独立作答再展开对照

## 一、选择题（5 题）

### 1. ⭐ 关于 Service 的描述，下列正确的是？

A. Service 默认运行在子线程，可以直接做网络请求
B. Service 没有用户界面，与 Activity 一样需要注册到 AndroidManifest
C. Service 启动后会一直运行，不会被系统回收
D. Service 必须配合 Notification 使用

<details>
<summary>查看答案</summary>

**答案：B**

- A 错：Service 默认运行在**主线程**，做网络请求需另开子线程，否则抛 NetworkOnMainThreadException。
- B 对：Service 是四大组件之一，必须在 AndroidManifest 中声明。
- C 错：前台 Service 几乎不会被杀，但普通后台 Service 在内存紧张时会被回收。
- D 错：仅**前台 Service** 必须配合 Notification 使用，普通 Service 不需要。
</details>

---

### 2. ⭐ 下列关于 startService 与 bindService 的生命周期，正确的是？

A. startService 触发 onCreate → onBind → onStartCommand
B. bindService 触发 onCreate → onBind → onUnbind → onDestroy
C. startService 多次启动会多次触发 onCreate
D. bindService 时若有多个客户端，每个客户端都会触发 onBind

<details>
<summary>查看答案</summary>

**答案：B**

- A 错：startService 触发 onCreate → onStartCommand，不调用 onBind。
- B 对：bindService 走 onCreate → onBind → onUnbind → onDestroy 这条路径。
- C 错：onCreate 只在 Service 首次创建时调用一次，多次 startService 只触发 onStartCommand。
- D 错：onBind 只在第一个客户端绑定时调用一次，后续客户端共享同一 Service 实例。
</details>

---

### 3. ⭐⭐ 关于 BroadcastReceiver 注册方式，下列说法错误的是？

A. 静态注册在 AndroidManifest 中通过 `<receiver>` 标签声明
B. 动态注册使用 `registerReceiver(receiver, filter)`，需在适当时机 `unregisterReceiver`
C. Android 8.0+ 起所有隐式广播都不能用静态注册接收
D. 静态注册在应用未启动时，系统会冷启动应用并触发 onReceive

<details>
<summary>查看答案</summary>

**答案：C**

C 错：Android 8.0+ 是限制**大多数**隐式广播的静态注册，但仍有白名单（如 `BOOT_COMPLETED`、`LOCALE_CHANGED`、`USB_DEVICE_ATTACHED` 等）可以静态注册；自定义广播若显式指定包名也仍可用静态注册。A、B、D 描述正确。
</details>

---

### 4. ⭐⭐ 关于 NotificationChannel，下列说法正确的是？

A. NotificationChannel 是 Android 7.0 引入的，可选使用
B. 同一渠道创建后，应用可以随时修改其重要性级别
C. Android 8.0+ 发送通知前必须先创建 NotificationChannel，否则通知不显示
D. 一个应用只能创建一个 NotificationChannel

<details>
<summary>查看答案</summary>

**答案：C**

- A 错：NotificationChannel 是 Android 8.0（API 26）引入的，且在该版本起**强制使用**。
- B 错：渠道一旦创建，**应用不能修改**其重要性级别（防止绕过用户控制），只能让用户在系统设置中调整。
- C 对：Android 8.0+ 通知必须归属到已创建的渠道，否则不显示且无报错。
- D 错：一个应用可以创建**多个**渠道，按业务类型分类（消息、下载、播放等）。
</details>

---

### 5. ⭐⭐⭐ 关于 WorkManager 的 PeriodicWorkRequest，下列描述错误的是？

A. 最小周期为 15 分钟，小于该值会被强制对齐到 15 分钟
B. 任务可以持久化到 Room 数据库，应用重启后自动恢复
C. PeriodicWorkRequest 支持设置初始延迟和约束后延迟
D. 同一 unique work 名称的周期任务，推荐用 `enqueueUniquePeriodicWork` 提交

<details>
<summary>查看答案</summary>

**答案：C**

C 错：PeriodicWorkRequest **不支持**初始延迟和约束后延迟（OneTimeWorkRequest 才支持 `setInitialDelay`）。周期任务在约束满足时立即执行，下次周期再触发。A、B、D 描述正确。
</details>

---

## 二、填空题（3 题）

### 6. ⭐ Android 中 Service 有两种启动方式：通过 `startService` 启动的 Service 走 `onCreate → ________ → onDestroy` 生命周期；通过 `bindService` 启动的 Service 走 `onCreate → ________ → onUnbind → onDestroy` 生命周期。

<details>
<summary>查看答案</summary>

**答案：onStartCommand、onBind**

- startService 路径：onCreate → **onStartCommand** → onDestroy，多次 startService 只触发 onStartCommand
- bindService 路径：onCreate → **onBind** → onUnbind → onDestroy，onBind 返回 IBinder 供客户端调用
</details>

---

### 7. ⭐⭐ Android 8.0（API 26）起，应用在后台调用 `startService()` 会抛 ________ 异常；解决方案是改用 ________ 启动 Service，并在 5 秒内调用 ________ 显示常驻通知。

<details>
<summary>查看答案</summary>

**答案：IllegalStateException、startForegroundService、startForeground**

- Android 8.0+ 后台应用 `startService` 抛 `IllegalStateException`
- 改用 `startForegroundService(intent)` 启动
- 在 `onCreate` 或 `onStartCommand` 开头调用 `startForeground(id, notification)` 绑定通知，5 秒内未调用会被系统杀掉并触发 ANR
</details>

---

### 8. ⭐⭐ 在 Android 12（API 31）起，创建 PendingIntent 必须显式指定 ________ 或 ________ 标志位；其中 ________ 表示 PendingIntent 内容不可变，安全性更高，是推荐默认值。

<details>
<summary>查看答案</summary>

**答案：FLAG_IMMUTABLE、FLAG_MUTABLE、FLAG_IMMUTABLE**

- Android 12 起 PendingIntent 必须指定 `FLAG_IMMUTABLE` 或 `FLAG_MUTABLE`，否则抛 `IllegalArgumentException`
- `FLAG_IMMUTABLE`：内容不可变，更安全，**默认推荐**
- `FLAG_MUTABLE`：可被其他应用修改，仅用于需要动态更新的场景（如媒体播放 RemoteInput）
</details>

---

## 三、简答题（4 题）

### 9. ⭐⭐ 对比 startService 与 bindService 两种启动方式在生命周期、通信方式、退出方式、适用场景上的差异。

<details>
<summary>查看答案</summary>

| 维度 | startService | bindService |
| ---- | ------------ | ----------- |
| 启动方法 | `startService(intent)` | `bindService(intent, conn, flags)` |
| 生命周期 | onCreate → onStartCommand → onDestroy | onCreate → onBind → onUnbind → onDestroy |
| 通信方式 | 无直接通信，只能用 Intent / 广播 | 通过 IBinder 接口直接调用 Service 方法 |
| 多次调用 | 多次 startService 触发多次 onStartCommand | 多个客户端共享同一 Service 实例 |
| 退出方式 | 必须显式 stopService 或 stopSelf | 所有客户端 unbind 后自动销毁 |
| 与启动方关系 | 启动后独立运行，启动方销毁不影响 Service | 与客户端生命周期绑定 |
| 适用场景 | 后台下载、音乐播放、定时同步 | Activity 与 Service 实时交互（控制播放进度） |

**记忆要点**：startService 是"启动后解耦"，bindService 是"绑定即通信"。
</details>

---

### 10. ⭐⭐ 简述 Android 8.0+ 对后台 Service 的限制及其解决方案，并说明前台服务为何必须显示通知。

<details>
<summary>查看答案</summary>

**Android 8.0+ 后台 Service 限制**：
1. 处于后台的应用调用 `startService()` 会抛 `IllegalStateException`
2. 后台应用无法启动普通 Service 持续运行

**解决方案**：
1. **使用前台服务**：调用 `startForegroundService()` 启动，并在 **5 秒内**调用 `startForeground()` 显示常驻通知
2. **使用 WorkManager/JobScheduler**：可延迟、可条件触发的任务改用调度方案
3. **使用 BroadcastReceiver**：响应式场景用广播触发

**前台服务必须显示通知的原因**：
1. **可见性换运行权**：让用户清楚地知道"有应用正在后台运行"，用户可见的服务系统几乎不会回收
2. **用户控制权**：用户可以滑动清除通知来主动停止服务，避免应用滥用后台资源
3. **系统资源管理**：通知机制让系统知道哪些 Service 是"用户主动感知"的，便于优先级管理
4. **防止滥用**：强制可见性让应用不能"偷偷"在后台长期运行，保护用户隐私和电量

**演进**：Android 14（API 34）进一步要求前台服务声明具体类型（如 `mediaPlayback`、`dataSync`、`location`），细化管理。
</details>

---

### 11. ⭐⭐ 对比静态注册与动态注册 BroadcastReceiver 的差异，并说明 Android 8.0+ 对隐式广播的限制。

<details>
<summary>查看答案</summary>

| 维度 | 静态注册 | 动态注册 |
| ---- | -------- | -------- |
| 配置位置 | AndroidManifest.xml `<receiver>` | 代码 `registerReceiver(receiver, filter)` |
| 生效时机 | 应用安装后即生效（含未启动） | 仅在注册后到反注册前生效 |
| 应用未启动时 | 系统会冷启动应用并触发接收 | 无法接收 |
| 资源占用 | 长期占资源，影响启动速度 | 灵活可控 |
| Android 8.0+ 限制 | 大多数隐式广播不再投递 | 全部支持 |
| 推荐场景 | 开机自启动、应用安装/卸载等少数 | 绝大多数业务广播 |

**Android 8.0+ 对隐式广播的限制**：
- 从 Android 8.0 起，**大多数隐式广播**不再投递给静态注册的接收方
- 仅**显式广播**（指定目标包名）或少数**白名单**广播仍可静态注册
- 白名单包括：`BOOT_COMPLETED`、`LOCALE_CHANGED`、`USB_DEVICE_ATTACHED/DETACHED`、`PACKAGE_ADDED/REMOVED` 等
- `CONNECTIVITY_CHANGE`、`BATTERY_CHANGED` 等系统广播**不能再静态注册**

**目的**：防止大量应用在系统事件时被同时唤醒，造成资源浪费和电量消耗。

**应对策略**：
1. 系统广播改用动态注册
2. 业务广播显式指定包名（`intent.setPackage(getPackageName())`）
3. 监听网络变化推荐用 `ConnectivityManager.NetworkCallback`（Android 10+）
</details>

---

### 12. ⭐⭐⭐ 对比 AlarmManager、JobScheduler、WorkManager 三种任务调度方案，并给出选型建议。

<details>
<summary>查看答案</summary>

| 维度 | AlarmManager | JobScheduler | WorkManager |
| ---- | ------------ | ------------ | ----------- |
| 最低 API | API 1 | API 21 | API 14（Jetpack 兼容） |
| 持久化 | 否（重启失效） | 是（setPersisted） | 是（Room 持久化） |
| 约束条件 | 仅时间 | 网络/充电/空闲/存储 | 网络/充电/空闲/存储/电量 |
| 任务链 | 不支持 | 不支持 | 支持 |
| 精确时间触发 | 支持（需权限） | 不支持（最小 15 分钟周期） | 不支持 |
| API 难度 | 中 | 中 | 低 |
| 跨版本兼容 | 自己处理 | 自己处理 | 自动 |
| 推荐场景 | 闹钟、日历提醒 | API 21+ 条件触发 | 后台持久化任务（首选） |

**选型建议**：
1. **精确闹钟**：仅 AlarmManager，Android 12+ 需声明 `SCHEDULE_EXACT_ALARM` 权限
2. **可延迟、需持久化、需约束**：WorkManager（**官方推荐**）
3. **老项目已用 JobScheduler**：可保留，新代码用 WorkManager
4. **持续运行、用户感知**：前台 Service + Notification
5. **响应式监听系统事件**：BroadcastReceiver

**为什么 WorkManager 是首选**：
- 向后兼容：内部自动选择 JobScheduler（API 21+）或 AlarmManager + BroadcastReceiver（API 14+）
- 持久化：任务持久化到 Room 数据库，应用或设备重启后自动恢复
- 任务链：支持串联、并行、合并的任务依赖
- 约束丰富：网络/充电/空闲/存储/电量等
- 与 LiveData/Flow 集成，便于 UI 观察任务状态
</details>

---

## 四、代码设计题（3 题）

### 13. ⭐⭐ Service 实现题：音乐播放前台服务

请实现一个**音乐播放前台 Service**，要求：
1. 继承 Service，使用 MediaPlayer 循环播放 `R.raw.bg_music`
2. 作为前台服务运行，显示"正在播放"通知，点击通知跳转 `MusicActivity`
3. 通知包含"暂停"按钮，点击后通过广播通知 Service 暂停播放
4. 在 AndroidManifest 中正确声明权限与 Service（Android 14 前台服务类型 `mediaPlayback`）
5. 启动方 Activity 适配 Android 8.0+ 调用 `startForegroundService`

<details>
<summary>查看答案</summary>

**AndroidManifest.xml**：

```xml
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />

<application>
    <service
        android:name=".service.MusicService"
        android:foregroundServiceType="mediaPlayback"
        android:exported="false" />

    <receiver
        android:name=".receiver.PauseReceiver"
        android:exported="false">
        <intent-filter>
            <action android:name="com.example.ACTION_PAUSE" />
        </intent-filter>
    </receiver>
</application>
```

**MusicService.java**：

```java
public class MusicService extends Service {
    private static final int NOTIFICATION_ID = 1001;
    private static final String CHANNEL_ID = "music_playback";
    public static final String ACTION_PAUSE = "com.example.ACTION_PAUSE";

    private MediaPlayer player;

    @Override
    public void onCreate() {
        super.onCreate();
        createChannel();
        player = MediaPlayer.create(this, R.raw.bg_music);
        player.setLooping(true);

        // 注册暂停广播接收方
        registerReceiver(pauseReceiver, new IntentFilter(ACTION_PAUSE));
    }

    private void createChannel() {
        NotificationChannel channel = new NotificationChannel(
            CHANNEL_ID, "音乐播放", NotificationManager.IMPORTANCE_LOW);
        channel.setDescription("后台音乐播放通知");
        getSystemService(NotificationManager.class).createNotificationChannel(channel);
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        if (!player.isPlaying()) player.start();
        startForeground(NOTIFICATION_ID, buildNotification(true));
        return START_STICKY;
    }

    private Notification buildNotification(boolean playing) {
        // 点击通知跳转 MusicActivity
        Intent contentIntent = new Intent(this, MusicActivity.class);
        PendingIntent contentPi = PendingIntent.getActivity(this, 0, contentIntent,
            PendingIntent.FLAG_IMMUTABLE);

        // 暂停按钮:发送广播到本 Service
        Intent pauseIntent = new Intent(ACTION_PAUSE).setPackage(getPackageName());
        PendingIntent pausePi = PendingIntent.getBroadcast(this, 1, pauseIntent,
            PendingIntent.FLAG_IMMUTABLE);

        return new NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("音乐播放器")
            .setContentText(playing ? "正在播放" : "已暂停")
            .setSmallIcon(R.drawable.ic_music)
            .setContentIntent(contentPi)
            .addAction(R.drawable.ic_pause, playing ? "暂停" : "播放", pausePi)
            .setOngoing(true)
            .build();
    }

    /** 接收暂停广播 */
    private final BroadcastReceiver pauseReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            if (player.isPlaying()) {
                player.pause();
                NotificationManager nm = getSystemService(NotificationManager.class);
                nm.notify(NOTIFICATION_ID, buildNotification(false));
            } else {
                player.start();
                NotificationManager nm = getSystemService(NotificationManager.class);
                nm.notify(NOTIFICATION_ID, buildNotification(true));
            }
        }
    };

    @Override
    public void onDestroy() {
        unregisterReceiver(pauseReceiver);
        if (player != null) {
            player.release();
            player = null;
        }
        super.onDestroy();
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
```

**MusicActivity.java**：

```java
public class MusicActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_music);

        findViewById(R.id.btn_play).setOnClickListener(v -> {
            Intent intent = new Intent(this, MusicService.class);
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                startForegroundService(intent);   // Android 8.0+
            } else {
                startService(intent);
            }
        });
    }
}
```

**说明**：
- Manifest 声明 `foregroundServiceType="mediaPlayback"`，适配 Android 14
- 通知点击用 `PendingIntent.FLAG_IMMUTABLE`，符合 Android 12+ 要求
- 暂停按钮通过广播触发，符合"通知按钮不直接启动 Service"的最佳实践
- `START_STICKY` 保证 Service 被杀后系统尝试重建
</details>

---

### 14. ⭐⭐ 广播收发题：网络状态监听 + 自定义广播

请实现以下需求：
1. 定义一个 `NetworkReceiver`，监听系统网络变化广播 `ConnectivityManager.CONNECTIVITY_ACTION`
2. 网络状态变化时，发送**自定义广播** `com.example.NETWORK_CHANGED`，携带 `is_connected` (boolean) 与 `network_type` (String) 字段
3. 再定义一个 `ToastReceiver` 接收上述自定义广播，弹出 Toast 提示"网络已连接: Wi-Fi"或"网络已断开"
4. 在 Activity 中用**动态注册**方式注册两个 Receiver，注意生命周期管理

<details>
<summary>查看答案</summary>

```java
public class MainActivity extends AppCompatActivity {
    public static final String ACTION_NETWORK_CHANGED = "com.example.NETWORK_CHANGED";
    public static final String EXTRA_CONNECTED = "is_connected";
    public static final String EXTRA_TYPE = "network_type";

    private NetworkReceiver networkReceiver;
    private ToastReceiver toastReceiver;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onStart() {
        super.onStart();
        // 1. 监听系统网络变化广播
        networkReceiver = new NetworkReceiver();
        registerReceiver(networkReceiver,
            new IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION));

        // 2. 监听自定义广播(显式指定包名,Android 8.0+ 仍可动态注册)
        toastReceiver = new ToastReceiver();
        IntentFilter filter = new IntentFilter(ACTION_NETWORK_CHANGED);
        registerReceiver(toastReceiver, filter);
    }

    @Override
    protected void onStop() {
        super.onStop();
        if (networkReceiver != null) {
            unregisterReceiver(networkReceiver);
            networkReceiver = null;
        }
        if (toastReceiver != null) {
            unregisterReceiver(toastReceiver);
            toastReceiver = null;
        }
    }

    /** 系统网络变化接收方:转发为自定义广播 */
    private class NetworkReceiver extends BroadcastReceiver {
        @Override
        public void onReceive(Context context, Intent intent) {
            ConnectivityManager cm = (ConnectivityManager)
                context.getSystemService(Context.CONNECTIVITY_SERVICE);
            NetworkInfo info = cm.getActiveNetworkInfo();
            boolean connected = info != null && info.isConnected();
            String type = "未知";
            if (connected) {
                type = (info.getType() == ConnectivityManager.TYPE_WIFI) ? "Wi-Fi" : "移动数据";
            }

            // 发送自定义广播,显式指定包名以兼容 Android 8.0+
            Intent custom = new Intent(ACTION_NETWORK_CHANGED);
            custom.setPackage(getPackageName());
            custom.putExtra(EXTRA_CONNECTED, connected);
            custom.putExtra(EXTRA_TYPE, type);
            sendBroadcast(custom);
        }
    }

    /** 自定义广播接收方:弹 Toast */
    private class ToastReceiver extends BroadcastReceiver {
        @Override
        public void onReceive(Context context, Intent intent) {
            boolean connected = intent.getBooleanExtra(EXTRA_CONNECTED, false);
            String type = intent.getStringExtra(EXTRA_TYPE);
            String msg = connected ? ("网络已连接: " + type) : "网络已断开";
            Toast.makeText(context, msg, Toast.LENGTH_SHORT).show();
        }
    }
}
```

**说明**：
- Android 7.0+ 起 `CONNECTIVITY_ACTION` 静态注册失效，必须动态注册
- 自定义广播 `setPackage(getPackageName())` 显式指定包名，确保投递并兼容 Android 8.0+
- 两个 Receiver 都在 `onStart` 注册、`onStop` 反注册，避免内存泄漏
- NetworkReceiver 转发广播实现"系统事件 → 应用内消息"的解耦
- Android 10+ 推荐改用 `ConnectivityManager.NetworkCallback`，但本题为考察广播机制
</details>

---

### 15. ⭐⭐⭐ Notification 通知题：消息推送通知

请实现一个**完整的消息通知工具类**，要求：
1. 在 Application 中创建 3 个渠道：消息（高）、下载（低）、音乐（低）
2. 实现 `notifyMessage(sender, content)`：发普通文本通知，点击跳转 `ChatActivity`，自动消失
3. 实现 `notifyMultiple(messages)`：用 InboxStyle 合并多条消息
4. 实现 `notifyProgress(progress)`：显示下载进度，更新同一 ID 通知，完成后清除进度
5. 通知 ID 与渠道 ID 用常量管理，PendingIntent 使用 `FLAG_IMMUTABLE`

<details>
<summary>查看答案</summary>

**App.java（Application 中创建渠道）**：

```java
public class App extends Application {
    public static final String CHANNEL_MSG_ID   = "message";
    public static final String CHANNEL_DL_ID    = "download";
    public static final String CHANNEL_MUSIC_ID = "music_playback";

    @Override
    public void onCreate() {
        super.onCreate();
        createChannels();
    }

    private void createChannels() {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) return;
        NotificationManager nm = getSystemService(NotificationManager.class);

        NotificationChannel msg = new NotificationChannel(
            CHANNEL_MSG_ID, "消息通知", NotificationManager.IMPORTANCE_HIGH);
        msg.enableLights(true);
        msg.enableVibration(true);

        NotificationChannel dl = new NotificationChannel(
            CHANNEL_DL_ID, "下载任务", NotificationManager.IMPORTANCE_LOW);

        NotificationChannel music = new NotificationChannel(
            CHANNEL_MUSIC_ID, "音乐播放", NotificationManager.IMPORTANCE_LOW);

        nm.createNotificationChannel(msg);
        nm.createNotificationChannel(dl);
        nm.createNotificationChannel(music);
    }
}
```

**NotifyHelper.java（通知工具类）**：

```java
public class NotifyHelper {
    public static final int MSG_NOTIFY_ID    = 2001;
    public static final int DL_NOTIFY_ID     = 2002;
    public static final int MUSIC_NOTIFY_ID  = 2003;

    private final Context context;
    private final NotificationManager nm;

    public NotifyHelper(Context ctx) {
        this.context = ctx.getApplicationContext();
        this.nm = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);
    }

    /** 1. 普通消息通知,点击跳转 ChatActivity */
    public void notifyMessage(String sender, String content) {
        Intent intent = new Intent(context, ChatActivity.class);
        intent.putExtra("sender", sender);
        intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP);
        PendingIntent pi = PendingIntent.getActivity(context, 0, intent,
            PendingIntent.FLAG_IMMUTABLE | PendingIntent.FLAG_UPDATE_CURRENT);

        Notification n = new NotificationCompat.Builder(context, App.CHANNEL_MSG_ID)
            .setSmallIcon(R.drawable.ic_msg)
            .setContentTitle(sender)
            .setContentText(content)
            .setContentIntent(pi)
            .setAutoCancel(true)
            .setPriority(NotificationCompat.PRIORITY_HIGH)   // 兼容 < 8.0
            .build();
        nm.notify(MSG_NOTIFY_ID, n);
    }

    /** 2. 多条消息合并:InboxStyle */
    public void notifyMultiple(List<String> messages) {
        NotificationCompat.InboxStyle style = new NotificationCompat.InboxStyle();
        for (String m : messages) style.addLine(m);
        style.setSummaryText("共 " + messages.size() + " 条消息");

        Intent intent = new Intent(context, MessageListActivity.class);
        PendingIntent pi = PendingIntent.getActivity(context, 0, intent,
            PendingIntent.FLAG_IMMUTABLE);

        Notification n = new NotificationCompat.Builder(context, App.CHANNEL_MSG_ID)
            .setSmallIcon(R.drawable.ic_msg)
            .setContentTitle("新消息")
            .setStyle(style)
            .setContentIntent(pi)
            .setAutoCancel(true)
            .build();
        nm.notify(MSG_NOTIFY_ID, n);
    }

    /** 3. 下载进度通知:progress 0~100,100 时清除进度 */
    public void notifyProgress(int progress) {
        NotificationCompat.Builder builder = new NotificationCompat.Builder(context, App.CHANNEL_DL_ID)
            .setSmallIcon(R.drawable.ic_download)
            .setContentTitle("正在下载")
            .setContentText("进度: " + progress + "%")
            .setOngoing(true);

        if (progress >= 100) {
            builder.setProgress(0, 0, false)
                   .setContentText("下载完成");
        } else {
            builder.setProgress(100, progress, false);
        }

        nm.notify(DL_NOTIFY_ID, builder.build());
    }

    /** 取消指定通知 */
    public void cancel(int notifyId) {
        nm.cancel(notifyId);
    }

    /** 取消全部 */
    public void cancelAll() {
        nm.cancelAll();
    }
}
```

**调用示例**：

```java
NotifyHelper helper = new NotifyHelper(this);

// 单条消息
helper.notifyMessage("Alice", "晚上一起吃饭吗?");

// 多条消息
helper.notifyMultiple(Arrays.asList(
    "Alice: 晚上一起吃饭吗?",
    "Bob: 代码已合并",
    "Tom: 项目明天上线"
));

// 模拟下载进度更新
for (int p = 0; p <= 100; p += 10) {
    helper.notifyProgress(p);
    Thread.sleep(500);   // 实际应在子线程
}
```

**说明**：
- 渠道按用户视角分类，让用户在系统设置中精细控制
- 高优先级通知用 `IMPORTANCE_HIGH` + `setPriority(PRIORITY_HIGH)`（兼容旧版本）
- 通知 ID 全局常量管理，避免冲突
- `PendingIntent.FLAG_IMMUTABLE | FLAG_UPDATE_CURRENT`：安全且能更新已有 Intent 数据
- 进度通知用同一 ID 反复 `notify` 更新，完成后 `setProgress(0,0,false)` 清除进度条
- `setOngoing(true)` 让下载中通知不可滑动清除，完成后需手动改回或 `cancel`
- `FLAG_ACTIVITY_NEW_TASK | FLAG_ACTIVITY_CLEAR_TOP`：跳转时清理任务栈，避免重复实例
</details>

---

## 考点统计与复习建议

### 考点分布统计表

| 题号 | 题型 | 涉及考点 | 难度 | 对应小节 |
| ---- | ---- | -------- | ---- | -------- |
| 1 | 选择 | Service 基本特征 | ⭐ | [[7.1 Service 服务基础、前台服务\|7.1]] |
| 2 | 选择 | startService vs bindService 生命周期 | ⭐ | [[7.1 Service 服务基础、前台服务\|7.1]] |
| 3 | 选择 | 广播注册方式与 8.0+ 限制 | ⭐⭐ | [[7.2 广播 BroadcastReceiver 使用\|7.2]] |
| 4 | 选择 | NotificationChannel | ⭐⭐ | [[7.3 Notification 通知实现\|7.3]] |
| 5 | 选择 | WorkManager PeriodicWorkRequest | ⭐⭐⭐ | [[7.4 工作任务调度基础\|7.4]] |
| 6 | 填空 | Service 两条生命周期 | ⭐ | [[7.1 Service 服务基础、前台服务\|7.1]] |
| 7 | 填空 | Android 8.0+ 后台限制 | ⭐⭐ | [[7.1 Service 服务基础、前台服务\|7.1]] |
| 8 | 填空 | PendingIntent FLAG_IMMUTABLE | ⭐⭐ | [[7.3 Notification 通知实现\|7.3]] |
| 9 | 简答 | startService vs bindService 对比 | ⭐⭐ | [[7.1 Service 服务基础、前台服务\|7.1]] |
| 10 | 简答 | 后台限制 + 前台服务通知原因 | ⭐⭐ | [[7.1 Service 服务基础、前台服务\|7.1]] |
| 11 | 简答 | 静态 vs 动态注册 + 隐式广播限制 | ⭐⭐ | [[7.2 广播 BroadcastReceiver 使用\|7.2]] |
| 12 | 简答 | 三种调度方案对比 | ⭐⭐⭐ | [[7.4 工作任务调度基础\|7.4]] |
| 13 | 代码 | 音乐播放前台 Service | ⭐⭐ | [[7.1 Service 服务基础、前台服务\|7.1]] |
| 14 | 代码 | 网络广播收发 | ⭐⭐ | [[7.2 广播 BroadcastReceiver 使用\|7.2]] |
| 15 | 代码 | Notification 完整工具类 | ⭐⭐⭐ | [[7.3 Notification 通知实现\|7.3]] |

### 复习建议

> [!tip] 高效复习路线
> 1. **第一优先（必考）**：Service 生命周期、startService vs bindService 对比，能默写前台 Service 完整代码（见第 1、2、6、9、10、13 题）
> 2. **第二优先**：前台服务 + Android 8.0+ 后台限制，理解为何"通知换运行权"（见第 7、10、13 题）
> 3. **第三优先**：广播注册方式与 Android 8.0+ 隐式广播限制，能区分静态/动态注册适用场景（见第 3、11、14 题）
> 4. **第四优先**：NotificationChannel 创建、PendingIntent FLAG_IMMUTABLE、通知样式（见第 4、8、15 题）
> 5. **第五优先**：WorkManager 任务调度，OneTimeWorkRequest vs PeriodicWorkRequest，三种方案对比（见第 5、12 题）
> 6. **动手实践**：15 题中代码设计题共 3 道，建议在 Android Studio 中至少完整实现第 13、15 题，跑通前台 Service + 通知 + 暂停按钮全流程
> 7. **版本要点**：Android 8.0 后台限制、Android 12 PendingIntent 标志位、Android 14 前台服务类型——三处版本变化是高频考点

## 章节导航

- 上级：[[MOC - 第7章|第7章 后台服务与消息通知]]
- 上一章习题：[[MOC - 第6章习题|第6章习题]]
- 下一章习题：[[MOC - 第8章习题|第8章习题]]
- 课程总览：[[MOC - 移动互联网开发技术|移动互联网开发技术]]
