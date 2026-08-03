---
domain: 网络与安全
subject: 移动互联网开发技术
type: exercise
chapter: 第4章 Android UI 界面开发
tags: [移动开发,习题,UI布局,RecyclerView,事件处理]
prerequisites: ["计算机网络A","Java程序设计"]
aliases: [第4章习题, UI开发习题, 第4章练习]
---

# MOC - 第4章习题

> [!info] 本章习题说明
> - 配套知识点：[[MOC - 第4章|第4章 Android UI 界面开发]]
> - 题目数量：**18 题**（选择 6 + 填空 3 + 简答 4 + 代码设计 5）
> - 难度梯度：⭐基础 / ⭐⭐中等 / ⭐⭐⭐较难
> - 答案折叠在每题下方的 `<details>` 块中，建议先独立作答再展开对照
> - 代码设计题需在 Android Studio 中动手实现，加深对 RecyclerView Adapter、布局 XML、事件处理的掌握

## 一、选择题（6 题）

### 1. ⭐ 在 LinearLayout 中使用 `android:layout_weight="2"` 分配剩余空间时，对应方向的尺寸属性应当写成？

A. `wrap_content`
B. `match_parent`
C. `0dp`
D. 不写该属性

<details>
<summary>查看答案</summary>

**答案：C**

使用 weight 时，对应方向尺寸应写 `0dp`，让系统按 `weight / 总权重 × 父容器尺寸` 直接计算最终尺寸。若写 `wrap_content` 会先按内容占一份再分配剩余空间，结果不直观；写 `match_parent` 会导致每项先占满再反向分配，行为反常。
</details>

---

### 2. ⭐⭐ 关于 RecyclerView，下列说法错误的是？

A. RecyclerView 必须设置 LayoutManager 才能显示内容
B. RecyclerView 强制使用 ViewHolder 模式
C. RecyclerView 内置了 `setOnItemClickListener`，可直接设置 Item 点击事件
D. RecyclerView 通过更换 LayoutManager 可实现线性、网格、瀑布流三种排列

<details>
<summary>查看答案</summary>

**答案：C**

RecyclerView **没有内置** `setOnItemClickListener`（这是与 ListView 的重要区别）。开发者需在 Adapter 内部为 `holder.itemView` 设置点击监听，并通过自定义接口回调把 position 传回 Activity。其他三项描述均正确。
</details>

---

### 3. ⭐ 关于 Android 尺寸单位，下列说法正确的是？

A. `px` 是推荐单位，所有尺寸都应使用 px
B. `dp` 会随系统字号设置缩放，适合用于文字大小
C. `sp` 用于控件尺寸与间距，`dp` 用于文字大小
D. `sp` 在 `dp` 基础上还会随系统字号设置缩放，是文字大小的推荐单位

<details>
<summary>查看答案</summary>

**答案：D**

- A 错：px 不随密度缩放，不同设备物理大小不一致，不应直接使用。
- B 错：dp **不**随系统字号缩放，只有 sp 才会。
- C 错：dp 用于控件尺寸与间距，sp 用于文字大小，二者刚好相反。
- D 对：sp 在 dp 基础上还跟随系统字号缩放，是文字大小推荐单位。
</details>

---

### 4. ⭐⭐ 关于 ListView 与 RecyclerView 的对比，下列描述错误的是？

A. ListView 不强制使用 ViewHolder，RecyclerView 强制使用
B. RecyclerView 通过更换 LayoutManager 可支持横向滚动，ListView 不支持
C. RecyclerView 默认带 Item 增删动画，ListView 默认无动画
D. RecyclerView 比 ListView 更轻量，不需要引入额外依赖

<details>
<summary>查看答案</summary>

**答案：D**

D 错：RecyclerView 不在 Android SDK 自带类库中，需在 `app/build.gradle` 引入 `androidx.recyclerview:recyclerview` 依赖，比 ListView 更"重"——但带来更强的能力。其他三项描述均正确。
</details>

---

### 5. ⭐⭐⭐ 在事件分发机制中，下列哪个方法**只有 ViewGroup 才有**？

A. `dispatchTouchEvent`
B. `onInterceptTouchEvent`
C. `onTouchEvent`
D. 以上三个方法所有 View 都有

<details>
<summary>查看答案</summary>

**答案：B**

