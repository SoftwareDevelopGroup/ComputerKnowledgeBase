---
domain: 物理与电路
subject: 电路与模拟电子技术
type: exercise
chapter: 第3章 正弦交流稳态电路
tags: [电路,习题,相量法,阻抗,功率,谐振,三相电路]
prerequisites: ["第2章 直流电阻电路分析"]
aliases: [第3章习题, 交流电路习题]
---

# MOC - 第3章习题

> [!info] 本MOC定位
> 本文件汇集第3章"正弦交流稳态电路"习题 28 题，按填空、选择、计算、分析四类编排，覆盖**相量运算、阻抗等效、有功/无功/视在功率、功率因数提高、谐振频率与品质因数、三相功率**等核心考点。答案与完整解题步骤以 `<details>` 折叠，便于先做后对。计算题均给出物理量与 SI 单位。建议先回看 [[MOC - 第3章]] 的核心考点。

## 一、填空题（6 题）

### 1.
我国工频 $f=$ ______ Hz，角频率 $\omega=$ ______ rad/s；民用照明相电压 $U_P=$ ______ V，对应线电压 $U_L=$ ______ V。

<details><summary>答案</summary>

$f=50$ Hz，$\omega=2\pi f\approx314$ rad/s；$U_P=220$ V，$U_L=\sqrt3\times220\approx380$ V。

</details>

### 2.
正弦量 $u=311\sin(628t-45°)$ V 的有效值 $U=$ ______ V，频率 $f=$ ______ Hz，初相 $\psi_u=$ ______，对应有效值相量 $\dot U=$ ______。

<details><summary>答案</summary>

$U=311/\sqrt2=220$ V；$f=628/(2\pi)=100$ Hz；$\psi_u=-45°$；$\dot U=220\angle{-45°}$ V。

</details>

### 3.
感抗 $X_L=$ ______，容抗 $X_C=$ ______。$L=0.1$ H、$f=50$ Hz 时 $X_L=$ ______ $\Omega$；$C=10\,\mu$F、$f=50$ Hz 时 $X_C=$ ______ $\Omega$。

<details><summary>答案</summary>

$X_L=\omega L=2\pi f L$；$X_C=\dfrac{1}{\omega C}=\dfrac{1}{2\pi f C}$。
$X_L=2\pi\times50\times0.1=31.4\,\Omega$；$X_C=\dfrac{1}{2\pi\times50\times10\times10^{-6}}=318.3\,\Omega$。

</details>

### 4.
RLC 串联电路发生串联谐振的条件是 ______ ，谐振频率 $f_0=$ ______ 。谐振时电路阻抗 $Z_0=$ ______ ，电流 ______ (最大/最小)，电感两端电压与电源电压之比等于 ______ 。

<details><summary>答案</summary>

条件：$X_L=X_C$（即 $\omega L=1/(\omega C)$）；$f_0=\dfrac{1}{2\pi\sqrt{LC}}$；$Z_0=R$（最小）；电流最大；比值等于品质因数 $Q$。

</details>

### 5.
感性负载 $\cos\varphi_1$ 提高到 $\cos\varphi_2$ 应并联 ______ (电容/电感)，所需容量 $C=$ ______ 。并联补偿过程中 ______ 与 ______ 保持不变。

<details><summary>答案</summary>

并联电容；$C=\dfrac{P}{\omega U^2}(\tan\varphi_1-\tan\varphi_2)$。有功 $P$ 与端电压 $U$ 保持不变。

</details>

### 6.
对称三相电路 Y 接时 $U_L=$ ______ $U_P$，$I_L=$ ______ $I_P$；△接时 $U_L=$ ______ $U_P$，$I_L=$ ______ $I_P$；对称三相总有功 $P=$ ______ 。

<details><summary>答案</summary>

Y 接：$U_L=\sqrt3\,U_P$，$I_L=I_P$；△接：$U_L=U_P$，$I_L=\sqrt3\,I_P$；$P=\sqrt3\,U_L I_L\cos\varphi$。

