---
domain: 物理与电路
subject: 大学物理B
type: exercise
chapter: 第8章 电磁感应与电磁场
tags: [大学物理,习题,法拉第定律,动生电动势,自感互感,麦克斯韦方程组]
prerequisites: ["第7章 恒定磁场"]
aliases: [第8章习题, 电磁感应习题]
---

# MOC - 第8章习题 电磁感应与电磁场

> [!abstract] 本章习题概览
> 本章习题共 **26 题**，覆盖 [[8.1 法拉第电磁感应定律|法拉第定律与楞次定律]]、[[8.2 动生电动势、感生电动势|动生/感生电动势与涡旋电场]]、[[8.3 自感、互感、磁场能量|自感互感与磁场能量]]、[[8.4 麦克斯韦方程组简介|位移电流与麦克斯韦方程组]] 四个知识板块。题型分布：填空 6 题、选择 6 题、计算 10 题、证明/讨论 4 题。答案与详解折叠于 `<details>` 中，建议先独立作答再核对。所有物理量采用 SI 单位。

---

## 一、填空题（6 题）

**1.** 法拉第电磁感应定律的数学表达式为 $\varepsilon=$ ______，其中负号是 ______ 定律的数学体现，反映了 ______ 守恒定律。

**2.** 一根长 $l=0.40\,\text{m}$ 的直导体棒在 $B=0.50\,\text{T}$ 的均匀磁场中以 $v=2.0\,\text{m/s}$ 速度运动，已知 $\vec B\perp\vec v\perp\vec l$，则棒两端的动生电动势大小为 ______ V。

**3.** 长直螺线管内部磁感应强度 $B$ 随时间均匀增大，变化率 $\dfrac{\mathrm dB}{\mathrm dt}=k$。在管内距轴 $r$ 处的涡旋电场大小为 $E_v=$ ______，方向沿 ______ 方向。

**4.** 一自感线圈的自感系数 $L=0.10\,\text{H}$，通有 $I=2.0\,\text{A}$ 的电流，线圈中储存的磁场能量 $W_m=$ ______ J；若电流在 $0.020\,\text{s}$ 内均匀降为零，则自感电动势大小为 ______ V。

**5.** RL 串联电路中 $R=5.0\,\Omega$、$L=0.20\,\text{H}$，其时间常数 $\tau=$ ______ s；接通直流电源后电流达到稳态值 $I_\infty$ 的 $63.2\%$ 需经过时间 ______ s。

**6.** 平行板电容器极板半径 $R=0.040\,\text{m}$，充电时极板间电场变化率 $\dfrac{\mathrm dE}{\mathrm dt}=2.0\times10^{12}\,\text{V/(m·s)}$，则极板间位移电流 $I_d=$ ______ A（取 $\varepsilon_0=8.85\times10^{-12}\,\text{F/m}$）。

<details>
<summary>填空题答案</summary>

1. $\varepsilon=-\dfrac{\mathrm d\Phi}{\mathrm dt}$（多匝为 $-N\dfrac{\mathrm d\Phi}{\mathrm dt}$ 或 $-\dfrac{\mathrm d\Psi}{\mathrm dt}$）；负号是**楞次**定律的数学体现，反映**能量**守恒定律。
2. $\varepsilon=Bvl=0.50\times2.0\times0.40=0.40\,\text{V}$。
3. $E_v=\dfrac{r}{2}\dfrac{\mathrm dB}{\mathrm dt}=\dfrac{kr}{2}$；方向沿**切向**（绕轴同心圆方向）。
4. $W_m=\tfrac12 LI^2=\tfrac12\times0.10\times2.0^2=0.20\,\text{J}$；$\varepsilon_L=L\dfrac{\mathrm dI}{\mathrm dt}=0.10\times\dfrac{2.0}{0.020}=10\,\text{V}$。
5. $\tau=\dfrac{L}{R}=\dfrac{0.20}{5.0}=0.040\,\text{s}$；达到 $63.2\%$（$=1-e^{-1}$）正好经过 $\tau=0.040\,\text{s}$。
6. $I_d=\varepsilon_0\pi R^2\dfrac{\mathrm dE}{\mathrm dt}=8.85\times10^{-12}\times\pi\times0.040^2\times2.0\times10^{12}\approx 8.90\times10^{-2}\,\text{A}$。

