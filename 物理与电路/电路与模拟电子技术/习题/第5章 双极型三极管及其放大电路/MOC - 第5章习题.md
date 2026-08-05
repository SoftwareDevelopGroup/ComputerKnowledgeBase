---
domain: 物理与电路
subject: 电路与模拟电子技术
type: exercise
chapter: 第5章 双极型三极管及其放大电路
tags: [模拟电子,习题,BJT,放大电路,Q点,微变等效电路]
prerequisites: ["第4章 半导体二极管与稳压管"]
aliases: [第5章习题, BJT放大电路习题]
---

# MOC - 第5章习题 双极型三极管及其放大电路

> [!abstract] 本章习题概览
> 本章习题共 **28 题**，覆盖 [[5.1 BJT 三极管结构、放大原理、三种工作区|BJT 结构与工作区]]、[[5.2 共射放大电路静态分析、Q 点计算|共射电路静态分析与 Q 点]]、[[5.3 微变等效电路、电压放大倍数计算|微变等效电路与电压放大倍数]]、[[5.4 共集、共基放大电路特点|共集/共基组态特点]]、[[5.5 分压式静态工作点稳定电路|分压式偏置与 Q 点稳定]] 五个知识板块。题型分布：填空 6 题、选择 6 题、计算 14 题、分析 2 题。答案与详解折叠于 `<details>` 中，建议先独立作答再核对。所有物理量采用 SI 单位，常温取 $T=300\,\text{K}$，硅管 $U_{BEQ}=0.7\,\text{V}$、$U_{CES}=0.3\,\text{V}$，热电压 $U_T\approx26\,\text{mV}$，低频小功率管 $r_{bb'}=200\,\Omega$。

---

## 一、填空题（6 题）

**1.** BJT 的三个电极分别称为 ______ 、 ______ 、 ______ ；三个掺杂区中 ______ 区掺杂浓度最高， ______ 区最薄且掺杂浓度最低， ______ 区面积最大。

**2.** BJT 三个电极电流始终满足 KCL 关系 $I_E=$ ______ ；在放大区，集电极电流与基极电流关系为 $I_C=$ ______ ，电流放大系数 $\beta=$ ______ 。

**3.** BJT 三种工作区中，截止区要求两结 ______ 偏，放大区要求发射结 ______ 偏、集电结 ______ 偏，饱和区要求两结 ______ 偏；作放大器时工作在 ______ 区。

**4.** 共射放大电路直流通路画法：耦合电容 ______ 、直流电源 ______ ；交流通路画法：耦合电容 ______ 、直流电源 ______ 。

**5.** 共射电路电压放大倍数 $A_u=$ ______ （公式），负号表示 ______ ；输入电阻 $R_i=$ ______ ，输出电阻 $R_o\approx$ ______ 。

**6.** 分压式偏置电路稳定 Q 点利用 ______ 反馈原理，两个稳定条件是 $I_1\ge$ ______ $I_B$ 和 $U_B\ge$ ______ $\,\text{V}$（硅管）。

<details>
<summary>填空题答案</summary>

1. 发射极 E、基极 B、集电极 C；发射区；基区；集电区。
2. $I_B+I_C$；$\beta I_B$（近似，忽略 $I_{CEO}$）；$\Delta I_C/\Delta I_B$。
3. 反；正；反；正；放大。
4. 开路；保留；短路；短路到地。
5. $-\beta R_L'/r_{be}$（$R_L'=R_c\parallel R_L$）；输出与输入反相；$R_b\parallel r_{be}$；$R_c$。
6. 直流电流负；$(5\sim10)$；$(3\sim5)$。

</details>

---

## 二、选择题（6 题）

**1.** 测得 NPN 硅三极管 $U_B=0.7\,\text{V}$，$U_C=0.3\,\text{V}$，$U_E=0\,\text{V}$，它工作在（ ）
A. 放大区
B. 饱和区
C. 截止区
D. 击穿区

**2.** 共射放大电路输出电压底部削平失真（NPN 管），应如何调整偏置？（ ）
A. 增大 $R_b$
B. 减小 $R_b$
C. 增大 $R_c$
D. 减小 $V_{CC}$

**3.** 关于微变等效电路，下列说法正确的是（ ）
A. 适用于大信号和直流分析
B. 三极管输入端等效为受控电流源
C. 三极管输出端等效为受控电流源 $\beta I_b$
D. $r_{be}$ 与静态电流 $I_{EQ}$ 无关

**4.** 共集电极放大电路的主要特点是（ ）
A. 电压放大倍数大且反相
B. 输入电阻小、输出电阻大
C. 电压放大倍数近似为 1、输入电阻大、输出电阻小
D. 高频特性最好

**5.** 分压式偏置电路中，旁路电容 $C_e$ 的作用是（ ）
A. 隔断直流
B. 使 $R_e$ 仅起直流负反馈而不影响交流增益
C. 提高输入电阻
D. 增大电压放大倍数

**6.** 温度升高时，下列哪个参数变化方向与其他三项对 $I_C$ 的影响不同？（ ）
A. $\beta$ 增大
B. $I_{CBO}$ 增大
C. $U_{BE}$ 增大
D. $I_{CEO}$ 增大

<details>
<summary>选择题答案</summary>

1. **B**。$U_{BE}=0.7\,\text{V}$ 发射结正偏，$U_{CE}=0.3\,\text{V}=U_{CES}$ 且 $U_{BC}=0.4\,\text{V}>0$ 集电结正偏，两结正偏为饱和区。
2. **A**。底部削平为饱和失真（NPN 共射），Q 点过高，应增大 $R_b$ 减小 $I_B$ 使 Q 点下移。
3. **C**。微变等效电路输入端为 $r_{be}$（电阻），输出端为受控电流源 $\beta I_b$（C 对）。仅适用低频小信号（A 错），$r_{be}$ 与 $I_{EQ}$ 有关（D 错）。
4. **C**。共集（射极输出器）$A_u\approx1$ 同相、$R_i$ 大、$R_o$ 小。
5. **B**。$C_e$ 对交流短路使 $R_e$ 不参与交流通路，仅保留直流负反馈稳定 Q 点，不影响交流增益。
6. **C**。温度升高使 $U_{BE}$ **减小**（约 $-2\,\text{mV}/^\circ\text{C}$），从而 $I_B\uparrow\to I_C\uparrow$。若 $U_{BE}$ 增大反而使 $I_B$ 减小，方向相反。其余三项（$\beta\uparrow$、$I_{CBO}\uparrow$、$I_{CEO}\uparrow$）均使 $I_C$ 增大。

</details>

---

## 三、计算题（14 题）

**1.（电流关系计算）** 某 NPN 三极管处于放大区，测得 $I_B=30\,\mu\text{A}$，$I_C=3\,\text{mA}$。求 $\bar\beta$ 与 $I_E$。

<details>
<summary>解答</summary>

$$\bar\beta=\frac{I_C}{I_B}=\frac{3\times10^{-3}}{30\times10^{-6}}=100$$
$$I_E=I_B+I_C=0.03+3=3.03\,\text{mA}$$

**单位检验**：$\bar\beta$ 无量纲，$I_E$ 单位 A（mA），正确。

</details>

**2.（穿透电流）** 某硅三极管 $I_{CBO}=0.2\,\mu\text{A}$，$\beta=60$。求 $I_{CEO}$。

<details>
<summary>解答</summary>

$$I_{CEO}=(1+\beta)I_{CBO}=(1+60)\times0.2\,\mu\text{A}=61\times0.2=12.2\,\mu\text{A}$$

**单位检验**：电流 $\mu\text{A}$，正确。

</details>

**3.（工作区判定）** 测得三个 NPN 硅管各极电位（V）如下，分别判定工作区：
(a) $U_B=0.7,\,U_C=4,\,U_E=0$；(b) $U_B=0.7,\,U_C=0.3,\,U_E=0$；(c) $U_B=0,\,U_C=12,\,U_E=0$。

<details>
<summary>解答</summary>

(a) $U_{BE}=0.7\,\text{V}$ 正偏；$U_{BC}=0.7-4=-3.3\,\text{V}<0$ 反偏。发射结正偏、集电结反偏 → **放大区**。

(b) $U_{BE}=0.7\,\text{V}$ 正偏；$U_{BC}=0.7-0.3=0.4\,\text{V}>0$ 正偏。两结正偏 → **饱和区**（$U_{CE}=0.3\,\text{V}=U_{CES}$）。

(c) $U_{BE}=0\,\text{V}<0.5\,\text{V}$，发射结未导通；两结均未正偏 → **截止区**。

</details>

**4.（固定偏置 Q 点）** 共射固定偏置电路：$V_{CC}=12\,\text{V}$，$R_b=400\,\text{k}\Omega$，$R_c=4\,\text{k}\Omega$，硅管 $\beta=50$。求 Q 点并验证放大区。

<details>
<summary>解答</summary>

$$I_{BQ}=\frac{V_{CC}-U_{BEQ}}{R_b}=\frac{12-0.7}{400\times10^3}=\frac{11.3}{4\times10^5}\approx2.83\times10^{-5}\,\text{A}=28.3\,\mu\text{A}$$
$$I_{CQ}=\beta I_{BQ}=50\times28.3\,\mu\text{A}=1415\,\mu\text{A}=1.415\,\text{mA}$$
$$U_{CEQ}=V_{CC}-I_{CQ}R_c=12-1.415\times10^{-3}\times4\times10^3=12-5.66=6.34\,\text{V}$$

验证：$U_{CEQ}=6.34\,\text{V}>U_{BEQ}=0.7\,\text{V}>U_{CES}=0.3\,\text{V}$，**放大区**。

**单位检验**：$\text{V}/\Omega=\text{A}$，$\text{A}\cdot\Omega=\text{V}$，正确。

</details>

**5.（饱和判定）** 上题电路仅将 $R_b$ 改为 $80\,\text{k}\Omega$，求 Q 点并判定工作区。

<details>
<summary>解答</summary>

先按放大区假设：
$$I_{BQ}=\frac{12-0.7}{80\times10^3}\approx1.41\times10^{-4}\,\text{A}=141\,\mu\text{A}$$
$$I_{CQ}=\beta I_{BQ}=50\times141=7050\,\mu\text{A}=7.05\,\text{mA}$$
$$U_{CEQ}=12-7.05\times10^{-3}\times4\times10^3=12-28.2=-16.2\,\text{V}<0$$

不合理，说明**饱和**。重算：
$$I_{CQ}=I_{CS}=\frac{V_{CC}-U_{CES}}{R_c}=\frac{12-0.3}{4\times10^3}=2.925\,\text{mA}$$
$$U_{CEQ}=U_{CES}=0.3\,\text{V}$$
临界饱和基极电流 $I_{BS}=I_{CS}/\beta=2.925/50=58.5\,\mu\text{A}$，$I_{BQ}=141\,\mu\text{A}>I_{BS}$，深度饱和。

</details>

**6.（共射完整动态分析）** 共射电路：$V_{CC}=12\,\text{V}$，$R_b=300\,\text{k}\Omega$，$R_c=3\,\text{k}\Omega$，$R_L=3\,\text{k}\Omega$，$\beta=50$，$r_{bb'}=200\,\Omega$。求 $A_u,R_i,R_o$。

<details>
<summary>解答</summary>

静态：$I_{BQ}=37.7\,\mu\text{A}$，$I_{CQ}=1.885\,\text{mA}$，$I_{EQ}\approx1.885\,\text{mA}$。
$$r_{be}=200+51\times\frac{26}{1.885}=200+703=903\,\Omega\approx0.903\,\text{k}\Omega$$
$$R_L'=R_c\parallel R_L=3\parallel3=1.5\,\text{k}\Omega$$
$$A_u=-\frac{\beta R_L'}{r_{be}}=-\frac{50\times1.5}{0.903}\approx-83.1$$
$$R_i=R_b\parallel r_{be}\approx r_{be}=0.903\,\text{k}\Omega$$
$$R_o\approx R_c=3\,\text{k}\Omega$$

**单位检验**：$r_{be},R_i,R_o$ 单位 $\Omega$，$A_u$ 无量纲，正确。

</details>

**7.（负载对增益影响）** 上题电路负载开路时求 $A_u$，并与带载比较。

<details>
<summary>解答</summary>

开路 $R_L'=\infty\parallel3=3\,\text{k}\Omega=R_c$：
$$A_u=-\frac{50\times3}{0.903}\approx-166$$
带载 $A_u\approx-83$，开路 $A_u\approx-166$，接入负载使增益降到约一半（因 $R_L=R_c$，并联后减半）。

</details>

**8.（$r_{be}$ 计算）** $\beta=80$，$I_{EQ}=2\,\text{mA}$，$r_{bb'}=200\,\Omega$。求 $r_{be}$。

<details>
<summary>解答</summary>

$$r_{be}=r_{bb'}+(1+\beta)\frac{U_T}{I_{EQ}}=200+81\times\frac{26}{2}=200+81\times13=200+1053=1253\,\Omega\approx1.25\,\text{k}\Omega$$

**单位检验**：$\Omega+\Omega=\Omega$，正确。

</details>

**9.（射极输出器动态分析）** 共集电路：$V_{CC}=12\,\text{V}$，$R_b=200\,\text{k}\Omega$，$R_e=2\,\text{k}\Omega$，$R_L=2\,\text{k}\Omega$，$\beta=60$，$r_{bb'}=200\,\Omega$，$R_s=1\,\text{k}\Omega$。求 $A_u,R_i,R_o$。

<details>
<summary>解答</summary>

静态（共集电路 $I_B$ 公式含 $(1+\beta)R_e$）：
$$I_{BQ}=\frac{V_{CC}-U_{BEQ}}{R_b+(1+\beta)R_e}=\frac{11.3}{200+61\times2}=\frac{11.3}{322}\,\text{mA}\approx35.1\,\mu\text{A}$$
$$I_{EQ}\approx(1+\beta)I_{BQ}=61\times35.1=2141\,\mu\text{A}\approx2.14\,\text{mA}$$
$$r_{be}=200+61\times\frac{26}{2.14}\approx200+741=941\,\Omega\approx0.941\,\text{k}\Omega$$
动态：
$$R_L'=R_e\parallel R_L=2\parallel2=1\,\text{k}\Omega$$
$$A_u=\frac{(1+\beta)R_L'}{r_{be}+(1+\beta)R_L'}=\frac{61\times1}{0.941+61}=\frac{61}{61.941}\approx0.985$$
$$R_i=R_b\parallel[r_{be}+(1+\beta)R_L']=200\parallel(0.941+61)=200\parallel61.9\approx47.3\,\text{k}\Omega$$
$$R_s'=R_s\parallel R_b\approx R_s=1\,\text{k}\Omega$$
$$R_o\approx R_e\parallel\frac{r_{be}+R_s'}{1+\beta}=2\parallel\frac{0.941+1}{61}\approx2\parallel0.0318\approx0.0318\,\text{k}\Omega=31.8\,\Omega$$

结果：$A_u\approx0.985$（同相跟随），$R_i\approx47.3\,\text{k}\Omega$（大），$R_o\approx31.8\,\Omega$（小）。

**单位检验**：$\Omega$ 与 $\text{k}\Omega$，$A_u$ 无量纲，正确。

</details>

**10.（共基动态分析）** 共基电路：$r_{be}=1\,\text{k}\Omega$，$\beta=50$，$R_c=3\,\text{k}\Omega$，$R_e=1\,\text{k}\Omega$，$R_L=3\,\text{k}\Omega$。求 $A_u,R_i,R_o$。

<details>
<summary>解答</summary>

$$R_L'=R_c\parallel R_L=3\parallel3=1.5\,\text{k}\Omega$$
$$A_u=\frac{\beta R_L'}{r_{be}}=\frac{50\times1.5}{1}=75\quad(\text{同相})$$
$$R_i=R_e\parallel\frac{r_{be}}{1+\beta}=1\parallel\frac{1}{51}\approx0.0196\,\text{k}\Omega=19.6\,\Omega$$
$$R_o\approx R_c=3\,\text{k}\Omega$$

**单位检验**：$\text{k}\Omega\parallel\text{k}\Omega=\text{k}\Omega$，$A_u$ 无量纲，正确。

</details>

**11.（分压式偏置 Q 点）** 分压式偏置电路：$V_{CC}=12\,\text{V}$，$R_{b1}=30\,\text{k}\Omega$，$R_{b2}=10\,\text{k}\Omega$，$R_c=2\,\text{k}\Omega$，$R_e=1\,\text{k}\Omega$，$\beta=50$。求 Q 点并验证放大区，检验稳定条件。

<details>
<summary>解答</summary>

$$U_{BQ}\approx V_{CC}\cdot\frac{R_{b2}}{R_{b1}+R_{b2}}=12\times\frac{10}{40}=3\,\text{V}$$
$$U_{EQ}=U_{BQ}-U_{BEQ}=3-0.7=2.3\,\text{V}$$
$$I_{EQ}=\frac{U_{EQ}}{R_e}=\frac{2.3}{1\times10^3}=2.3\,\text{mA},\quad I_{CQ}\approx2.3\,\text{mA}$$
$$I_{BQ}=\frac{I_{CQ}}{\beta}=\frac{2.3}{50}=0.046\,\text{mA}=46\,\mu\text{A}$$
$$U_{CEQ}=V_{CC}-I_{CQ}R_c-U_{EQ}=12-2.3\times2-2.3=12-4.6-2.3=5.1\,\text{V}$$

验证：$U_{CEQ}=5.1\,\text{V}>U_{BEQ}=0.7\,\text{V}>U_{CES}=0.3\,\text{V}$，**放大区**。

稳定条件：
- $I_1\approx V_{CC}/(R_{b1}+R_{b2})=12/40=0.3\,\text{mA}=300\,\mu\text{A}$，$I_1/I_B=300/46\approx6.5\ge5$，满足；
- $U_B=3\,\text{V}\ge3\,\text{V}$，满足。
设计合理。

**单位检验**：V、A、$\Omega$ 自洽。

</details>

**12.（分压式动态分析）** 上题电路，$r_{bb'}=200\,\Omega$，$R_L=2\,\text{k}\Omega$，有 $C_e$ 旁路。求 $A_u,R_i,R_o$。

<details>
<summary>解答</summary>

$$r_{be}=200+51\times\frac{26}{2.3}=200+51\times11.3\approx200+576=776\,\Omega\approx0.776\,\text{k}\Omega$$
$$R_L'=R_c\parallel R_L=2\parallel2=1\,\text{k}\Omega$$
$$A_u=-\frac{\beta R_L'}{r_{be}}=-\frac{50\times1}{0.776}\approx-64.4$$
$$R_i=R_{b1}\parallel R_{b2}\parallel r_{be}=30\parallel10\parallel0.776$$
$30\parallel10=7.5\,\text{k}\Omega$，$7.5\parallel0.776\approx0.703\,\text{k}\Omega=703\,\Omega$。
$$R_o\approx R_c=2\,\text{k}\Omega$$

**单位检验**：$\Omega$ 与 $\text{k}\Omega$，$A_u$ 无量纲，正确。

</details>

**13.（无 $C_e$ 时增益）** 上题电路若 $C_e$ 开路失效，重新求 $A_u$ 与 $R_i$，并与有 $C_e$ 对比。

<details>
<summary>解答</summary>

无 $C_e$ 时 $R_e$ 参与交流：
$$A_u=-\frac{\beta R_L'}{r_{be}+(1+\beta)R_e}=-\frac{50\times1}{0.776+51\times1}=-\frac{50}{51.776}\approx-0.966$$
$$R_i=R_{b1}\parallel R_{b2}\parallel[r_{be}+(1+\beta)R_e]=30\parallel10\parallel(0.776+51)$$
$30\parallel10=7.5\,\text{k}\Omega$，$7.5\parallel51.776\approx6.55\,\text{k}\Omega$。

对比：有 $C_e$ 时 $A_u\approx-64.4$、$R_i\approx703\,\Omega$；无 $C_e$ 时 $A_u\approx-0.966$、$R_i\approx6.55\,\text{k}\Omega$。无 $C_e$ 使增益降到约 $1/67$，输入电阻增大约 9 倍——$R_e$ 引入交流负反馈，牺牲增益换取高输入电阻与稳定性。

**单位检验**：$\Omega$ 与 $\text{k}\Omega$，$A_u$ 无量纲，正确。

</details>

**14.（温度稳定性对比）** 固定偏置电路 $\beta=50$，$I_{BQ}=40\,\mu\text{A}$，$I_{CQ}=2\,\text{mA}$。温度升高使 $\beta$ 增至 60（$I_B$ 不变）。求 $I_C$ 变化量与相对变化。若改用分压式偏置（$U_{BQ}=3\,\text{V}$，$R_e=1\,\text{k}\Omega$，$U_{BEQ}$ 由 $0.7\,\text{V}$ 降至 $0.6\,\text{V}$，$\beta$ 同样变化），求 $I_C$ 变化量与相对变化（原 $I_{CQ}=2.3\,\text{mA}$），并对比稳定性。

<details>
<summary>解答</summary>

**固定偏置**：
$$I_C'=\beta' I_B=60\times40=2400\,\mu\text{A}=2.4\,\text{mA}$$
$$\Delta I_C=2.4-2.0=0.4\,\text{mA},\quad \frac{\Delta I_C}{I_C}=\frac{0.4}{2.0}=20\%$$

**分压式偏置**：$\beta$ 变化不影响 $I_C$（公式不含 $\beta$），仅 $U_{BE}$ 变化影响。
$$U_{EQ}'=U_{BQ}-U_{BEQ}'=3-0.6=2.4\,\text{V}$$
$$I_{EQ}'=\frac{2.4}{1\times10^3}=2.4\,\text{mA},\quad I_{CQ}'\approx2.4\,\text{mA}$$
$$\Delta I_C=2.4-2.3=0.1\,\text{mA},\quad \frac{\Delta I_C}{I_C}=\frac{0.1}{2.3}\approx4.3\%$$

**对比**：固定偏置 $I_C$ 变化 $20\%$，分压式偏置仅 $4.3\%$，稳定性显著改善；且分压式中 $\beta$ 变化对 $I_C$ 几乎无影响。

**单位检验**：电流 mA，比例无量纲，正确。

</details>

---

## 四、分析题（2 题）

**1.（失真分析与 Q 点调整）** 某共射放大电路（NPN 管）输入正弦信号，用示波器观察到输出波形出现失真：
(a) 若输出电压 $u_o$ 底部（低电平）削平，是何种失真？Q 点偏高还是偏低？应如何调整 $R_b$？
(b) 若输出电压 $u_o$ 顶部（高电平）削平，是何种失真？Q 点偏高还是偏低？应如何调整 $R_b$？
(c) 若 Q 点已位于放大区中点，但增大输入信号后正负半周同时削平，说明什么？

<details>
<summary>分析</summary>

(a) NPN 共射电路输出底部削平，对应 $u_{CE}$ 底部（低电平）被削——**饱和失真**。此时 Q 点偏高（$I_{CQ}$ 偏大、$U_{CEQ}$ 偏小，靠近饱和区）。应**增大 $R_b$** 减小 $I_B$，使 Q 点沿直流负载线下移至放大区中部。

(b) 输出顶部削平，对应 $u_{CE}$ 顶部（高电平）被削——**截止失真**。此时 Q 点偏低（$I_{CQ}$ 偏小、$U_{CEQ}$ 偏大，靠近截止区）。应**减小 $R_b$** 增大 $I_B$，使 Q 点上移至放大区中部。

(c) Q 点在中点但信号过大导致双向削平，说明**输入信号幅度超过电路最大不失真动态范围**，并非 Q 点设置问题。解决方法是减小输入信号幅度，或提高电源电压 $V_{CC}$、调整 $R_c$ 以扩展动态范围。

> [!note] 失真判定要领
> NPN 共射电路："**饱和削底，截止削顶**"——因饱和时 $i_C$ 上不去（$u_{CE}$ 下不去），截止时 $i_C$ 下不去（$u_{CE}$ 上不去）。PNP 极性相反，失真方向也相反。调整方向：饱和增大 $R_b$，截止减小 $R_b$，目标是将 Q 点设在放大区中点（直流负载线放大段中点）以获得最大动态范围。

</details>

**2.（分压式偏置电路故障分析）** 分压式偏置共射放大电路：$V_{CC}=12\,\text{V}$，$R_{b1}=30\,\text{k}\Omega$，$R_{b2}=10\,\text{k}\Omega$，$R_c=2\,\text{k}\Omega$，$R_e=1\,\text{k}\Omega$，$\beta=50$。正常工作时 $U_B\approx3\,\text{V}$。现测得以下几种故障现象，分别分析原因：
(a) 测得 $U_B=12\,\text{V}$，$U_C=12\,\text{V}$，$U_E=0\,\text{V}$；
(b) 测得 $U_B=0\,\text{V}$，$U_C=12\,\text{V}$，$U_E=0\,\text{V}$；
(c) 测得 $U_B=3\,\text{V}$，$U_C=12\,\text{V}$，$U_E=0\,\text{V}$；
(d) 测得 $U_B=3\,\text{V}$，$U_C=0.3\,\text{V}$，$U_E=2.3\,\text{V}$（正常）。

<details>
<summary>分析</summary>

正常情况：$U_B\approx3\,\text{V}$，$U_E\approx2.3\,\text{V}$，$I_C\approx2.3\,\text{mA}$，$U_C=V_{CC}-I_C R_c=12-4.6=7.4\,\text{V}$，$U_{CE}=7.4-2.3=5.1\,\text{V}$（放大区）。

(a) $U_B=12\,\text{V}=V_{CC}$：说明 $R_{b1}$ 短路或 $R_{b2}$ 开路，基极直接接 $V_{CC}$。$U_E=0$ 表明无发射极电流，三极管截止。$U_C=12\,\text{V}=V_{CC}$ 也说明 $I_C=0$（$R_c$ 无压降）。可能原因：**$R_{b2}$ 开路（脱焊）或基极内部断线**，使基极悬空或直接接 $V_{CC}$ 但无基极电流（若 $R_{b2}$ 开路，$U_B$ 由 $R_{b1}$ 与 BJT 输入电阻分压，可能接近 $V_{CC}$；若 $R_{b1}$ 短路则 $U_B=V_{CC}$ 但发射结会因过流损坏）。最可能：**$R_{b1}$ 短路**使 $U_B=V_{CC}$，发射结正偏但因 $R_e$ 限流 $I_E$ 应不为零——若 $U_E=0$ 则发射结开路。综合判断：**三极管发射结损坏（断路）**。

(b) $U_B=0\,\text{V}$：基极无偏置电压。可能原因：**$R_{b1}$ 开路**（脱焊），或基极对地短路。此时发射结无正偏，三极管截止，$I_C=0$，$U_C=V_{CC}=12\,\text{V}$，$U_E=0$。结论：**$R_{b1}$ 开路或基极接地短路**。

(c) $U_B=3\,\text{V}$ 正常但 $U_E=0\,\text{V}$：说明 $U_{BE}=3\,\text{V}\gg0.7\,\text{V}$ 远超正常值，发射结应导通但 $I_E=0$——**三极管发射结断路损坏**（或发射极内部断线）。因 $I_C=0$，$U_C=V_{CC}=12\,\text{V}$。结论：**BJT 发射结损坏（C-E 间断路）**。

(d) $U_B=3\,\text{V}$，$U_E=2.3\,\text{V}$ 正常，但 $U_C=0.3\,\text{V}=U_{CES}$：说明 $I_C$ 过大三极管深度饱和。$U_{CE}=U_C-U_E=0.3-2.3=-2\,\text{V}<0$，不正常（NPN 应 $U_C>U_E$）。可能原因：**集电极电阻 $R_c$ 短路**（$U_C$ 被钳在低电位）或负载过重、$\beta$ 异常增大使 Q 点进入饱和。若 $R_c$ 短路则 $U_C$ 应等于 $V_{CC}=12\,\text{V}$ 而非 $0.3\,\text{V}$，故排除。更可能是**三极管 C-E 间击穿短路**（$U_{CE}\approx0$），集电极直接经 $R_e$ 到地，$U_C\approx U_E+0.3$ 但实测 $U_C<U_E$ 不符——需重新审视。若 $R_c$ 正常，$U_C=0.3$ 表明 $I_C=(12-0.3)/2=5.85\,\text{mA}$，但 $I_B$ 由偏置决定约 $46\,\mu\text{A}$，$\beta I_B=2.3\,\text{mA}\ll5.85\,\text{mA}$，说明 $I_C$ 不受 $I_B$ 控制——**C-E 间击穿短路**。

> [!note] 故障分析要领
> 分压式偏置电路故障诊断的关键测量点是 $U_B,U_E,U_C$：
> - $U_B$ 异常 → 偏置电阻 $R_{b1},R_{b2}$ 故障；
> - $U_{BE}=U_B-U_E$ 远偏离 $0.7\,\text{V}$（硅管）→ 发射结损坏；
> - $U_{CE}=U_C-U_E$ 过小（接近 0 或负值）→ 饱和或 C-E 击穿；
> - $U_C\approx V_{CC}$ → 截止（$I_C=0$）。
> 正常放大区：$U_{BE}\approx0.7\,\text{V}$，$U_{CE}>0.7\,\text{V}$，$U_C>U_B>U_E$（NPN）。

</details>

---

## 考点统计表

| 知识点 | 涉及题号 | 题数 | 难度分布 |
| :--- | :--- | :---: | :--- |
| [[5.1 BJT 三极管结构、放大原理、三种工作区\|BJT 结构与电流关系]] | 填空1、填空2、计算1 | 3 | 易 |
| [[5.1 BJT 三极管结构、放大原理、三种工作区\|穿透电流 $I_{CEO}$]] | 计算2 | 1 | 易 |
| [[5.1 BJT 三极管结构、放大原理、三种工作区\|三种工作区判定]] | 选择1、计算3 | 2 | 中 |
| [[5.1 BJT 三极管结构、放大原理、三种工作区\|温度对参数影响]] | 选择6、计算14 | 2 | 中 |
| [[5.2 共射放大电路静态分析、Q 点计算\|固定偏置 Q 点计算]] | 填空3、计算4 | 2 | 中 |
| [[5.2 共射放大电路静态分析、Q 点计算\|饱和判定与重算]] | 计算5 | 1 | 中 |
| [[5.2 共射放大电路静态分析、Q 点计算\|Q 点与失真]] | 选择2、分析1 | 2 | 中 |
| [[5.3 微变等效电路、电压放大倍数计算\|交流通路与直流通路画法]] | 填空4 | 1 | 易 |
| [[5.3 微变等效电路、电压放大倍数计算\|$r_{be}$ 计算]] | 计算8 | 1 | 中 |
| [[5.3 微变等效电路、电压放大倍数计算\|电压放大倍数与 $R_i,R_o$]] | 填空5、计算6、计算7 | 3 | 中 |
| [[5.4 共集、共基放大电路特点\|共集电路动态分析]] | 选择4、计算9 | 2 | 中-难 |
| [[5.4 共集、共基放大电路特点\|共基电路动态分析]] | 计算10 | 1 | 中 |
| [[5.4 共集、共基放大电路特点\|三种组态特点]] | 选择4 | 1 | 中 |
| [[5.5 分压式静态工作点稳定电路\|分压式偏置 Q 点]] | 填空6、计算11 | 2 | 中 |
| [[5.5 分压式静态工作点稳定电路\|分压式动态分析]] | 计算12、计算13 | 2 | 中-难 |
| [[5.5 分压式静态工作点稳定电路\|旁路电容 $C_e$ 作用]] | 选择5、计算13 | 2 | 中 |
| [[5.5 分压式静态工作点稳定电路\|温度稳定性对比]] | 计算14 | 1 | 中-难 |
| [[5.5 分压式静态工作点稳定电路\|故障分析]] | 分析2 | 1 | 难 |
| 合计 | — | 28 | — |

> [!tip] 复习建议
> - **BJT 工作区判定**（选择1、计算3）是核心考点，务必掌握"先看发射结是否正偏导通，再看集电结偏置"的两步法，记住 $U_{CE}>U_{BE}$ 放大、$U_{CE}<U_{BE}$ 饱和；
> - **电流关系与 $\beta$**（填空1、2、计算1、2）记牢 $I_E=I_B+I_C$、$I_C=\beta I_B$、$I_{CEO}=(1+\beta)I_{CBO}$；
> - **固定偏置 Q 点**（计算4、5）必会公式 $I_{BQ}=(V_{CC}-U_{BEQ})/R_b$，且务必验证放大区，发现 $U_{CEQ}<0$ 要按饱和区重算；
> - **微变等效电路**（填空4、5、计算6、7、8）是重点，三步法（静态 → $r_{be}$ → 动态）要熟练，$A_u=-\beta R_L'/r_{be}$ 负号不能漏，$R_i$ 含 $R_b$ 并联；
> - **共集/共基特点**（选择4、计算9、10）掌握对比表，共集 $A_u\approx1$、$R_i$ 大、$R_o$ 小；共基 $A_u$ 大同相、$R_i$ 小、高频好；
> - **分压式偏置**（填空6、计算11、12、13、14、分析2）是重点也是难点，Q 点公式 $U_B\approx V_{CC}R_{b2}/(R_{b1}+R_{b2})$、$I_E=(U_B-U_{BE})/R_e$ 必背，注意 $U_{CEQ}=V_{CC}-I_C R_c-U_E$ 多一项 $U_E$；$C_e$ 有无对 $A_u$ 影响极大，需区分公式；
> - **失真与故障分析**（选择2、分析1、分析2）是综合应用题，需将 Q 点位置、波形削平方向、故障现象与电路参数联系起来理解。

## 章节导航

> [!nav] 导航
> [[MOC - 第5章|第5章 知识点目录]] · [[MOC - 电路与模拟电子技术|课程总览]] · 上一章习题：[[MOC - 第4章习题|第4章 半导体二极管与稳压管习题]] · 下一章习题：[[MOC - 第6章习题|第6章 场效应管与 FET 放大电路习题]]