</details>

## 二、选择题（6 题）

### 7.
下列关于相量法的说法，错误的是（　）。
A. 相量法只适用于同频率正弦量
B. 相量法的核心是省略旋转因子 $e^{j\omega t}$
C. 相量法可处理非线性电路
D. 相量法把微分方程变为复数代数方程

<details><summary>答案</summary>

**C**。相量法仅适用于**线性**电路。非线性电路不满足叠加定理，不能用相量法。

</details>

### 8.
某负载 $\dot U$ 与 $\dot I$ 取关联方向，测得 $\dot U=100\angle30°$ V，$\dot I=5\angle{-30°}$ A，则该负载呈（　）。
A. 纯阻性　B. 感性　C. 容性　D. 无法判定

<details><summary>答案</summary>

**B**。$\varphi=\psi_u-\psi_i=30°-(-30°)=60°>0$，电压超前电流，呈感性。阻抗 $Z=\dot U/\dot I=20\angle60°\,\Omega$。

</details>

### 9.
RLC 串联电路中 $U_R=3$ V，$U_L=6$ V，$U_C=10$ V，则总电压 $U$ 为（　）V。
A. 19　B. $\sqrt{9+36+100}$　C. 5　D. 13

<details><summary>答案</summary>

**C**。$\dot U=\dot U_R+\dot U_L+\dot U_C$，模 $U=\sqrt{U_R^2+(U_L-U_C)^2}=\sqrt{3^2+(6-10)^2}=\sqrt{9+16}=5$ V。注意不是简单相加，选 C 而非 B（B 错把三者平方和开方）。

</details>

### 10.
提高功率因数的正确方法是（　）。
A. 串联电感　B. 串联电容
C. 并联电容　D. 增大负载电阻

<details><summary>答案</summary>

**C**。感性负载并联电容，电容发出无功补偿电感吸收的无功，使总无功减小、$\cos\varphi$ 升高，且不影响负载本身的电压电流。

</details>

### 11.
RLC 串联电路谐振时，下列说法正确的是（　）。
A. 阻抗最大　B. 电流最小　C. $U_L$ 可能远大于电源电压　D. 电路呈容性

<details><summary>答案</summary>

**C**。串联谐振阻抗最小（$Z=R$）、电流最大、呈阻性；过电压使 $U_L=QU$ 远大于电源电压（$Q\gg1$ 时）。故选 C。

</details>

### 12.
对称三相电源 △ 接，若一相绕组接反，则（　）。
A. 对外无影响　B. 回路内出现两倍相电压的环流
C. 输出电压升高　D. 中线电流增大

<details><summary>答案</summary>

**B**。△ 接要求 $\dot U_A+\dot U_B+\dot U_C=0$；一相反接后三者之和为 $2\dot U$（两倍相电压），绕组阻抗很小，回路内出现大环流，可能烧毁绕组。故 △ 接电源必须严格核对极性。

</details>

## 三、计算题（14 题）

### 13.（相量加减）
已知 $i_1=10\sqrt2\sin(314t+30°)$ A，$i_2=10\sqrt2\sin(314t-90°)$ A。求 $i_1+i_2$ 的瞬时表达式并绘相量图说明。

<details><summary>答案</summary>

$\dot I_1=10\angle30°=8.66+j5$；$\dot I_2=10\angle{-90°}=-j10$。
$\dot I=\dot I_1+\dot I_2=8.66-j5=10\angle{-30°}$ A。
故 $i(t)=10\sqrt2\sin(314t-30°)$ A。
相量图中 $\dot I_1$、$\dot I_2$ 夹角 $120°$，由几何关系合成模 $|\dot I|=10$ A，幅角 $-30°$。

</details>

### 14.（相量与瞬时值互化）
正弦电流 $i=14.14\sin(314t+60°)$ A。写出有效值相量 $\dot I$；若频率变为原来的两倍但相量不变，写出新的瞬时式。