</details>

---

## 二、选择题（6 题）

**1.** 关于法拉第电磁感应定律，下列说法正确的是（ ）
A. 只要闭合回路处于磁场中就会产生感应电动势
B. 感应电动势与穿过回路的磁通量成正比
C. 感应电动势与穿过回路的磁通量的变化率成正比
D. 磁通量越大，感应电动势越大

**2.** 楞次定律说明感应电流的磁场总是（ ）
A. 与原磁场方向相同
B. 与原磁场方向相反
C. 阻碍引起感应电流的磁通量变化
D. 与原磁场方向垂直

**3.** 关于动生电动势 $\varepsilon=\int(\vec v\times\vec B)\cdot\mathrm d\vec l$，下列正确的是（ ）
A. 其非静电力来源于洛伦兹力
B. 洛伦兹力对单个电荷做正功
C. 仅当导体在均匀磁场中平动时才成立
D. 与导体运动速度无关

**4.** 关于涡旋电场（感生电场），下列说法正确的是（ ）
A. 涡旋电场由静止电荷产生
B. 涡旋电场是保守场，可定义电势
C. 涡旋电场线是闭合曲线
D. 涡旋电场的高斯定理为 $\oint\vec E_v\cdot\mathrm d\vec S\ne 0$

**5.** 长直螺线管内部磁场随时间增大时，管内一点激发的涡旋电场（ ）
A. 方向沿轴向
B. 方向沿径向
C. 方向沿切向，且与磁场增大方向配套为顺时针（从磁场方向看）
D. 大小与到轴距离的平方成正比

**6.** 麦克斯韦引入位移电流假设是为了解决（ ）
A. 法拉第定律在非稳恒条件下的矛盾
B. 安培环路定理在非稳恒条件下的矛盾
C. 高斯定理不适用于磁场的问题
D. 库仑定律在运动电荷情形下的修正

<details>
<summary>选择题答案</summary>

1. **C**。感应电动势正比于磁通量的**变化率**，与磁通量本身无关。
2. **C**。楞次定律核心是"阻碍磁通量变化"，方向随增减而变。
3. **A**。动生电动势非静电力即洛伦兹力 $\vec f=q\vec v\times\vec B$；洛伦兹力对电荷总功为零（B 错）；公式适用于任意运动（C 错）；与速度明显相关（D 错）。
4. **C**。涡旋电场无源有旋，电场线闭合；由变化磁场产生，非保守，不能定义电势（B 错）；高斯定理 $\oint\vec E_v\cdot\mathrm d\vec S=0$（D 错）。
5. **C**。涡旋电场沿切向；$B$ 增大时由楞次定律感应电场驱动电流产生反向磁场，从 $B$ 方向看为顺时针；$E_v\propto r$（D 错）。
6. **B**。位移电流修补安培环路定理在电容器充电等暂态过程中的矛盾。

</details>

---

## 三、计算题（10 题）

**1.（法拉第定律应用）** 半径 $R=0.10\,\text{m}$ 的圆形线圈共 $N=100$ 匝，置于均匀磁场中，磁场方向垂直线圈平面。磁感应强度 $B=0.30+0.15t$（SI）。求线圈中的感应电动势大小，并判断 $t>0$ 时感应电流方向。

<details>
<summary>解答</summary>

取面法向与 $\vec B$ 同向。单匝磁通 $\Phi=B\pi R^2$，
$$\varepsilon=-N\frac{\mathrm d\Phi}{\mathrm dt}=-N\pi R^2\frac{\mathrm dB}{\mathrm dt}=-100\times\pi\times0.10^2\times0.15\approx -0.471\,\text{V}$$
大小 $|\varepsilon|\approx 0.471\,\text{V}$。

$\dfrac{\mathrm dB}{\mathrm dt}=0.15>0$，磁通量增加，由楞次定律感应电流磁场反抗 $\vec B$，故感应电流方向（从 $\vec B$ 方向看）为顺时针。

**单位检验**：$\text{T}\cdot\text{m}^2/\text{s}=\text{Wb/s}=\text{V}$，正确。

