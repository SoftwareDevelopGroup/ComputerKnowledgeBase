---
domain: 网络与安全
subject: 信息安全技术
type: exercise
chapter: 第7章 安全通信协议
tags: [信息安全,习题,TLS握手,VPN,SSH,无线安全,协议分析]
prerequisites: ["计算机网络A"]
aliases: [第7章习题, 安全通信协议习题, Chapter 7 Exercises]
---

# MOC - 第7章习题 安全通信协议

> [!abstract] 本章习题概览
> 本章习题共 **15 题**，覆盖 [[7.1 HTTPS、TLS、SSL 握手流程|HTTPS/TLS 握手]]、[[7.2 VPN 技术：IPSec、SSL VPN|VPN/IPSec/SSL VPN]]、[[7.3 SSH 安全远程协议|SSH 协议]]、[[7.4 无线网络安全 WPA2、WPA3|无线安全 WPA2/WPA3]] 四个板块。题型分布：选择 5 题、填空 3 题、简答 4 题、协议分析 3 题。答案与详解折叠于 `<details>` 中，协议分析题给出完整流程说明。

---

## 一、选择题（5 题）

**1.** 关于 TLS 1.3 相对 TLS 1.2 的改进，下列说法**错误**的是（ ）

A. 握手从 2-RTT 降为 1-RTT，恢复场景支持 0-RTT
B. 强制使用前向保密（PFS），移除 RSA 密钥交换与静态 DH
C. 仅允许 AEAD 加密套件（如 AES-GCM、ChaCha20-Poly1305）
D. 保留 CBC 模式与压缩功能以兼容旧客户端

**2.** 关于前向保密（PFS），下列描述**正确**的是（ ）

A. PFS 要求服务端长期私钥每次会话都更换
B. 使用 RSA 密钥交换的 TLS 1.2 会话具备 PFS
C. PFS 依赖每次会话使用临时密钥对，长期私钥仅用于签名认证
D. 启用 PFS 后，攻击者囤积密文仍可在私钥泄露后批量解密

**3.** 关于 IPSec 的 AH 与 ESP，下列说法**正确**的是（ ）

A. AH 提供加密与完整性，ESP 仅提供完整性
B. ESP 提供加密与完整性，AH 仅提供完整性+认证不加密
C. AH 与 NAT-T 完全兼容，可穿越 NAT
D. 传输模式封装整个 IP 包，隧道模式仅保护载荷

**4.** 下列 SSH 认证方式中，**安全性最高且生产推荐**的是（ ）

A. 口令认证（PasswordAuthentication）
B. 键盘交互认证（KeyboardInteractive）
C. 公钥认证（PubkeyAuthentication）+ 私钥口令短语
D. 主机认证（HostbasedAuthentication）

**5.** 关于 WPA3 相对 WPA2 的改进，下列说法**错误**的是（ ）

A. 个人模式用 SAE 替代 PSK，抗离线字典攻击
B. 引入前向保密，口令破解后历史会话仍不可解
C. 企业模式提供 192 位安全套件
D. WPA3-Personal Transition 模式下，纯 WPA3 客户端仍可被降级攻击

<details>
<summary>选择题答案</summary>

1. **D**。TLS 1.3 移除了 CBC 模式与压缩功能（压缩会引入 CRIME/BREACH 攻击面），仅保留 AEAD；不保留这些特性以兼容旧客户端，旧客户端应使用 TLS 1.2。

2. **C**。PFS 依赖每次会话使用**临时密钥对**（如 ECDHE），会话结束后销毁；长期私钥只用于签名认证，不参与密钥传输。RSA 密钥交换中私钥用于解密 PreMasterSecret，无 PFS；启用 PFS 后即使私钥泄露，历史会话因临时密钥已销毁而不可解。

3. **B**。ESP 提供加密+完整性+认证，AH 仅提供完整性+认证不加密。AH 对 IP 头计算 MAC，NAT 修改源 IP 后 MAC 失败，与 NAT 不兼容；隧道模式封装整个 IP 包，传输模式仅保护载荷。

