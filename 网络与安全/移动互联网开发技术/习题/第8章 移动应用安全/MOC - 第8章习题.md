---
domain: 网络与安全
subject: 移动互联网开发技术
type: exercise
chapter: 第8章 移动应用安全
tags: [移动开发,习题,移动安全,加密,防抓包,权限,加固]
prerequisites: ["计算机网络A","Java程序设计"]
aliases: [第8章习题, 移动安全习题, 第8章练习]
---

# MOC - 第8章习题

> [!info] 本章习题说明
> - 配套知识点：[[MOC - 第8章|第8章 移动应用安全]]
> - 题目数量：**15 题**（选择 5 + 填空 3 + 简答 4 + 方案设计 3）
> - 难度梯度：⭐基础 / ⭐⭐中等 / ⭐⭐⭐较难
> - 答案折叠在每题下方的 `<details>` 块中，建议先独立作答再展开对照
> - 安全相关命令仅限授权实验环境使用

## 一、选择题（5 题）

### 1. ⭐ 关于 OWASP Mobile Top 10，下列描述错误的是？

A. M3 不安全的通信主要指 HTTP 明文与 HTTPS 缺证书校验
B. M5 密码学实现不足包含密钥硬编码与弱算法（DES/MD5）
C. Mobile Top 10 编号与名称在所有版本中完全一致
D. M6 不安全的授权与组件 exported 未保护密切相关

<details>
<summary>查看答案</summary>

**答案：C**

C 错：OWASP Mobile Top 10 在 2014、2016、2024 多次更新，编号与名称均有调整（如 2024 整合为 8 大类）。答题应以风险类别含义为准，不必死记编号顺序。A、B、D 描述均正确。
</details>

---

### 2. ⭐⭐ 关于 Android Keystore，下列说法正确的是？

A. Keystore 中的密钥私钥会导出到内存供应用使用
B. Keystore 密钥可被 root 用户直接读取私钥材料
C. Keystore 可绑定设备硬件（TEE/StrongBox），私钥不出硬件
D. Keystore 不支持设置密钥有效期

<details>
<summary>查看答案</summary>

**答案：C**

- A 错：Keystore 的私钥**不会导出到内存**，所有加密/签名操作在 Keystore 内部（TEE/StrongBox）完成。
- B 错：root 用户也只能调用 Keystore 接口，无法直接读取私钥材料。
- C 对：Keystore 支持硬件隔离（TEE/StrongBox），可绑定设备硬件。
- D 错：Keystore 支持通过 `setKeyValidityEnd` 等设置有效期，还支持 `setUserAuthenticationRequired`。
</details>

---

### 3. ⭐⭐ 关于 SSL Pinning（证书固定），下列描述错误的是？

A. SSL Pinning 在系统默认校验之外额外比对证书指纹
B. 即使攻击者拥有被信任的根证书，也无法伪造指纹匹配的假证书
C. 配置 Pinning 时建议只配 1 个 pin，避免冗余
D. Pinning 可固定整个证书、公钥或中间 CA 公钥

<details>
<summary>查看答案</summary>

**答案：C**

C 错：Pinning 应至少配置 **2 个 pin**（主 + 备），用于应对证书轮换/续期。若主证书过期更换且无备用 pin，APP 所有请求会因 SSL 握手失败而无法使用，造成"自我拒绝服务"。A、B、D 描述正确。
</details>

---

### 4. ⭐⭐ 关于 Android 组件 exported 属性，下列说法正确的是？

A. `exported="false"` 的组件可被其他应用调用，只是需要权限
B. Android 12（API 31）起，含 IntentFilter 的组件必须显式声明 exported
C. 含 IntentFilter 的组件在所有版本中都默认 exported=false
D. exported 属性只对 Activity 有效，对 Service/Receiver/Provider 无效

<details>
<summary>查看答案</summary>

**答案：B**

- A 错：`exported="false"` 表示**仅本应用可调用**，与权限无关。
- B 对：Android 12（API 31）起，含 IntentFilter 的组件必须显式声明 exported，否则编译报错。
- C 错：Android 12 之前含 IntentFilter 的组件默认 exported=true，是常见安全漏洞来源。
- D 错：exported 对四大组件（Activity/Service/Receiver/Provider）均有效。
</details>

---