</details>

**2.（动生电动势——平动切割）** 长 $l=0.50\,\text{m}$ 的金属棒在 $B=0.40\,\text{T}$ 的均匀磁场中以 $v=3.0\,\text{m/s}$ 速度垂直切割磁感线运动（$\vec B\perp\vec v\perp\vec l$）。求棒两端的电势差及哪端电势高。

<details>
<summary>解答</summary>

$$\varepsilon=Bvl=0.40\times3.0\times0.50=0.60\,\text{V}$$

由 $\vec v\times\vec B$ 方向（洛伦兹力作用于正电荷的方向）判断，正电荷积累的一端电势高。具体哪端取决于 $\vec v$、$\vec B$、$\vec l$ 的几何配置：取 $\vec v$ 沿 $+\hat x$、$\vec B$ 沿 $+\hat z$，则 $\vec v\times\vec B=+vB\,\hat y$，正电荷推向 $+\hat y$ 端，该端电势高。

**单位检验**：$\text{T}\cdot\text{m/s}\cdot\text{m}=\text{V}$，正确。

</details>

**3.（动生电动势——转动）** 长 $l=0.40\,\text{m}$ 的导体棒在 $B=0.50\,\text{T}$ 的均匀磁场中绕一端以 $\omega=30\,\text{rad/s}$ 转动，$\vec B\perp$ 转动平面。求棒两端的动生电动势。

<details>
<summary>解答</summary>

距轴 $r$ 处线速度 $v=\omega r$，
$$\varepsilon=\int_0^l B\omega r\,\mathrm dr=\frac12 B\omega l^2=\frac12\times0.50\times30\times0.40^2=1.2\,\text{V}$$

自由端（线速度大的一端）电势高。

**单位检验**：$\text{T}\cdot\text{rad/s}\cdot\text{m}^2=\text{V}$，正确（rad 无量纲）。

</details>

**4.（矩形线圈在非均匀磁场中）** 通有电流 $I_0=5.0\,\text{A}$ 的长直导线旁，一矩形线圈共 $N=50$ 匝，与导线共面，靠近导线一边距导线 $a=0.05\,\text{m}$，远离一边距 $b=0.15\,\text{m}$，长边 $l=0.20\,\text{m}$ 平行于导线。线圈以 $v=0.020\,\text{m/s}$ 远离导线（沿径向）。求初始时刻线圈中的感应电动势。

<details>
<summary>解答</summary>

长直导线磁场 $B(r)=\dfrac{\mu_0 I_0}{2\pi r}$。设线圈内边距导线 $r_1(t)$，$\dfrac{\mathrm dr_1}{\mathrm dt}=v$，宽度 $w=b-a=0.10\,\text{m}$。单匝磁通
$$\Phi=\int_{r_1}^{r_1+w}\frac{\mu_0 I_0}{2\pi r}l\,\mathrm dr=\frac{\mu_0 I_0 l}{2\pi}\ln\frac{r_1+w}{r_1}$$
求导：
$$\frac{\mathrm d\Phi}{\mathrm dt}=\frac{\mu_0 I_0 l v}{2\pi}\left(\frac{1}{r_1+w}-\frac{1}{r_1}\right)$$
代入 $r_1=0.05\,\text{m}$，$w=0.10\,\text{m}$：
- 系数 $\dfrac{\mu_0 I_0 l v}{2\pi}=\dfrac{4\pi\times10^{-7}\times5.0\times0.20\times0.020}{2\pi}=4.0\times10^{-9}\,\text{Wb/s}$
- 括号 $\left(\dfrac{1}{0.15}-\dfrac{1}{0.05}\right)=6.67-20=-13.33\,\text{m}^{-1}$

$$\varepsilon=-N\frac{\mathrm d\Phi}{\mathrm dt}=-50\times4.0\times10^{-9}\times(-13.33)\approx 2.67\times10^{-6}\,\text{V}$$

磁通量随线圈远离而减小，由楞次定律感应电流磁场与原磁场同向以补偿。

**单位检验**：$\text{Wb/s}=\text{V}$，正确。

</details>