- `dispatchTouchEvent`：Activity、ViewGroup、View 都有。
- `onInterceptTouchEvent`：**仅 ViewGroup 有**，因为只有容器才需要决定"是否拦截事件不传给子 View"。View 是叶子节点没有子 View，无需拦截；Activity 是顶层分发者也无需拦截。
- `onTouchEvent`：Activity、ViewGroup、View 都有。
</details>

---

### 6. ⭐ 关于 Android 资源目录，下列说法错误的是？

A. `mipmap/` 目录专门用于存放应用启动器图标
B. `values-zh-rCN/strings.xml` 用于提供简中文字符串资源
C. `drawable/` 目录可存放 PNG、VectorDrawable、Shape XML 等图片资源
D. `values-night/` 用于提供横屏模式下的资源变体

<details>
<summary>查看答案</summary>

**答案：D**

D 错：`values-night/` 是**夜间模式（深色模式）**的资源变体，与屏幕方向无关。横屏模式的限定符是 `values-land/`。其他三项描述均正确。
</details>

---

## 二、填空题（3 题）

### 7. ⭐ 实现 RecyclerView.Adapter 必须重写三个方法，分别是 ________、________、________。

<details>
<summary>查看答案</summary>

**答案：`onCreateViewHolder`、`onBindViewHolder`、`getItemCount`**

- `onCreateViewHolder(parent, viewType)`：加载 Item 布局并创建 ViewHolder。
- `onBindViewHolder(holder, position)`：把数据绑定到 ViewHolder。
- `getItemCount()`：返回数据总条数。
</details>

---

### 8. ⭐ Android 常用的四种布局是 ________、________、________、________，其中默认根布局、官方主推的扁平化布局是 ________。

<details>
<summary>查看答案</summary>

**答案：LinearLayout（线性布局）、RelativeLayout（相对布局）、ConstraintLayout（约束布局）、FrameLayout（帧布局）；官方主推的是 ConstraintLayout**

ConstraintLayout 通过约束求解器在运行时计算控件位置，最大优势是用扁平结构替代多层嵌套，减少 View 树层级、提升测量性能。
</details>

---

### 9. ⭐⭐ Android 触摸事件分发机制中，事件流向自顶向下依次调用 ________、________、________ 三个方法。其中只有 ViewGroup 才拥有的是 ________。

<details>
<summary>查看答案</summary>

**答案：`dispatchTouchEvent`、`onInterceptTouchEvent`、`onTouchEvent`；只有 ViewGroup 才有的是 `onInterceptTouchEvent`**

事件流向：Activity → ViewGroup → View。`dispatchTouchEvent` 负责分发，`onInterceptTouchEvent` 负责拦截（仅 ViewGroup），`onTouchEvent` 负责消费处理。
</details>

---

## 三、简答题（4 题）

### 10. ⭐⭐ 对比 LinearLayout、RelativeLayout、ConstraintLayout、FrameLayout 四种布局的定位方式、性能特点与典型场景。

<details>
<summary>查看答案</summary>

| 维度 | LinearLayout | RelativeLayout | ConstraintLayout | FrameLayout |
| ---- | ------------ | -------------- | ---------------- | ----------- |
| 定位方式 | 单方向顺序排列 + 权重 | 相对父容器/兄弟组件 | 约束求解 + Bias + Chain | 左上角叠加 |
| 嵌套倾向 | 高（复杂结构需多层） | 中 | 极低（扁平化） | 低 |
| 性能 | 中 | 中（双趟测量） | 高（求解器优化） | 高 |
| 比例分配 | weight 支持 | 不直接支持 | Guideline + 百分比支持 | 不支持 |
| 典型场景 | 简单表单、按钮行 | 中等复杂相对关系 | 复杂界面、扁平化首选 | Fragment 容器、图层叠加 |
| 推荐度 | 简单场景可用 | 旧项目兼容 | **官方主推** | 容器专用 |

**选型原则**：复杂界面优先 ConstraintLayout 扁平化；简单线性结构用 LinearLayout；Fragment 容器固定用 FrameLayout；旧项目保留 RelativeLayout。
</details>

---

### 11. ⭐⭐ 简述 RecyclerView 的四大核心组件及其职责。

<details>
<summary>查看答案</summary>

