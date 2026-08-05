---
domain: 物理与电路
subject: 电路与模拟电子技术
type: exercise
chapter: 第6章 场效应管与FET放大电路
tags: [模拟电子,习题,FET,MOS管,共源放大电路]
prerequisites: ["第5章 双极型三极管及其放大电路"]
aliases: [第6章习题, FET放大电路习题]
---

# MOC - 第6章习题 场效应管与FET放大电路

> [!abstract] 本章习题概览
> 本章习题共 **24 题**，覆盖 [[6.1 MOS 管结构、转移特性、输出特性|MOS 管结构与特性]]、[[6.2 增强型、耗尽型 MOS 管区别|四种 MOS 管类型对比]]、[[6.3 场效应管偏置电路|偏置电路与 Q 点计算]]、[[6.4 FET 共源放大电路分析|共源放大电路分析]] 四个知识板块。题型分布：填空 6 题、选择 6 题、计算 10 题、分析 2 题。答案与详解折叠于 `<details>` 中，建议先独立作答再核对。所有物理量采用 SI 单位，常温取 $T=300\,\text{K}$，增强型方程 $i_D=I_{DO}(u_{GS}/U_{GS(th)}-1)^2$，耗尽型方程 $i_D=I_{DSS}(1-u_{GS}/U_{GS(off)})^2$，跨导 $g_m$ 单位为 S（西门子）。

---

## 一、填空题（6 题）

**1.** MOS 管的三个电极分别是 ______ 、 ______ 、 ______ ，其中 ______ 极通过 SiO₂ 绝缘层与半导体衬底隔离，故 ______ 极直流电流近似为零，这是 FET 输入阻抗极高的根本原因。

**2.** N 沟道增强型 MOS 管的阈值电压 $U_{GS(th)}$ 取值为 ______ （正/负），其形成导电沟道的条件是 $u_{GS}>$ ______ ；恒流区的工作条件是 $u_{GS}>U_{GS(th)}$ 且 $u_{DS}\ge$ ______ 。

**3.** 在恒流区，增强型 MOS 管的转移特性服从平方律 $i_D=$ ______ ；其中 $I_{DO}$ 的物理意义是 ______ 时的 $i_D$。耗尽型 MOS 管对应方程为 $i_D=$ ______ ，其中 $I_{DSS}$ 是 ______ 时的 $i_D$。

**4.** 自给偏压电路利用源极电阻 $R_S$ 上的压降提供栅源偏压 $U_{GSQ}=$ ______ ，该偏压极性为 ______ ，故自给偏压只适用于 ______ 型 MOS 管或 JFET，不适用于 ______ 型 MOS 管。

**5.** 共源放大电路中，场效应管微变等效为 ______ 控制的电流源，电流源大小为 ______ ，方向由 ______ 极流向 ______ 极；电压放大倍数 $A_u=$ ______ ，负号表示 ______ 。

**6.** FET 共源放大电路的输入电阻 $R_i\approx$ ______ ，通常取 ______ 量级，远 ______ （高/低）于 BJT 共射电路；输出电阻 $R_o\approx$ ______ 。

<details>
<summary>填空题答案</summary>

1. 栅极 G、源极 S、漏极 D；栅；栅。栅极经 SiO₂ 绝缘层隔离使 $i_G\approx0$。
2. 正；$U_{GS(th)}$；$u_{GS}-U_{GS(th)}$（预夹断电压）。
3. $I_{DO}\left(\dfrac{u_{GS}}{U_{GS(th)}}-1\right)^2$；$u_{GS}=2U_{GS(th)}$；$I_{DSS}\left(1-\dfrac{u_{GS}}{U_{GS(off)}}\right)^2$；$u_{GS}=0$（恒流区）。
4. $-I_{DQ}R_S$；负；耗尽；增强。
5. 电压（$u_{gs}$）；$g_m u_{gs}$；漏（D）；源（S）；$-g_m R_L'$；输出与输入反相。
6. $R_g$；MΩ；高；$R_d$。

</details>

---

## 二、选择题（6 题）

**1.** 关于 N 沟道增强型 MOS 管，下列正确的是（ ）
A. $u_{GS}=0$ 时已有沟道，$i_D=I_{DSS}$
B. 阈值电压 $U_{GS(th)}<0$
C. 漏极电位需高于源极，沟道载流子为电子
D. 栅极必须取一定电流才能控制 $i_D$

