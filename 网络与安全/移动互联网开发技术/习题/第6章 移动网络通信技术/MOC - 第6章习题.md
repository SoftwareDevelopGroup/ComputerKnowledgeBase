---
domain: 网络与安全
subject: 移动互联网开发技术
type: exercise
chapter: 第6章 移动网络通信技术
tags: [移动开发,习题,网络请求,JSON,OkHttp,异步]
prerequisites: ["计算机网络A","Java程序设计"]
aliases: [第6章习题, 网络通信习题, 第6章练习]
---

# MOC - 第6章习题

> [!info] 本章习题说明
> - 配套知识点：[[MOC - 第6章|第6章 移动网络通信技术]]
> - 题目数量：**18 题**（选择 6 + 填空 3 + 简答 4 + 代码设计 5）
> - 难度梯度：⭐基础 / ⭐⭐中等 / ⭐⭐⭐较难
> - 答案折叠在每题下方的 `<details>` 块中，建议先独立作答再展开对照

## 一、选择题（6 题）

### 1. ⭐ Android 系统从哪个 API 版本开始，在主线程进行网络操作会抛出 NetworkOnMainThreadException？

A. API 8
B. API 11
C. API 14
D. API 21

<details>
<summary>查看答案</summary>

**答案：B**

Android 从 API 11（Honeycomb）开始，严格禁止主线程执行网络操作，违规会抛出 `NetworkOnMainThreadException`。此举是为避免网络耗时阻塞 UI 线程导致 ANR。
</details>

---

### 2. ⭐ 关于 HTTP 状态码，下列描述正确的是？

A. 200 表示请求成功，201 表示服务器内部错误
B. 301 是临时重定向，302 是永久重定向
C. 401 表示未授权，需要身份认证；403 表示禁止访问
D. 5xx 类状态码表示客户端错误

<details>
<summary>查看答案</summary>

**答案：C**

- A 错：200 表示成功，201 表示 Created（资源已创建）。
- B 错：301 是永久重定向，302 是临时重定向，正好相反。
- C 对：401 Unauthorized 需认证，403 Forbidden 禁止访问。
- D 错：5xx 是服务端错误，4xx 才是客户端错误。
</details>

---

### 3. ⭐⭐ 关于 OkHttp 的 execute() 和 enqueue() 方法，下列说法正确的是？

A. execute() 是异步方法，enqueue() 是同步方法
B. 两者都可以在主线程直接调用
C. enqueue() 的 Callback 在主线程执行
D. execute() 在调用线程阻塞，enqueue() 立即返回，结果通过 Callback 异步回调

<details>
<summary>查看答案</summary>

**答案：D**

- A 错：execute() 同步阻塞，enqueue() 异步回调。
- B 错：execute() 在主线程调用会抛 NetworkOnMainThreadException。
- C 错：enqueue() 的 Callback onResponse/onFailure 都在**子线程**执行，需手动切回主线程更新 UI。
- D 对：execute() 阻塞调用线程，enqueue() 立即返回。
</details>

---

### 4. ⭐⭐ 使用 Gson 解析以下 JSON 字符串到 `List<User>`，正确写法是？

```json
[{"name":"Tom"},{"name":"Jerry"}]
```

A. `List<User> list = gson.fromJson(json, List.class);`
B. `List<User> list = gson.fromJson(json, new TypeToken<List<User>>(){}.getType());`
C. `List<User> list = gson.fromJson(json, User.class);`
D. `List<User> list = gson.fromJson(json, ArrayList<User>.class);`

<details>
<summary>查看答案</summary>

**答案：B**

由于 Java 泛型擦除，`List.class` 和 `ArrayList<User>.class` 都无法保留泛型信息，会导致元素被解析为 LinkedTreeMap。必须用 `TypeToken<List<User>>(){}.getType()` 保留泛型，让 Gson 知道列表元素类型是 User。

- A 错：List.class 无泛型信息。
- C 错：User.class 只能解析单个对象，不能解析数组。
- D 错：Java 不支持 `ArrayList<User>.class` 这种语法。
</details>