### 5. ⭐⭐ 关于应用加固，下列描述错误的是？

A. ProGuard/R8 通过类名方法名重命名提高反编译门槛
B. 加壳后必须重新签名才能发布
C. 加固能让 APP 变得无法破解，是绝对安全的方案
D. 反调试应多点、动态检测，单点检测易被 Hook 绕过

<details>
<summary>查看答案</summary>

**答案：C**

C 错：加固**不能**让 APP 无法破解，只能提高攻击成本。攻击者用 Root 设备 + Frida + IDA Pro + 足够时间理论上能突破任何加固。加固的工程价值在于提高门槛、延长破解时间、配合法律手段。A、B、D 描述正确。
</details>

---

## 二、填空题（3 题）

### 6. ⭐ 移动应用安全的三大目标是防逆向、________ 和 ________。

<details>
<summary>查看答案</summary>

**答案：防篡改、防调试**

应用加固的三大目标：防逆向（阻止阅读代码）、防篡改（阻止修改后重签名分发）、防调试（阻止用调试器/Hook 工具动态分析）。
</details>

---

### 7. ⭐⭐ AES 加密推荐使用 ________ 模式，该模式同时提供机密性与 ________；使用时 IV 必须 ________ 且不可复用。

<details>
<summary>查看答案</summary>

**答案：GCM、完整性（或完整性校验/MAC）、随机**

- AES/GCM/NoPadding 是 Android 推荐模式：GCM 同时提供机密性与完整性，无需额外 HMAC
- IV 必须用 `SecureRandom` 随机生成，且同一密钥下 IV 不可复用，否则 GCM 安全性完全破坏
- 不推荐 ECB（相同明文→相同密文）和裸 CBC（需额外 HMAC）
</details>

---

### 8. ⭐⭐ Android 12（API 31）起，PendingIntent 必须显式声明 ________ 或 ________ 标志；推荐使用前者，因为后者允许接收方修改 Intent 内容，存在安全风险。

<details>
<summary>查看答案</summary>

**答案：FLAG_IMMUTABLE、FLAG_MUTABLE**

- Android 12 起 PendingIntent 必须显式声明 `FLAG_IMMUTABLE` 或 `FLAG_MUTABLE`
- 推荐用 `FLAG_IMMUTABLE`：Intent 内容不可被接收方修改
- `FLAG_MUTABLE` 仅在必须让接收方填充字段时使用（如通知回复框），且必须最小化可变字段
</details>

---

## 三、简答题（4 题）

### 9. ⭐⭐ 简述 HTTPS 抓包工具（如 Charles）能解密 HTTPS 流量的根本原因，并说明 SSL Pinning 如何防护。

<details>
<summary>查看答案</summary>

**根本原因**：
HTTPS 默认仅信任系统 CA 列表。抓包工具通过让用户/Root 将自己的根证书安装到系统 CA 列表，污染了信任锚点。握手时工具出示由该根证书签发的"假证书"，系统校验通过，工具即成为中间人，分别与 APP 和真实服务器建立独立 HTTPS 连接，从而解密流量。

**SSL Pinning 防护原理**：
SSL Pinning 在客户端预先存储服务器证书的指纹（公钥哈希），握手时除系统校验外，**额外比对服务器证书的指纹是否与预期一致**。即使攻击者拥有被信任的根证书，也无法伪造出指纹匹配的假证书（除非拿到服务器私钥），从而拦截 MITM 抓包。

**Pinning 的固定对象**：
- 固定整个证书：证书更换需发版
- 固定公钥（推荐）：证书续期只要公钥不变即可
- 固定中间 CA 公钥：灵活性最高
</details>

---

### 10. ⭐⭐ 对比原生 SharedPreferences、EncryptedSharedPreferences、SQLCipher 三种本地存储方案的特点与适用场景。

<details>
<summary>查看答案</summary>

| 方案 | 明文风险 | 加密强度 | 密钥位置 | 适用场景 |
| ---- | -------- | -------- | -------- | -------- |
| 原生 SharedPreferences | 高 | 无 | — | 非敏感配置（夜间模式、字体大小） |
| EncryptedSharedPreferences | 低 | AES-256-GCM | Android Keystore | 敏感配置（Token、密码哈希） |
| SQLCipher | 低 | AES-256 | 密码派生（建议 Keystore） | 敏感结构化数据（聊天记录、订单） |