| 组件 | 职责 | 是否必需 |
| ---- | ---- | -------- |
| **Adapter** | 连接数据源与视图，负责创建 ViewHolder 与绑定数据 | 是 |
| **ViewHolder** | 持有 Item 内部控件引用，避免反复 `findViewById` | 是 |
| **LayoutManager** | 决定 Item 的排列方式（线性/网格/瀑布流） | 是 |
| **ItemDecoration** | Item 之间的分隔线、间距等装饰 | 否 |
| **ItemAnimator** | Item 增删改的动画（有默认实现） | 否 |

**关键点**：
- Adapter 三个必须重写的方法：`onCreateViewHolder`、`onBindViewHolder`、`getItemCount`。
- 三种 LayoutManager：`LinearLayoutManager`（线性）、`GridLayoutManager`（网格）、`StaggeredGridLayoutManager`（瀑布流）。
- RecyclerView 把"排列""装饰""动画"三个职责分离，体现了关注点分离的设计思想。
</details>

---

### 12. ⭐⭐ 辨析 dp、sp、px 三种尺寸单位的含义，并说明各自适用场景。

<details>
<summary>查看答案</summary>

| 单位 | 全称 | 含义 | 是否随密度缩放 | 是否随系统字号缩放 | 典型用途 |
| ---- | ---- | ---- | -------------- | ------------------ | -------- |
| `px` | pixel | 屏幕物理像素 | 否 | 否 | 几乎不用 |
| `dp` / `dip` | density-independent pixel | 密度无关像素，1dp = 1px on mdpi（160dpi） | 是 | 否 | 控件尺寸、间距、边距 |
| `sp` | scale-independent pixel | 缩放无关像素，dp 基础上还跟随系统字号缩放 | 是 | 是 | **所有文字大小** |

**换算公式**：$px = dp \times \frac{dpi}{160}$

**核心要点**：
- dp 用于控件尺寸与间距，保证不同密度屏幕上视觉大小一致。
- sp 用于文字大小，除随密度缩放外还会跟随系统"字号设置"放大，适配无障碍需求。
- px 不应直接使用，因为高密度屏幕上 100px 物理尺寸远小于低密度屏幕。
</details>

---

### 13. ⭐⭐⭐ 详细描述 Android 触摸事件分发机制的流程，说明 `dispatchTouchEvent`、`onInterceptTouchEvent`、`onTouchEvent` 三个方法的作用与调用顺序。

<details>
<summary>查看答案</summary>

**事件传递方向**：Activity → 顶层 ViewGroup → 子 ViewGroup → 子 View；消费后向上回传。

**三个方法作用**：

| 方法 | 拥有者 | 作用 |
| ---- | ------ | ---- |
| `dispatchTouchEvent` | Activity / ViewGroup / View | 分发事件：决定交给自己处理还是向下分发 |
| `onInterceptTouchEvent` | **仅 ViewGroup** | 拦截事件：判断是否把事件拦截给自己，不传给子 View |
| `onTouchEvent` | Activity / ViewGroup / View | 处理事件：消费触摸事件的具体逻辑 |

**调用顺序**：

1. **Activity.dispatchTouchEvent** 接收事件，调用顶层 ViewGroup 的 dispatchTouchEvent。
2. **ViewGroup.dispatchTouchEvent** 调用 `onInterceptTouchEvent` 判断是否拦截：
   - 返回 `true`：拦截，调用本 ViewGroup 的 `onTouchEvent` 处理。
   - 返回 `false`：不拦截，把事件分发给命中（点击区域内）的子 View。
3. **子 View.dispatchTouchEvent** 先调 `OnTouchListener.onTouch`（若设置了）：
   - `onTouch` 返回 `true`：消费，事件结束。
   - `onTouch` 返回 `false`：调 View 自身的 `onTouchEvent`，再判断是否触发 `onClick`/`onLongClick`。
4. **若子 View 不消费**：事件回传给父 ViewGroup 的 `onTouchEvent`，逐层向上回传，最终到 Activity 的 `onTouchEvent`。

**返回值口诀**：
- `dispatchTouchEvent` 返回 true：本层"消费"，不再向下传。
- `onInterceptTouchEvent` 返回 true：拦截，不传给子 View，自己处理。
- `onTouchEvent` 返回 true：消费事件；返回 false：不消费，回传给上层。

