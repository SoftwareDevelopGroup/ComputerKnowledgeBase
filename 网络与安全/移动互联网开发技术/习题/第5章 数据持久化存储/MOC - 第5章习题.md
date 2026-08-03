---
domain: 网络与安全
subject: 移动互联网开发技术
type: exercise
chapter: 第5章 数据持久化存储
tags: [移动开发,习题,SharedPreferences,SQLite,存储权限]
prerequisites: ["计算机网络A","Java程序设计"]
aliases: [第5章习题, 数据存储习题, 第5章练习]
---

# MOC - 第5章习题

> [!info] 本章习题说明
> - 配套知识点：[[MOC - 第5章|第5章 数据持久化存储]]
> - 题目数量：**15 题**（选择 5 + 填空 3 + 简答 4 + 代码设计 3）
> - 难度梯度：⭐基础 / ⭐⭐中等 / ⭐⭐⭐较难
> - 答案折叠在每题下方的 `<details>` 块中，建议先独立作答再展开对照
> - 代码题要求完整可运行代码，覆盖 SQLite CRUD、SharedPreferences、运行时权限申请三大核心

## 一、选择题（5 题）

### 1. ⭐ 关于 SharedPreferences 的描述，下列错误的是？

A. SharedPreferences 底层以 XML 文件保存数据
B. SharedPreferences 适合保存登录状态、配置项等少量数据
C. SharedPreferences 写入数据时必须调用 `edit()` 获取 Editor 对象
D. SharedPreferences 支持跨进程并发写入且保证线程安全

<details>
<summary>查看答案</summary>

**答案：D**

SharedPreferences **不是**进程安全的，多进程并发写会丢数据。跨进程共享数据应使用 `ContentProvider` 或 Jetpack `DataStore`。其他三项均正确：XML 存储、适合少量配置、写入需经 Editor。
</details>

---

### 2. ⭐ 关于 SharedPreferences 的 `apply()` 与 `commit()`，下列说法正确的是？

A. `apply()` 同步写入磁盘并返回 `boolean` 表示是否成功
B. `commit()` 异步写入磁盘，不阻塞当前线程
C. `apply()` 先把修改写入内存再异步刷盘，无返回值
D. 关键数据建议用 `apply()` 以保证立即落盘

<details>
<summary>查看答案</summary>

**答案：C**

- A 错：`apply()` 是异步，无返回值；返回 boolean 的是 `commit()`。
- B 错：`commit()` 是同步阻塞调用。
- C 对：`apply()` 先写内存后异步刷盘，主线程调用安全。
- D 错：关键数据需立即落盘应用 `commit()`，`apply()` 在刷盘前进程被杀可能丢失。
</details>

---

### 3. ⭐⭐ 关于 Android 内部存储与外部存储的对比，下列说法错误的是？

A. 内部存储保存在 `/data/data/<包名>/` 下，无需任何权限
B. 外部存储的应用专属目录（`getExternalFilesDir`）无需权限即可读写
C. 应用卸载后，内部存储与外部存储公共目录下的文件都会被删除
D. Android 10 引入的 Scoped Storage 限制了应用对外部公共目录的直接访问

<details>
<summary>查看答案</summary>

**答案：C**

外部存储**公共目录**（如 `Pictures/`、`Downloads/`）下的文件在应用卸载后**不会**被删除；只有应用专属目录（`Android/data/<包名>/`）才会随卸载清理。其他三项均正确。
</details>

---

### 4. ⭐⭐ 关于 SQLiteOpenHelper 的回调方法，下列说法正确的是？

A. `onCreate` 在每次应用启动时都会被调用
B. `onUpgrade` 在数据库版本号升高时被调用，用于表结构迁移
C. `getReadableDatabase` 永远返回只读数据库对象，不能写入
D. `onUpgrade` 默认实现会自动备份旧数据并迁移到新表

<details>
<summary>查看答案</summary>

**答案：B**

- A 错：`onCreate` 仅在**首次创建**数据库时调用一次。
- B 对：版本号升高时调用 `onUpgrade`，开发者在此执行 `ALTER TABLE` 或建新表。
- C 错：`getReadableDatabase` 在磁盘正常时返回的也是**可写**对象，仅在磁盘满等情况下才退化只读。
- D 错：`onUpgrade` 默认实现为空（基类方法体为空），开发者必须自己实现迁移逻辑。
</details>

---

### 5. ⭐⭐ 关于 Android 运行时权限申请，下列说法错误的是？