4. **C**。公钥认证的私钥不离机，无口令可被暴力破解，配合私钥口令短语形成"持有物+口令"双因素，安全性最高。口令认证抗暴力破解弱；键盘交互本身不必然更强；主机认证需严格主机信任，少用。

5. **D**。降级攻击针对的是**过渡模式下仍接受 WPA2-PSK 的客户端**，迫使它们走 PSK 路径再离线破解。**纯 WPA3 客户端**只支持 SAE，无法被降级到 PSK。因此应尽快淘汰 WPA2 客户端，切换纯 WPA3。

</details>

---

## 二、填空题（3 题）

**1.** TLS 1.2 完整握手中，客户端发出的第一条消息是 ______；服务端回应的密钥交换消息在 RSA 模式下省略，在 ECDHE 模式下是 ______；客户端通知对端"后续消息改用新协商参数加密"的消息是 ______，它本身**不加密**。握手最后双方互发的 ______ 用于校验整个握手过程的完整性。

**2.** IPSec 中 SA（安全关联）是 ______（单向/双向）的逻辑连接，由 ______、______、______ 三元组唯一标识；IKE 协商分两阶段，阶段 1 建立 ______ SA（管理通道），阶段 2 建立 ______ SA（加密实际流量）。

**3.** WPA2 的 4-way 握手用 ______（主密钥）、AP 随机数 ______、客户端随机数 ______、双方 ______ 地址共同派生成对临时密钥 ______；其中 ______ 模式下该主密钥由口令短语与 SSID 经 PBKDF2 派生，可被 ______ 攻击破解。

<details>
<summary>填空题答案</summary>

1. **ClientHello**；**ServerKeyExchange**；**ChangeCipherSpec**；**Finished**。

2. **单向**；**SPI（Security Parameter Index）**、**目的 IP**、**协议标识（AH/ESP）**；**IKE SA（ISAKMP SA）**；**IPSec SA（CHILD_SA）**。

3. **PMK（成对主密钥）**；**ANonce**；**SNonce**；**MAC**；**PTK（成对临时密钥）**；**PSK（个人模式）**；**离线字典**。

</details>

---

## 三、简答题（4 题）

**1.** 简述 TLS 1.2 完整握手的流程，并说明 Finished 消息为何能验证握手完整性。

**2.** 对比 IPSec 传输模式与隧道模式在封装结构、保护范围、典型场景上的差异，并说明 site-to-site VPN 为何首选隧道模式。

**3.** 简述 SSH2 的握手流程（版本协商 → 算法协商 → 密钥交换 → 认证 → 会话），并说明首次连接时主机指纹校验的作用。

**4.** 简述 WEP 的主要缺陷，以及 WPA2 通过哪些机制修复了这些缺陷。

<details>
<summary>简答题答案</summary>

**1. TLS 1.2 完整握手流程**

```
ClientHello → ServerHello → Certificate → ServerKeyExchange
→ ServerHelloDone → ClientKeyExchange → ChangeCipherSpec → Finished(C)
→ ChangeCipherSpec → Finished(S) → Application Data
```

- **ClientHello**：客户端发送支持的版本、随机数 $R_c$、Cipher Suites、SNI、扩展。
- **ServerHello**：服务端选定版本、随机数 $R_s$、Cipher Suite。
- **Certificate**：下发服务端证书链。
- **ServerKeyExchange**：ECDHE 模式下发送服务端临时公钥参数与签名（RSA 模式省略）。
- **ServerHelloDone**：通知服务端消息发送完毕。
- **ClientKeyExchange**：客户端回传密钥交换素材（RSA 加密 PreMasterSecret，或 ECDHE 临时公钥）。
- **ChangeCipherSpec**：通知对端后续消息加密。
- **Finished**：首条加密消息，双向互发。

Finished 能验证握手完整性的原因：Finished 的内容是对**全部握手消息**的哈希经 PRF 计算得到的验证值，并用新协商的密钥加密。任何中间人对 ClientHello/ServerHello/Certificate 的篡改都会导致双方计算的哈希不一致，Finished 校验失败触发 `bad_record_mac` 告警断连，从而抵抗 MITM。

**2. 传输模式 vs 隧道模式**