---

### 5. ⭐⭐ 关于 OkHttp 拦截器，下列描述错误的是？

A. 应用拦截器通过 `addInterceptor` 添加，只调用一次
B. 网络拦截器通过 `addNetworkInterceptor` 添加，每次网络请求都会调用
C. 应用拦截器能看到重定向过程
D. 拦截器可用于添加公共 Header、日志、Token 等

<details>
<summary>查看答案</summary>

**答案：C**

C 错：应用拦截器在重定向之前只调用一次，**看不到重定向过程**；网络拦截器才会对每次网络请求（包括重定向）都调用。A、B、D 描述正确。
</details>

---

### 6. ⭐⭐⭐ 关于 WebSocket 与 HTTP 的区别，下列说法错误的是？

A. WebSocket 是全双工通信，HTTP 是请求-响应模式
B. WebSocket 建立连接后服务端可主动推送消息
C. WebSocket 握手时使用 HTTP 协议升级而来
D. WebSocket 不需要心跳保活，连接会一直有效

<details>
<summary>查看答案</summary>

**答案：D**

D 错：移动网络下 NAT 设备会在连接空闲一段时间后回收映射，导致连接"假死"，WebSocket **必须通过心跳保活**（定期发 Ping 或空消息）维持连接。A、B、C 描述正确。
</details>

---

## 二、填空题（3 题）

### 7. ⭐ Android 中，主线程做网络操作会抛出 ________ 异常，该异常是从 API ________ 开始引入的。

<details>
<summary>查看答案</summary>

**答案：NetworkOnMainThreadException、11（Honeycomb）**

Android 3.0（API 11）起严格禁止主线程做网络操作，违规抛 NetworkOnMainThreadException，目的是防止网络耗时阻塞 UI 导致 ANR。
</details>

---

### 8. ⭐ OkHttp 中同步执行请求的方法是 ________，异步执行请求的方法是 ________；其中 ________ 方法不能在主线程调用。

<details>
<summary>查看答案</summary>

**答案：execute()、enqueue()、execute()**

- `execute()`：同步阻塞，在调用线程执行，主线程调用会抛 NetworkOnMainThreadException。
- `enqueue()`：异步，立即返回，结果通过 Callback 回调（回调在子线程）。
</details>

---

### 9. ⭐⭐ 使用 Gson 解析 `List<Article>` 时，为避免泛型擦除导致类型丢失，应使用 ________ 类获取泛型 Type；若 JSON 字段名与 Java 字段不一致，应使用 ________ 注解映射字段名。

<details>
<summary>查看答案</summary>

**答案：TypeToken、@SerializedName**

- `TypeToken<List<Article>>(){}.getType()` 通过匿名内部类保留泛型信息，让 Gson 知道元素类型。
- `@SerializedName("article_id")` 把 JSON 中的 article_id 映射到 Java 字段。
</details>

---

## 三、简答题（4 题）

### 10. ⭐⭐ 简述 Android 单线程模型与主线程禁止网络操作的原因，并说明主线程做耗时操作的后果。

<details>
<summary>查看答案</summary>

**Android 单线程模型**：所有 UI 操作（绘制、事件分发、视图更新）都在主线程（Main Thread / UI Thread）执行，其他线程不允许直接更新 UI（否则抛 CalledFromWrongThreadException）。

**禁止主线程网络操作的原因**：
- 网络是耗时操作，延迟不可控（可能几秒甚至超时）
- 主线程被网络阻塞会导致 UI 卡顿、无响应
- Android 3.0（API 11）起直接抛 NetworkOnMainThreadException，从机制上避免此类问题

**主线程做耗时操作的后果**：
- 输入事件分发超过 5 秒、BroadcastReceiver 超过 10 秒，触发 ANR（Application Not Responding）弹窗
- UI 渲染掉帧、动画卡顿
- 用户体验差，可能被系统强制关闭
</details>

---

### 11. ⭐⭐ 对比 Thread+Handler、AsyncTask、HandlerThread、线程池、RxJava 五种异步方案的特点与适用场景。