**典型应用**：处理外层 ViewPager 与内层 ListView 的滑动冲突，在父容器 `onInterceptTouchEvent` 中按 dx/dy 比较判定方向，决定是否拦截。
</details>

---

## 四、代码设计题（5 题）

### 14. ⭐⭐⭐ RecyclerView Adapter 完整实现

请编写一个完整的 RecyclerView 适配器，实现通讯录列表：
1. 数据模型 `Contact`，包含 `name` 和 `phone` 两个字段；
2. 适配器 `ContactAdapter` 继承 `RecyclerView.Adapter`，强制使用 ViewHolder；
3. Item 布局 `item_contact.xml` 包含姓名 TextView 和电话 TextView；
4. 提供 Item 点击事件回调接口 `OnItemClickListener`；
5. 在 `ContactListActivity` 中初始化数据、设置 LayoutManager、绑定适配器。

<details>
<summary>查看答案</summary>

```java
// ============ Contact.java ============
public class Contact {
    private String name;
    private String phone;
    public Contact(String name, String phone) {
        this.name = name;
        this.phone = phone;
    }
    public String getName()  { return name; }
    public String getPhone() { return phone; }
}
```

```java
// ============ ContactAdapter.java ============
public class ContactAdapter extends RecyclerView.Adapter<ContactAdapter.ContactViewHolder> {

    private List<Contact> data;
    private OnItemClickListener listener;

    public interface OnItemClickListener {
        void onItemClick(int position);
    }

    public ContactAdapter(List<Contact> data, OnItemClickListener listener) {
        this.data = data;
        this.listener = listener;
    }

    @NonNull
    @Override
    public ContactViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_contact, parent, false);
        return new ContactViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ContactViewHolder holder, int position) {
        Contact c = data.get(position);
        holder.tvName.setText(c.getName());
        holder.tvPhone.setText(c.getPhone());
        holder.itemView.setOnClickListener(v -> {
            if (listener != null) {
                listener.onItemClick(holder.getAdapterPosition());
            }
        });
    }

    @Override
    public int getItemCount() {
        return data == null ? 0 : data.size();
    }

    static class ContactViewHolder extends RecyclerView.ViewHolder {
        TextView tvName;
        TextView tvPhone;

        ContactViewHolder(@NonNull View itemView) {
            super(itemView);
            tvName  = itemView.findViewById(R.id.tv_name);
            tvPhone = itemView.findViewById(R.id.tv_phone);
        }
    }
}
```

```xml
<!-- res/layout/item_contact.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="horizontal"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:padding="12dp">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:orientation="vertical">
        <TextView
            android:id="@+id/tv_name"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="16sp"
            android:textStyle="bold" />
        <TextView
            android:id="@+id/tv_phone"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="14sp"
            android:textColor="#666666" />
    </LinearLayout>
</LinearLayout>
```