<details><summary>答案</summary>

有效值 $I=14.14/\sqrt2=10$ A，$\dot I=10\angle60°$ A。
角频率加倍 $\omega'=628$ rad/s 时：$i'(t)=10\sqrt2\sin(628t+60°)$ A。

</details>

### 15.（RL 串联）
RL 串联电路 $R=6\,\Omega$，$X_L=8\,\Omega$，接 $u=100\sqrt2\sin\omega t$ V。求 $Z$、$\dot I$、$i(t)$、$P$、$Q$、$\cos\varphi$。

<details><summary>答案</summary>

$Z=R+jX_L=6+j8=10\angle53.1°\,\Omega$。
$\dot I=\dot U/Z=100\angle0°/10\angle53.1°=10\angle{-53.1°}$ A；$i(t)=10\sqrt2\sin(\omega t-53.1°)$ A。
$P=UI\cos\varphi=100\times10\times\cos53.1°=600$ W（或 $I^2R=600$ W）。
$Q=UI\sin\varphi=100\times10\times\sin53.1°=800$ var。
$\cos\varphi=\cos53.1°=0.6$（感性）。

</details>

### 16.（RC 串联）
RC 串联 $R=40\,\Omega$，$C=79.6\,\mu$F，接 $u=100\sqrt2\sin(314t)$ V。求 $Z$、$\dot I$、$P$、$Q$ 并判断电路性质。

<details><summary>答案</summary>

$X_C=1/(\omega C)=1/(314\times79.6\times10^{-6})=40\,\Omega$。
$Z=R-jX_C=40-j40=56.57\angle{-45°}\,\Omega$（容性）。
$\dot I=100/56.57\angle45°=1.768\angle45°$ A。
$P=UI\cos\varphi=100\times1.768\times0.707=125$ W；$Q=UI\sin\varphi=-125$ var（容性无功为负）。

</details>

### 17.（RLC 串联综合）
RLC 串联电路 $R=30\,\Omega$，$L=127$ mH，$C=40\,\mu$F，接 $u=220\sqrt2\sin(314t)$ V。求 $Z$、$\dot I$、$P$、$Q$、$S$、$\cos\varphi$ 并指出电路性质。

<details><summary>答案</summary>

$X_L=314\times0.127=39.9\approx40\,\Omega$；$X_C=1/(314\times40\times10^{-6})=79.6\approx80\,\Omega$。
$Z=30+j(40-80)=30-j40=50\angle{-53.1°}\,\Omega$（容性）。
$\dot I=220\angle0°/50\angle{-53.1°}=4.4\angle53.1°$ A。
$P=220\times4.4\times\cos(-53.1°)=580.8$ W（或 $I^2R=4.4^2\times30=580.8$ W）。
$Q=220\times4.4\times\sin(-53.1°)=-774.4$ var。
$S=UI=968$ VA。$\cos\varphi=0.6$（容性，电流超前电压）。

</details>

### 18.（阻抗并联）
两支路并联：$Z_1=6+j8=10\angle53.1°\,\Omega$，$Z_2=-j10\,\Omega$，端口 $\dot U=100\angle0°$ V。求 $Z_{\text{eq}}$、$\dot I$、$\dot I_1$、$\dot I_2$。

<details><summary>答案</summary>

$Z_{\text{eq}}=\dfrac{Z_1 Z_2}{Z_1+Z_2}=\dfrac{10\angle53.1°\times10\angle{-90°}}{(6+j8)+(-j10)}=\dfrac{100\angle{-36.9°}}{6-j2}=\dfrac{100\angle{-36.9°}}{6.325\angle{-18.4°}}=15.81\angle{-18.5°}\,\Omega$。
$\dot I=100/15.81\angle{-18.5°}=6.33\angle18.5°$ A。
$\dot I_1=\dot U/Z_1=100/10\angle53.1°=10\angle{-53.1°}$ A。
$\dot I_2=\dot U/Z_2=100/(-j10)=10\angle90°$ A。
校验 KCL：$\dot I_1+\dot I_2=6-j8+j10=6+j2=6.33\angle18.4°\approx\dot I$ ✓。