<details>
<summary>查看答案</summary>

| 方案 | API 难度 | 灵活性 | 状态 | 典型用途 |
| ---- | -------- | ------ | ---- | -------- |
| Thread + Handler | 中 | 高 | 通用 | 自定义线程 + UI 更新 |
| AsyncTask | 低 | 低 | **已废弃**（API 30） | 简单异步任务（了解原理） |
| HandlerThread | 中 | 中 | 通用 | 串行后台任务 |
| 线程池 + Handler | 中高 | 高 | 通用 | 并发任务管理 |
| RxJava/Retrofit | 高 | 极高 | 主流 | 复杂异步、链式调用 |

**适用场景**：
- **Thread+Handler**：简单一次性任务，自定义线程控制
- **AsyncTask**：已废弃，了解原理即可，新代码不要用
- **HandlerThread**：需要串行执行多个后台任务（如文件下载队列）
- **线程池+Handler**：并发任务管理（图片加载、批量请求）
- **RxJava/Retrofit**：复杂异步链、REST API 调用、数据流处理，生产环境主流方案
</details>

---

### 12. ⭐⭐ 简述 OkHttp 的核心特性，并说明 OkHttpClient 为什么应该作为全局单例使用。

<details>
<summary>查看答案</summary>

**OkHttp 核心特性**：
1. **连接池**：默认 5 个空闲连接、5 分钟保活，复用 TCP/TLS 连接，减少握手开销
2. **GZIP 压缩**：自动添加 `Accept-Encoding: gzip`，减少流量
3. **响应缓存**：支持磁盘缓存，避免重复请求
4. **HTTP/2 支持**：多路复用，单连接并行多请求
5. **自动重试**：网络请求失败自动重试（默认 1 次）
6. **拦截器机制**：灵活的请求/响应处理链
7. **WebSocket 内置**：支持长连接通信

**OkHttpClient 应作为单例的原因**：
- OkHttpClient 内部持有 **ConnectionPool（连接池）、Dispatcher（调度器）、Cache（缓存）** 等共享资源
- 每次 `new OkHttpClient()` 会**重建连接池**，导致已建立的 TCP/TLS 连接无法复用，所有请求都要重新握手
- 重建连接池会浪费系统资源、增加延迟、消耗电量
- 单例模式复用连接池，大幅提升后续请求性能（免去 TCP/TLS 握手）

正确做法：在 Application 或工具类中持有一个全局 client 实例，所有网络请求共用。
</details>

---

### 13. ⭐⭐ 对比 HTTP 与 WebSocket 在通信模式、连接管理、应用场景上的差异，并说明 WebSocket 长连接为何需要心跳保活。

<details>
<summary>查看答案</summary>

| 维度 | HTTP | WebSocket |
| ---- | ---- | --------- |
| 通信模式 | 请求-响应 | 全双工 |
| 连接 | 短连接（默认） | 长连接 |
| 服务器推送 | 不支持（需轮询） | 原生支持 |
| 头部开销 | 每次请求带 Header | 握手后仅 2~10 字节帧头 |
| 协议 | http/https | ws/wss |
| 典型场景 | 普通数据接口 | 即时通讯、实时推送 |

**WebSocket 长连接需要心跳保活的原因**：
1. **NAT 超时**：移动网络下运营商 NAT 设备会在连接空闲一段时间（通常几十秒到几分钟）后回收映射表项，导致连接"假死"——客户端以为连接还在，实际数据已无法到达对端
2. **应用层探测**：定期发送心跳（空消息或 Ping 帧）可以让 NAT 维持映射，同时双向探测连接是否仍然可用
3. **快速发现断连**：如果心跳无响应，可立即触发重连，避免用户感知到消息丢失

OkHttp 提供 `pingInterval` 内置心跳，推荐使用，也可以应用层自定义心跳消息。
</details>

---

## 四、代码设计题（5 题）

### 14. ⭐⭐ Thread+Handler 异步请求代码题