| 维度 | 传输模式 | 隧道模式 |
| ---- | -------- | -------- |
| 封装结构 | IP头 \| ESP头 \| 加密(TCP头+数据) \| ESP认证 | 新IP头 \| ESP头 \| 加密(原IP头+TCP头+数据) \| ESP认证 |
| 保护范围 | 仅 IP 载荷 | 整个原始 IP 包 |
| 源/目的 IP | 保留原 IP，可见 | 隐藏在内层，外层为网关 IP |
| 典型场景 | 主机↔主机 | 网关↔网关（site-to-site） |

site-to-site VPN 首选隧道模式的原因：分支内网主机（如 10.2.x.x）要与总部内网主机（如 10.1.x.x）通信，需经过两端公网网关。隧道模式把**整个内网 IP 包封装进新 IP 头**，外层源/目的为两端网关公网 IP，内网拓扑完全隐藏；且两端内网主机无需感知 IPSec，由网关代为加解密。传输模式要求通信两端本身参与 IPSec，不适合跨网关的内网互通。

**3. SSH2 握手流程**

1. **版本协商**：双方交换版本串（如 `SSH-2.0-OpenSSH_8.9p1`），确认都支持 SSH2，不兼容则断开。
2. **算法协商（KEXINIT）**：双方互发支持的密钥交换/加密/MAC/压缩算法列表，按客户端优先序取交集选定。
3. **密钥交换（DH/ECDH）**：客户端发 DH 公钥 $e$，服务端回 DH 公钥 $f$ + 主机公钥 + 对交换哈希 $H$ 的签名。双方用 $(e,f)$ 计算共享秘密 $K$，再用 $K$ 与 $H$ 派生会话密钥（加密 C→S、S→C，MAC C→S、S→C）。NEWKEYS 通知切换。
4. **用户认证**：客户端发 USERAUTH_REQUEST（公钥认证附签名），服务端校验返回 SUCCESS/FAILURE。
5. **会话/通道建立**：CHANNEL_OPEN 建立 session 通道，承载 Shell/SFTP/端口转发。

首次连接主机指纹校验的作用：客户端尚未保存服务端主机公钥时，提示用户确认指纹（公钥哈希），确认后写入 `~/.ssh/known_hosts`。后续连接若服务端公钥变化将告警"HOST KEY HAS CHANGED"，提示可能遭受中间人或服务器被替换。这是 SSH 抗 MITM 的关键——服务端在密钥交换中用主机私钥对 $H$ 签名，客户端用 known_hosts 中的公钥验证，确保对端确为该主机。

**4. WEP 缺陷与 WPA2 修复**

WEP 主要缺陷：
- IV 过短（24 bit），繁忙网络数小时即重复，相同 IV+密钥产生相同密钥流，可异或恢复明文。
- RC4 流加密弱点，IV 拼接进密钥参与 RC4 调度，FMS/KoreK 攻击利用弱 IV 快速恢复主密钥。
- 完整性用 CRC-32，线性可被篡改而不被发现。
- 无双向认证，无法识别伪造 AP。

WPA2 的修复：
- 用 **CCMP（AES-CCM）** 替换 RC4：AES 分组密码 + Counter 模式（机密性）+ CBC-MAC（完整性），消除流密码与 IV 重复问题。
- 完整性用 **CBC-MAC**，密码学安全，替代线性的 CRC-32。
- **48 位包序号**防重放，替代 24 位 IV。
- 通过 **4-way 握手**派生每会话独立 PTK，配合 PMK 实现密钥分层；企业模式 802.1X 提供每用户独立密钥与双向认证。
- 引入 PSK / 802.1X 两种模式，企业模式可撤销单用户。

</details>

---

## 四、协议分析题（3 题）

**1.（TLS 1.3 握手分析）** 阅读以下场景，回答问题：
> 某安全工程师用 Wireshark 抓取浏览器访问 `https://www.example.com` 的流量，观察到：TCP 三次握手后，客户端发出 ClientHello（含 `key_share` 扩展携带客户端 ECDHE 公钥、`supported_versions` 含 0x0304）；服务端回 ServerHello（`selected_version` 0x0304、`key_share` 携带服务端 ECDHE 公钥），随后报文全部显示为"Application Data"（TLS 1.3 Encrypted Extensions/Certificate/CertificateVerify/Finished 均被加密封装），最后客户端发一条 Finished，开始承载 HTTP。