A. 危险权限必须在运行时动态申请，安装时不会自动授权
B. `checkSelfPermission` 返回 `PERMISSION_GRANTED` 表示已授权
C. 用户勾选"不再询问"并拒绝后，再次调用 `requestPermissions` 仍会弹窗
D. `MANAGE_EXTERNAL_STORAGE` 不能通过 `requestPermissions` 申请，需引导用户去系统设置

<details>
<summary>查看答案</summary>

**答案：C**

用户勾选"不再询问"后，再次调用 `requestPermissions` **不会弹窗**，系统直接回调 `onRequestPermissionsResult` 返回 DENIED。此时应通过 `shouldShowRequestPermissionRationale` 返回 false 判断该状态，并引导用户去系统设置手动开启。其他三项均正确。
</details>

---

## 二、填空题（3 题）

### 6. ⭐ SharedPreferences 写入数据的标准三步流程是：先调用 ________ 获取 Editor 对象，再调用 ________ 写入键值对，最后调用 ________ 或 ________ 提交修改。

<details>
<summary>查看答案</summary>

**答案：`edit()`、`putXxx(key, value)`、`apply()`、`commit()`**

完整示例：`sp.edit().putString("k", "v").apply();`。`apply()` 异步无返回值，`commit()` 同步返回 `boolean`。
</details>

---

### 7. ⭐⭐ Android 自 6.0（API 23）起把权限分为 ________ 和 ________ 两类，前者安装即生效，后者必须运行时通过 ________ 方法申请，并在 ________ 回调中处理授权结果。

<details>
<summary>查看答案</summary>

**答案：普通权限（Normal Permissions）、危险权限（Dangerous Permissions）、`requestPermissions()`、`onRequestPermissionsResult()`**

危险权限按权限组归类（如 STORAGE、LOCATION、CAMERA），每组内的权限共享授权行为。
</details>

---

### 8. ⭐⭐ SQLite 数据库操作中，查询返回的结果集通过 ________ 对象遍历，初始指针位于第一行 ________，必须先调用 ________ 方法才能读取数据；遍历结束后应调用 ________ 释放资源。

<details>
<summary>查看答案</summary>

**答案：`Cursor`、之前（before first）、`moveToNext()`、`close()`**

典型模式：
```java
try (Cursor c = db.query(...)) {
    while (c.moveToNext()) {
        long id = c.getLong(c.getColumnIndexOrThrow("_id"));
    }
}
```
不关闭 Cursor 会导致内存泄漏与数据库锁。
</details>

---

## 三、简答题（4 题）

### 9. ⭐⭐ 对比 SharedPreferences、内部存储文件、外部存储文件、SQLite 四种持久化方案，说明各自的适用场景与局限性。

<details>
<summary>查看答案</summary>

| 方案 | 数据模型 | 适用场景 | 局限性 |
| ---- | -------- | -------- | ------ |
| SharedPreferences | 键值对 | 登录状态、配置项、简单标记 | 仅支持 6 种基本类型；不适合大数据；非进程安全 |
| 内部存储文件 | 字节流 | 应用私有日志、缓存、小文件 | 容量受内部存储限制；用户不可见；卸载删除 |
| 外部存储文件 | 字节流 | 用户可见文档、媒体大文件；应用产出大文件 | 公共目录需权限；Android 10+ 受 Scoped Storage 限制 |
| SQLite | 关系表 | 结构化业务数据、需条件查询与事务 | API 较底层；需手动管理 Cursor 与版本迁移 |

**选型决策**：
- 配置类小数据 → SharedPreferences
- 应用私有非结构化数据 → 内部存储
- 用户可见或大文件 → 外部存储（注意 Scoped Storage）
- 需要查询/事务的结构化数据 → SQLite（或 Room）
</details>

---

### 10. ⭐⭐ 简述 SQLiteOpenHelper 中 `onCreate` 与 `onUpgrade` 的触发时机与典型用途，并说明数据库版本升级时应注意的事项。

<details>
<summary>查看答案</summary>

**触发时机**：

| 回调 | 触发时机 | 典型用途 |
| ---- | -------- | -------- |
| `onCreate(db)` | 首次调用 `getWritableDatabase/getReadableDatabase` 且数据库文件不存在时调用一次 | 执行 `CREATE TABLE` 建表、初始化默认数据 |
| `onUpgrade(db, old, new)` | 数据库已存在且 `DB_VERSION` 升高时调用一次 | 执行 `ALTER TABLE` 增加字段、新建表、数据迁移 |

**版本升级注意事项**：