请使用 **Thread + Handler** 实现以下需求：
1. MainActivity 中点击"加载"按钮，在子线程发起 HTTP 请求访问 `https://api.example.com/news`
2. 请求成功后，通过 Handler 把返回的字符串发回主线程，显示在 TextView 中
3. 请求失败时，通过 Handler 把错误信息发回主线程，Toast 提示
4. Handler 使用静态内部类 + WeakReference 避免内存泄漏

<details>
<summary>查看答案</summary>

```java
public class MainActivity extends AppCompatActivity {
    private static final int MSG_SUCCESS = 1;
    private static final int MSG_FAIL = 2;
    private TextView tvResult;

    // 静态内部类 Handler + WeakReference 避免内存泄漏
    private static class SafeHandler extends Handler {
        private final WeakReference<MainActivity> ref;

        SafeHandler(MainActivity activity) {
            super(Looper.getMainLooper());
            ref = new WeakReference<>(activity);
        }

        @Override
        public void handleMessage(Message msg) {
            MainActivity a = ref.get();
            if (a == null || a.isFinishing()) return;
            switch (msg.what) {
                case MSG_SUCCESS:
                    a.tvResult.setText((String) msg.obj);
                    break;
                case MSG_FAIL:
                    Toast.makeText(a, "加载失败: " + msg.obj, Toast.LENGTH_SHORT).show();
                    break;
            }
        }
    }

    private final SafeHandler handler = new SafeHandler(this);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tvResult = findViewById(R.id.tv_result);
        findViewById(R.id.btn_load).setOnClickListener(v -> loadNews());
    }

    private void loadNews() {
        new Thread(() -> {
            try {
                URL url = new URL("https://api.example.com/news");
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setConnectTimeout(10000);
                conn.setReadTimeout(15000);
                try (InputStream is = conn.getInputStream();
                     Scanner sc = new Scanner(is).useDelimiter("\\A")) {
                    String result = sc.hasNext() ? sc.next() : "";
                    handler.obtainMessage(MSG_SUCCESS, result).sendToTarget();
                }
            } catch (IOException e) {
                handler.obtainMessage(MSG_FAIL, e.getMessage()).sendToTarget();
            }
        }).start();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        handler.removeCallbacksAndMessages(null);
    }
}
```
</details>

---

### 15. ⭐⭐ Gson 解析 JSON 代码题

给定如下 JSON 字符串，请编写代码：
1. 定义对应的 POJO 类（使用 `@SerializedName` 处理字段名差异）
2. 用 Gson 解析为 Java 对象
3. 遍历列表并打印每本书的标题与作者

```json
{
  "status": "ok",
  "total": 2,
  "books": [
    { "book_id": 101, "title": "Android 开发", "author": "郭霖", "price": 89.0 },
    { "book_id": 102, "title": "Java 编程思想", "author": "Bruce Eckel", "price": 108.0 }
  ]
}
```

<details>
<summary>查看答案</summary>

```java
// ============ POJO 类 ============
public class BookResponse {
    private String status;
    private int total;
    private List<Book> books;
    // getter/setter
}

public class Book {
    @SerializedName("book_id")
    private long id;

    private String title;
    private String author;
    private double price;

    // getter/setter
    @Override
    public String toString() {
        return title + " - " + author;
    }
}

// ============ 解析代码 ============
public class ParseDemo {
    public static void main(String[] args) {
        String json = "{ ... }";   // 上面给的 JSON

        Gson gson = new Gson();
        BookResponse resp = gson.fromJson(json, BookResponse.class);

        System.out.println("状态: " + resp.getStatus());
        System.out.println("总数: " + resp.getTotal());
        for (Book b : resp.getBooks()) {
            System.out.println(b.getTitle() + " - " + b.getAuthor() + " - " + b.getPrice());
        }
    }
}
```

**输出**：
```
状态: ok
总数: 2
Android 开发 - 郭霖 - 89.0
Java 编程思想 - Bruce Eckel - 108.0
```

**说明**：
- `@SerializedName("book_id")` 把 JSON 的 `book_id` 映射到 Java 的 `id` 字段
- Gson 自动处理嵌套对象和数组，无需手动逐字段解析
- 解析失败会抛 JsonSyntaxException，生产环境应 try-catch
</details>