> (1) 据此判断本次连接使用的 TLS 版本，并给出两条依据。
> (2) 完整写出 TLS 1.3 1-RTT 握手的消息顺序，标注哪条消息之后开始加密。
> (3) 若该连接后续恢复时启用 0-RTT，说明 0-RTT 的安全代价及应如何限制使用。
> (4) 工程师发现 ServerHello 之后抓包看不到 Certificate 明文，而 TLS 1.2 抓包可见明文证书。说明这一差异的安全意义。

<details>
<summary>协议分析1解答</summary>

**(1) 版本判断：TLS 1.3**

依据：
- ClientHello 的 `supported_versions` 扩展含 0x0304（=TLS 1.3），ServerHello 的 `selected_version` 为 0x0304。
- ServerHello 之后报文全部为"Application Data"封装，即握手消息被加密——这是 TLS 1.3 独有特性（TLS 1.2 中 Certificate 等仍明文）。

**(2) TLS 1.3 1-RTT 握手消息顺序**

```
C → S: ClientHello (版本, Rc, 套件, key_share=ECDHE公钥, SNI, supported_versions)
S → C: ServerHello (Rs, 选定套件, key_share=服务端ECDHE公钥, selected_version)
       ── 此后所有握手消息加密 ──
S → C: {EncryptedExtensions}
S → C: {Certificate}
S → C: {CertificateVerify} (用证书私钥对握手哈希签名)
S → C: {Finished}
C → S: {Finished}
C ↔ S: Application Data (1-RTT 后即可传输)
```

**加密起点**：ServerHello 之后所有消息（含 EncryptedExtensions、Certificate、CertificateVerify、Finished）均加密。握手从 1 个 RTT 后即可承载应用数据。

**(3) 0-RTT 的安全代价与限制**

0-RTT 基于 PSK（会话恢复票据），客户端在 ClientHello 中携带 Early Data。代价：
- **无前向保密**：Early Data 基于 PSK，PSK 泄露则历史 0-RTT 数据可解。
- **可被重放**：攻击者可截获 0-RTT 请求重新发送给服务器，服务器可能重复执行操作。

限制使用：
- 0-RTT 仅用于**幂等请求**（如 GET、HEAD），禁止承载改变状态的操作（支付、下单、POST 写入）。
- 服务端应维护 anti-replay 缓存或使用一次性票据，拒绝重复使用的 0-RTT 票据。
- 应用层可对 0-RTT 请求做幂等性校验。

**(4) 握手加密的安全意义**

TLS 1.2 中证书明文传输，被动观察者可得知服务端证书内容（域名、颁发者、有效期），用于流量分析、审查（如识别访问了哪些站点）。TLS 1.3 把 Certificate 等握手消息加密后：
- 证书内容、客户端 SNI（配合 ECH）对被动观察者不可见，**降低元数据泄露**。
- 中间人无法仅凭明文握手推断服务端身份，需主动介入才能探测，提升了隐私与抗审查能力。
- 同时 Finished 加密后，攻击者更难通过握手消息特征做指纹识别。

</details>

**2.（IPSec VPN 部署分析）** 阅读以下场景，回答问题：
> 某企业北京总部（内网 10.1.0.0/16）与上海分支（内网 10.2.0.0/16）通过 IPSec site-to-site VPN 互联。两端 VPN 网关公网 IP 分别为 1.1.1.1 与 2.2.2.2，使用 IKEv2 + ESP 隧道模式 + AES-256-GCM，NAT-T 已启用。捕获到 IKEv2 交换：① IKE_SA_INIT（SAi, KEi, Ni）↔（SAr, KEr, Nr）；② IKE_AUTH（加密）协商成功；③ 此后两端 10.1↔10.2 流量以 ESP 封装。