**关键差异**：
- **加密范围**：SP 明文，EncryptedSharedPreferences 键值双加密，SQLCipher 整库加密
- **API 兼容**：EncryptedSharedPreferences 与原生 SP 接口一致，迁移成本低；SQLCipher 与 SQLiteDatabase 接口一致
- **性能**：SP 最快，EncryptedSharedPreferences 略慢（首次解密），SQLCipher 中等
- **数据量**：SP/EncryptedSharedPreferences 适合小数据（<1MB），SQLCipher 适合结构化大数据

**选型原则**：按数据敏感度分级——非敏感用原生方案换性能，敏感用 Keystore + 加密换安全。
</details>

---

### 11. ⭐⭐ 简述 Android 组件暴露的典型风险，并说明如何用 exported=false、自定义权限、签名级权限三层方案进行防护。

<details>
<summary>查看答案</summary>

**组件暴露的典型风险**：
- **Activity**：恶意 APP `startActivity` 绕过登录直进敏感页面（如支付页）
- **Service**：`startService`/`bindService` 触发任意操作
- **BroadcastReceiver**：`sendBroadcast` 伪造广播触发逻辑，篡改状态
- **ContentProvider**：`query` 越权读取或 SQL 注入泄露数据

**三层防护方案**：

1. **第一层 `exported="false"`（默认不暴露）**：
   - 仅本应用可调用，最简单最强
   - Android 12 起含 IntentFilter 的组件必须显式声明 exported
   - 适用于：仅本应用内部使用的组件

2. **第二层 普通自定义权限（normal）**：
   - 通过 `<permission android:protectionLevel="normal">` 声明
   - 组件用 `android:permission` 限定调用方
   - 调用方声明 `<uses-permission>`
   - 局限：恶意应用主动声明 uses-permission 即可绕过

3. **第三层 签名级权限（signature，最可靠）**：
   - `protectionLevel="signature"`，系统自动比较调用方与声明方 APK 签名
   - 仅同签名应用可获取权限，第三方应用无法绕过
   - 适用于：自家多应用互调（如主应用与 SDK 应用）

**额外建议**：组件入口都应做业务校验（如登录状态、参数白名单），不信任调用方传入的参数。
</details>

---

### 12. ⭐⭐⭐ 简述应用加固的五层手段（代码混淆、加壳、反调试、完整性校验、SO 保护）的原理与各自局限。

<details>
<summary>查看答案</summary>

| 层次 | 原理 | 局限 |
| ---- | ---- | ---- |
| 代码混淆（ProGuard/R8） | 类/方法/字段重命名为短名，移除未使用代码 | 字符串与算法仍可见，反混淆可还原部分逻辑 |
| 加壳 | DEX 加密抽取，壳程序运行时解密加载 | 内存 dump 可提取真实 DEX，FART 等脱壳工具针对主流壳有效；性能损耗（冷启动慢 200ms~1s） |
| 反调试 | ptrace 自附加、TracerPid 检测、Frida/Xposed 检测 | 检测函数本身可被 Hook 让其永远返回 false；单点必被绕过 |
| 完整性校验 | 签名校验、文件哈希校验识别二次打包 | 校验代码放 Java 层易被 Hook；应放 SO 中多点检测 |
| SO 保护 | 关键算法放 Native，O-LLVM 混淆、字符串加密、反调试 | IDA Pro 仍可逆向，门槛高于 Java 但非不可破 |

**总体局限**：加固不等于绝对安全，只能提高攻击成本。应多层叠加，配合数据加密、SSL Pinning、组件防护形成纵深防御。
</details>

---

## 四、方案设计题（3 题）

### 13. ⭐⭐ 本地数据加密方案设计

某健康管理 APP 需要在本地存储以下数据，请为每类数据选择合适的存储与加密方案，并说明理由：

| 数据项 | 敏感度 | 选型 | 理由 |
| ------ | ------ | ---- | ---- |
| 用户登录 Token | 高 | ? | ? |
| 用户健康档案（结构化） | 高 | ? | ? |
| 夜间模式开关 | 低 | ? | ? |
| 用户头像图片 | 中 | ? | ? |
| 主加密密钥 | 极高 | ? | ? |

<details>
<summary>查看答案</summary>

