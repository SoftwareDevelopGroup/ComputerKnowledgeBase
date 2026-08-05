---
domain: 网络与安全
subject: 移动互联网开发技术
type: exercise
chapter: 第3章 Activity 与页面交互
tags: [移动开发,习题,Activity生命周期,Intent,启动模式,Fragment]
prerequisites: ["计算机网络A","Java程序设计"]
aliases: [第3章习题, Activity习题, 第3章练习]
---

# MOC - 第3章习题

> [!info] 本章习题说明
> - 配套知识点：[[MOC - 第3章|第3章 Activity 与页面交互]]
> - 题目数量：**18 题**（选择 6 + 填空 3 + 简答 4 + 代码设计 5）
> - 难度梯度：⭐基础 / ⭐⭐中等 / ⭐⭐⭐较难
> - 答案折叠在每题下方的 `<details>` 块中，建议先独立作答再展开对照

## 一、选择题（6 题）

### 1. ⭐ 下列哪个回调方法在 Activity 整个生命周期中只会被调用一次？

A. onStart
B. onResume
C. onCreate
D. onPause

<details>
<summary>查看答案</summary>

**答案：C**

`onCreate` 在 Activity 首次创建时调用一次，用于加载布局和初始化。其他回调可能因状态切换被多次触发，例如按 Home 再返回时 `onStart`/`onResume`/`onPause` 都会再次调用。
</details>

---

### 2. ⭐ 用户在 Activity A 中按 Home 键回到桌面，下列回调顺序正确的是？

A. onPause → onDestroy
B. onPause → onStop
C. onStop → onDestroy
D. onRestart → onPause

<details>
<summary>查看答案</summary>

**答案：B**

按 Home 键时 Activity 由可见变为不可见：先 `onPause`（失去焦点）后 `onStop`（完全不可见）。Activity 仍在内存中存活，不会调用 `onDestroy`。
</details>

---

### 3. ⭐⭐ 关于 Activity 四种启动模式，下列描述正确的是？

A. singleTop 模式下，每次启动该 Activity 都会新建实例
B. singleTask 模式下，Activity 在整个系统中只有一个实例
C. singleInstance 模式下，Activity 独占一个任务栈
D. standard 模式下，同一个 Task 中只能有一个该 Activity 实例

<details>
<summary>查看答案</summary>

**答案：C**

- A 错：singleTop 栈顶已有该实例则复用，不会新建。
- B 错：singleTask 是"在当前 Task 中唯一"，并非全局唯一；全局唯一是 singleInstance。
- C 对：singleInstance 让 Activity 独占一个 Task，全局唯一。
- D 错：standard 默认每次都新建，可以有多个实例。
</details>

---

### 4. ⭐⭐ 关于隐式 Intent 的匹配规则，下列说法错误的是？

A. 一个 Intent 必须同时匹配 action、category、data 才能启动目标组件
B. `<intent-filter>` 中可以声明多个 action，Intent 只需匹配其中之一
C. Intent 中每个 category 都必须在 filter 中存在
D. 通过 `startActivity` 启动的隐式 Intent 不携带 `CATEGORY_DEFAULT`

<details>
<summary>查看答案</summary>

**答案：D**

D 错：通过 `startActivity` 启动的隐式 Intent **默认携带** `CATEGORY_DEFAULT`，因此 filter 中必须声明 `<category android:name="android.intent.category.DEFAULT" />` 才能被匹配到。
</details>

---

### 5. ⭐⭐ 下列关于 Fragment 的说法，正确的是？

A. Fragment 可以独立运行，不依赖 Activity
B. Fragment 的 `onCreateView` 用于初始化非视图数据
C. Fragment 通过 `getActivity()` 获取宿主 Activity
D. Fragment 之间无法通信

<details>
<summary>查看答案</summary>

**答案：C**

- A 错：Fragment 必须寄生于 Activity。
- B 错：`onCreateView` 用于加载 Fragment 视图布局，非视图初始化应在 `onCreate`。
- C 对：`getActivity()` 返回宿主 Activity。
- D 错：Fragment 之间可通过共享 ViewModel、接口回调或 Fragment Result API 通信。
</details>

---

### 6. ⭐⭐⭐ 用户旋转屏幕时，默认情况下 Activity 的回调顺序是？

A. onPause → onResume
B. onPause → onStop → onRestart → onResume
C. onPause → onStop → onDestroy → onCreate → onStart → onResume
D. onConfigurationChanged