> (1) 说明 IKEv2 阶段 1（IKE_SA_INIT + IKE_AUTH）各自的作用与产物。
> (2) 画出隧道模式下，北京内网主机 10.1.5.10 访问上海内网主机 10.2.3.20 的 IP 包封装结构（含新 IP 头、ESP 头、原 IP 头、载荷、ESP 尾）。
> (3) 解释为何启用 NAT-T，并说明它如何封装 ESP。
> (4) 若安全策略要求"分支仅能访问总部 10.1.0.0/16 的 TCP 443 与 TCP 3306，不得访问其他端口与网段"，应在 IPSec 哪个机制中配置？给出 TSi/TSr 的大致内容。

<details>
<summary>协议分析2解答</summary>

**(1) IKEv2 阶段 1 的作用与产物**

| 交换 | 作用 | 产物 |
| ---- | ---- | ---- |
| IKE_SA_INIT | 明文协商 IKE 安全参数（加密/HMAC/DH 组/PRF），交换 DH 公钥与 nonce，建立后续 IKE_AUTH 加密所需的密钥材料 | 双向 **IKE SA**（管理通道），此后 IKE 消息加密 |
| IKE_AUTH | 在 IKE SA 保护下互相认证（证书/PSK），协商第一个 CHILD_SA（IPSec SA）的参数与流量选择器 TSi/TSr | **IPSec SA**（CHILD_SA），用于加密实际 ESP 流量 |

阶段 1 的核心目标是建立一个加密的管理通道并对等认证，为阶段 2（衍生 IPSec SA）提供安全基础。

**(2) 隧道模式封装结构**

```
新IP头       ESP头        加密(原IP头 + TCP头 + 应用数据)        ESP尾        ESP认证
src=1.1.1.1  SPI=...      原src=10.1.5.10                      padding      MIC
dst=2.2.2.2  Seq=...      原dst=10.2.3.20                      next=TCP
                          TCP头: dport=...                      ...
                          应用数据
```

说明：
- **新 IP 头**：src=1.1.1.1（北京网关），dst=2.2.2.2（上海网关），协议=50（ESP）。
- **ESP 头**：SPI 标识 SA，Seq 防重放。
- **加密载荷**：整个原始 IP 包（原 IP 头 + TCP 头 + 应用数据），原 IP 头 src=10.1.5.10、dst=10.2.3.20 被加密隐藏。
- **ESP 尾**：padding + next header（标识内层为 IPv4）。
- **ESP 认证**：AES-256-GCM 作为 AEAD 同时提供加密与完整性（GCM 模式下 MIC 即认证标签）。

**(3) NAT-T 的作用与封装**

启用 NAT-T 的原因：ESP 协议号 50 不基于 UDP/TCP 端口，NAT 设备无法像处理 TCP/UDP 那样维护端口映射表；且 ESP 的完整性校验覆盖 IP 头（部分场景），NAT 修改 IP 后校验失败。因此 ESP 默认无法穿越 NAT。

NAT-T 封装方式：在 ESP 报文外再封装一层 **UDP 头**（目的端口 4500），使 NAT 设备能像处理普通 UDP 一样维护映射：
```
新IP头 | UDP头(4500) | ESP头 | 加密(原IP包) | ESP尾 | ESP认证
```
双方在 IKE_SA_INIT 阶段通过 NATD 载荷探测路径是否存在 NAT，若存在则后续 ESP 用 UDP 4500 封装。

**(4) TSi/TSr 配置**

应在 IPSec 的**流量选择器（Traffic Selector, TS）** 中配置，它是 CHILD_SA 协商时 IKE_AUTH/CREATE_CHILD_SA 携带的字段，定义"哪些流量走这个 SA"。

配置为：
- **TSi（initiator→responder 方向）**：src=10.2.0.0/16，dst=10.1.0.0/16，协议=TCP，端口=443,3306
- **TSr（反向）**：src=10.1.0.0/16，dst=10.2.0.0/16，协议=TCP，端口=443,3306

匹配 TS 的流量进入 ESP 加密，不匹配的流量被丢弃（SPD discard）。这样分支仅能通过 VPN 访问总部 443 与 3306，其他端口与网段流量不会进入 SA，实现最小授权。注意 TS 是单向的，双向通信需双向都配置。