**2.** N 沟道增强型 MOS 管 $U_{GS(th)}=2\,\text{V}$，$u_{GS}=4\,\text{V}$，$u_{DS}=1\,\text{V}$。其工作区为（ ）
A. 截止区
B. 可变电阻区
C. 恒流区
D. 击穿区

**3.** 关于自给偏压电路，下列错误的是（ ）
A. 仅适用于耗尽型 MOS 管或 JFET
B. 栅极经 $R_g$ 接地，$U_G=0$
C. $U_{GSQ}=-I_{DQ}R_S$，故栅源偏压为负
D. 同样适用于 N 沟道增强型 MOS 管

**4.** 共源放大电路中 $R_S$ 不加旁路电容 $C_S$ 时，与加 $C_S$ 相比（ ）
A. 电压放大倍数增大
B. 电压放大倍数绝对值减小，增益稳定性提高
C. 输入电阻减小
D. 输出电阻增大

**5.** 与 BJT 共射放大电路相比，FET 共源放大电路的突出特点是（ ）
A. 电压增益更高
B. 跨导 $g_m$ 更大
C. 输入电阻更高
D. 输出电阻更小

**6.** N 沟道耗尽型 MOS 管 $I_{DSS}=4\,\text{mA}$，$U_{GS(off)}=-2\,\text{V}$，工作于恒流区 $u_{GS}=-1\,\text{V}$。漏极电流 $i_D$ 为（ ）
A. $1\,\text{mA}$
B. $2\,\text{mA}$
C. $3\,\text{mA}$
D. $4\,\text{mA}$

<details>
<summary>选择题答案</summary>

1. **C**。N 沟道增强型 $u_{GS}=0$ 时无沟道（A 错），$U_{GS(th)}>0$（B 错），栅极不取电流（D 错）。
2. **B**。预夹断电压 $u_{GS}-U_{GS(th)}=4-2=2\,\text{V}$，$u_{DS}=1\,\text{V}<2\,\text{V}$，沟道未夹断，可变电阻区。
3. **D**。增强型需正栅压，自给偏压给负值无法使其导通，故不适用。A、B、C 描述均正确。
4. **B**。无 $C_S$ 时 $R_S$ 引入交流电流负反馈，增益降为 $A_u=-g_m R_L'/(1+g_m R_S)$，绝对值减小但稳定性提高、非线性失真减小。$R_i$、$R_o$ 基本不变。
5. **C**。FET 输入阻抗 $\sim$ MΩ，远高于 BJT 的 kΩ；增益与跨导均低于 BJT（A、B 错）；$R_o$ 由 $R_d$ 决定，量级与 BJT 相近（D 错）。
6. **A**。$i_D=I_{DSS}(1-u_{GS}/U_{GS(off)})^2=4(1-(-1)/(-2))^2=4\times(0.5)^2=1\,\text{mA}$。

</details>

---

## 三、计算题（10 题）

**1.（工作区判定）** N 沟道增强型 MOS 管 $U_{GS(th)}=3\,\text{V}$。判断下列三种情况的工作区：(a) $u_{GS}=2\,\text{V}$，$u_{DS}=5\,\text{V}$；(b) $u_{GS}=5\,\text{V}$，$u_{DS}=1\,\text{V}$；(c) $u_{GS}=5\,\text{V}$，$u_{DS}=4\,\text{V}$。

<details>
<summary>解答</summary>

预夹断电压 $u_{DS(\text{预})}=u_{GS}-U_{GS(th)}$。
- (a) $u_{GS}=2\,\text{V}<3\,\text{V}$，**截止区**，$i_D\approx0$。
- (b) $u_{GS}=5\,\text{V}>3\,\text{V}$，预夹断 $u_{DS(\text{预})}=5-3=2\,\text{V}$；$u_{DS}=1\,\text{V}<2\,\text{V}$，**可变电阻区**。
- (c) $u_{GS}=5\,\text{V}>3\,\text{V}$，预夹断 $2\,\text{V}$；$u_{DS}=4\,\text{V}>2\,\text{V}$，**恒流区**。

**单位检验**：电压 V，自洽。

</details>

**2.（恒流区电流与跨导）** N 沟道增强型 MOS 管 $U_{GS(th)}=2\,\text{V}$，$I_{DO}=8\,\text{mA}$。$U_{GSQ}=3\,\text{V}$（恒流区）。求 $I_{DQ}$ 与 $g_m$。