<details>
<summary>查看答案</summary>

**答案：C**

默认配置下旋转屏幕会让 Activity 完全销毁重建：`onPause → onStop → onDestroy → onCreate → onStart → onResume`。只有当 AndroidManifest 中配置了 `android:configChanges="orientation|screenSize"` 时才会只调 `onConfigurationChanged` 而不重建（选项 D 是特殊配置下的情况）。
</details>

---

## 二、填空题（3 题）

### 7. ⭐ Activity 的三种基本状态分别是 ________、________、________。

<details>
<summary>查看答案</summary>

**答案：运行态（Resumed）、暂停态（Paused）、停止态（Stopped）**

- Resumed：可见 + 可交互
- Paused：部分可见 + 不可交互
- Stopped：完全不可见
</details>

---

### 8. ⭐ Activity 之间传递对象有两种序列化方式，分别是实现 ________ 接口和实现 ________ 接口。其中 ________ 性能更高，是 Android 推荐的方式。

<details>
<summary>查看答案</summary>

**答案：Serializable、Parcelable、Parcelable**

Serializable 是 Java 自带的反射机制，性能较差；Parcelable 是 Android 专用的内存序列化方案，性能约高 10 倍，是 Android 推荐方式。
</details>

---

### 9. ⭐⭐ Android 的四种启动模式分别是 ________、________、________、________，其中默认模式是 ________。

<details>
<summary>查看答案</summary>

**答案：standard、singleTop、singleTask、singleInstance；默认是 standard**

- standard：每次新建（默认）
- singleTop：栈顶复用
- singleTask：栈中唯一，清上方
- singleInstance：独占任务栈
</details>

---

## 三、简答题（4 题）

### 10. ⭐⭐ 简述 Activity 七个生命周期回调方法的作用及典型应用场景。

<details>
<summary>查看答案</summary>

**七个回调方法及作用：**

| 回调 | 作用 | 典型应用 |
| ---- | ---- | -------- |
| `onCreate` | Activity 首次创建，初始化 | 加载布局、初始化视图与数据、从 savedInstanceState 恢复状态 |
| `onStart` | Activity 即将可见 | 注册广播、开启动画 |
| `onResume` | Activity 获得焦点可交互 | 开启摄像头、定位、传感器 |
| `onPause` | Activity 失去焦点 | 持久化关键数据、释放摄像头 |
| `onStop` | Activity 完全不可见 | 释放重型资源、保存草稿 |
| `onDestroy` | Activity 销毁 | 释放所有资源、反注册广播 |
| `onRestart` | 由 Stopped 重新进入可见前 | 复用已有数据 |

应用场景示例：摄像头应在 onResume 开启、onPause 释放；广播接收器在 onStart 注册、onStop 解除；表单数据在 onSaveInstanceState 保存、onCreate 恢复。
</details>

---

### 11. ⭐⭐ 对比显式 Intent 与隐式 Intent，并分别说明各自适用场景。

<details>
<summary>查看答案</summary>

| 维度 | 显式 Intent | 隐式 Intent |
| ---- | ----------- | ----------- |
| 目标指定 | 类名（`TargetActivity.class`） | action + category + data 匹配 |
| 应用范围 | 通常应用内 | 跨应用、系统应用 |
| 匹配机制 | 直接跳转，无需匹配 | 系统按 intent-filter 匹配 |
| 安全性 | 高，不会被劫持 | 较低，可能被恶意 Activity 接管 |
| 典型场景 | 应用内页面跳转（登录→主页） | 打开网页、拨号、分享等系统功能 |

**显式 Intent 适用场景**：应用内部已知目标的跳转，如登录页跳主页、列表页跳详情页。

**隐式 Intent 适用场景**：调用系统或其他应用的功能，如打开浏览器访问 URL、拨打电话、发送短信、分享文本到社交应用。
</details>

---

### 12. ⭐⭐ 解释四种启动模式（standard、singleTop、singleTask、singleInstance）的行为差异，并各举一个典型应用场景。

<details>
<summary>查看答案</summary>