</details>

**3.（WPA2 4-way 握手与离线字典攻击分析）** 阅读以下场景，回答问题：
> 某渗透测试人员在授权范围内捕获某家庭 Wi-Fi（WPA2-PSK，SSID=HomeNet）的完整 4-way 握手报文，包括 EAPOL-Key Msg1~Msg4 与双方 MAC 地址。随后用 hashcat 离线破解 PSK，2 小时内得到口令 `password123`。

> (1) 完整写出 4-way 握手的四条消息及每条消息携带的关键内容，说明哪一步完成"客户端证明持有 PMK"。
> (2) 说明攻击者为何能离线破解 PSK，给出 PMK 与 PTK 的派生关系。
> (3) 该家庭用户将口令改为 16 位随机字符串是否能根本解决问题？为什么？
> (4) 若升级到 WPA3-Personal，攻击者捕获 SAE 交互后能否同样离线破解？说明 SAE 在抗字典攻击上的关键机制。

<details>
<summary>协议分析3解答</summary>

**(1) 4-way 握手四条消息**

| 消息 | 方向 | 关键内容 | 作用 |
| ---- | ---- | -------- | ---- |
| Msg1 | AP→STA | ANonce, AP MAC | 客户端据此可计算 PTK |
| Msg2 | STA→AP | SNonce, MIC | 客户端回传 SNonce，并用 PTK 计算 MIC，AP 校验 MIC |
| Msg3 | AP→STA | 加密的 GTK, MIC, 安装密钥指示 | AP 确认 PTK，下发组密钥 |
| Msg4 | STA→AP | MIC | 客户端确认，握手完成 |

**"客户端证明持有 PMK"的步骤**：Msg2 中客户端用派生的 PTK 计算 MIC，AP 用自己派生的 PTK 校验该 MIC。MIC 正确即证明客户端持有正确的 PMK（从而持有正确 PSK），因为只有正确 PMK 才能派生出正确 PTK 与 MIC。这是**隐式**的密钥证明，无需暴露 PMK 本身。

**(2) 离线破解 PSK 的原理**

攻击者能离线破解的根本原因：4-way 握手中 ANonce、SNonce、双方 MAC 地址均在空中明文传输，MIC 也在 Msg2/Msg3/Msg4 中可见。攻击者拥有这些材料后可**离线**重复以下过程：
1. 猜测 PSK 候选 $\text{PSK}'$；
2. 由 $\text{PSK}'$ 与 SSID 经 PBKDF2-HMAC-SHA1（4096 轮）派生 $\text{PMK}'$：
   $$ \text{PMK}' = \text{PBKDF2}(\text{PSK}',\ \text{SSID},\ 4096,\ 32) $$
3. 用 $\text{PMK}'$ + ANonce + SNonce + 双方 MAC 派生 $\text{PTK}'$：
   $$ \text{PTK}' = \text{PRF}(\text{PMK}',\ \text{ANonce},\ \text{SNonce},\ \text{AP\_MAC},\ \text{STA\_MAC}) $$
4. 用 $\text{PTK}'$ 计算 Msg2 的 MIC，与捕获的 MIC 比对；若一致则 $\text{PSK}'$ 即正确口令。

整个过程无需与 AP 在线交互，攻击者可利用 GPU 每秒尝试数百万候选，弱口令（如 `password123`）在字典中数分钟即被破解。

**(3) 长随机口令是否根本解决**

将口令改为 16 位随机字符串**显著提升抗破解能力**，使字典与暴力破解在计算上不可行（熵约 96 bit，远超当前 GPU 破解能力）。但这**不是根本解决**：
- 仍**无前向保密**：若 PSK 将来泄露（如用户分享给访客、设备丢失），过去捕获的握手仍可被解密。
- 仍依赖**口令强度**，一旦用户为方便改回弱口令即失效。
- 多设备共享同一 PSK，撤销困难，单设备泄露波及全网。

根本解决需协议层升级到 WPA3-SAE：抗离线字典攻击 + 前向保密，使口令强度不再是唯一安全支柱。

**(4) WPA3 SAE 能否被离线破解**