```xml
<!-- res/layout/activity_contact_list.xml -->
<androidx.recyclerview.widget.RecyclerView
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/rv_contacts"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

```java
// ============ ContactListActivity.java ============
public class ContactListActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_contact_list);

        RecyclerView rv = findViewById(R.id.rv_contacts);
        rv.setLayoutManager(new LinearLayoutManager(this));
        rv.addItemDecoration(new DividerItemDecoration(this,
                DividerItemDecoration.VERTICAL));

        List<Contact> contacts = new ArrayList<>();
        contacts.add(new Contact("张三", "13800138000"));
        contacts.add(new Contact("李四", "13900139000"));
        contacts.add(new Contact("王五", "13700137000"));

        ContactAdapter adapter = new ContactAdapter(contacts, position -> {
            Toast.makeText(this, "点击：" + contacts.get(position).getName(),
                    Toast.LENGTH_SHORT).show();
        });
        rv.setAdapter(adapter);
    }
}
```

```groovy
// app/build.gradle 添加依赖
dependencies {
    implementation 'androidx.recyclerview:recyclerview:1.3.2'
}
```
</details>

---

### 15. ⭐⭐ 登录页布局 XML（ConstraintLayout）

请用 ConstraintLayout 实现登录页布局：
1. 顶部 Logo（ImageView）水平居中、距顶 64dp；
2. Logo 下方账号输入框（占满宽度，hint="请输入账号"）；
3. 账号下方密码输入框（占满宽度，inputType="textPassword"）；
4. 底部"登录"按钮贴右下角、"注册"按钮位于登录按钮左侧、底部对齐；
5. 整个布局只有一层，不允许嵌套其他 ViewGroup。

<details>
<summary>查看答案</summary>

```xml
<!-- res/layout/activity_login.xml -->
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="24dp">

    <!-- Logo：水平居中、距顶 64dp -->
    <ImageView
        android:id="@+id/iv_logo"
        android:layout_width="96dp"
        android:layout_height="96dp"
        android:src="@mipmap/ic_launcher"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        android:layout_marginTop="64dp" />

    <!-- 账号输入框：Logo 下方 -->
    <EditText
        android:id="@+id/et_account"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:hint="请输入账号"
        android:inputType="text"
        app:layout_constraintTop_toBottomOf="@id/iv_logo"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        android:layout_marginTop="32dp" />

    <!-- 密码输入框：账号下方 -->
    <EditText
        android:id="@+id/et_password"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:hint="请输入密码"
        android:inputType="textPassword"
        app:layout_constraintTop_toBottomOf="@id/et_account"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        android:layout_marginTop="16dp" />

    <!-- 登录按钮：贴右下角 -->
    <Button
        android:id="@+id/btn_login"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="登录"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        android:layout_marginBottom="24dp" />

    <!-- 注册按钮：位于登录按钮左侧、底部对齐 -->
    <Button
        android:id="@+id/btn_register"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="注册"
        app:layout_constraintBottom_toBottomOf="@id/btn_login"
        app:layout_constraintRight_toLeftOf="@id/btn_login"
        android:layout_marginRight="12dp" />
</androidx.constraintlayout.widget.ConstraintLayout>
```

**要点**：
- 输入框宽度用 `0dp` + 左右约束，等价于 `match_parent` 但符合约束布局规范。
- 注册按钮通过 `toLeftOf` 和 `Bottom_toBottomOf` 与登录按钮形成相对关系，自动底部对齐。
- 整个布局**仅一层** ConstraintLayout，无嵌套。
</details>

---

### 16. ⭐⭐ 事件处理代码：点击 + 长按 + 触摸

请编写代码实现以下需求：
1. 给一个 Button 同时绑定点击事件和长按事件；
2. 点击时弹出 Toast "已点击"；
3. 长按时弹出 Toast "已长按"，并保证长按后松手不再触发点击；
4. 给一个自定义 View 绑定触摸监听，打印按下、移动、抬起的相对坐标。

<details>
<summary>查看答案</summary>

```java
public class EventDemoActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_event_demo);

        Button btn = findViewById(R.id.btn_event);

        // 1. 点击事件
        btn.setOnClickListener(v ->
            Toast.makeText(this, "已点击", Toast.LENGTH_SHORT).show());

        // 2. 长按事件:返回 true 消费事件, 松手后不再触发 onClick
        btn.setOnLongClickListener(v -> {
            Toast.makeText(this, "已长按", Toast.LENGTH_SHORT).show();
            return true;   // 关键: 返回 true 才不会继续触发 onClick
        });

        // 3. 触摸事件:打印按下/移动/抬起的相对坐标
        View touchView = findViewById(R.id.view_touch);
        touchView.setOnTouchListener((v, event) -> {
            float x = event.getX();      // 相对 View 左上角
            float y = event.getY();
            switch (event.getActionMasked()) {
                case MotionEvent.ACTION_DOWN:
                    Log.d("Touch", "按下: (" + x + ", " + y + ")");
                    break;
                case MotionEvent.ACTION_MOVE:
                    Log.d("Touch", "移动: (" + x + ", " + y + ")");
                    break;
                case MotionEvent.ACTION_UP:
                    Log.d("Touch", "抬起: (" + x + ", " + y + ")");
                    break;
                case MotionEvent.ACTION_CANCEL:
                    Log.d("Touch", "取消");
                    break;
            }
            return true;   // 消费触摸事件
        });
    }
}
```

**要点**：
- `onLongClick` 返回 `true` 才能阻止松手后触发 `onClick`；返回 `false` 两者都会触发。
- `getX/getY` 是相对 View 左上角的坐标；`getRawX/getRawY` 是相对屏幕左上角。
- `onTouch` 返回 `true` 消费事件后，`onClick` 不会再触发——本例中 Button 的点击仍生效是因为 `onTouch` 是给另一个 View 设置的。
</details>

---

### 17. ⭐⭐ 多语言适配实践

请实现一个中英文双语的设置页：
1. 在 `res/values/strings.xml` 和 `res/values-en/strings.xml` 中分别定义中英文版本字符串；
2. 字符串包括：应用标题、设置项"消息通知"、"关于我们"、"退出登录"；
3. 布局中所有文字必须通过 `@string/` 引用，不允许硬编码字面量；
4. 在 Activity 中点击"退出登录"时，弹出中英文自适应的 Toast 提示。

<details>
<summary>查看答案</summary>

```xml
<!-- res/values/strings.xml（默认中文兜底） -->
<resources>
    <string name="app_name">移动应用</string>
    <string name="settings_title">设置</string>
    <string name="setting_notify">消息通知</string>
    <string name="setting_about">关于我们</string>
    <string name="setting_logout">退出登录</string>
    <string name="toast_logout_confirm">已退出登录</string>