| 启动模式 | 行为 | 典型场景 |
| -------- | ---- | -------- |
| **standard** | 每次启动都新建实例并入栈 | 普通详情页、列表页（默认模式） |
| **singleTop** | 栈顶已是该 Activity 则复用（调 onNewIntent），否则新建 | 推送通知点击页、消息列表页（避免重复新建） |
| **singleTask** | 栈中已有该实例则复用并清掉其上方所有 Activity | 应用主界面、登录页（"回到主页"清栈） |
| **singleInstance** | 独占一个新 Task，全局唯一实例 | 系统级全局唯一页面（如系统拨号界面、地图主页） |

**示例场景**：
- standard：商品详情页，每次点击都新建实例，允许栈中有多个。
- singleTop：消息列表页，从通知栏多次点击只复用栈顶实例。
- singleTask：主页 MainActivity，从任意深层页跳回时清掉中间页。
- singleInstance：电话拨号界面，全局唯一，独占 Task。
</details>

---

### 13. ⭐⭐ 简述 Fragment 与 Activity 生命周期的关系，并说明 Fragment 比 Activity 多出的回调方法及其作用。

<details>
<summary>查看答案</summary>

**关系**：Fragment 的生命周期由宿主 Activity 的生命周期驱动，Activity 的 `onCreate` → Fragment `onAttach/onCreate/onCreateView/onActivityCreated` → Activity `onStart` → Fragment `onStart` → Activity `onResume` → Fragment `onResume`，销毁过程同步对应。

**Fragment 多出的回调方法**：

| 回调 | 作用 |
| ---- | ---- |
| `onAttach` | Fragment 与 Activity 建立关联，可获取 Activity 引用 |
| `onCreateView` | 创建 Fragment 的视图布局（加载 XML） |
| `onActivityCreated` | 宿主 Activity 的 onCreate 完成（已废弃，新版用 onViewCreated） |
| `onDestroyView` | Fragment 视图销毁，可清理视图资源 |
| `onDetach` | Fragment 与 Activity 解除关联 |

这些额外回调是因为 Fragment 既有"实例生命周期"又有"视图生命周期"，需要分别处理视图创建与销毁；Activity 没有这种分离。
</details>

---

## 四、代码设计题（5 题）

### 14. ⭐⭐ 生命周期分析题

某 Activity 中有如下代码，请分析：
1. 用户首次启动该 Activity，写出回调顺序；
2. 用户按 Home 键后再返回应用，写出回调顺序；
3. 用户旋转屏幕，写出回调顺序，并说明 `count` 的值变化及如何保留它。

```java
public class CounterActivity extends AppCompatActivity {
    private int count = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_counter);
        count = 0;
        Log.d("LC", "onCreate");
    }
    @Override protected void onStart()   { super.onStart();   Log.d("LC", "onStart"); }
    @Override protected void onResume()  { super.onResume();  Log.d("LC", "onResume"); }
    @Override protected void onPause()   { super.onPause();   Log.d("LC", "onPause"); }
    @Override protected void onStop()    { super.onStop();    Log.d("LC", "onStop"); }
    @Override protected void onDestroy() { super.onDestroy(); Log.d("LC", "onDestroy"); }
    @Override protected void onRestart() { super.onRestart(); Log.d("LC", "onRestart"); }

    public void onClickIncrement(View v) {
        count++;
    }
}
```

<details>
<summary>查看答案</summary>

**(1) 首次启动**：
```
onCreate → onStart → onResume
```

**(2) 按 Home 键后返回**：
```
按 Home：onPause → onStop
返回应用：onRestart → onStart → onResume
```

**(3) 旋转屏幕**：
```
onPause → onStop → onDestroy → onCreate → onStart → onResume
```

**`count` 值变化**：旋转屏后 Activity 销毁重建，`onCreate` 中 `count = 0` 把计数清零，用户之前的累加结果丢失。

**保留方案**：通过 `onSaveInstanceState` 保存 count，在 `onCreate` 中恢复：

```java
public class CounterActivity extends AppCompatActivity {
    private int count = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_counter);
        if (savedInstanceState != null) {
            count = savedInstanceState.getInt("count", 0);   // 恢复
        } else {
            count = 0;
        }
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putInt("count", count);   // 保存
    }

    public void onClickIncrement(View v) {
        count++;
    }
}
```
</details>

---

### 15. ⭐⭐ Intent 跳转代码题

请编写实现以下需求的完整代码：
1. `MainActivity` 中有一个"登录"按钮，点击后通过**显式 Intent** 跳转到 `LoginActivity`，并携带一个 `welcome` 字符串"欢迎使用本系统"；
2. `LoginActivity` 中有用户名输入框和"提交"按钮，点击提交后通过**隐式 Intent** 打开系统浏览器访问 `https://www.example.com`，并将用户名作为 URL 查询参数 `user`。