---

### 16. ⭐⭐⭐ OkHttp 异步请求代码题

请使用 OkHttp 异步请求实现以下功能：
1. POST 请求 `https://api.example.com/login`，提交 JSON body `{"username":"admin","password":"123456"}`
2. 添加拦截器自动在请求头加上 `Authorization: Bearer <token>`
3. 在 onResponse 回调中把响应体字符串发回主线程，更新 TextView
4. 失败时 Toast 提示错误信息

<details>
<summary>查看答案</summary>

```java
public class LoginActivity extends AppCompatActivity {
    private TextView tvResult;
    private OkHttpClient client;

    // 自定义拦截器:添加 Token
    private static class AuthInterceptor implements Interceptor {
        @NonNull
        @Override
        public Response intercept(Chain chain) throws IOException {
            Request original = chain.request();
            Request authed = original.newBuilder()
                .header("Authorization", "Bearer " + TokenManager.getToken())
                .build();
            return chain.proceed(authed);
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        tvResult = findViewById(R.id.tv_result);

        client = new OkHttpClient.Builder()
            .connectTimeout(10, TimeUnit.SECONDS)
            .addInterceptor(new AuthInterceptor())
            .build();

        findViewById(R.id.btn_login).setOnClickListener(v -> doLogin());
    }

    private void doLogin() {
        // 构建 JSON body
        String json = "{\"username\":\"admin\",\"password\":\"123456\"}";
        RequestBody body = RequestBody.create(json,
            MediaType.parse("application/json; charset=utf-8"));

        Request request = new Request.Builder()
            .url("https://api.example.com/login")
            .post(body)
            .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                runOnUiThread(() ->
                    Toast.makeText(LoginActivity.this,
                        "登录失败: " + e.getMessage(), Toast.LENGTH_SHORT).show());
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                String result = response.body().string();
                runOnUiThread(() -> tvResult.setText(result));
            }
        });
    }
}
```

**说明**：
- 拦截器统一添加 Token，避免每个请求重复写
- enqueue() 异步执行，Callback 在子线程，需用 `runOnUiThread` 切回主线程更新 UI
- POST JSON 需指定 `application/json` 的 MediaType
</details>

---

### 17. ⭐⭐⭐ OkHttp 文件上传代码题

请使用 OkHttp Multipart 实现图片上传：
1. 上传本地图片 `/sdcard/Pictures/photo.jpg` 到 `https://api.example.com/upload`
2. 同时携带表单字段 `title=我的照片`、`description=2026年夏`
3. 进度回调可选，核心是 MultipartBody 构建

<details>
<summary>查看答案</summary>

```java
public class UploadActivity extends AppCompatActivity {
    private static final int REQ_PERMISSION = 1001;
    private OkHttpClient client = new OkHttpClient();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_upload);
        findViewById(R.id.btn_upload).setOnClickListener(v -> {
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.READ_EXTERNAL_STORAGE)
                    != PackageManager.PERMISSION_GRANTED) {
                ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.READ_EXTERNAL_STORAGE}, REQ_PERMISSION);
            } else {
                uploadFile();
            }
        });
    }

    private void uploadFile() {
        File file = new File(Environment.getExternalStorageDirectory(), "Pictures/photo.jpg");
        if (!file.exists()) {
            Toast.makeText(this, "文件不存在", Toast.LENGTH_SHORT).show();
            return;
        }

        // 构建 MultipartBody
        RequestBody fileBody = RequestBody.create(file,
            MediaType.parse("image/jpeg"));

        MultipartBody multipart = new MultipartBody.Builder()
            .setType(MultipartBody.FORM)
            .addFormDataPart("title", "我的照片")
            .addFormDataPart("description", "2026年夏")
            .addFormDataPart("file", file.getName(), fileBody)
            .build();

        Request request = new Request.Builder()
            .url("https://api.example.com/upload")
            .post(multipart)
            .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                runOnUiThread(() ->
                    Toast.makeText(UploadActivity.this,
                        "上传失败: " + e.getMessage(), Toast.LENGTH_SHORT).show());
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                String result = response.body().string();
                runOnUiThread(() ->
                    Toast.makeText(UploadActivity.this,
                        "上传成功: " + result, Toast.LENGTH_SHORT).show());
            }
        });
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == REQ_PERMISSION && grantResults.length > 0
                && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            uploadFile();
        }
    }
}
```