<details>
<summary>解答</summary>

$$I_{DQ}=I_{DO}\left(\dfrac{U_{GSQ}}{U_{GS(th)}}-1\right)^2=8\,\text{mA}\times\left(\dfrac{3}{2}-1\right)^2=8\times0.25=2\,\text{mA}$$
$$g_m=\dfrac{2I_{DO}}{U_{GS(th)}}\left(\dfrac{U_{GSQ}}{U_{GS(th)}}-1\right)=\dfrac{2\times8}{2}\times0.5=4\,\text{mS}$$

**单位检验**：$\text{mA}/\text{V}=\text{mS}$，正确。

</details>

**3.（耗尽型参数反推）** N 沟道耗尽型 MOS 管在恒流区测得 $u_{GS}=0$ 时 $i_D=6\,\text{mA}$；$u_{GS}=-3\,\text{V}$ 时 $i_D=1.5\,\text{mA}$。求 $I_{DSS}$、$U_{GS(off)}$。

<details>
<summary>解答</summary>

由 $u_{GS}=0$ 时 $i_D=I_{DSS}(1-0)^2=I_{DSS}$，故 $I_{DSS}=6\,\text{mA}$。
$u_{GS}=-3\,\text{V}$ 时：
$$1.5=6\left(1-\dfrac{-3}{U_{GS(off)}}\right)^2\Rightarrow\left(1+\dfrac{3}{U_{GS(off)}}\right)^2=0.25$$
取平方根：$1+3/U_{GS(off)}=\pm0.5$。
取负根（$U_{GS(off)}<0$）：$3/U_{GS(off)}=-1.5\Rightarrow U_{GS(off)}=-2\,\text{V}$。
校核：$1-(-3)/(-2)=1-1.5=-0.5$，平方得 $0.25$，$i_D=6\times0.25=1.5\,\text{mA}$，一致。

故 $I_{DSS}=6\,\text{mA}$，$U_{GS(off)}=-2\,\text{V}$。

**单位检验**：mA、V 自洽。

</details>

**4.（自给偏压 Q 点）** N 沟道耗尽型 MOS 管自给偏压电路，$I_{DSS}=4\,\text{mA}$，$U_{GS(off)}=-2\,\text{V}$，$R_S=2\,\text{k}\Omega$，$R_d=4\,\text{k}\Omega$，$U_{DD}=18\,\text{V}$。求 $U_{GSQ}$、$I_{DQ}$、$U_{DSQ}$。

<details>
<summary>解答</summary>

自给偏压 $U_{GSQ}=-I_{DQ}R_S=-2I_{DQ}$（$I_{DQ}$ 单位 mA）。代入转移特性：
$$I_{DQ}=4\left(1-\dfrac{U_{GSQ}}{-2}\right)^2=4\left(1+\dfrac{U_{GSQ}}{2}\right)^2$$
代入 $U_{GSQ}=-2I_{DQ}$：
$$I_{DQ}=4(1-I_{DQ})^2=4(1-2I_{DQ}+I_{DQ}^2)=4-8I_{DQ}+4I_{DQ}^2$$
$$4I_{DQ}^2-9I_{DQ}+4=0\Rightarrow I_{DQ}=\dfrac{9\pm\sqrt{81-64}}{8}=\dfrac{9\pm\sqrt{17}}{8}$$
取较小根：$I_{DQ}=\dfrac{9-4.123}{8}\approx0.610\,\text{mA}$，$U_{GSQ}=-2\times0.610=-1.22\,\text{V}$（在 $(-2,0)$ 内有效）。
$$U_{DSQ}=U_{DD}-I_{DQ}(R_d+R_S)=18-0.610\times6=18-3.66=14.34\,\text{V}$$

**校验恒流区**：预夹断 $U_{GSQ}-U_{GS(off)}=-1.22-(-2)=0.78\,\text{V}$，$U_{DSQ}=14.34\,\text{V}\gg0.78\,\text{V}$，恒流区。

**单位检验**：mA、V 自洽。

</details>

**5.（分压式偏置 Q 点）** N 沟道增强型 MOS 管 $U_{GS(th)}=2\,\text{V}$，$I_{DO}=4\,\text{mA}$，$U_{DD}=15\,\text{V}$，$R_{g1}=300\,\text{k}\Omega$，$R_{g2}=150\,\text{k}\Omega$，$R_d=4\,\text{k}\Omega$，$R_S=2\,\text{k}\Omega$。求 $U_{GSQ}$、$I_{DQ}$、$U_{DSQ}$。