<details>
<summary>查看答案</summary>

```java
// ============ MainActivity.java ============
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        findViewById(R.id.btn_login).setOnClickListener(v -> {
            // 显式 Intent 跳转
            Intent intent = new Intent(MainActivity.this, LoginActivity.class);
            intent.putExtra("welcome", "欢迎使用本系统");
            startActivity(intent);
        });
    }
}

// ============ LoginActivity.java ============
public class LoginActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        // 接收正向传来的数据
        String welcome = getIntent().getStringExtra("welcome");
        TextView tvWelcome = findViewById(R.id.tv_welcome);
        if (welcome != null) tvWelcome.setText(welcome);

        EditText etUser = findViewById(R.id.et_username);
        findViewById(R.id.btn_submit).setOnClickListener(v -> {
            String username = etUser.getText().toString().trim();
            if (username.isEmpty()) {
                Toast.makeText(this, "请输入用户名", Toast.LENGTH_SHORT).show();
                return;
            }
            // 隐式 Intent 打开浏览器, 携带用户名作为查询参数
            String url = "https://www.example.com?user=" + Uri.encode(username);
            Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
            if (intent.resolveActivity(getPackageManager()) != null) {
                startActivity(intent);
            } else {
                Toast.makeText(this, "未找到浏览器", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

对应布局省略（`activity_main.xml` 含 `btn_login` 按钮；`activity_login.xml` 含 `tv_welcome`、`et_username`、`btn_submit`）。
</details>

---

### 16. ⭐⭐⭐ 启动模式场景分析题

假设应用有以下页面与栈状态：
- `MainActivity`（已配置 `launchMode="singleTask"`）
- `DetailActivity`（standard）
- 当前栈状态（顶→底）：`DetailActivity → MainActivity`

请回答：
1. 此时再启动 `MainActivity`，写出栈变化和回调顺序；
2. 此时再启动 `DetailActivity`（标准模式），栈变成什么？
3. 若 `MainActivity` 改为 `singleInstance`，从 `MainActivity` 启动 `DetailActivity`，Task 结构如何？

<details>
<summary>查看答案</summary>

**(1) 启动 MainActivity（singleTask）**

栈中已有 MainActivity 实例，系统找到它并**清掉其上方的 DetailActivity**，复用 MainActivity 实例：
- 栈变为：`MainActivity`（DetailActivity 被销毁）
- DetailActivity 回调：`onPause → onStop → onDestroy`
- MainActivity 回调：`onNewIntent → onRestart → onStart → onResume`

**(2) 再启动 DetailActivity（standard）**

新建 DetailActivity 实例入栈：
- 栈变为：`DetailActivity → MainActivity`

**(3) MainActivity 改为 singleInstance**

singleInstance 让 MainActivity 独占一个 Task（假设 TaskA），且全局唯一：
- `TaskA：MainActivity`（MainActivity 是该 Task 唯一 Activity）
- 从 MainActivity 启动 DetailActivity 时，DetailActivity 会被放入**另一个 Task**（TaskB），不会进入 TaskA：
  - `TaskB：DetailActivity`
  - `TaskA：MainActivity`
- 按返回键时先退出 DetailActivity（TaskB），再回到 MainActivity（TaskA）。
</details>

---

### 17. ⭐⭐⭐ Fragment 实现题

请编写代码实现"底部导航栏 + 三个 Fragment 切换"功能：
1. 三个 Fragment：`HomeFragment`、`FindFragment`、`MineFragment`；
2. Activity 中通过 `BottomNavigationView` 切换；
3. 使用 `hide/show` 方式切换（避免 Fragment 反复重建）；
4. 初始显示 `HomeFragment`。

<details>
<summary>查看答案</summary>

```java
// ============ HomeFragment.java（FindFragment、MineFragment 类似） ============
public class HomeFragment extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_home, container, false);
        TextView tv = view.findViewById(R.id.tv_title);
        tv.setText("首页");
        return view;
    }
}