**说明**：
- `MultipartBody.FORM` 类型支持同时上传文本字段与文件
- `addFormDataPart(name, value)` 添加普通字段
- `addFormDataPart(name, filename, requestBody)` 添加文件字段
- 读取外部存储需要 `READ_EXTERNAL_STORAGE` 权限（Android 10+ 推荐用 Scoped Storage）
</details>

---

### 18. ⭐⭐⭐ WebSocket 客户端代码题

请使用 OkHttp WebSocket 实现简单聊天客户端：
1. 连接 `wss://api.example.com/ws/chat`
2. 收到服务端消息时，通过 Handler 切回主线程显示在 TextView
3. 点击"发送"按钮，把输入框内容发送出去
4. 设置 30 秒心跳保活
5. Activity 销毁时关闭连接

<details>
<summary>查看答案</summary>

```java
public class ChatActivity extends AppCompatActivity {
    private EditText etInput;
    private TextView tvMessages;
    private Button btnSend;
    private WebSocket webSocket;
    private OkHttpClient client;
    private Handler handler = new Handler(Looper.getMainLooper());

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat);
        etInput = findViewById(R.id.et_input);
        tvMessages = findViewById(R.id.tv_messages);
        btnSend = findViewById(R.id.btn_send);

        // 30 秒心跳保活
        client = new OkHttpClient.Builder()
            .pingInterval(30, TimeUnit.SECONDS)
            .build();

        btnSend.setOnClickListener(v -> {
            String msg = etInput.getText().toString().trim();
            if (msg.isEmpty() || webSocket == null) return;
            webSocket.send(msg);
            appendMessage("我: " + msg);
            etInput.setText("");
        });

        connectWebSocket();
    }

    private void connectWebSocket() {
        Request request = new Request.Builder()
            .url("wss://api.example.com/ws/chat")
            .build();

        webSocket = client.newWebSocket(request, new WebSocketListener() {
            @Override
            public void onOpen(WebSocket ws, Response response) {
                handler.post(() -> appendMessage("系统: 已连接"));
            }

            @Override
            public void onMessage(WebSocket ws, String text) {
                // 子线程收到消息,切回主线程更新 UI
                handler.post(() -> appendMessage("对方: " + text));
            }

            @Override
            public void onMessage(WebSocket ws, ByteString bytes) {
                handler.post(() -> appendMessage("对方(二进制): " + bytes.size() + "B"));
            }

            @Override
            public void onClosing(WebSocket ws, int code, String reason) {
                ws.close(1000, null);
                handler.post(() -> appendMessage("系统: 连接关闭 " + code));
            }

            @Override
            public void onClosed(WebSocket ws, int code, String reason) {
                handler.post(() -> appendMessage("系统: 已断开"));
            }

            @Override
            public void onFailure(WebSocket ws, Throwable t, Response response) {
                handler.post(() -> appendMessage("系统: 连接失败 " + t.getMessage()));
            }
        });
    }

    private void appendMessage(String msg) {
        tvMessages.append(msg + "\n");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Activity 销毁时关闭连接,避免泄漏
        if (webSocket != null) {
            webSocket.close(1000, "Activity 销毁");
            webSocket = null;
        }
    }
}
```

**说明**：
- `pingInterval(30, TimeUnit.SECONDS)` 让 OkHttp 自动每 30 秒发 Ping 帧，无需手写
- `WebSocketListener` 回调都在子线程，更新 UI 必须切回主线程（Handler / runOnUiThread）
- Activity 销毁时务必 `webSocket.close()` 关闭连接，否则连接泄漏、耗电
- 真实 IM 场景应把 WebSocket 放在 Service 中，与 Activity 解耦
</details>

---