| 数据项 | 敏感度 | 选型 | 理由 |
| ------ | ------ | ---- | ---- |
| 用户登录 Token | 高 | EncryptedSharedPreferences | 小数据 + 敏感 + 自动 AES-256-GCM 加密，密钥进 Keystore，API 与原生 SP 一致 |
| 用户健康档案（结构化） | 高 | SQLCipher 加密 SQLite | 结构化数据需查询，整库 AES-256 加密；密码本身从 Keystore 派生 |
| 夜间模式开关 | 低 | 原生 SharedPreferences | 非敏感配置，无需加密，换取最佳性能 |
| 用户头像图片 | 中 | 内部存储 + AES 加密文件 | 私有目录防其他应用读取，关键头像可加密；不要存 SD 卡 |
| 主加密密钥 | 极高 | Android Keystore（setUserAuthenticationRequired=true） | 私钥不出 TEE/StrongBox，硬件隔离；可绑定指纹解锁 |

**附加措施**：
- `android:allowBackup="false"` 禁止备份
- Release 包用 BuildConfig.DEBUG 控制日志
- 配合 R8 混淆 + 加固提高反编译门槛

**设计理念**：按数据敏感度分级选型，非敏感用原生方案换性能，敏感用 Keystore + 加密换安全，而不是"全部用最强加密"。
</details>

---

### 14. ⭐⭐⭐ HTTPS 防抓包方案设计与代码实现

某金融 APP 需要防止网络流量被 Charles/Fiddler 抓包。请设计多层防抓包方案，并给出 OkHttp `CertificatePinner` 的完整实现代码。要求：

1. 全站 HTTPS，禁止明文 HTTP
2. Network Security Config 区分 debug/release，Release 不信任用户 CA
3. OkHttp 启用 CertificatePinner，至少配 2 个 pin
4. 单例封装 OkHttpClient，生产环境日志降为 BASIC
5. 启动时检测代理设置

<details>
<summary>查看答案</summary>

**多层防抓包方案设计**：

| 层次 | 措施 | 作用 |
| ---- | ---- | ---- |
| 协议层 | 全站 HTTPS，`usesCleartextTraffic="false"` | 禁止明文 HTTP |
| 信任层 | Network Security Config 仅信任系统 CA | 普通用户安装抓包 CA 无效 |
| 固定层 | OkHttp CertificatePinner 固定公钥 | Root 用户安装系统 CA 也无法抓包 |
| 检测层 | 启动时检测代理设置 | 提示用户关闭代理 |
| 业务层 | 请求加 HMAC 签名 + 时间戳 + Nonce | 防重放、防篡改 |

**res/xml/network_security_config.xml**：
```xml
<network-security-config>
    <base-config cleartextTrafficPermitted="false">
        <trust-anchors>
            <certificates src="system"/>
        </trust-anchors>
    </base-config>
    <debug-overrides>
        <trust-anchors>
            <certificates src="system"/>
            <certificates src="user"/>
        </trust-anchors>
    </debug-overrides>
    <domain-config>
        <domain includeSubdomains="true">api.example.com</domain>
        <pin-set expiration="2026-12-31">
            <pin digest="SHA-256">AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=</pin>
            <pin digest="SHA-256">BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=</pin>
        </pin-set>
    </domain-config>
</network-security-config>
```

**OkHttpClient 单例封装**：
```java
public class SecureHttpClient {
    private static volatile OkHttpClient instance;

    public static OkHttpClient getClient() {
        if (instance == null) {
            synchronized (SecureHttpClient.class) {
                if (instance == null) {
                    instance = buildClient();
                }
            }
        }
        return instance;
    }

    private static OkHttpClient buildClient() {
        CertificatePinner pinner = new CertificatePinner.Builder()
            .add("api.example.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
            .add("api.example.com", "sha256/BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=")
            .build();

        return new OkHttpClient.Builder()
            .certificatePinner(pinner)
            .connectTimeout(10, TimeUnit.SECONDS)
            .readTimeout(15, TimeUnit.SECONDS)
            .addInterceptor(new HttpLoggingInterceptor()
                .setLevel(HttpLoggingInterceptor.Level.BASIC))   // 生产环境 BASIC
            .build();
    }
}
```