</details>

### 19.（功率因数提高）
感性负载 $P=20$ kW，$\cos\varphi_1=0.6$（滞后），$U=380$ V，$f=50$ Hz。将 $\cos\varphi$ 提高到 0.9（滞后），求并联电容 $C$ 及补偿前后线路电流。

<details><summary>答案</summary>

$\varphi_1=\arccos0.6=53.13°$，$\tan\varphi_1=1.333$；$\varphi_2=\arccos0.9=25.84°$，$\tan\varphi_2=0.484$。
$C=\dfrac{P}{\omega U^2}(\tan\varphi_1-\tan\varphi_2)=\dfrac{2\times10^4}{314\times380^2}(1.333-0.484)=\dfrac{2\times10^4\times0.849}{4.53\times10^7}=3.75\times10^{-4}$ F $=375\,\mu$F。
$I_1=P/(U\cos\varphi_1)=2\times10^4/(380\times0.6)=87.7$ A。
$I_2=P/(U\cos\varphi_2)=2\times10^4/(380\times0.9)=58.5$ A。
电流下降约 33.3%，线路损耗 $I^2R$ 下降约 56%。

</details>

### 20.（复功率守恒）
某负载 $\dot U=220\angle0°$ V，$\dot I=10\angle{-30°}$ A（关联方向）。求 $\tilde S,P,Q,S,\cos\varphi$。

<details><summary>答案</summary>

$\tilde S=\dot U\dot I^{\,*}=220\angle0°\times10\angle30°=2200\angle30°=1905.3+j1100$ VA。
$P=1905.3$ W，$Q=1100$ var（感性），$S=2200$ VA，$\cos\varphi=\cos30°=0.866$。
校验：$P=UI\cos\varphi=220\times10\times0.866=1905$ W ✓。

</details>

### 21.（串联谐振）
RLC 串联电路 $R=10\,\Omega$，$L=10$ mH，$C=1\,\mu$F。求谐振频率 $f_0$、品质因数 $Q$、谐振时电流 $I_0$ 与 $U_L$（设 $U=1$ V）。

<details><summary>答案</summary>

$f_0=\dfrac{1}{2\pi\sqrt{LC}}=\dfrac{1}{2\pi\sqrt{10^{-2}\times10^{-6}}}=\dfrac{1}{2\pi\times10^{-4}}=1591.5$ Hz。
$\omega_0=2\pi f_0=10^4$ rad/s。
$Q=\omega_0 L/R=10^4\times10^{-2}/10=10$。
$I_0=U/R=1/10=0.1$ A。
$U_L=Q\cdot U=10\times1=10$ V（电源仅 1 V，电感两端 10 V，过电压 10 倍）。

</details>

### 22.（谐振调谐）
收音机调谐回路 $L=300\,\mu$H，$R=20\,\Omega$。欲接收 $f_0=1000$ kHz 电台，求电容 $C$ 与通频带 $B$。

<details><summary>答案</summary>

$C=\dfrac{1}{(2\pi f_0)^2 L}=\dfrac{1}{(2\pi\times10^6)^2\times300\times10^{-6}}=\dfrac{1}{3.947\times10^{13}\times3\times10^{-4}}=\dfrac{1}{1.184\times10^{10}}=8.45\times10^{-11}$ F $=84.5$ pF。
$Q=\omega_0 L/R=2\pi\times10^6\times300\times10^{-6}/20=1884/20=94.2$。
$B=f_0/Q=10^6/94.2=10.6$ kHz。

</details>

### 23.（并联谐振）
RLC 并联 $R=10$ k$\Omega$，$L=1$ mH，$C=0.1\,\mu$F。求 $f_0$、$Q$、谐振阻抗、谐振时 $I$ 与 $I_L$（设 $U=10$ V）。