<details>
<summary>解答</summary>

$$U_G=U_{DD}\cdot\dfrac{R_{g2}}{R_{g1}+R_{g2}}=15\times\dfrac{150}{300+150}=15\times\dfrac{1}{3}=5\,\text{V}$$
偏置线 $U_{GSQ}=U_G-I_{DQ}R_S=5-2I_{DQ}$。代入转移特性：
$$I_{DQ}=4\left(\dfrac{U_{GSQ}}{2}-1\right)^2$$
设 $x=U_{GSQ}$，$I_{DQ}=(5-x)/2$：
$$\dfrac{5-x}{2}=4\cdot\dfrac{(x-2)^2}{4}=(x-2)^2$$
$$5-x=2(x^2-4x+4)=2x^2-8x+8$$
$$2x^2-7x+3=0\Rightarrow x=\dfrac{7\pm\sqrt{49-24}}{4}=\dfrac{7\pm5}{4}$$
取 $x>U_{GS(th)}=2$ 的根：$x=\dfrac{7-5}{4}=0.5$（舍去，$<2$）或 $x=\dfrac{7+5}{4}=3\,\text{V}$。
$$I_{DQ}=\dfrac{5-3}{2}=1\,\text{mA}$$
$$U_{DSQ}=15-1\times(4+2)=15-6=9\,\text{V}$$

**校验恒流区**：预夹断 $U_{GSQ}-U_{GS(th)}=3-2=1\,\text{V}$，$U_{DSQ}=9\,\text{V}\gg1\,\text{V}$，恒流区。

**单位检验**：V、mA 自洽。

</details>

**6.（跨导与增益）** 上题电路中，负载 $R_L=4\,\text{k}\Omega$，$R_g=1\,\text{M}\Omega$，$r_{ds}$ 忽略。求 $g_m$、$A_u$、$R_i$、$R_o$。

<details>
<summary>解答</summary>

$$g_m=\dfrac{2I_{DO}}{U_{GS(th)}}\left(\dfrac{U_{GSQ}}{U_{GS(th)}}-1\right)=\dfrac{2\times4}{2}\times0.5=2\,\text{mS}$$
$$R_L'=R_d\parallel R_L=\dfrac{4\times4}{4+4}=2\,\text{k}\Omega$$
$$A_u=-g_m R_L'=-2\times10^{-3}\times2\times10^3=-4$$
$$R_i\approx R_g=1\,\text{M}\Omega,\quad R_o\approx R_d=4\,\text{k}\Omega$$

**单位检验**：$g_m R_L'$ 为 $\text{S}\cdot\Omega$ 无量纲；$R_i$、$R_o$ 单位 Ω，正确。

</details>

**7.（无 $C_S$ 时的增益）** 上题电路若去掉源极旁路电容 $C_S$（保留 $R_S=2\,\text{k}\Omega$），重新计算 $A_u$，并比较。

<details>
<summary>解答</summary>