1. **生产环境不可一刀切删表重建**：会丢失用户数据，必须用 `ALTER TABLE` 增量迁移。
2. **按版本号分步迁移**：使用 `if (oldVersion < N)` 顺序执行每个版本的迁移脚本，确保从任意旧版本都能升级到最新。
3. **降级也需考虑**：默认 `onDowngrade` 抛异常，若可能降级需重写。
4. **数据迁移要包事务**：迁移失败应回滚，避免数据库处于不一致状态。
5. **测试覆盖**：每个版本升级路径都应在测试环境验证。

示例：

```java
@Override
public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
    if (oldVersion < 2) {
        db.execSQL("ALTER TABLE user ADD COLUMN phone TEXT");
    }
    if (oldVersion < 3) {
        db.execSQL("CREATE TABLE IF NOT EXISTS order (...)");
    }
}
```
</details>

---

### 11. ⭐⭐ 解释 SQL 注入的原理，并说明在 Android SQLite 中如何防止 SQL 注入。

<details>
<summary>查看答案</summary>

**SQL 注入原理**：

当应用把用户输入直接拼接到 SQL 字符串中时，攻击者可构造特殊输入改变 SQL 语义。例如登录查询：

```java
// 危险写法
String sql = "SELECT * FROM user WHERE name = '" + userInput + "'";
```

若用户输入 `' OR '1'='1`，最终 SQL 变为：

```sql
SELECT * FROM user WHERE name = '' OR '1'='1'
```

该条件恒为真，攻击者无需账号即可获取全部用户数据。更严重的注入可执行 `DROP TABLE` 等破坏性命令。

**防护方法**：

1. **参数化查询**：使用 `?` 占位符 + `selectionArgs` 数组，`SQLiteDatabase` 会自动转义参数值。
   ```java
   // 安全写法
   Cursor c = db.rawQuery(
       "SELECT * FROM user WHERE name = ?",
       new String[]{ userInput });
   ```

2. **使用 `query/update/delete` 便捷方法**：这些方法内部已使用参数化机制。
   ```java
   Cursor c = db.query("user", null,
       "name = ?", new String[]{ userInput },
       null, null, null);
   ```

3. **禁止字符串拼接 SQL**：任何接受用户输入的查询都必须使用占位符，不得用 `+` 拼接。

4. **校验输入**：对用户输入做格式校验（如用户名仅允许字母数字），作为额外防线。
</details>

---

### 12. ⭐⭐⭐ 简述 Android 10 引入的 Scoped Storage（分区存储）的核心规则，并说明应用应如何适配。

<details>
<summary>查看答案</summary>

**Scoped Storage 核心规则**：

1. **应用专属目录自由访问**：`getExternalFilesDir(type)` 返回的 `Android/data/<包名>/files/` 目录无需任何权限即可读写，卸载自动清理。

2. **公共目录通过 MediaStore 访问**：`Pictures/`、`Music/`、`Movies/`、`Downloads/` 等公共目录必须通过 `MediaStore` API 或 SAF（Storage Access Framework）访问，不能直接用 `File` 路径。

3. **访问其他应用媒体需权限**：访问其他应用写入的媒体文件需要 `READ_EXTERNAL_STORAGE`（Android 13+ 改为 `READ_MEDIA_IMAGES/VIDEO/AUDIO`）。访问自己写入的媒体文件无需权限。

4. **`getExternalStorageDirectory()` 废弃**：Android 10+ 即使申请权限也无法通过旧 API 写入公共目录。

5. **`requestLegacyExternalStorage` 临时兼容**：targetSdk ≤ 29 的应用可在 Manifest 中声明 `android:requestLegacyExternalStorage="true"` 暂时使用旧 API，但 Android 11+ targetSdk 30 起失效。

**适配策略**：

| 场景 | 推荐方案 |
| ---- | -------- |
| 应用私有文件 | `getExternalFilesDir`（免权限） |
| 用户可见媒体 | `MediaStore` API |
| 用户选择文档 | SAF（`ACTION_OPEN_DOCUMENT`） |
| 整个外部存储 | `MANAGE_EXTERNAL_STORAGE`（需审核） |

**适配步骤**：

1. 把所有写入公共目录的代码改为 MediaStore 或应用专属目录。
2. targetSdk 升级到 30+ 时移除 `requestLegacyExternalStorage`。
3. 移除 `WRITE_EXTERNAL_STORAGE`（Android 10+ 已无效），保留 `READ_EXTERNAL_STORAGE` 或细分媒体权限。
4. 测试覆盖 Android 10/11/12/13 各版本。
</details>

---

## 四、代码设计题（3 题）