</resources>
```

```xml
<!-- res/values-en/strings.xml（英文） -->
<resources>
    <string name="app_name">Mobile App</string>
    <string name="settings_title">Settings</string>
    <string name="setting_notify">Notifications</string>
    <string name="setting_about">About Us</string>
    <string name="setting_logout">Log Out</string>
    <string name="toast_logout_confirm">You have logged out</string>
</resources>
```

```xml
<!-- res/layout/activity_settings.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/settings_title"
        android:textSize="22sp"
        android:textStyle="bold"
        android:layout_marginBottom="16dp" />

    <TextView
        android:id="@+id/tv_notify"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:padding="12dp"
        android:text="@string/setting_notify"
        android:textSize="16sp" />

    <TextView
        android:id="@+id/tv_about"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:padding="12dp"
        android:text="@string/setting_about"
        android:textSize="16sp" />

    <Button
        android:id="@+id/btn_logout"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="24dp"
        android:text="@string/setting_logout" />
</LinearLayout>
```

```java
// ============ SettingsActivity.java ============
public class SettingsActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);

        findViewById(R.id.btn_logout).setOnClickListener(v -> {
            // getString 自动按当前系统语言加载对应字符串
            Toast.makeText(this,
                getString(R.string.toast_logout_confirm),
                Toast.LENGTH_SHORT).show();
        });
    }
}
```

**要点**：
- 所有文字一律 `@string/xxx` 或 `getString()`，绝不在代码或布局中硬编码。
- 默认 `values/strings.xml` 必须覆盖所有 key，作为兜底。
- 切换系统语言后回到应用，Activity 重建会自动重载对应语言资源。
</details>

---

### 18. ⭐⭐⭐ 综合题：通讯录列表 + 点击 + 长按删除

请综合运用 RecyclerView、事件处理实现通讯录功能：
1. 用 RecyclerView 展示联系人列表（姓名 + 电话）；
2. 点击 Item 弹出 Toast 显示联系人详情；
3. 长按 Item 弹出确认对话框，确认后删除该联系人，并触发删除动画；
4. 删除后剩余 Item 的点击 position 必须正确，不能错位；
5. 添加分隔线。

<details>
<summary>查看答案</summary>

```java
// ============ Contact.java ============
public class Contact {
    private String name;
    private String phone;
    public Contact(String name, String phone) {
        this.name = name;
        this.phone = phone;
    }
    public String getName()  { return name; }
    public String getPhone() { return phone; }
}
```

```java
// ============ ContactAdapter.java（支持点击 + 长按） ============
public class ContactAdapter extends RecyclerView.Adapter<ContactAdapter.ContactViewHolder> {

    private List<Contact> data;
    private OnItemClickListener clickListener;
    private OnItemLongClickListener longListener;

    public interface OnItemClickListener {
        void onItemClick(int position);
    }
    public interface OnItemLongClickListener {
        void onItemLongClick(int position);
    }

    public ContactAdapter(List<Contact> data,
                          OnItemClickListener clickListener,
                          OnItemLongClickListener longListener) {
        this.data = data;
        this.clickListener = clickListener;
        this.longListener = longListener;
    }