<details><summary>答案</summary>

$f_0=\dfrac{1}{2\pi\sqrt{LC}}=\dfrac{1}{2\pi\sqrt{10^{-3}\times10^{-7}}}=15.92$ kHz。
$\omega_0=10^5$ rad/s。
$Q=R/(\omega_0 L)=10000/(10^5\times10^{-3})=100$。
谐振阻抗 $Z_0=R=10$ k$\Omega$（最大）。
$I_0=U/R=10/10000=1$ mA。
$I_L=U/(\omega_0 L)=10/(10^5\times10^{-3})=10/100=0.1$ A $=100$ mA（过电流，为电源电流的 100 倍）。

</details>

### 24.（对称 Y-Y 三相电路）
对称三相电源 Y 接，相电压 $U_P=220$ V。负载 Y 接每相 $Z=8+j6=10\angle36.9°\,\Omega$。求线电流、$\dot I_A,\dot I_B,\dot I_C$ 及三相总有功。

<details><summary>答案</summary>

$I_L=I_P=U_P/|Z|=220/10=22$ A。
$\dot I_A=22\angle{-36.9°}$ A；$\dot I_B=22\angle{-156.9°}$ A；$\dot I_C=22\angle83.1°$ A。
$P=\sqrt3 U_L I_L\cos\varphi=\sqrt3\times380\times22\times0.8=11.58$ kW。
校验 $P=3I^2 R=3\times22^2\times8=11.62$ kW ✓。

</details>

### 25.（对称 △ 接负载）
对称三相电源 $U_L=380$ V，负载 △ 接每相 $Z=10\angle30°\,\Omega$。求相电流、线电流、三相总有功与无功。

<details><summary>答案</summary>

$U_P=U_L=380$ V；$I_P=U_P/|Z|=380/10=38$ A。
$I_L=\sqrt3 I_P=\sqrt3\times38=65.8$ A。
$\cos\varphi=\cos30°=0.866$，$\sin\varphi=0.5$。
$P=\sqrt3 U_L I_L\cos\varphi=\sqrt3\times380\times65.8\times0.866=37.5$ kW。
$Q=\sqrt3 U_L I_L\sin\varphi=\sqrt3\times380\times65.8\times0.5=21.65$ kvar。

</details>

### 26.（Y-△ 等效变换）
对称电源 $U_L=380$ V，负载每相 $Z_\triangle=30+j40=50\angle53.1°\,\Omega$，△ 接。改为 Y 接且保持对外等效，求 Y 接每相阻抗 $Z_Y$ 与线电流。

<details><summary>答案</summary>

$Z_Y=Z_\triangle/3=(30+j40)/3=10+j13.33=16.67\angle53.1°\,\Omega$。
Y 接 $U_P=U_L/\sqrt3=220$ V。
$I_L=I_P=U_P/|Z_Y|=220/16.67=13.2$ A。
（注：等效后端口电流、功率不变；可校验原 △ 接 $I_L=\sqrt3\times380/50=13.16$ A，一致 ✓。）

</details>

## 四、分析题（2 题）

### 27.（相量图与电路性质）
某二端网络端口电压 $u=100\sqrt2\sin\omega t$ V，电流 $i=10\sqrt2\sin(\omega t+60°)$ A（关联方向）。要求：
(1) 写出 $\dot U,\dot I$，求 $Z$ 与 $\varphi$；
(2) 画相量图（以 $\dot U$ 为参考）说明电压电流相位关系；
(3) 判断电路性质，指出该电路可能由哪些元件构成。

<details><summary>答案</summary>

(1) $\dot U=100\angle0°$ V，$\dot I=10\angle60°$ A。$\varphi=\psi_u-\psi_i=0-60°=-60°$。
$Z=\dot U/\dot I=10\angle{-60°}=5-j8.66\,\Omega$。

(2) 相量图：$\dot U$ 沿正实轴水平向右；$\dot I$ 在其上方逆时针偏 $60°$（电流超前电压 $60°$）。