// ============ MainActivity.java ============
public class MainActivity extends AppCompatActivity {
    private Fragment homeFrag = new HomeFragment();
    private Fragment findFrag = new FindFragment();
    private Fragment mineFrag = new MineFragment();
    private Fragment activeFrag = homeFrag;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 初始化：把三个 Fragment 都 add, 但只显示首页
        getSupportFragmentManager().beginTransaction()
            .add(R.id.fragment_container, mineFrag).hide(mineFrag)
            .add(R.id.fragment_container, findFrag).hide(findFrag)
            .add(R.id.fragment_container, homeFrag)
            .commit();

        BottomNavigationView nav = findViewById(R.id.bottom_nav);
        nav.setOnItemSelectedListener(item -> {
            Fragment target = null;
            int id = item.getItemId();
            if (id == R.id.nav_home)      target = homeFrag;
            else if (id == R.id.nav_find) target = findFrag;
            else if (id == R.id.nav_mine) target = mineFrag;
            if (target != null) {
                getSupportFragmentManager().beginTransaction()
                    .hide(activeFrag)
                    .show(target)
                    .commit();
                activeFrag = target;
                return true;
            }
            return false;
        });
    }
}
```

```xml
<!-- res/layout/activity_main.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <FrameLayout
        android:id="@+id/fragment_container"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1" />

    <com.google.android.material.bottomnavigation.BottomNavigationView
        android:id="@+id/bottom_nav"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        app:menu="@menu/bottom_nav_menu" />
</LinearLayout>
```

```xml
<!-- res/menu/bottom_nav_menu.xml -->
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@+id/nav_home" android:title="首页" android:icon="@drawable/ic_home" />
    <item android:id="@+id/nav_find" android:title="发现" android:icon="@drawable/ic_find" />
    <item android:id="@+id/nav_mine" android:title="我的" android:icon="@drawable/ic_mine" />
</menu>
```

```xml
<!-- res/layout/fragment_home.xml（其他 Fragment 类似） -->
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <TextView
        android:id="@+id/tv_title"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:textSize="24sp" />
</FrameLayout>
```
</details>

---

### 18. ⭐⭐⭐ 综合题：Activity 间数据传递与回传

请实现以下需求：
1. `MainActivity` 中点击"选择城市"按钮，跳转到 `CityActivity`；
2. `CityActivity` 显示城市列表（用 ListView 模拟即可），用户点击某城市后；
3. 把城市名称和邮政编码回传给 `MainActivity`；
4. `MainActivity` 接收后在 TextView 中显示"已选择：城市名（邮编）"；
5. 用户取消选择时（按返回键），`MainActivity` 不更新。

<details>
<summary>查看答案</summary>

```java
// ============ MainActivity.java ============
public class MainActivity extends AppCompatActivity {
    private static final int REQ_CITY = 2001;
    private TextView tvResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvResult = findViewById(R.id.tv_result);
        findViewById(R.id.btn_select_city).setOnClickListener(v -> {
            Intent intent = new Intent(this, CityActivity.class);
            startActivityForResult(intent, REQ_CITY);
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQ_CITY && resultCode == RESULT_OK && data != null) {
            String city = data.getStringExtra("city");
            String zip  = data.getStringExtra("zip");
            tvResult.setText("已选择：" + city + "（" + zip + "）");
        }
        // 若 resultCode != RESULT_OK（用户取消）则不更新, 保持原显示
    }
}
```

```java
// ============ CityActivity.java ============
public class CityActivity extends AppCompatActivity {
    // 模拟城市数据
    private final String[] cities = {"北京", "上海", "广州", "深圳"};
    private final String[] zips   = {"100000", "200000", "510000", "518000"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_city);

        ListView listView = findViewById(R.id.lv_cities);
        ArrayAdapter<String> adapter = new ArrayAdapter<>(
            this, android.R.layout.simple_list_item_1, cities);
        listView.setAdapter(adapter);

        listView.setOnItemClickListener((parent, view, position, id) -> {
            Intent result = new Intent();
            result.putExtra("city", cities[position]);
            result.putExtra("zip", zips[position]);
            setResult(RESULT_OK, result);
            finish();
        });

        // 用户按返回键时默认 resultCode 为 RESULT_CANCELED, 无需特殊处理
    }

    @Override
    public void onBackPressed() {
        // 显式标记取消（也可不写, 系统默认就是 RESULT_CANCELED）
        setResult(RESULT_CANCELED);
        super.onBackPressed();
    }
}
```

```xml
<!-- res/layout/activity_main.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <Button
        android:id="@+id/btn_select_city"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="选择城市" />

    <TextView
        android:id="@+id/tv_result"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp"
        android:text="尚未选择"
        android:textSize="18sp" />