### 13. ⭐⭐⭐ SQLite 用户表 CRUD 完整实现

请编写代码实现以下需求：
1. 创建 `UserDBHelper`，数据库名 `user.db`，版本 1，建表 `user`（字段：`_id` 主键自增、`username` 文本非空唯一、`age` 整数、`email` 文本）；
2. 实现 `UserDao` 类，提供 `insert / delete / update / queryById / queryAll` 五个方法；
3. `queryAll` 按 `_id` 降序返回所有用户；
4. 所有 SQL 操作必须使用参数化查询；
5. 提供 `User` 实体类。

<details>
<summary>查看答案</summary>

```java
// ============ User.java ============
public class User {
    public long id;
    public String username;
    public int age;
    public String email;

    @Override
    public String toString() {
        return String.format("User{id=%d, name=%s, age=%d, email=%s}",
            id, username, age, email);
    }
}

// ============ UserDBHelper.java ============
public class UserDBHelper extends SQLiteOpenHelper {

    private static final String DB_NAME    = "user.db";
    private static final int    DB_VERSION = 1;

    public static final String TABLE_USER   = "user";
    public static final String COL_ID       = "_id";
    public static final String COL_USERNAME = "username";
    public static final String COL_AGE      = "age";
    public static final String COL_EMAIL    = "email";

    private static final String SQL_CREATE =
        "CREATE TABLE " + TABLE_USER + " (" +
            COL_ID       + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
            COL_USERNAME + " TEXT NOT NULL UNIQUE, " +
            COL_AGE      + " INTEGER DEFAULT 0, " +
            COL_EMAIL    + " TEXT" +
        ")";

    public UserDBHelper(Context ctx) {
        super(ctx, DB_NAME, null, DB_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(SQL_CREATE);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // 演示用:生产环境应分步 ALTER 迁移
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_USER);
        onCreate(db);
    }
}

// ============ UserDao.java ============
public class UserDao {

    private final UserDBHelper helper;

    public UserDao(Context ctx) {
        // 使用 ApplicationContext 防止 Activity 泄漏
        helper = new UserDBHelper(ctx.getApplicationContext());
    }

    /** 新增用户,返回新行 _id;-1 表示失败 */
    public long insert(User u) {
        SQLiteDatabase db = helper.getWritableDatabase();
        try {
            ContentValues cv = new ContentValues();
            cv.put(UserDBHelper.COL_USERNAME, u.username);
            cv.put(UserDBHelper.COL_AGE, u.age);
            cv.put(UserDBHelper.COL_EMAIL, u.email);
            return db.insert(UserDBHelper.TABLE_USER, null, cv);
        } finally {
            db.close();
        }
    }

    /** 按 _id 删除用户,返回受影响行数 */
    public int delete(long id) {
        SQLiteDatabase db = helper.getWritableDatabase();
        try {
            return db.delete(UserDBHelper.TABLE_USER,
                UserDBHelper.COL_ID + " = ?",
                new String[]{ String.valueOf(id) });
        } finally {
            db.close();
        }
    }

    /** 更新用户信息,返回受影响行数 */
    public int update(User u) {
        SQLiteDatabase db = helper.getWritableDatabase();
        try {
            ContentValues cv = new ContentValues();
            cv.put(UserDBHelper.COL_USERNAME, u.username);
            cv.put(UserDBHelper.COL_AGE, u.age);
            cv.put(UserDBHelper.COL_EMAIL, u.email);
            return db.update(UserDBHelper.TABLE_USER, cv,
                UserDBHelper.COL_ID + " = ?",
                new String[]{ String.valueOf(u.id) });
        } finally {
            db.close();
        }
    }

    /** 按 _id 查询单个用户,不存在返回 null */
    public User queryById(long id) {
        SQLiteDatabase db = helper.getReadableDatabase();
        try (Cursor c = db.query(UserDBHelper.TABLE_USER, null,
                UserDBHelper.COL_ID + " = ?",
                new String[]{ String.valueOf(id) },
                null, null, null)) {
            if (c.moveToFirst()) {
                return cursorToUser(c);
            }
            return null;
        } finally {
            db.close();
        }
    }

    /** 查询全部用户,按 _id 降序 */
    public List<User> queryAll() {
        SQLiteDatabase db = helper.getReadableDatabase();
        List<User> list = new ArrayList<>();
        try (Cursor c = db.query(UserDBHelper.TABLE_USER, null,
                null, null, null, null,
                UserDBHelper.COL_ID + " DESC")) {
            while (c.moveToNext()) {
                list.add(cursorToUser(c));
            }
        } finally {
            db.close();
        }
        return list;
    }

    /** 把 Cursor 当前行解析为 User 对象 */
    private User cursorToUser(Cursor c) {
        User u = new User();
        u.id       = c.getLong  (c.getColumnIndexOrThrow(UserDBHelper.COL_ID));
        u.username = c.getString(c.getColumnIndexOrThrow(UserDBHelper.COL_USERNAME));
        u.age      = c.getInt   (c.getColumnIndexOrThrow(UserDBHelper.COL_AGE));
        u.email    = c.getString(c.getColumnIndexOrThrow(UserDBHelper.COL_EMAIL));
        return u;
    }
}
```