**不能**。SAE（Simultaneous Authentication of Equals）基于蜻蜓（Dragonfly）协议，其抗离线字典攻击的关键机制：

1. **强制在线交互**：SAE 协议要求双方基于口令派生群元素并交换 commit 消息（含临时公钥），口令验证必须**在线**与 AP 完成交互。攻击者捕获全部 SAE 报文后，无法仅凭这些报文离线验证候选口令——因为每个候选需配合 AP 持有的群元素秘密才能完成验证，而该秘密不在空中传输。
2. **每次会话引入临时密钥**：SAE 交换包含临时 DH 成分，每次会话产生不同 PMK，提供**前向保密**。即使将来口令被破解，过去会话的 PMK 因临时成分已销毁而不可恢复。
3. **AP 可限速/锁定**：在线尝试使 AP 能检测失败次数并限速或锁定，阻断暴力破解。

因此 WPA3-Personal 下，攻击者捕获 SAE 交互后无法离线穷举口令，必须在线与 AP 交互尝试，弱口令的破解成本从"分钟级离线"提升到"在线+限速+可被检测"。

</details>

---

## 考点统计表

| 知识点 | 涉及题号 | 题数 | 难度分布 |
| :--- | :--- | :---: | :--- |
| [[7.1 HTTPS、TLS、SSL 握手流程\|HTTPS/TLS 握手]] | 选择1、选择2、填空1、简答1、协议1 | 5 | 中-难 |
| [[7.2 VPN 技术：IPSec、SSL VPN\|VPN/IPSec/SSL VPN]] | 选择3、填空2、简答2、协议2 | 4 | 中-难 |
| [[7.3 SSH 安全远程协议\|SSH 协议]] | 选择4、简答3 | 2 | 中 |
| [[7.4 无线网络安全 WPA2、WPA3\|无线安全 WPA2/WPA3]] | 选择5、填空3、简答4、协议3 | 4 | 中-难 |
| 合计 | — | 15 | — |

> [!tip] 复习建议
> - **TLS 握手流程**必背 TLS 1.2 完整握手九步与 TLS 1.3 1-RTT 简化；区分 RSA 密钥交换（无 PFS）与 ECDHE（有 PFS），理解 TLS 1.3 强制 PFS 与握手加密的隐私意义。
> - **TLS 1.2 vs 1.3 对比**是高频选择/简答考点，重点记：1-RTT/0-RTT、仅 AEAD、移除 CBC/压缩/RSA 静态交换、握手消息加密。
> - **IPSec 协议栈**用"两个协议（AH/ESP）×两个模式（传输/隧道）×两个阶段（IKE SA/IPSec SA）"框架记忆；SA 单向、三元组标识；隧道模式封装结构必能画。
> - **IPSec vs SSL VPN 对比**：层次、客户端、可达范围、NAT 穿越是对比表重点；选型经验法则"分支用 IPSec、远程办公用 SSL VPN"。
> - **SSH 握手四步**（版本→算法→KEX→认证）必背；公钥认证优于口令认证的原因（私钥不离机）是简答高频；首次连接指纹校验抗 MITM 的原理要讲清。
> - **无线安全演进**用"WEP→WPA→WPA2→WPA3"四代表记忆，每代算法与缺陷对应：WEP（RC4+24bit IV）、WPA（TKIP 过渡）、WPA2（CCMP/AES）、WPA3（SAE+PFS）。
> - **4-way 握手**必能画时序图，记住 PMK→PTK 派生输入（PMK+ANonce+SNonce+MAC）；理解 WPA2 PSK 为何可离线破解、WPA3 SAE 为何不可。
> - **协议分析题**用"框架答题"：先列消息顺序→再解释关键字段作用→再分析安全性质→最后给限制/改进；务必把"为什么"讲透，而非只罗列"是什么"。

## 章节导航

> [!nav] 导航
> [[MOC - 第7章|第7章 知识点目录]] · [[MOC - 信息安全技术|课程总览]] · 上一章习题：[[MOC - 第6章习题|第6章 数据安全与存储安全习题]] · 下一章习题：[[MOC - 第8章习题|第8章 信息安全法律法规与运维规范习题]]