## 考点统计与复习建议

### 考点分布统计表

| 题号 | 题型 | 涉及考点 | 难度 | 对应小节 |
| ---- | ---- | -------- | ---- | -------- |
| 1 | 选择 | NetworkOnMainThreadException | ⭐ | [[6.2 异步网络请求、主线程禁止网络操作\|6.2]] |
| 2 | 选择 | HTTP 状态码 | ⭐ | [[6.1 HTTP、HTTPS 协议移动端适配\|6.1]] |
| 3 | 选择 | OkHttp execute vs enqueue | ⭐⭐ | [[6.4 OkHttp 等网络框架基础\|6.4]] |
| 4 | 选择 | Gson 泛型解析 | ⭐⭐ | [[6.3 JSON 数据解析\|6.3]] |
| 5 | 选择 | 拦截器类型 | ⭐⭐ | [[6.4 OkHttp 等网络框架基础\|6.4]] |
| 6 | 选择 | WebSocket 与 HTTP 区别 | ⭐⭐⭐ | [[6.5 WebSocket 长连接简介\|6.5]] |
| 7 | 填空 | 主线程网络异常 | ⭐ | [[6.2 异步网络请求、主线程禁止网络操作\|6.2]] |
| 8 | 填空 | OkHttp 同步异步方法 | ⭐ | [[6.4 OkHttp 等网络框架基础\|6.4]] |
| 9 | 填空 | TypeToken / @SerializedName | ⭐⭐ | [[6.3 JSON 数据解析\|6.3]] |
| 10 | 简答 | 单线程模型与 ANR | ⭐⭐ | [[6.2 异步网络请求、主线程禁止网络操作\|6.2]] |
| 11 | 简答 | 异步方案对比 | ⭐⭐ | [[6.2 异步网络请求、主线程禁止网络操作\|6.2]] |
| 12 | 简答 | OkHttp 特性与单例 | ⭐⭐ | [[6.4 OkHttp 等网络框架基础\|6.4]] |
| 13 | 简答 | HTTP vs WebSocket | ⭐⭐ | [[6.5 WebSocket 长连接简介\|6.5]] |
| 14 | 代码 | Thread+Handler 异步请求 | ⭐⭐ | [[6.2 异步网络请求、主线程禁止网络操作\|6.2]] |
| 15 | 代码 | Gson 解析 JSON | ⭐⭐ | [[6.3 JSON 数据解析\|6.3]] |
| 16 | 代码 | OkHttp 异步 POST + 拦截器 | ⭐⭐⭐ | [[6.4 OkHttp 等网络框架基础\|6.4]] |
| 17 | 代码 | OkHttp 文件上传 | ⭐⭐⭐ | [[6.4 OkHttp 等网络框架基础\|6.4]] |
| 18 | 代码 | WebSocket 聊天客户端 | ⭐⭐⭐ | [[6.5 WebSocket 长连接简介\|6.5]] |

### 复习建议

> [!tip] 高效复习路线
> 1. **第一优先（必考）**：主线程禁止网络操作 + 异步方案，能默写 Thread+Handler 完整代码（见第 1、7、10、14 题）
> 2. **第二优先**：OkHttp 同步/异步区别、拦截器机制、单例原因（见第 3、5、8、12、16 题）
> 3. **第三优先**：JSON 解析，JSONObject 与 Gson 对比，TypeToken 处理泛型（见第 4、9、15 题）
> 4. **第四优先**：WebSocket 与 HTTP 区别、心跳保活、生命周期管理（见第 6、13、18 题）
> 5. **动手实践**：18 题中代码设计题共 5 道，建议在 Android Studio 中至少完整实现第 14、16、18 题，跑通异步请求、OkHttp POST、WebSocket 全流程

## 章节导航

- 上级：[[MOC - 第6章|第6章 移动网络通信技术]]
- 上一章习题：[[MOC - 第5章习题|第5章习题]]
- 下一章习题：[[MOC - 第7章习题|第7章习题]]
- 课程总览：[[MOC - 移动互联网开发技术|移动互联网开发技术]]