**5.（转动线圈——交流电动势）** $N=200$ 匝、面积 $S=0.020\,\text{m}^2$ 的矩形线圈在 $B=0.50\,\text{T}$ 的均匀磁场中绕垂直于 $\vec B$ 的轴以 $\omega=120\pi\,\text{rad/s}$（即 $60\,\text{Hz}$）匀速转动。求感应电动势的最大值、有效值与瞬时表达式（$t=0$ 时线圈法向与 $\vec B$ 平行）。

<details>
<summary>解答</summary>

$$\varepsilon_{\max}=NBS\omega=200\times0.50\times0.020\times120\pi=2400\pi\approx 7.54\times10^3\,\text{V}$$
瞬时值 $\varepsilon(t)=\varepsilon_{\max}\sin\omega t\approx 7.54\times10^3\sin(120\pi t)\,\text{V}$。
有效值 $\varepsilon_{\text{rms}}=\dfrac{\varepsilon_{\max}}{\sqrt2}\approx 5.33\times10^3\,\text{V}$。

**单位检验**：$\text{T}\cdot\text{m}^2\cdot\text{s}^{-1}=\text{V}$，正确。

</details>

**6.（涡旋电场计算）** 长直螺线管半径 $R=0.10\,\text{m}$，内部磁场随时间变化 $\dfrac{\mathrm dB}{\mathrm dt}=0.040\,\text{T/s}$。求管内距轴 $r=0.050\,\text{m}$ 处与管外距轴 $r=0.20\,\text{m}$ 处的涡旋电场大小，并说明方向。

<details>
<summary>解答</summary>

管内（$r<R$）：$E_v=\dfrac{r}{2}\dfrac{\mathrm dB}{\mathrm dt}=\dfrac{0.050}{2}\times0.040=1.0\times10^{-3}\,\text{V/m}$。

管外（$r>R$）：$E_v=\dfrac{R^2}{2r}\dfrac{\mathrm dB}{\mathrm dt}=\dfrac{0.10^2}{2\times0.20}\times0.040=1.0\times10^{-3}\,\text{V/m}$。

方向：$\dfrac{\mathrm dB}{\mathrm dt}>0$，磁场增大，涡旋电场驱动感应电流产生反向磁场，由楞次定律，从 $\vec B$ 方向看为顺时针切向。

**单位检验**：$\dfrac{\text{m}\cdot\text{T/s}}{1}=\dfrac{\text{V/m}}{1}$，正确。

</details>

**7.（自感计算）** 长直螺线管长 $l=0.30\,\text{m}$、半径 $r=0.020\,\text{m}$、匝数 $N=800$，内部为真空。求自感系数 $L$ 及通有 $I=1.5\,\text{A}$ 电流时的磁场能量。

<details>
<summary>解答</summary>

截面积 $S=\pi r^2=\pi\times0.020^2=1.257\times10^{-3}\,\text{m}^2$。
$$L=\mu_0\frac{N^2}{l}S=4\pi\times10^{-7}\times\frac{800^2}{0.30}\times1.257\times10^{-3}$$
$$=4\pi\times10^{-7}\times2.133\times10^6\times1.257\times10^{-3}\approx 3.37\times10^{-3}\,\text{H}=3.37\,\text{mH}$$
磁场能量 $W_m=\tfrac12 LI^2=\tfrac12\times3.37\times10^{-3}\times1.5^2\approx 3.79\times10^{-3}\,\text{J}$。

**单位检验**：$\text{H}\cdot\text{A}^2=\text{J}$，正确。

</details>

**8.（互感计算）** 一长直螺线管（$N_1=500$ 匝、长 $l=0.40\,\text{m}$、截面积 $S=2.0\times10^{-4}\,\text{m}^2$）上密绕一个 $N_2=50$ 匝的短线圈，二者共轴，介质真空。求互感 $M$；若原线圈电流以 $\dfrac{\mathrm dI_1}{\mathrm dt}=5.0\,\text{A/s}$ 变化，求副线圈中的互感电动势。

<details>
<summary>解答</summary>