**调用示例**：

```java
UserDao dao = new UserDao(this);

// 增
User u = new User();
u.username = "alice"; u.age = 20; u.email = "alice@example.com";
long newId = dao.insert(u);

// 查
User found = dao.queryById(newId);
List<User> all = dao.queryAll();

// 改
found.age = 21;
dao.update(found);

// 删
dao.delete(newId);
```

**评分要点**：
- 主键命名为 `_id` ✓
- 使用 `ContentValues` 与参数化查询 ✓
- `Cursor` 使用 `try-with-resources` 或 `try-finally` 关闭 ✓
- `queryAll` 按 `_id DESC` 排序 ✓
- 数据库连接在 `finally` 中关闭 ✓
</details>

---

### 14. ⭐⭐ SharedPreferences 登录状态管理

请编写代码实现以下需求：
1. 创建 `LoginManager` 类，封装 SharedPreferences 操作；
2. 文件名 `user_prefs`，提供 `saveLogin(username, token)`、`isLoggedIn()`、`getUsername()`、`getToken()`、`logout()` 五个方法；
3. `saveLogin` 同时保存用户名、登录 token、登录时间戳（`is_login=true`）；
4. `logout` 清空登录相关字段但保留其他配置；
5. 在 `SplashActivity` 中根据登录状态决定跳转 `MainActivity` 或 `LoginActivity`。

<details>
<summary>查看答案</summary>

```java
// ============ LoginManager.java ============
public class LoginManager {

    private static final String SP_NAME = "user_prefs";

    private static final String KEY_IS_LOGIN   = "is_login";
    private static final String KEY_USERNAME   = "username";
    private static final String KEY_TOKEN      = "token";
    private static final String KEY_LOGIN_TIME = "login_time";

    private final SharedPreferences sp;

    public LoginManager(Context ctx) {
        // 使用 ApplicationContext 防止 Activity 泄漏
        sp = ctx.getApplicationContext()
                .getSharedPreferences(SP_NAME, Context.MODE_PRIVATE);
    }

    /** 保存登录状态:用户名 + token + 时间戳 */
    public void saveLogin(String username, String token) {
        sp.edit()
          .putBoolean(KEY_IS_LOGIN, true)
          .putString(KEY_USERNAME, username)
          .putString(KEY_TOKEN, token)
          .putLong(KEY_LOGIN_TIME, System.currentTimeMillis())
          .apply();
    }

    /** 是否已登录 */
    public boolean isLoggedIn() {
        return sp.getBoolean(KEY_IS_LOGIN, false);
    }

    /** 获取当前登录用户名 */
    public String getUsername() {
        return sp.getString(KEY_USERNAME, "");
    }

    /** 获取登录 token */
    public String getToken() {
        return sp.getString(KEY_TOKEN, "");
    }

    /** 退出登录:仅清登录相关字段,保留其他配置 */
    public void logout() {
        sp.edit()
          .putBoolean(KEY_IS_LOGIN, false)
          .remove(KEY_USERNAME)
          .remove(KEY_TOKEN)
          .remove(KEY_LOGIN_TIME)
          .apply();
    }

    /** 获取登录时间戳(毫秒),未登录返回 0 */
    public long getLoginTime() {
        return sp.getLong(KEY_LOGIN_TIME, 0L);
    }
}

// ============ SplashActivity.java ============
public class SplashActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);

        // 延迟 1 秒后判断跳转,模拟启动闪屏
        new Handler(Looper.getMainLooper()).postDelayed(this::route, 1000);
    }

    private void route() {
        LoginManager lm = new LoginManager(this);
        Intent target;
        if (lm.isLoggedIn()) {
            // 已登录:直接进主页
            target = new Intent(this, MainActivity.class);
        } else {
            // 未登录:进登录页
            target = new Intent(this, LoginActivity.class);
        }
        startActivity(target);
        finish();
    }
}

// ============ LoginActivity.java(登录成功后调用) ============
public class LoginActivity extends AppCompatActivity {

    private EditText etUser, etPass;
    private LoginManager loginManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        loginManager = new LoginManager(this);
        etUser = findViewById(R.id.et_username);
        etPass = findViewById(R.id.et_password);

        findViewById(R.id.btn_login).setOnClickListener(v -> doLogin());
    }

    private void doLogin() {
        String user = etUser.getText().toString().trim();
        String pass = etPass.getText().toString().trim();
        if (user.isEmpty() || pass.isEmpty()) {
            Toast.makeText(this, "请输入账号密码", Toast.LENGTH_SHORT).show();
            return;
        }
        // 实际项目应调用服务端接口校验,此处模拟
        if ("admin".equals(user) && "123456".equals(pass)) {
            String token = "fake_token_" + System.currentTimeMillis();
            loginManager.saveLogin(user, token);     // 保存登录状态
            startActivity(new Intent(this, MainActivity.class));
            finish();
        } else {
            Toast.makeText(this, "账号或密码错误", Toast.LENGTH_SHORT).show();
        }
    }
}

// ============ MainActivity.java(退出登录按钮) ============
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        LoginManager lm = new LoginManager(this);
        TextView tvWelcome = findViewById(R.id.tv_welcome);
        tvWelcome.setText("欢迎, " + lm.getUsername());

        findViewById(R.id.btn_logout).setOnClickListener(v -> {
            lm.logout();   // 清空登录状态
            startActivity(new Intent(this, LoginActivity.class));
            finish();
        });
    }
}
```