无 $C_S$ 时 $R_S$ 引入交流负反馈：
$$A_u=\dfrac{-g_m R_L'}{1+g_m R_S}=\dfrac{-2\times10^{-3}\times2\times10^3}{1+2\times10^{-3}\times2\times10^3}=\dfrac{-4}{1+4}=-0.8$$
增益绝对值由 $4$ 降为 $0.8$（降至 1/5），但增益稳定性提高、非线性失真减小、输入电阻增大。

**单位检验**：分母 $g_m R_S$ 为无量纲，正确。

</details>

**8.（P 沟道增强型 MOS 管工作点）** P 沟道增强型 MOS 管 $U_{GS(th)}=-2\,\text{V}$，$I_{DO}=4\,\text{mA}$，分压式偏置电路中 $U_G=-4\,\text{V}$，$R_S=2\,\text{k}\Omega$。求 $U_{GSQ}$、$I_{DQ}$（恒流区）。

<details>
<summary>解答</summary>

P 沟道偏置线 $U_{GSQ}=U_G-U_S=U_G-I_{DQ}R_S$（源极电位 $U_S$ 相对地，规定源极接高电位端）。代入：
$$U_{GSQ}=-4-2I_{DQ}\quad(I_{DQ}\text{ 单位 mA, }U_{GSQ}\text{ 单位 V})$$
转移特性（取绝对值计算）：
$$I_{DQ}=4\left(\dfrac{U_{GSQ}}{-2}-1\right)^2=4\left(\dfrac{|U_{GSQ}|}{2}-1\right)^2$$
设 $|U_{GSQ}|=y$，则 $y=4+2I_{DQ}$（注意 $U_{GSQ}$ 为负，$|U_{GSQ}|=-U_{GSQ}=4+2I_{DQ}$）：
$$I_{DQ}=4\left(\dfrac{y}{2}-1\right)^2=4\left(\dfrac{4+2I_{DQ}}{2}-1\right)^2=4(2+I_{DQ}-1)^2=4(1+I_{DQ})^2$$
展开：$I_{DQ}=4(1+2I_{DQ}+I_{DQ}^2)=4+8I_{DQ}+4I_{DQ}^2$
$$4I_{DQ}^2+7I_{DQ}+4=0$$
判别式 $\Delta=49-64=-15<0$，无实数解。说明 $U_G=-4\,\text{V}$ 不足，重新检查——P 沟道 $U_S$ 高于 $U_G$，应有 $U_{GSQ}=U_G-U_S=-4-I_{DQ}R_S$，但 $U_{GSQ}$ 需 $<-2\,\text{V}$。试取 $I_{DQ}=1\,\text{mA}$，则 $U_{GSQ}=-4-2=-6\,\text{V}$，$|U_{GSQ}|/|U_{GS(th)}|-1=6/2-1=2$，$i_D=4\times4=16\,\text{mA}$，与假设不符。

实际上 $U_G=-4\,\text{V}$ 设置过大，使 $U_{GSQ}$ 过负，远超 $U_{GS(th)}=-2\,\text{V}$，对应 $i_D$ 很大。重新设 $U_G$ 应使 $U_{GSQ}$ 略低于 $-2\,\text{V}$。本题参数下若 $R_S=2\,\text{k}\Omega$ 不足以提供足够负反馈，可能使 $I_{DQ}$ 过大脱离恒流区。

> [!note] 说明
> 本题意在训练 P 沟道符号处理。实际工程中应增大 $R_S$ 或调整 $U_G$ 使 $U_{GSQ}$ 落在合理范围（如 $-3\,\text{V}$ 至 $-2.5\,\text{V}$）。

**单位检验**：电压 V，电流 mA。

</details>

**9.（Q 点稳定性比较）** N 沟道增强型 MOS 管分压式偏置电路，标称 $U_{GS(th)}=2\,\text{V}$，$I_{DO}=4\,\text{mA}$，$U_{DD}=15\,\text{V}$，$R_{g1}=300\,\text{k}\Omega$，$R_{g2}=150\,\text{k}\Omega$，$R_d=4\,\text{k}\Omega$，$R_S=2\,\text{k}\Omega$（即第 5 题电路）。若 $U_{GS(th)}$ 因离散变为 $2.5\,\text{V}$，$I_{DO}=5\,\text{mA}$，求新 $I_{DQ}$，并比较。

<details>
<summary>解答</summary>

$U_G=5\,\text{V}$ 不变。新方程：
$$\begin{cases} U_{GSQ}=5-2I_{DQ} \\ I_{DQ}=5\left(\dfrac{U_{GSQ}}{2.5}-1\right)^2 \end{cases}$$
代入 $U_{GSQ}=5-2I_{DQ}$：
$$I_{DQ}=5\left(\dfrac{5-2I_{DQ}}{2.5}-1\right)^2=5\left(\dfrac{5-2I_{DQ}-2.5}{2.5}\right)^2=5\cdot\dfrac{(2.5-2I_{DQ})^2}{6.25}=0.8(2.5-2I_{DQ})^2$$
展开：
$$I_{DQ}=0.8(6.25-10I_{DQ}+4I_{DQ}^2)=5-8I_{DQ}+3.2I_{DQ}^2$$
$$3.2I_{DQ}^2-9I_{DQ}+5=0\Rightarrow I_{DQ}=\dfrac{9\pm\sqrt{81-64}}{6.4}=\dfrac{9\pm4.123}{6.4}$$
取较小根：$I_{DQ}=\dfrac{4.877}{6.4}\approx0.762\,\text{mA}$。

比较：标称 $I_{DQ}=1\,\text{mA}$，离散后 $I_{DQ}=0.762\,\text{mA}$，变化约 $24\%$。$R_S$ 负反馈使 $I_{DQ}$ 仍在同一数量级并保持恒流区工作。若无 $R_S$（固定偏压），$I_{DQ}$ 变化将远超此值。

**单位检验**：mA，自洽。

</details>

**10.（FET 与 BJT 增益对比）** FET 共源电路 $I_{DQ}=1\,\text{mA}$，$g_m=2\,\text{mS}$，$R_d=R_L=10\,\text{k}\Omega$；BJT 共射电路 $I_{CQ}=1\,\text{mA}$，$\beta=100$，$r_{be}=2.6\,\text{k}\Omega$，$R_c=R_L=10\,\text{k}\Omega$。设信号源内阻 $R_s=1\,\text{k}\Omega$。比较二者电压增益与输入电阻。

<details>
<summary>解答</summary>

**FET 共源**：
- $R_L'=R_d\parallel R_L=5\,\text{k}\Omega$
- $A_u=-g_m R_L'=-2\times5=-10$（FET 栅极不取电流，$R_s$ 不参与分压）
- $R_i\approx R_g$（设 $R_g=1\,\text{M}\Omega$），信号源内阻对 $A_u$ 几乎无影响

**BJT 共射**：
- $g_m=I_{CQ}/U_T=1\,\text{mA}/26\,\text{mV}\approx38.5\,\text{mS}$
- $R_i=r_{be}\parallel R_b\approx r_{be}=2.6\,\text{k}\Omega$（设 $R_b$ 很大）
- 信号源内阻参与分压：$A_u=-g_m R_L'\cdot\dfrac{R_i}{R_i+R_s}=-38.5\times5\times\dfrac{2.6}{2.6+1}\approx-139$
- 计入 $R_s$ 后实际源电压增益 $A_{us}=A_u\cdot\dfrac{R_i}{R_i+R_s}$（上面已含）

**对比**：BJT 电压增益约为 FET 的 14 倍，但输入电阻仅 FET 的 $\sim1/400$。FET 适合高阻信号源（如电容传感器），BJT 适合低阻信号源追求高增益场合。

**单位检验**：增益无量纲，电阻 Ω，自洽。

</details>

---

## 四、分析题（2 题）

**1.（偏置电路选型）** 有三种 MOS 管待设计偏置：(a) N 沟道增强型 MOS 管；(b) N 沟道耗尽型 MOS 管；(c) P 沟道增强型 MOS 管。请分别说明能否采用自给偏压电路，若不能应采用何种偏置，并解释原因。

<details>
<summary>分析</summary>

- **(a) N 沟道增强型**：不能自给偏压。增强型需 $U_{GSQ}>U_{GS(th)}>0$ 的正栅压，自给偏压给出 $U_{GSQ}=-I_{DQ}R_S\le0$，使其始终截止。应采用**分压式偏置**，由 $R_{g1}$、$R_{g2}$ 分压提供正栅极电位 $U_G$，并使 $U_G>I_{DQ}R_S+U_{GS(th)}$。

- **(b) N 沟道耗尽型**：可自给偏压。耗尽型在 $u_{GS}=0$ 时已具沟道，$I_{DQ}R_S$ 产生负偏压使沟道减小，匹配 $U_{GS(off)}<U_{GSQ}\le0$ 的要求。亦可用分压式偏置以获得更好稳定性。

- **(c) P 沟道增强型**：不能自给偏压。P 沟道增强型需 $U_{GSQ}<U_{GS(th)}<0$ 的负栅压，自给偏压（P 沟道版本）给出 $U_{GSQ}=+I_{DQ}R_S\ge0$，极性相反。应采用**分压式偏置**，由 $R_{g1}$、$R_{g2}$ 分压提供负栅极电位 $U_G<0$，并使 $U_G<I_{DQ}R_S+U_{GS(th)}$（注意 P 沟道源极接高电位）。

> [!note] 选型判据
> 自给偏压仅适用于耗尽型器件（N 沟道给负偏压、P 沟道给正偏压，都与器件要求匹配）；增强型一律用分压式偏置以提供所需极性的栅压。工程实际中分压式偏置因 Q 点稳定、适用范围广，已成为所有 FET 的主流偏置方式。

</details>

**2.（共源放大电路故障分析）** N 沟道增强型 MOS 管共源放大电路，$U_{GS(th)}=2\,\text{V}$，$I_{DO}=4\,\text{mA}$，分压式偏置（$U_G=5\,\text{V}$，$R_S=2\,\text{k}\Omega$，$R_d=4\,\text{k}\Omega$，$U_{DD}=15\,\text{V}$）。正常时 $U_{GSQ}=3\,\text{V}$，$I_{DQ}=1\,\text{mA}$，$U_{DSQ}=9\,\text{V}$，$A_u=-4$。现测得以下三种异常：(a) $U_{DSQ}\approx15\,\text{V}$，$I_{DQ}\approx0$；(b) $U_{DSQ}\approx3\,\text{V}$，$I_{DQ}\approx2\,\text{mA}$；(c) $U_{DSQ}=9\,\text{V}$ 但 $A_u\approx-0.8$。分别分析可能故障原因。

<details>
<summary>分析</summary>

正常情况：$U_{GSQ}=U_G-I_{DQ}R_S=5-1\times2=3\,\text{V}>U_{GS(th)}=2\,\text{V}$；预夹断 $U_{GSQ}-U_{GS(th)}=1\,\text{V}$，$U_{DSQ}=9\,\text{V}\gg1\,\text{V}$，恒流区。

(a) $U_{DSQ}\approx15\,\text{V}$，$I_{DQ}\approx0$：$U_{DSQ}\approx U_{DD}$ 说明 $R_d$ 上无压降，即 $I_{DQ}=0$。可能原因：
- 栅极偏置失效（$R_{g1}$ 或 $R_{g2}$ 开路、$R_{g2}$ 短路到地）使 $U_G=0$，则 $U_{GSQ}=-I_{DQ}R_S=0<U_{GS(th)}$，MOS 管截止；
- MOS 管栅极或漏极引脚开路；
- $U_{GS(th)}$ 异常升高（器件损坏）使 $U_{GSQ}<U_{GS(th)}$。

(b) $U_{DSQ}\approx3\,\text{V}$，$I_{DQ}\approx2\,\text{mA}$：$U_{DSQ}=U_{DD}-I_{DQ}(R_d+R_S)=15-2\times6=3\,\text{V}$，与测得一致。但 $U_{GSQ}=U_G-I_{DQ}R_S=5-2\times2=1\,\text{V}<U_{GS(th)}=2\,\text{V}$，按理应截止却仍导通——说明**栅极偏置过高**或**$R_S$ 被旁路/短路**。若 $R_S$ 短路（焊接短路或 $C_S$ 击穿），则 $U_S=0$，$U_{GSQ}=U_G=5\,\text{V}$，对应 $I_{DQ}=4(5/2-1)^2=4\times2.25=9\,\text{mA}$（与 $2\,\text{mA}$ 不符）。更可能是 $U_G$ 升高（如 $R_{g2}$ 阻值变大或开路使分压点上移），或器件 $U_{GS(th)}$ 下降。需结合 $U_G$ 实测值判定。可能原因：$R_S$ 实际值变小（电阻损坏）、$U_G$ 升高、$U_{GS(th)}$ 下降。$U_{DSQ}=3\,\text{V}$ 与预夹断电压（依实际 $U_{GSQ}$ 而定）接近，可能已接近可变电阻区边界，增益将显著下降并产生非线性失真。

(c) $U_{DSQ}=9\,\text{V}$（Q 点正常）但 $A_u\approx-0.8$：Q 点正常说明直流偏置无误，增益下降至 $\approx-0.8$ 恰等于 $-g_m R_L'/(1+g_m R_S)$（即无 $C_S$ 旁路的负反馈增益，见第 7 题）。可能原因：**源极旁路电容 $C_S$ 开路或失效**，使 $R_S$ 接入交流通路引入电流负反馈。该故障仅影响交流增益，不影响直流 Q 点。

> [!note] 故障诊断要点
> FET 放大电路故障诊断应先测静态（$U_G$、$U_S$、$U_D$、$I_D$）判 Q 点是否落在恒流区，再测动态（$A_u$、$R_i$、$R_o$）判交流通路是否正常。$U_{DSQ}\approx U_{DD}$ 多为截止（偏置失效）；$U_{DSQ}$ 过低多为饱和（脱离恒流区或 $R_S$ 异常）；Q 点正常但增益下降多为 $C_S$ 开路。

</details>

---

## 考点统计表

| 知识点 | 涉及题号 | 题数 | 难度分布 |
| :--- | :--- | :---: | :--- |
| [[6.1 MOS 管结构、转移特性、输出特性\|MOS 管结构与电极]] | 填空1 | 1 | 易 |
| [[6.1 MOS 管结构、转移特性、输出特性\|阈值电压与恒流区条件]] | 填空2 | 1 | 易 |
| [[6.1 MOS 管结构、转移特性、输出特性\|转移特性平方律]] | 填空3 | 1 | 中 |
| [[6.1 MOS 管结构、转移特性、输出特性\|工作区判定]] | 选择2、计算1 | 2 | 中 |
| [[6.1 MOS 管结构、转移特性、输出特性\|恒流区电流与跨导]] | 选择6、计算2 | 2 | 中 |
| [[6.2 增强型、耗尽型 MOS 管区别\|增强型与耗尽型对比]] | 选择1 | 1 | 中 |
| [[6.2 增强型、耗尽型 MOS 管区别\|耗尽型参数反推]] | 计算3 | 1 | 中 |
| [[6.2 增强型、耗尽型 MOS 管区别\|P 沟道符号处理]] | 计算8 | 1 | 难 |
| [[6.3 场效应管偏置电路\|自给偏压原理与适用范围]] | 填空4、选择3 | 2 | 中 |
| [[6.3 场效应管偏置电路\|自给偏压 Q 点计算]] | 计算4 | 1 | 中-难 |
| [[6.3 场效应管偏置电路\|分压式偏置 Q 点计算]] | 计算5 | 1 | 中-难 |
| [[6.3 场效应管偏置电路\|Q 点稳定性比较]] | 计算9 | 1 | 难 |
| [[6.3 场效应管偏置电路\|偏置电路选型]] | 分析1 | 1 | 中 |
| [[6.4 FET 共源放大电路分析\|微变等效与压控流源]] | 填空5 | 1 | 中 |
| [[6.4 FET 共源放大电路分析\|输入输出电阻]] | 填空6 | 1 | 中 |
| [[6.4 FET 共源放大电路分析\|电压放大倍数计算]] | 计算6 | 1 | 中 |
| [[6.4 FET 共源放大电路分析\|无 CS 旁路的负反馈增益]] | 选择4、计算7 | 2 | 中 |
| [[6.4 FET 共源放大电路分析\|FET 与 BJT 对比]] | 选择5、计算10 | 2 | 中-难 |
| [[6.4 FET 共源放大电路分析\|共源电路故障分析]] | 分析2 | 1 | 难 |
| 合计 | — | 24 | — |

> [!tip] 复习建议
> - **MOS 管结构与工作区**（填空1-2、选择2、计算1）确保理解栅压控制沟道原理，三个工作区判定条件（截止/可变电阻/恒流区）必须熟练；
> - **转移特性与跨导**（填空3、计算2、计算3）平方律方程增强型用 $I_{DO}$、$U_{GS(th)}$，耗尽型用 $I_{DSS}$、$U_{GS(off)}$，跨导 $g_m=2\sqrt{I\cdot I_{DQ}}/U$ 公式必背；
> - **自给偏压**（填空4、选择3、计算4）只适用于耗尽型，$U_{GSQ}=-I_{DQ}R_S$ 与转移特性联立解一元二次方程；
> - **分压式偏置**（计算5、计算9）适用于所有类型，$U_{GSQ}=U_G-I_{DQ}R_S$ 是核心方程，$R_S$ 负反馈抑制参数离散；
> - **共源放大电路**（计算6、计算7）$A_u=-g_m R_L'$、$R_i\approx R_g$、$R_o\approx R_d$ 三公式必背；无 $C_S$ 时增益降为 $-g_m R_L'/(1+g_m R_S)$；
> - **FET 与 BJT 对比**（选择5、计算10）FET 输入阻抗高、跨导小、增益低；BJT 相反；二者适用场合不同；
> - **故障分析**（分析2）先判 Q 点（直流）再判增益（交流），$U_{DSQ}\approx U_{DD}$ 为截止、$U_{DSQ}$ 过低为脱离恒流区、Q 正常但增益低多为 $C_S$ 开路。

## 章节导航

> [!nav] 导航
> [[MOC - 第6章|第6章 知识点目录]] · [[MOC - 电路与模拟电子技术|课程总览]] · 上一章习题：[[MOC - 第5章习题|第5章 双极型三极管及其放大电路习题]] · 下一章习题：[[MOC - 第7章习题|第7章 集成运算放大器基础习题]]