**代理检测**：
```java
public class ProxyDetector {
    public static boolean isProxySet(Context context) {
        String host = System.getProperty("http.proxyHost");
        String port = System.getProperty("http.proxyPort");
        if (host != null && !host.isEmpty() && port != null) {
            return true;
        }
        WifiManager wm = (WifiManager) context.getSystemService(Context.WIFI_SERVICE);
        ProxyInfo proxy = wm.getConnectionInfo().getHttpProxy();
        return proxy != null && proxy.getHost() != null;
    }
}

// Application.onCreate 中
if (ProxyDetector.isProxySet(this)) {
    Toast.makeText(this, "检测到代理,请关闭后重试", Toast.LENGTH_LONG).show();
}
```

**说明**：
- Pin 至少配 2 个（主 + 备），应对证书轮换
- Network Security Config 的 `debug-overrides` 仅 debuggable=true 时生效
- 代理检测只能提高门槛，不能替代 Pinning
- 应配合 [[8.5 应用加固基础概念|8.5 加固]] 防止 Pinning 被 Hook 绕过
</details>

---

### 15. ⭐⭐⭐ 代码分析与漏洞修复

下列代码存在多处安全漏洞，请逐一指出并给出修复方案：

```java
// 代码片段 1:登录处理
public class LoginManager {
    private static final String AES_KEY = "1234567890abcdef";   // ①

    public void login(String username, String password) {
        SharedPreferences sp = context.getSharedPreferences("user", MODE_PRIVATE);
        sp.edit().putString("password", password).apply();      // ②
        Log.d("LoginManager", "login: " + username + "/" + password);  // ③

        // 网络请求
        new Thread(() -> {
            try {
                URL url = new URL("http://api.example.com/login");  // ④
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                // ⑤ 未做任何证书校验
                // ...
            } catch (Exception e) {}
        }).start();
    }
}
```

```xml
<!-- 代码片段 2:AndroidManifest.xml -->
<application android:allowBackup="true">   <!-- ⑥ -->
    <activity android:name=".PaymentActivity" android:exported="true">  <!-- ⑦ -->
        <intent-filter>
            <action android:name="com.example.PAY"/>
        </intent-filter>
    </activity>
</application>
```

<details>
<summary>查看答案</summary>

**漏洞分析与修复**：

| 编号 | 漏洞 | 风险 | 修复方案 |
| ---- | ---- | ---- | -------- |
| ① | AES 密钥硬编码 | 反编译即可获取，等于没加密 | 用 Android Keystore 生成密钥，私钥不出 TEE |
| ② | 密码明文存 SharedPreferences | root/备份可读 | 绝不存密码；如必须校验，用 PBKDF2 加盐哈希后存 EncryptedSharedPreferences |
| ③ | 日志打印密码 | adb logcat 可读 | Release 移除日志；Token/密码打码打印 |
| ④ | HTTP 明文通信 | 流量可被嗅探 | 升级 HTTPS：`https://api.example.com/login` |
| ⑤ | 未做证书校验 | HTTPS 抓包工具可解密 | OkHttp 启用 CertificatePinner（SSL Pinning） |
| ⑥ | allowBackup=true | adb backup 可导出沙箱 | 改为 `allowBackup="false"` |
| ⑦ | PaymentActivity exported=true 无权限 | 恶意 APP 直接到支付页 | `exported="false"`；确需暴露配签名级权限 |

**修复后代码**：

```java
public class LoginManager {
    // ① 密钥改用 Keystore
    private SecretKey getKey() throws Exception {
        return KeystoreHelper.getOrCreateKey();
    }

    public void login(String username, String password) {
        // ② 密码不存本地,仅向服务端校验;若记住登录态,存 Token
        // ③ 日志打码
        LogUtil.d("LoginManager", "login: " + mask(username));

        new Thread(() -> {
            try {
                // ④ HTTPS
                URL url = new URL("https://api.example.com/login");
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                // ⑤ OkHttp 已配 CertificatePinner,见 SecureHttpClient
                // ... 提交 username + PBKDF2 哈希
            } catch (Exception e) {
                LogUtil.e("LoginManager", "login failed", e);
            }
        }).start();
    }
}
```

```xml
<application android:allowBackup="false"
             android:usesCleartextTraffic="false"
             android:networkSecurityConfig="@xml/network_security_config">
    <activity android:name=".PaymentActivity" android:exported="false"/>
</application>
```