</LinearLayout>
```

```xml
<!-- res/layout/activity_city.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <ListView
        android:id="@+id/lv_cities"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
</LinearLayout>
```
</details>

---

## 考点统计与复习建议

### 考点分布统计表

| 题号 | 题型 | 涉及考点 | 难度 | 对应小节 |
| ---- | ---- | -------- | ---- | -------- |
| 1 | 选择 | onCreate 调用次数 | ⭐ | [[3.1 Activity 生命周期、状态切换\|3.1]] |
| 2 | 选择 | 按 Home 键回调 | ⭐ | [[3.1 Activity 生命周期、状态切换\|3.1]] |
| 3 | 选择 | 启动模式行为 | ⭐⭐ | [[3.4 任务栈、启动模式\|3.4]] |
| 4 | 选择 | 隐式 Intent 匹配 | ⭐⭐ | [[3.2 Intent 显式跳转、隐式意图\|3.2]] |
| 5 | 选择 | Fragment 基础 | ⭐⭐ | [[3.5 Fragment 碎片基础使用\|3.5]] |
| 6 | 选择 | 旋转屏回调 | ⭐⭐⭐ | [[3.1 Activity 生命周期、状态切换\|3.1]] |
| 7 | 填空 | 三种状态 | ⭐ | [[3.1 Activity 生命周期、状态切换\|3.1]] |
| 8 | 填空 | Serializable/Parcelable | ⭐ | [[3.3 Activity 之间数据传递、回传数据\|3.3]] |
| 9 | 填空 | 四种启动模式 | ⭐⭐ | [[3.4 任务栈、启动模式\|3.4]] |
| 10 | 简答 | 七个回调作用 | ⭐⭐ | [[3.1 Activity 生命周期、状态切换\|3.1]] |
| 11 | 简答 | 显式 vs 隐式 Intent | ⭐⭐ | [[3.2 Intent 显式跳转、隐式意图\|3.2]] |
| 12 | 简答 | 四种启动模式对比 | ⭐⭐ | [[3.4 任务栈、启动模式\|3.4]] |
| 13 | 简答 | Fragment 生命周期 | ⭐⭐ | [[3.5 Fragment 碎片基础使用\|3.5]] |
| 14 | 代码 | 生命周期分析与状态保存 | ⭐⭐ | [[3.1 Activity 生命周期、状态切换\|3.1]] |
| 15 | 代码 | Intent 跳转代码 | ⭐⭐ | [[3.2 Intent 显式跳转、隐式意图\|3.2]] |
| 16 | 代码 | 启动模式场景分析 | ⭐⭐⭐ | [[3.4 任务栈、启动模式\|3.4]] |
| 17 | 代码 | Fragment 底部导航实现 | ⭐⭐⭐ | [[3.5 Fragment 碎片基础使用\|3.5]] |
| 18 | 代码 | 数据传递与回传 | ⭐⭐⭐ | [[3.3 Activity 之间数据传递、回传数据\|3.3]] |

### 复习建议

> [!tip] 高效复习路线
> 1. **第一优先（必考）**：Activity 七个生命周期回调的**顺序与触发时机**，必须能默写五种典型场景的回调序列（见第 1、2、6、14 题）。
> 2. **第二优先**：四种启动模式的**栈行为差异**，结合 singleTask 清栈、singleInstance 独占 Task 的场景理解（见第 3、9、12、16 题）。
> 3. **第三优先**：Intent 显式/隐式机制、putExtra 与 startActivityForResult 回传流程，能写完整代码（见第 4、8、11、15、18 题）。
> 4. **第四优先**：Fragment 生命周期与 Activity 的对应、动态添加流程（见第 5、13、17 题）。
> 5. **动手实践**：18 题中代码设计题共 5 道，建议在 Android Studio 中至少完整实现第 15、17、18 题，加深对 Intent、Fragment、回传机制的理解。

## 章节导航

- 上级：[[MOC - 第3章|第3章 Activity 与页面交互]]
- 上一章习题：[[MOC - 第2章习题|第2章习题]]
- 下一章习题：[[MOC - 第4章习题|第4章习题]]
- 课程总览：[[MOC - 移动互联网开发技术|移动互联网开发技术]]