**评分要点**：
- 键名常量化 ✓
- 使用 `apply()` 而非 `commit()`（异步不阻塞） ✓
- `logout` 用 `remove` 而非 `clear`（避免误删其他配置） ✓
- 使用 `ApplicationContext` 避免 Activity 泄漏 ✓
- `SplashActivity` 根据状态决定跳转目标 ✓
</details>

---

### 15. ⭐⭐⭐ 运行时申请存储权限完整实现

请编写代码实现以下需求：
1. 创建 `FileExportActivity`，包含一个"导出文件"按钮；
2. 点击按钮时检查 `WRITE_EXTERNAL_STORAGE` 权限：已授权则直接执行导出；未授权则申请；
3. 申请前若 `shouldShowRequestPermissionRationale` 返回 true，先弹出解释对话框；
4. 在 `onRequestPermissionsResult` 中处理结果：授权则导出，拒绝则判断是否"不再询问"，是则引导去系统设置；
5. Android 10+ 优先用应用专属目录（`getExternalFilesDir`）免权限导出；
6. 提供对应的 `AndroidManifest.xml` 权限声明。

<details>
<summary>查看答案</summary>

```java
// ============ FileExportActivity.java ============
public class FileExportActivity extends AppCompatActivity {

    private static final int REQ_STORAGE = 3001;
    // Android 13+ 用 READ_MEDIA_*;此处演示传统存储权限
    private static final String[] STORAGE_PERMS = {
        Manifest.permission.WRITE_EXTERNAL_STORAGE,
        Manifest.permission.READ_EXTERNAL_STORAGE
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_export);

        findViewById(R.id.btn_export).setOnClickListener(v -> handleExportClick());
    }

    private void handleExportClick() {
        // Android 10+:应用专属目录免权限,直接导出
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            exportToAppExternalDir();
            return;
        }
        // Android 9 及以下:检查权限
        if (hasStoragePermission()) {
            exportToPublicDir();
        } else {
            requestStoragePermission();
        }
    }

    /** 检查是否已授权所有存储权限 */
    private boolean hasStoragePermission() {
        for (String perm : STORAGE_PERMS) {
            if (ContextCompat.checkSelfPermission(this, perm)
                    != PackageManager.PERMISSION_GRANTED) {
                return false;
            }
        }
        return true;
    }

    /** 申请存储权限:先判断是否需要解释 */
    private void requestStoragePermission() {
        boolean shouldExplain = false;
        for (String perm : STORAGE_PERMS) {
            if (ActivityCompat.shouldShowRequestPermissionRationale(this, perm)) {
                shouldExplain = true;
                break;
            }
        }
        if (shouldExplain) {
            // 之前拒绝过但未勾选"不再询问",先解释再申请
            new AlertDialog.Builder(this)
                .setTitle("需要存储权限")
                .setMessage("导出文件需要写入外部存储,拒绝将无法使用该功能。")
                .setPositiveButton("去授权", (d, w) ->
                    ActivityCompat.requestPermissions(
                        this, STORAGE_PERMS, REQ_STORAGE))
                .setNegativeButton("取消", null)
                .show();
        } else {
            // 首次申请 或 已勾选"不再询问"
            ActivityCompat.requestPermissions(this, STORAGE_PERMS, REQ_STORAGE);
        }
    }

    /** 处理授权结果 */
    @Override
    public void onRequestPermissionsResult(int requestCode,
                                           @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode != REQ_STORAGE) return;

        boolean allGranted = grantResults.length > 0;
        for (int r : grantResults) {
            if (r != PackageManager.PERMISSION_GRANTED) {
                allGranted = false;
                break;
            }
        }

        if (allGranted) {
            exportToPublicDir();
        } else {
            // 判断是否勾选了"不再询问"
            boolean neverAsk = false;
            for (String perm : STORAGE_PERMS) {
                if (!ActivityCompat.shouldShowRequestPermissionRationale(this, perm)) {
                    neverAsk = true;
                    break;
                }
            }
            if (neverAsk) {
                guideToSettings();
            } else {
                Toast.makeText(this, "权限被拒绝,无法导出", Toast.LENGTH_SHORT).show();
            }
        }
    }

    /** 引导用户去系统设置手动开启权限 */
    private void guideToSettings() {
        new AlertDialog.Builder(this)
            .setTitle("权限已被禁用")
            .setMessage("存储权限被设为不再询问,请到系统设置中手动开启")
            .setPositiveButton("去设置", (d, w) -> {
                Intent intent = new Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS);
                intent.setData(Uri.parse("package:" + getPackageName()));
                startActivity(intent);
            })
            .setNegativeButton("取消", null)
            .show();
    }

    /** 导出到外部存储公共目录(Android 9 及以下) */
    private void exportToPublicDir() {
        File dir = Environment.getExternalStoragePublicDirectory(
            Environment.DIRECTORY_DOWNLOADS);
        if (dir == null) {
            Toast.makeText(this, "外部存储不可用", Toast.LENGTH_SHORT).show();
            return;
        }
        if (!dir.exists()) dir.mkdirs();
        File file = new File(dir, "app_export.txt");
        try (FileOutputStream fos = new FileOutputStream(file)) {
            String content = "导出时间: " +
                new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.CHINA)
                    .format(new Date());
            fos.write(content.getBytes(StandardCharsets.UTF_8));
            Toast.makeText(this, "已导出到: " + file.getAbsolutePath(),
                Toast.LENGTH_LONG).show();
        } catch (IOException e) {
            Log.e("Export", "write fail", e);
            Toast.makeText(this, "导出失败: " + e.getMessage(),
                Toast.LENGTH_SHORT).show();
        }
    }

    /** 导出到应用专属目录(Android 10+,免权限) */
    private void exportToAppExternalDir() {
        File dir = getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS);
        if (dir == null) {
            Toast.makeText(this, "外部存储不可用", Toast.LENGTH_SHORT).show();
            return;
        }
        if (!dir.exists()) dir.mkdirs();
        File file = new File(dir, "app_export.txt");
        try (FileOutputStream fos = new FileOutputStream(file)) {
            String content = "导出时间: " +
                new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.CHINA)
                    .format(new Date());
            fos.write(content.getBytes(StandardCharsets.UTF_8));
            Toast.makeText(this, "已导出到: " + file.getAbsolutePath(),
                Toast.LENGTH_LONG).show();
        } catch (IOException e) {
            Log.e("Export", "write fail", e);
            Toast.makeText(this, "导出失败: " + e.getMessage(),
                Toast.LENGTH_SHORT).show();
        }
    }
}
```