**考核要点**：
- 能识别硬编码、明文存储、日志泄露、HTTP 明文、缺证书校验、allowBackup、组件暴露七类漏洞
- 修复方案对应 [[8.2 本地数据加密、敏感信息保护|8.2]]、[[8.3 HTTPS 防抓包、证书校验|8.3]]、[[8.4 权限最小化、恶意调用防范|8.4]] 三个小节
</details>

---

## 考点统计与复习建议

### 考点分布统计表

| 题号 | 题型 | 涉及考点 | 难度 | 对应小节 |
| ---- | ---- | -------- | ---- | -------- |
| 1 | 选择 | OWASP Mobile Top 10 | ⭐ | [[8.1 移动应用常见安全风险\|8.1]] |
| 2 | 选择 | Android Keystore | ⭐⭐ | [[8.2 本地数据加密、敏感信息保护\|8.2]] |
| 3 | 选择 | SSL Pinning 配置 | ⭐⭐ | [[8.3 HTTPS 防抓包、证书校验\|8.3]] |
| 4 | 选择 | exported 属性 | ⭐⭐ | [[8.4 权限最小化、恶意调用防范\|8.4]] |
| 5 | 选择 | 应用加固局限性 | ⭐⭐ | [[8.5 应用加固基础概念\|8.5]] |
| 6 | 填空 | 加固三大目标 | ⭐ | [[8.5 应用加固基础概念\|8.5]] |
| 7 | 填空 | AES/GCM 模式 | ⭐⭐ | [[8.2 本地数据加密、敏感信息保护\|8.2]] |
| 8 | 填空 | PendingIntent 标志 | ⭐⭐ | [[8.4 权限最小化、恶意调用防范\|8.4]] |
| 9 | 简答 | HTTPS 抓包与 SSL Pinning | ⭐⭐ | [[8.3 HTTPS 防抓包、证书校验\|8.3]] |
| 10 | 简答 | 本地存储方案对比 | ⭐⭐ | [[8.2 本地数据加密、敏感信息保护\|8.2]] |
| 11 | 简答 | 组件暴露三层防护 | ⭐⭐ | [[8.4 权限最小化、恶意调用防范\|8.4]] |
| 12 | 简答 | 加固五层手段 | ⭐⭐⭐ | [[8.5 应用加固基础概念\|8.5]] |
| 13 | 方案 | 本地数据加密选型 | ⭐⭐ | [[8.2 本地数据加密、敏感信息保护\|8.2]] |
| 14 | 方案 | 防抓包方案 + OkHttp 实现 | ⭐⭐⭐ | [[8.3 HTTPS 防抓包、证书校验\|8.3]] |
| 15 | 代码 | 漏洞分析与修复 | ⭐⭐⭐ | 综合 8.2/8.3/8.4 |

### 复习建议

> [!tip] 高效复习路线
> 1. **第一优先（必考）**：SSL Pinning 原理与 OkHttp CertificatePinner 实现（见第 3、9、14 题），能默写完整代码
> 2. **第二优先**：本地数据加密方案选型、Keystore、EncryptedSharedPreferences、SQLCipher（见第 2、7、10、13 题）
> 3. **第三优先**：组件暴露风险与三层防护（exported/自定义权限/签名权限）（见第 4、8、11 题）
> 4. **第四优先**：应用加固五层手段与局限（见第 5、6、12 题）
> 5. **综合应用**：漏洞分析题（第 15 题）覆盖 8.2/8.3/8.4 三小节，建议对照代码逐项排查
> 6. **动手实践**：在 Android Studio 中实现 OkHttp CertificatePinner、EncryptedSharedPreferences，并尝试在 root 设备上验证防护效果（仅限授权实验环境）

> [!warning] 安全实践提示
> - 所有抓包、root 读取、组件调用测试**仅限自有应用的授权实验环境**
> - 禁止对他人应用进行逆向、抓包、组件越权调用
> - 加固与防护手段用于保护自有产品，不可用于规避他人合法安全机制

## 章节导航

- 上级：[[MOC - 第8章|第8章 移动应用安全]]
- 上一章习题：[[MOC - 第7章习题|第7章习题]]
- 下一章习题：[[MOC - 第9章习题|第9章习题]]
- 课程总览：[[MOC - 移动互联网开发技术|移动互联网开发技术]]