    @NonNull
    @Override
    public ContactViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_contact, parent, false);
        return new ContactViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ContactViewHolder holder, int position) {
        Contact c = data.get(position);
        holder.tvName.setText(c.getName());
        holder.tvPhone.setText(c.getPhone());

        // 关键:用 getAdapterPosition() 而非 position,保证删除后下标准确
        holder.itemView.setOnClickListener(v -> {
            if (clickListener != null) {
                clickListener.onItemClick(holder.getAdapterPosition());
            }
        });
        holder.itemView.setOnLongClickListener(v -> {
            if (longListener != null) {
                longListener.onItemLongClick(holder.getAdapterPosition());
            }
            return true;   // 消费长按事件
        });
    }

    @Override
    public int getItemCount() {
        return data == null ? 0 : data.size();
    }

    static class ContactViewHolder extends RecyclerView.ViewHolder {
        TextView tvName;
        TextView tvPhone;
        ContactViewHolder(@NonNull View itemView) {
            super(itemView);
            tvName  = itemView.findViewById(R.id.tv_name);
            tvPhone = itemView.findViewById(R.id.tv_phone);
        }
    }
}
```

```xml
<!-- res/layout/item_contact.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="horizontal"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:padding="12dp">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:orientation="vertical">
        <TextView
            android:id="@+id/tv_name"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="16sp"
            android:textStyle="bold" />
        <TextView
            android:id="@+id/tv_phone"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="14sp"
            android:textColor="#666666" />
    </LinearLayout>
</LinearLayout>
```

```java
// ============ ContactListActivity.java ============
public class ContactListActivity extends AppCompatActivity {

    private List<Contact> contacts = new ArrayList<>();
    private ContactAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_contact_list);

        initData();

        RecyclerView rv = findViewById(R.id.rv_contacts);
        rv.setLayoutManager(new LinearLayoutManager(this));
        // 分隔线
        rv.addItemDecoration(new DividerItemDecoration(this,
                DividerItemDecoration.VERTICAL));

        adapter = new ContactAdapter(contacts,
            // 点击:显示详情
            position -> {
                Contact c = contacts.get(position);
                Toast.makeText(this,
                    c.getName() + " / " + c.getPhone(),
                    Toast.LENGTH_SHORT).show();
            },
            // 长按:弹删除对话框
            position -> showDeleteDialog(position));
        rv.setAdapter(adapter);
    }

    private void showDeleteDialog(int position) {
        new AlertDialog.Builder(this)
            .setTitle("删除联系人")
            .setMessage("确认删除 " + contacts.get(position).getName() + "？")
            .setPositiveButton("删除", (d, w) -> {
                contacts.remove(position);
                adapter.notifyItemRemoved(position);
                // 关键:通知后续位置变化,避免点击错位
                adapter.notifyItemRangeChanged(position, contacts.size() - position);
            })
            .setNegativeButton("取消", null)
            .show();
    }

    private void initData() {
        contacts.add(new Contact("张三", "13800138000"));
        contacts.add(new Contact("李四", "13900139000"));
        contacts.add(new Contact("王五", "13700137000"));
        contacts.add(new Contact("赵六", "13600136000"));
        contacts.add(new Contact("钱七", "13500135000"));
    }
}
```

```xml
<!-- res/layout/activity_contact_list.xml -->
<androidx.recyclerview.widget.RecyclerView
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/rv_contacts"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

**关键点**：
1. **`holder.getAdapterPosition()` 代替 `position`**：在有增删时 `position` 是绑定时的旧值，可能与实际下标不一致；`getAdapterPosition()` 返回最新下标，避免点击错位。
2. **删除后两个通知**：`notifyItemRemoved(position)` 触发滑出动画；`notifyItemRangeChanged(position, count)` 通知后续位置数据下标变化。
3. **长按返回 true**：`setOnLongClickListener` 返回 `true` 才能消费长按事件，避免与点击冲突。
4. **分隔线**：用 `DividerItemDecoration` 系统内置实现，无需自定义。
</details>

---

## 考点统计与复习建议

### 考点分布统计表