(3) 电流超前电压 $60°$，呈容性。可由 RC 串联构成：$R=5\,\Omega$，$X_C=8.66\,\Omega$（$C=1/(\omega\times8.66)$）。

</details>

### 28.（功率因数补偿的工程分析）
某工厂负载 $P=100$ kW，$\cos\varphi_1=0.7$（滞后），$U=380$ V，$f=50$ Hz。
(1) 说明为何不能采用串联电容提高 $\cos\varphi$；
(2) 现欲将 $\cos\varphi_2$ 提高到 0.95，计算应并联的电容；
(3) 分析若过补偿（补偿到容性）会有哪些不利后果。

<details><summary>答案</summary>

(1) 串联电容会改变负载端电压，使负载工作点偏离额定；且串联谐振可能引起过电压。并联电容不影响负载两端电压（$U$ 不变），仅补偿无功，是标准做法。

(2) $\tan\varphi_1=\tan(\arccos0.7)=1.020$；$\tan\varphi_2=\tan(\arccos0.95)=0.329$。
$C=\dfrac{P}{\omega U^2}(\tan\varphi_1-\tan\varphi_2)=\dfrac{10^5}{314\times380^2}(1.020-0.329)=\dfrac{10^5\times0.691}{4.53\times10^7}=1.525\times10^{-3}$ F $\approx1525\,\mu$F。

(3) 过补偿（总电路呈容性）的后果：① 线路电流不降反升，铜耗增加；② 容性无功向系统倒送，可能引起电网电压升高（容升效应），危害绝缘；③ 增加电容投资与运行维护成本。故工程上多补偿到 0.9~0.95 滞后即可。

</details>

## 考点统计表

| 考点 | 题号 | 题数 | 权重 |
| ---- | ---- | ---- | ---- |
| 正弦量三要素、有效值、相量变换 | 1, 2, 7, 13, 14 | 5 | ★★★ |
| 阻抗与导纳、串并联等效 | 3, 9, 15, 16, 17, 18, 26 | 7 | ★★★★ |
| R/L/C 相量模型与电路性质判断 | 8, 16, 27 | 3 | ★★★ |
| 有功/无功/视在/复功率 | 15, 17, 20 | 3 | ★★★★ |
| 功率因数及其提高 | 5, 10, 19, 28 | 4 | ★★★★★ |
| 串联谐振频率与品质因数 | 4, 11, 21, 22 | 4 | ★★★★ |
| 并联谐振 | 23 | 1 | ★★★ |
| 三相 Y/△ 连接与功率 | 6, 12, 24, 25 | 4 | ★★★★ |
| 相量图与综合分析 | 27, 28 | 2 | ★★★ |
| **合计** | 1—28 | 28 | — |

> [!tip] 复习建议
> - 相量法是核心工具，务必熟练复数代数/极坐标互化（题 13、14、27）；
> - 功率因数提高是重点工程应用（题 5、10、19、28），掌握 $C=\dfrac{P}{\omega U^2}(\tan\varphi_1-\tan\varphi_2)$ 及"过补偿避免"；
> - 谐振重点在 $f_0$、$Q$、过电压/过电流三要素（题 21—23）；
> - 三相电路用一相法化简，统一公式 $P=\sqrt3 U_L I_L\cos\varphi$（题 24—26）。

## 章节导航

- 本章首页：[[MOC - 第3章]]
- 知识点：
  - [[3.1 正弦量、相量表示法]]
  - [[3.2 RLC 元件相量模型、阻抗与导纳]]
  - [[3.3 正弦电路功率：有功、无功、视在功率]]
  - [[3.4 串联谐振、并联谐振]]
  - [[3.5 三相交流电路基础]]
- 上一章习题：[[MOC - 第2章习题]]
- 下一章习题：[[MOC - 第4章习题]]

## 相关标签

#电路 #习题 #相量法 #阻抗 #功率 #谐振 #三相电路