长螺线管内 $B=\mu_0\dfrac{N_1}{l}I_1$，副线圈磁链 $\Psi_{21}=N_2 BS=\mu_0\dfrac{N_1 N_2}{l}SI_1$。
$$M=\mu_0\frac{N_1 N_2}{l}S=4\pi\times10^{-7}\times\frac{500\times50}{0.40}\times2.0\times10^{-4}$$
$$=4\pi\times10^{-7}\times6.25\times10^4\times2.0\times10^{-4}\approx 1.57\times10^{-5}\,\text{H}=15.7\,\mu\text{H}$$
互感电动势
$$\varepsilon_{21}=-M\frac{\mathrm dI_1}{\mathrm dt}=-1.57\times10^{-5}\times5.0\approx -7.85\times10^{-5}\,\text{V}$$
大小 $|\varepsilon_{21}|\approx 7.85\times10^{-5}\,\text{V}$，方向由楞次定律判定（反抗 $I_1$ 变化）。

**单位检验**：$\text{H}\cdot\text{A/s}=\text{V}$，正确。

</details>

**9.（RL 暂态过程）** 一个 $R=8.0\,\Omega$、$L=0.40\,\text{H}$ 的串联电路接通 $\mathcal E=16\,\text{V}$ 直流电源。求：(1) 时间常数；(2) 电流达到稳态值一半所需时间；(3) 稳态时线圈储存的能量。

<details>
<summary>解答</summary>

(1) $\tau=\dfrac{L}{R}=\dfrac{0.40}{8.0}=0.050\,\text{s}$。

(2) $I(t)=\dfrac{\mathcal E}{R}(1-e^{-t/\tau})$，令 $I=\dfrac12 I_\infty=\dfrac12\dfrac{\mathcal E}{R}$：
$$1-e^{-t/\tau}=\frac12\Rightarrow e^{-t/\tau}=\frac12\Rightarrow t=\tau\ln 2=0.050\times0.693\approx 0.0347\,\text{s}$$

(3) $I_\infty=\dfrac{\mathcal E}{R}=\dfrac{16}{8.0}=2.0\,\text{A}$；$W_m=\tfrac12 LI_\infty^2=\tfrac12\times0.40\times2.0^2=0.80\,\text{J}$。

**单位检验**：$\tau$ 单位 $\text{H}/\Omega=\text{s}$；$W_m$ 单位 $\text{H}\cdot\text{A}^2=\text{J}$，正确。

</details>

**10.（位移电流与磁场）** 圆形平行板电容器极板半径 $R=0.060\,\text{m}$，板间为真空，充电时极板间电场变化率 $\dfrac{\mathrm dE}{\mathrm dt}=2.0\times10^{12}\,\text{V/(m·s)}$。求：(1) 极板间位移电流；(2) 极板内距轴 $r=0.030\,\text{m}$ 处的磁感应强度；(3) 极板边缘 $r=R$ 处的磁感应强度。

<details>
<summary>解答</summary>

(1) $I_d=\varepsilon_0\pi R^2\dfrac{\mathrm dE}{\mathrm dt}=8.85\times10^{-12}\times\pi\times0.060^2\times2.0\times10^{12}$
$\approx 0.200\,\text{A}$。

(2) 板内 $r<R$：回路包围位移电流 $I_d(r)=\dfrac{r^2}{R^2}I_d$，由安培-麦克斯韦定律 $B\cdot 2\pi r=\mu_0 I_d(r)$：
$$B=\frac{\mu_0 I_d r}{2\pi R^2}=\frac{4\pi\times10^{-7}\times0.200\times0.030}{2\pi\times0.060^2}=\frac{2.40\times10^{-9}}{2.262\times10^{-3}}\approx 1.06\times10^{-6}\,\text{T}$$

(3) 板外 $r\ge R$：$B\cdot 2\pi R=\mu_0 I_d$，
$$B=\frac{\mu_0 I_d}{2\pi R}=\frac{4\pi\times10^{-7}\times0.200}{2\pi\times0.060}\approx 6.67\times10^{-7}\,\text{T}$$

方向均沿切向，从 $\dfrac{\mathrm dE}{\mathrm dt}$ 方向看为顺时针（与充电电流配套）。

**单位检验**：$B$ 单位 $\text{T}$；$I_d$ 单位 $\text{F/m}\cdot\text{m}^2\cdot\text{V/(m·s)}=\text{A}$，正确。

</details>