```xml
<!-- ============ AndroidManifest.xml ============ -->
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.storage">

    <!-- 外部存储读写权限(Android 10+ 中 WRITE 实际无效,但 Android 9 及以下需要) -->
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"
        android:maxSdkVersion="32" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"
        android:maxSdkVersion="29" />

    <!-- Android 13+ 细分媒体权限(本例未使用,完整适配时需添加) -->
    <!--
    <uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
    <uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />
    <uses-permission android:name="android.permission.READ_MEDIA_AUDIO" />
    -->

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:requestLegacyExternalStorage="true"
        android:theme="@style/Theme.AppCompat.Light.NoActionBar">

        <activity
            android:name=".FileExportActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

```xml
<!-- ============ res/layout/activity_export.xml ============ -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp"
    android:gravity="center">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="文件导出演示"
        android:textSize="20sp"
        android:layout_marginBottom="24dp" />

    <Button
        android:id="@+id/btn_export"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="导出文件到外部存储" />
</LinearLayout>
```

**评分要点**：
- 在 Manifest 中声明权限 ✓
- 使用 `checkSelfPermission` 检查权限 ✓
- 使用 `requestPermissions` 申请权限 ✓
- 处理 `shouldShowRequestPermissionRationale` 解释场景 ✓
- 在 `onRequestPermissionsResult` 中正确处理授权/拒绝/不再询问三种情况 ✓
- 引导用户去系统设置处理"不再询问" ✓
- Android 10+ 优先用 `getExternalFilesDir` 免权限方案 ✓
- Android 9 及以下区分公共目录与权限申请 ✓
</details>

---

## 考点统计与复习建议

### 考点分布统计表

| 题号 | 题型 | 涉及考点 | 难度 | 对应小节 |
| ---- | ---- | -------- | ---- | -------- |
| 1 | 选择 | SharedPreferences 特性 | ⭐ | [[5.1 SharedPreferences 轻量存储\|5.1]] |
| 2 | 选择 | apply vs commit | ⭐ | [[5.1 SharedPreferences 轻量存储\|5.1]] |
| 3 | 选择 | 内部 vs 外部存储 | ⭐⭐ | [[5.2 文件读写（内部存储、外部存储）\|5.2]] |
| 4 | 选择 | SQLiteOpenHelper 回调 | ⭐⭐ | [[5.3 SQLite 数据库基础操作\|5.3]] |
| 5 | 选择 | 运行时权限"不再询问" | ⭐⭐ | [[5.4 权限管理：存储权限申请\|5.4]] |
| 6 | 填空 | SP 写入三步 | ⭐ | [[5.1 SharedPreferences 轻量存储\|5.1]] |
| 7 | 填空 | 权限分类与申请流程 | ⭐⭐ | [[5.4 权限管理：存储权限申请\|5.4]] |
| 8 | 填空 | Cursor 使用 | ⭐⭐ | [[5.3 SQLite 数据库基础操作\|5.3]] |
| 9 | 简答 | 四种存储方案对比 | ⭐⭐ | [[MOC - 第5章\|全章]] |
| 10 | 简答 | onCreate/onUpgrade | ⭐⭐ | [[5.3 SQLite 数据库基础操作\|5.3]] |
| 11 | 简答 | SQL 注入防护 | ⭐⭐ | [[5.3 SQLite 数据库基础操作\|5.3]] |
| 12 | 简答 | Scoped Storage 适配 | ⭐⭐⭐ | [[5.2 文件读写（内部存储、外部存储）\|5.2]] |
| 13 | 代码 | SQLite CRUD 完整实现 | ⭐⭐⭐ | [[5.3 SQLite 数据库基础操作\|5.3]] |
| 14 | 代码 | SharedPreferences 登录管理 | ⭐⭐ | [[5.1 SharedPreferences 轻量存储\|5.1]] |
| 15 | 代码 | 运行时权限申请完整流程 | ⭐⭐⭐ | [[5.4 权限管理：存储权限申请\|5.4]] |

### 复习建议

> [!tip] 高效复习路线
> 1. **第一优先（必考）**：SharedPreferences 写入三步流程与 apply/commit 区别（见第 1、2、6、14 题），必须能默写。
> 2. **第二优先**：SQLite 完整 CRUD 实现与参数化查询（见第 4、8、10、11、13 题），重点掌握 `SQLiteOpenHelper`、`Cursor`、`ContentValues`、`?` 占位符防注入。
> 3. **第三优先**：运行时权限申请三步流程与"不再询问"处理（见第 5、7、15 题），能写完整代码并区分 Android 版本差异。
> 4. **第四优先**：四种存储方案选型与 Scoped Storage 适配（见第 3、9、12 题），理解 Android 10+ 存储分区变化。
> 5. **动手实践**：15 题中代码设计题共 3 道，建议在 Android Studio 中至少完整实现第 13、15 题——SQLite CRUD 是数据库章节核心，权限申请是工程合规必备。
> 6. **版本适配**：复习时对照 Android 6.0/10/11/13 四个关键版本的存储与权限演化节点，理解每代系统的变化原因（隐私保护）。

## 章节导航

- 上级：[[MOC - 第5章|第5章 数据持久化存储]]
- 上一章习题：[[MOC - 第4章习题|第4章习题]]
- 下一章习题：[[MOC - 第6章习题|第6章习题]]
- 课程总览：[[MOC - 移动互联网开发技术|移动互联网开发技术]]