| 题号 | 题型 | 涉及考点 | 难度 | 对应小节 |
| ---- | ---- | -------- | ---- | -------- |
| 1 | 选择 | LinearLayout weight 用法 | ⭐ | [[4.1 Layout 布局：线性、相对、约束布局\|4.1]] |
| 2 | 选择 | RecyclerView 特性 | ⭐⭐ | [[4.3 列表控件 ListView、RecyclerView\|4.3]] |
| 3 | 选择 | dp/sp/px 单位 | ⭐ | [[4.4 资源文件：图片、字符串、尺寸资源\|4.4]] |
| 4 | 选择 | ListView vs RecyclerView | ⭐⭐ | [[4.3 列表控件 ListView、RecyclerView\|4.3]] |
| 5 | 选择 | 事件分发机制三方法 | ⭐⭐⭐ | [[4.5 事件处理：点击事件、触摸事件\|4.5]] |
| 6 | 选择 | 资源目录限定符 | ⭐ | [[4.4 资源文件：图片、字符串、尺寸资源\|4.4]] |
| 7 | 填空 | Adapter 三方法 | ⭐ | [[4.3 列表控件 ListView、RecyclerView\|4.3]] |
| 8 | 填空 | 四种布局名称 | ⭐ | [[4.1 Layout 布局：线性、相对、约束布局\|4.1]] |
| 9 | 填空 | 事件分发三方法 | ⭐⭐ | [[4.5 事件处理：点击事件、触摸事件\|4.5]] |
| 10 | 简答 | 四种布局对比 | ⭐⭐ | [[4.1 Layout 布局：线性、相对、约束布局\|4.1]] |
| 11 | 简答 | RecyclerView 四大组件 | ⭐⭐ | [[4.3 列表控件 ListView、RecyclerView\|4.3]] |
| 12 | 简答 | dp/sp/px 区别 | ⭐⭐ | [[4.4 资源文件：图片、字符串、尺寸资源\|4.4]] |
| 13 | 简答 | 事件分发流程 | ⭐⭐⭐ | [[4.5 事件处理：点击事件、触摸事件\|4.5]] |
| 14 | 代码 | RecyclerView Adapter 实现 | ⭐⭐⭐ | [[4.3 列表控件 ListView、RecyclerView\|4.3]] |
| 15 | 代码 | ConstraintLayout 布局 XML | ⭐⭐ | [[4.1 Layout 布局：线性、相对、约束布局\|4.1]] |
| 16 | 代码 | 点击+长按+触摸事件 | ⭐⭐ | [[4.5 事件处理：点击事件、触摸事件\|4.5]] |
| 17 | 代码 | 多语言适配 | ⭐⭐ | [[4.4 资源文件：图片、字符串、尺寸资源\|4.4]] |
| 18 | 代码 | 通讯录综合（含删除动画） | ⭐⭐⭐ | [[4.3 列表控件 ListView、RecyclerView\|4.3]] + [[4.5 事件处理：点击事件、触摸事件\|4.5]] |

### 复习建议

> [!tip] 高效复习路线
> 1. **第一优先（必考）**：RecyclerView Adapter 三个方法的完整实现，必须能在白板上默写（见第 2、7、14、18 题）。重点掌握 ViewHolder 模式、点击事件回调接口设计、`getAdapterPosition()` 防错位。
> 2. **第二优先**：四种布局的特点与选型，LinearLayout 权重计算、ConstraintLayout 约束/Bias/Chain/Guideline（见第 1、8、10、15 题）。
> 3. **第三优先**：事件分发机制三方法的调用顺序与返回值含义，能画流程图说明（见第 5、9、13 题）。
> 4. **第四优先**：dp/sp/px 单位辨析、资源目录限定符、多语言适配实践（见第 3、6、12、17 题）。
> 5. **动手实践**：18 题中代码设计题共 5 道，建议在 Android Studio 中至少完整实现第 14、15、18 题，掌握 RecyclerView + 事件处理的完整业务闭环。
> 6. **难点突破**：第 18 题的"删除后 position 错位"是高频踩坑点，必须理解为何用 `getAdapterPosition()` 而非 `position`，以及 `notifyItemRemoved` 后为何要调 `notifyItemRangeChanged`。

## 章节导航

- 上级：[[MOC - 第4章|第4章 Android UI 界面开发]]
- 上一章习题：[[MOC - 第3章习题|第3章习题]]
- 下一章习题：[[MOC - 第5章习题|第5章习题]]
- 课程总览：[[MOC - 移动互联网开发技术|移动互联网开发技术]]