---

## 四、证明题与讨论题（4 题）

**1.（证明：转动导体棒的动生电动势）** 长 $l$ 的导体棒在均匀磁场 $\vec B$ 中绕其一端以角速度 $\omega$ 转动，$\vec B\perp$ 转动平面。试用洛伦兹力观点严格推导棒两端的动生电动势 $\varepsilon=\tfrac12 B\omega l^2$，并说明能量来源。

<details>
<summary>证明</summary>

距轴 $r$ 处导体微元 $\mathrm dr$ 的运动速度 $v(r)=\omega r$，方向沿切向，且 $\vec v\perp\vec B\perp\mathrm d\vec l$（棒沿径向）。该微元处单位电荷所受洛伦兹力（即非静电场）$\vec E_{\text{非}}=\vec v\times\vec B$，方向沿棒由轴指向自由端，大小 $E_{\text{非}}=\omega r B$。

电动势
$$\varepsilon=\int_0^l\vec E_{\text{非}}\cdot\mathrm d\vec l=\int_0^l B\omega r\,\mathrm dr=B\omega\left[\frac{r^2}{2}\right]_0^l=\frac12 B\omega l^2$$

**能量来源**：维持棒匀速转动需要外力矩做功。棒中感应电流（若构成回路）受安培力反抗转动，外力矩克服此力矩做功，转化为电能。洛伦兹力对单个电荷总功为零，但作为"中间媒介"将机械能转化为电能。$\blacksquare$

</details>

**2.（讨论：涡旋电场与静电场的异同）** 试从源、环路定理、高斯定理、力线特征、是否保守、能否定义电势等方面系统比较静电场与涡旋电场，并说明二者在法拉第电磁感应定律中如何统一。

<details>
<summary>讨论</summary>

| 属性 | 静电场 $\vec E_s$ | 涡旋电场 $\vec E_v$ |
| ---- | ---- | ---- |
| 源 | 静止电荷 | 随时间变化的磁场 |
| 高斯定理 | $\oint\vec E_s\cdot\mathrm d\vec S=\dfrac{q_{\text{内}}}{\varepsilon_0}$（有源） | $\oint\vec E_v\cdot\mathrm d\vec S=0$（无源） |
| 环路定理 | $\oint\vec E_s\cdot\mathrm d\vec l=0$（无旋、保守） | $\oint\vec E_v\cdot\mathrm d\vec l=-\int\dfrac{\partial\vec B}{\partial t}\cdot\mathrm d\vec S\ne 0$（有旋、非保守） |
| 力线 | 起于正电荷、止于负电荷 | 闭合曲线 |
| 电势 | 可定义 $\varphi$，$\vec E_s=-\nabla\varphi$ | 不能定义电势 |
| 做功 | 路径无关 | 路径有关 |

**统一**：一般情形下总电场 $\vec E=\vec E_s+\vec E_v$。法拉第电磁感应定律的普遍形式 $\oint\vec E\cdot\mathrm d\vec l=-\int\dfrac{\partial\vec B}{\partial t}\cdot\mathrm d\vec S$ 中，左边是总电场（含静电场与涡旋电场）。由于 $\oint\vec E_s\cdot\mathrm d\vec l=0$，实际贡献环流的只有涡旋电场 $\vec E_v$，故等式右边的 $-\dfrac{\partial\vec B}{\partial t}$ 仅由 $\vec E_v$ 平衡。静电场与涡旋电场在麦克斯韦方程组中各司其职：前者由高斯定理约束（有源），后者由法拉第定律约束（有旋），共同构成完整的电场描述。$\blacksquare$

</details>

**3.（证明：由磁能密度求同轴电缆单位长度自感）** 同轴电缆内芯半径 $R_1$、外导体半径 $R_2$，通有等值反向电流 $I$，介质真空。设电流在内芯截面上均匀分布。试用磁场能量方法推导单位长度自感 $L_0=\dfrac{\mu_0}{8\pi}+\dfrac{\mu_0}{2\pi}\ln\dfrac{R_2}{R_1}$，说明每项的物理来源。

<details>
<summary>证明</summary>

由安培环路定理，磁场分布（见 [[MOC - 第7章|第7章]]）：
- 内芯内 $r<R_1$：$B(r)=\dfrac{\mu_0 I r}{2\pi R_1^2}$（电流均匀分布）；
- 两导体间 $R_1<r<R_2$：$B(r)=\dfrac{\mu_0 I}{2\pi r}$；
- 外部 $r>R_2$：$B=0$。

单位长度总磁能 $W_{m,0}=\int\dfrac{B^2}{2\mu_0}\,\mathrm dV$，取单位长度、半径 $r$、厚 $\mathrm dr$ 的圆柱壳 $\mathrm dV=2\pi r\,\mathrm dr$：

内芯内：
$$W_{m,0}^{(内)}=\int_0^{R_1}\frac{1}{2\mu_0}\left(\frac{\mu_0 I r}{2\pi R_1^2}\right)^2 2\pi r\,\mathrm dr=\frac{\mu_0 I^2}{4\pi R_1^4}\int_0^{R_1}r^3\,\mathrm dr=\frac{\mu_0 I^2}{16\pi}$$

两导体间：
$$W_{m,0}^{(间)}=\int_{R_1}^{R_2}\frac{1}{2\mu_0}\left(\frac{\mu_0 I}{2\pi r}\right)^2 2\pi r\,\mathrm dr=\frac{\mu_0 I^2}{4\pi}\int_{R_1}^{R_2}\frac{\mathrm dr}{r}=\frac{\mu_0 I^2}{4\pi}\ln\frac{R_2}{R_1}$$

由 $W_{m,0}=\dfrac12 L_0 I^2$：
$$L_0=\frac{2W_{m,0}}{I^2}=\frac{\mu_0}{8\pi}+\frac{\mu_0}{2\pi}\ln\frac{R_2}{R_1}$$

- 第一项 $\dfrac{\mu_0}{8\pi}$ 来自**内芯内部磁场能量**（与电流分布有关，称为内自感）；
- 第二项 $\dfrac{\mu_0}{2\pi}\ln\dfrac{R_2}{R_1}$ 来自**两导体之间磁场能量**（外部磁通对应的主自感）。

若内芯为薄壁（电流集中在表面），内自感项消失，仅剩对数项。$\blacksquare$

</details>

**4.（讨论：麦克斯韦方程组的物理意义与对称性）** 写出真空中的麦克斯韦方程组（积分形式），逐一说明其物理意义；并讨论：(a) 方程组的对称结构如何导致电磁波的存在；(b) 为什么变化电场与变化磁场能相互激发形成自维持的波；(c) 光速 $c=\dfrac{1}{\sqrt{\mu_0\varepsilon_0}}$ 的理论意义。

<details>
<summary>讨论</summary>

**麦克斯韦方程组（真空，积分形式）**：
$$\oint_S\vec E\cdot\mathrm d\vec S=\frac{q_{\text{内}}}{\varepsilon_0}\quad(1)\qquad \oint_S\vec B\cdot\mathrm d\vec S=0\quad(2)$$
$$\oint_L\vec E\cdot\mathrm d\vec l=-\int_S\frac{\partial\vec B}{\partial t}\cdot\mathrm d\vec S\quad(3)\qquad \oint_L\vec B\cdot\mathrm d\vec l=\mu_0 I+\mu_0\varepsilon_0\frac{\mathrm d\Phi_E}{\mathrm dt}\quad(4)$$

**物理意义**：
- (1) 电场高斯定理：电荷是电场的源，电场线起于正电荷止于负电荷；
- (2) 磁场高斯定理：磁单极不存在，磁感线闭合；
- (3) 法拉第电磁感应定律：变化磁场激发涡旋电场；
- (4) 安培-麦克斯韦定律：传导电流与变化电场（位移电流）共同激发磁场。

**(a) 对称性导致电磁波**：在无源区域（$q=0$、$I=0$），方程 (3)(4) 退化为
$$\nabla\times\vec E=-\frac{\partial\vec B}{\partial t},\qquad \nabla\times\vec B=\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}$$
二者在 $\vec E\leftrightarrow\vec B$ 的互换下近乎对称（仅系数与符号略异）。对 (3) 取旋度并利用 (4)，得到 $\nabla^2\vec E=\mu_0\varepsilon_0\dfrac{\partial^2\vec E}{\partial t^2}$，即波动方程；对 $\vec B$ 同理。波动方程的解即电磁波。

**(b) 自维持机制**：变化电场产生磁场（方程 4 位移电流项），该磁场又随时间变化产生电场（方程 3），二者相互耦合、相互激发。一旦场被源激发，即使源消失，场也能脱离源以波的形式传播。这与静电场/恒定磁场"依附于源"截然不同。

**(c) 光速的理论意义**：$c=\dfrac{1}{\sqrt{\mu_0\varepsilon_0}}\approx 2.998\times10^8\,\text{m/s}$ 仅由真空电磁常数 $\mu_0$、$\varepsilon_0$ 决定，与参照系无关（在经典框架下）。麦克斯韦据此预言光即电磁波，把光学统一进电磁学。这一"常数光速"也是爱因斯坦狭义相对论的出发点之一（见 [[MOC - 第11章|第11章]]）：光速不依赖光源或观察者的运动，违背了伽利略速度合成，迫使时空观革命。$\blacksquare$

</details>

---

## 考点统计表

| 知识点 | 涉及题号 | 题数 | 难度分布 |
| :--- | :--- | :---: | :--- |
| [[8.1 法拉第电磁感应定律\|法拉第定律与磁通量]] | 填空1、选择1、选择2、计算1 | 4 | 易-中 |
| [[8.1 法拉第电磁感应定律\|楞次定律判方向]] | 选择2、计算1、计算4 | 3 | 中 |
| [[8.2 动生电动势、感生电动势\|动生电动势（平动）]] | 填空2、计算2 | 2 | 易-中 |
| [[8.2 动生电动势、感生电动势\|动生电动势（转动）]] | 计算3、证明1 | 2 | 中 |
| [[8.2 动生电动势、感生电动势\|涡旋电场与感生电动势]] | 填空3、选择4、选择5、计算6 | 4 | 中 |
| [[8.2 动生电动势、感生电动势\|非均匀磁场中的电动势]] | 计算4 | 1 | 难 |
| [[8.3 自感、互感、磁场能量\|自感计算]] | 填空4、计算7 | 2 | 中 |
| [[8.3 自感、互感、磁场能量\|互感计算]] | 计算8 | 1 | 中 |
| [[8.3 自感、互感、磁场能量\|RL 暂态过程]] | 填空5、计算9 | 2 | 中 |
| [[8.3 自感、互感、磁场能量\|磁场能量]] | 填空4、计算7、证明3 | 3 | 中-难 |
| [[8.4 麦克斯韦方程组简介\|位移电流]] | 填空6、选择6、计算10 | 3 | 中 |
| [[8.4 麦克斯韦方程组简介\|麦克斯韦方程组]] | 选择6、计算10、讨论4 | 3 | 难 |
| [[8.2 动生电动势、感生电动势\|涡旋电场与静电场比较]] | 讨论2 | 1 | 难 |
| 合计 | — | 26 | — |

> [!tip] 复习建议
> - **法拉第定律**（计算1、5）是基础，确保 $\varepsilon=-N\dfrac{\mathrm d\Phi}{\mathrm dt}$ 与方向判定熟练；
> - **动生电动势**区分平动（$Bvl$）与转动（$\tfrac12 B\omega l^2$），后者必须积分；
> - **涡旋电场**与位移电流是本章两个对称的核心概念，对比记忆 $E_v\propto r$（管内）/ $\propto 1/r$（管外）的分布；
> - **自感、互感、磁能**计算要熟练螺线管公式 $L=\mu_0 n^2 V$ 与 $W_m=\tfrac12 LI^2=\int\dfrac{B^2}{2\mu_0}\mathrm dV$；
> - **麦克斯韦方程组**四个方程务必完整记忆，并理解每个方程的物理意义与对称结构。

## 章节导航

> [!nav] 导航
> [[MOC - 第8章|第8章 知识点目录]] · [[MOC - 大学物理B|课程总览]] · 上一章习题：[[MOC - 第7章习题|第7章 恒定磁场习题]] · 下一章习题：[[MOC - 第9章习题|第9章 机械振动与机械波习题]]
