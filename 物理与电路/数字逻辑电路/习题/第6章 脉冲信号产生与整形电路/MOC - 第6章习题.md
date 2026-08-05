---
domain: 物理与电路
subject: 数字逻辑电路
type: exercise
chapter: 第6章 脉冲信号产生与整形电路
tags: [数字逻辑,数电习题,脉冲整形,555定时器,施密特,单稳态,多谐振荡器]
prerequisites: ["电路与模拟电子技术"]
aliases: [第6章习题, 脉冲电路习题, 555定时器习题]
---

# MOC - 第6章习题 脉冲信号产生与整形电路

> [!abstract] 本章习题概览
> 本章习题共 **18 题**，覆盖 [[6.1 施密特触发器|施密特触发器]]、[[6.2 单稳态触发器|单稳态触发器]]、[[6.3 多谐振荡器|多谐振荡器]]、[[6.4 555 定时器原理与应用|555 定时器]] 四个知识板块。题型分布：选择 6 题、填空 4 题、分析计算 8 题。重点考查回差电压计算、暂稳态时间 $t_w$、振荡周期 $T$ 与占空比 $q$ 的推导，以及 555 三种应用电路的参数设计。答案与详解折叠于 `<details>` 中，建议先独立作答再核对。

---

## 一、选择题（6 题）

**1.** 施密特触发器的最主要特征是（ ）
A. 有两个暂稳态，自动产生矩形波
B. 有一个稳态和一个暂稳态，触发后返回
C. 有两个稳态，靠电平触发翻转，且有回差电压
D. 无稳态，自激振荡

**2.** 单稳态触发器的暂稳态持续时间 $t_w$ 主要取决于（ ）
A. 触发脉冲的宽度
B. 触发脉冲的幅度
C. 定时元件 $R$、$C$ 的参数
D. 电源电压 $V_{CC}$

**3.** 微分型单稳态触发器的暂稳态时间约为（ ）
A. $0.7RC$
B. $1.1RC$
C. $1.4RC$
D. $2.2RC$

**4.** 由 555 定时器构成的多谐振荡器，其占空比 $q$ 满足（ ）
A. $q$ 恒等于 50%
B. $q$ 恒大于 50%
C. $q$ 恒小于 50%
D. $q$ 可为任意值且与 $R_1$、$R_2$ 无关

**5.** 555 定时器构成施密特触发器时（5 脚不外接电压），回差电压 $\Delta U_T$ 为（ ）
A. $\tfrac{1}{3}V_{CC}$
B. $\tfrac{2}{3}V_{CC}$
C. $\tfrac{1}{2}V_{CC}$
D. $V_{CC}$

**6.** 下列关于石英晶体多谐振荡器的叙述，正确的是（ ）
A. 振荡频率由外接 RC 决定，调节方便
B. 振荡频率由石英晶体决定，频率稳定度高
C. 不需要电源即可起振
D. 输出波形为正弦波

<details>
<summary>选择题答案</summary>

1. **C**。施密特触发器有两个稳态、靠电平触发、具有回差电压。A 是多谐振荡器；B 是单稳态触发器；D 是多谐振荡器。
2. **C**。$t_w$ 由定时元件 $R$、$C$ 决定，与触发脉冲宽度、幅度几乎无关。
3. **A**。微分型 $t_w\approx0.7RC$；积分型 $t_w\approx1.1RC$。
4. **B**。基本 555 多谐振荡器充电经 $R_1+R_2$、放电只经 $R_2$，$T_1>T_2$，故 $q=\tfrac{R_1+R_2}{R_1+2R_2}>50\%$。要 $q<50\%$ 需加二极管。
5. **A**。$U_{T+}=\tfrac{2}{3}V_{CC}$、$U_{T-}=\tfrac{1}{3}V_{CC}$，$\Delta U_T=\tfrac{2}{3}V_{CC}-\tfrac{1}{3}V_{CC}=\tfrac{1}{3}V_{CC}$。
6. **B**。石英晶体的谐振频率极其稳定（$10^{-6}$ 量级以上），振荡频率由晶体决定而非 RC。A 错：RC 振荡器才由 RC 决定；C 错：必须供电；D 错：输出仍是矩形波。

</details>

---

## 二、填空题（4 题）

**1.** 施密特触发器的正向阈值电压 $U_{T+}=\text{______}$、负向阈值电压 $U_{T-}=\text{______}$（设 555 构成、$V_{CC}=12\,\text{V}$、5 脚不外接），回差电压 $\Delta U_T=\text{______}$。

**2.** 74LS121 集成单稳态触发器，外接 $R_{ext}=20\,\text{k}\Omega$、$C_{ext}=0.1\,\mu\text{F}$，输出脉宽 $t_w\approx\text{______}$。

**3.** 对称型多谐振荡器，$R=20\,\text{k}\Omega$、$C=0.01\,\mu\text{F}$，振荡周期 $T\approx\text{______}$，频率 $f\approx\text{______}$。

**4.** 555 定时器构成多谐振荡器，$R_1=R_2=10\,\text{k}\Omega$、$C=0.1\,\mu\text{F}$，振荡周期 $T\approx\text{______}$，占空比 $q\approx\text{______}$。

<details>
<summary>填空题答案</summary>

1. $U_{T+}=\tfrac{2}{3}V_{CC}=\tfrac{2}{3}\times12=8\,\text{V}$；$U_{T-}=\tfrac{1}{3}V_{CC}=\tfrac{1}{3}\times12=4\,\text{V}$；$\Delta U_T=8-4=4\,\text{V}$。
2. $t_w\approx0.7R_{ext}C_{ext}=0.7\times20\times10^3\times0.1\times10^{-6}=1.4\times10^{-3}\,\text{s}=1.4\,\text{ms}$。
   - 单位检验：$\text{k}\Omega\cdot\mu\text{F}=\text{ms}$，$0.7\times2=1.4\,\text{ms}$ ✓
3. $T\approx1.4RC=1.4\times20\times10^3\times0.01\times10^{-6}=2.8\times10^{-4}\,\text{s}=0.28\,\text{ms}=280\,\mu\text{s}$；
   $f=1/T\approx1/0.28\,\text{ms}\approx3.57\,\text{kHz}$。
   - 单位检验：$20\times0.01\times\text{ms}=0.2\,\text{ms}$，$1.4\times0.2=0.28\,\text{ms}$ ✓
4. $T=0.693(R_1+2R_2)C=0.693\times(10+2\times10)\times10^3\times0.1\times10^{-6}=0.693\times3\times10^{-3}=2.079\,\text{ms}$；
   $q=\tfrac{R_1+R_2}{R_1+2R_2}=\tfrac{10+10}{10+20}=\tfrac{20}{30}\approx66.7\%$。
   - 单位检验：$\text{k}\Omega\cdot\mu\text{F}=\text{ms}$，$0.693\times30\times0.1=2.079\,\text{ms}$ ✓

</details>

---

## 三、分析计算题（8 题）

**1.（施密特回差计算）** 由 CMOS 反相器构成的施密特触发器，$V_{DD}=10\,\text{V}$，反相器阈值 $U_{TH}=5\,\text{V}$，反馈电阻 $R_1=10\,\text{k}\Omega$、$R_2=50\,\text{k}\Omega$。求 $U_{T+}$、$U_{T-}$、$\Delta U_T$。

<details>
<summary>解答</summary>

由 CMOS 型施密特阈值公式：

$$U_{T+}=\left(1+\frac{R_1}{R_2}\right)U_{TH}=\left(1+\frac{10}{50}\right)\times5=1.2\times5=6\,\text{V}$$

$$U_{T-}=\left(1-\frac{R_1}{R_2}\right)U_{TH}=\left(1-\frac{10}{50}\right)\times5=0.8\times5=4\,\text{V}$$

$$\boxed{\Delta U_T=U_{T+}-U_{T-}=6-4=2\,\text{V}}$$

**单位检验**：阈值电压单位为 $\text{V}$，$R_1/R_2$ 无量纲 ✓
**说明**：回差 $\Delta U_T=\tfrac{2R_1}{R_2}U_{TH}=\tfrac{2\times10}{50}\times5=2\,\text{V}$ ✓ 一致。

</details>

**2.（单稳态时间计算）** 微分型单稳态触发器，$R=30\,\text{k}\Omega$、$C=0.01\,\mu\text{F}$。求暂稳态时间 $t_w$。

<details>
<summary>解答</summary>

微分型单稳态触发器：

$$t_w \approx 0.7\,RC = 0.7 \times 30\times10^3 \times 0.01\times10^{-6}$$

$$= 0.7 \times 3\times10^{-4} = 2.1\times10^{-4}\,\text{s} = 0.21\,\text{ms}$$

**单位检验**：用快捷量纲 $\text{k}\Omega\cdot\mu\text{F}=\text{ms}$：
$$RC = 30\times0.01 = 0.3\,\text{ms}$$
$$t_w = 0.7\times0.3 = 0.21\,\text{ms}\;\checkmark$$

（用 $\Omega\cdot\text{F}=\text{s}$ 核算：$30\times10^3\times0.01\times10^{-6}=3\times10^{-4}\,\text{s}=0.3\,\text{ms}$，一致 ✓）

$$\boxed{t_w \approx 0.21\,\text{ms}}$$

**说明**：若误用积分型公式 $1.1RC$ 会得 $1.1\times0.3=0.33\,\text{ms}$，注意区分电路类型。

</details>

**3.（多谐振荡周期计算）** 对称型多谐振荡器，$R=15\,\text{k}\Omega$、$C=0.047\,\mu\text{F}$。求振荡周期 $T$ 和频率 $f$。

<details>
<summary>解答</summary>

对称型多谐振荡器（占空比 50%）：

$$T \approx 1.4\,RC = 1.4 \times 15\times10^3 \times 0.047\times10^{-6}$$

$$= 1.4 \times 7.05\times10^{-4} = 9.87\times10^{-4}\,\text{s} = 0.987\,\text{ms}$$

$$f = \frac{1}{T} = \frac{1}{9.87\times10^{-4}} \approx 1013\,\text{Hz} \approx 1.01\,\text{kHz}$$

$$\boxed{T \approx 0.987\,\text{ms},\quad f \approx 1.01\,\text{kHz}}$$

**单位检验**：用快捷量纲 $\text{k}\Omega\cdot\mu\text{F}=\text{ms}$：
$$RC = 15\times0.047 = 0.705\,\text{ms}$$
$$T = 1.4\times0.705 = 0.987\,\text{ms}\;\checkmark$$
$$f = \frac{1}{0.987\,\text{ms}} = \frac{1000}{0.987}\,\text{Hz} \approx 1013\,\text{Hz}\;\checkmark$$

**说明**：计算时统一量纲，$\text{k}\Omega\cdot\mu\text{F}=\text{ms}$ 最不易出错，避免指数运算出错。

</details>

**4.（555 施密特应用）** 用 555 定时器构成施密特触发器，$V_{CC}=9\,\text{V}$，5 脚不外接电压。求 $U_{T+}$、$U_{T-}$、$\Delta U_T$。若要把回差减小为 $\tfrac{1}{4}V_{CC}$，应在 5 脚加多大的控制电压 $U_{CO}$？

<details>
<summary>解答</summary>

**(1) 5 脚不外接时**：

$$U_{T+}=\frac{2}{3}V_{CC}=\frac{2}{3}\times9=6\,\text{V}$$

$$U_{T-}=\frac{1}{3}V_{CC}=\frac{1}{3}\times9=3\,\text{V}$$

$$\Delta U_T=6-3=3\,\text{V}=\frac{1}{3}V_{CC}$$

**(2) 5 脚加控制电压 $U_{CO}$ 时**：两阈值变为 $U_{T+}=U_{CO}$、$U_{T-}=\tfrac{1}{2}U_{CO}$，回差：

$$\Delta U_T = U_{CO}-\frac{1}{2}U_{CO}=\frac{1}{2}U_{CO}$$

要求 $\Delta U_T=\tfrac{1}{4}V_{CC}=\tfrac{1}{4}\times9=2.25\,\text{V}$：

$$\frac{1}{2}U_{CO}=2.25 \Rightarrow U_{CO}=4.5\,\text{V}$$

此时 $U_{T+}=4.5\,\text{V}$、$U_{T-}=2.25\,\text{V}$。

$$\boxed{U_{CO}=4.5\,\text{V}}$$

**单位检验**：电压单位 $\text{V}$，比例关系无量纲 ✓
**说明**：5 脚加控制电压可线性调节回差，是 555 施密特的优势之一。

</details>

**5.（555 单稳态设计）** 用 555 定时器构成单稳态触发器，要求输出脉宽 $t_w=1\,\text{s}$。若取 $C=10\,\mu\text{F}$，求定时电阻 $R$。

<details>
<summary>解答</summary>

555 单稳态触发器：

$$t_w \approx 1.1\,RC \Rightarrow R = \frac{t_w}{1.1\,C}$$

$$R = \frac{1}{1.1 \times 10\times10^{-6}} = \frac{1}{1.1\times10^{-5}} = \frac{10^5}{1.1} \approx 90.9\times10^3\,\Omega \approx 91\,\text{k}\Omega$$

**单位检验**：$t_w$ 用 $\text{s}$、$C$ 用 $\text{F}$，$R=t_w/(1.1C)$ 单位为 $\Omega$：
$$\frac{1}{1.1\times10\times10^{-6}}=\frac{1}{1.1\times10^{-5}}\approx9.09\times10^4\,\Omega=90.9\,\text{k}\Omega\;\checkmark$$

$$\boxed{R \approx 91\,\text{k}\Omega}$$

**验证**：$t_w=1.1\times91\times10^3\times10\times10^{-6}=1.1\times0.91=1.001\,\text{s}\approx1\,\text{s}$ ✓
**说明**：实际取标称电阻 $91\,\text{k}\Omega$ 或 $100\,\text{k}\Omega$（后者得 $1.1\,\text{s}$）。

</details>

**6.（555 多谐振荡器综合计算）** 用 555 定时器构成多谐振荡器，$R_1=10\,\text{k}\Omega$、$R_2=20\,\text{k}\Omega$、$C=0.1\,\mu\text{F}$。求：(1) 振荡周期 $T$；(2) 频率 $f$；(3) 占空比 $q$；(4) 高电平时间 $T_1$ 和低电平时间 $T_2$。

<details>
<summary>解答</summary>

**(1) 振荡周期**：

$$T = 0.693\,(R_1+2R_2)\,C = 0.693 \times (10+2\times20)\times10^3 \times 0.1\times10^{-6}$$

$$= 0.693 \times 50\times10^3 \times 10^{-7} = 0.693 \times 5\times10^{-3} = 3.465\times10^{-3}\,\text{s}$$

$$\boxed{T \approx 3.465\,\text{ms}}$$

**(2) 频率**：

$$f = \frac{1}{T} = \frac{1}{3.465\times10^{-3}} \approx 288.6\,\text{Hz}$$

$$\boxed{f \approx 289\,\text{Hz}}$$

**(3) 占空比**：

$$q = \frac{R_1+R_2}{R_1+2R_2} = \frac{10+20}{10+40} = \frac{30}{50} = 0.6 = 60\%$$

$$\boxed{q = 60\%}$$

**(4) 高低电平时间**：

$$T_1 = 0.693\,(R_1+R_2)\,C = 0.693 \times 30\times10^3 \times 0.1\times10^{-6} = 0.693 \times 3\times10^{-3} = 2.079\,\text{ms}$$

$$T_2 = 0.693\,R_2\,C = 0.693 \times 20\times10^3 \times 0.1\times10^{-6} = 0.693 \times 2\times10^{-3} = 1.386\,\text{ms}$$

**单位检验**：$\text{k}\Omega\cdot\mu\text{F}=\text{ms}$。
- $T_1=0.693\times30\times0.1=2.079\,\text{ms}$ ✓
- $T_2=0.693\times20\times0.1=1.386\,\text{ms}$ ✓
- $T=T_1+T_2=2.079+1.386=3.465\,\text{ms}$ ✓
- $q=T_1/T=2.079/3.465=0.6=60\%$ ✓

**说明**：放电时只经 $R_2$，故 $T_2$ 不含 $R_1$；这是基本 555 多谐 $q>50\%$ 的原因。

</details>

**7.（555 多谐振荡器参数设计）** 用 555 定时器设计一个多谐振荡器，要求振荡频率 $f=1\,\text{kHz}$、占空比 $q=60\%$。取 $C=0.1\,\mu\text{F}$，求 $R_1$、$R_2$。

<details>
<summary>解答</summary>

由目标频率得周期：

$$T = \frac{1}{f} = \frac{1}{1000} = 1\times10^{-3}\,\text{s} = 1\,\text{ms}$$

由周期公式 $T=0.693(R_1+2R_2)C$：

$$(R_1+2R_2)C = \frac{T}{0.693} = \frac{1\times10^{-3}}{0.693} \approx 1.443\times10^{-3}\,\text{s}$$

$$R_1+2R_2 = \frac{1.443\times10^{-3}}{0.1\times10^{-6}} = 1.443\times10^4\,\Omega = 14.43\,\text{k}\Omega \quad\cdots(*)$$

由占空比 $q=\dfrac{R_1+R_2}{R_1+2R_2}=0.6$：

$$R_1+R_2 = 0.6\,(R_1+2R_2) = 0.6 \times 14.43 = 8.66\,\text{k}\Omega \quad\cdots(**)$$

由 $(*)$ 减 $(**)$：

$$R_2 = 14.43 - 8.66 = 5.77\,\text{k}\Omega$$

代入 $(**)$：

$$R_1 = 8.66 - 5.77 = 2.89\,\text{k}\Omega$$

$$\boxed{R_1 \approx 2.89\,\text{k}\Omega,\quad R_2 \approx 5.77\,\text{k}\Omega}$$

**单位检验**：$R$ 单位 $\text{k}\Omega$，$C$ 单位 $\mu\text{F}$，$RC$ 单位 $\text{ms}$ ✓
**验证**：
- $R_1+2R_2=2.89+2\times5.77=14.43\,\text{k}\Omega$
- $T=0.693\times14.43\times10^3\times0.1\times10^{-6}=0.693\times1.443=0.9996\,\text{ms}\approx1\,\text{ms}$ ✓
- $q=(2.89+5.77)/14.43=8.66/14.43=0.6=60\%$ ✓

**说明**：实际取标称值 $R_1=3\,\text{k}\Omega$、$R_2=5.6\,\text{k}\Omega$，再核算频率与占空比即可。

</details>

**8.（综合应用分析）** 如图所示电路用 555 定时器构成多谐振荡器，$V_{CC}=12\,\text{V}$，$R_1=20\,\text{k}\Omega$、$R_2=20\,\text{k}\Omega$、$C=1\,\mu\text{F}$，5 脚接 $0.01\,\mu\text{F}$ 滤波电容接地。请回答：
(1) 计算 $u_C$ 在充放电过程中变化的上下限电平；
(2) 计算振荡周期 $T$、频率 $f$、占空比 $q$；
(3) 若要在 5 脚外加控制电压使频率变为原来的一半，应加多大 $U_{CO}$？说明原理。

<details>
<summary>解答</summary>

**(1) $u_C$ 上下限电平**：

电容 $C$ 在 $\tfrac{1}{3}V_{CC}$ 与 $\tfrac{2}{3}V_{CC}$ 之间充放电：

$$U_{C,\max}=\frac{2}{3}V_{CC}=\frac{2}{3}\times12=8\,\text{V}$$

$$U_{C,\min}=\frac{1}{3}V_{CC}=\frac{1}{3}\times12=4\,\text{V}$$

**说明**：6 脚达 $\tfrac{2}{3}V_{CC}$ 复位、2 脚低于 $\tfrac{1}{3}V_{CC}$ 置位，故 $u_C$ 在 $4\sim8\,\text{V}$ 间振荡。

**(2) 周期、频率、占空比**：

$$T = 0.693\,(R_1+2R_2)\,C = 0.693 \times (20+2\times20)\times10^3 \times 1\times10^{-6}$$

$$= 0.693 \times 60\times10^{-3} = 41.58\times10^{-3}\,\text{s} = 41.58\,\text{ms}$$

$$f = \frac{1}{T} = \frac{1}{41.58\times10^{-3}} \approx 24.05\,\text{Hz}$$

$$q = \frac{R_1+R_2}{R_1+2R_2} = \frac{20+20}{20+40} = \frac{40}{60} \approx 66.7\%$$

$$\boxed{T \approx 41.58\,\text{ms},\quad f \approx 24\,\text{Hz},\quad q \approx 66.7\%}$$

**单位检验**：$\text{k}\Omega\cdot\mu\text{F}=\text{ms}$，$0.693\times60\times1=41.58\,\text{ms}$ ✓

**(3) 5 脚加控制电压使频率减半**：

5 脚加 $U_{CO}$ 后，两个比较阈值变为 $U_{T+}=U_{CO}$、$U_{T-}=\tfrac{1}{2}U_{CO}$，电容在 $\tfrac{1}{2}U_{CO}\sim U_{CO}$ 间充放电。

**充电阶段 $T_1$**：电容从 $\tfrac{1}{2}U_{CO}$ 经 $R_1+R_2$ 向 $V_{CC}$ 充电至 $U_{CO}$：
$$T_1=(R_1+R_2)C\ln\frac{V_{CC}-\tfrac{1}{2}U_{CO}}{V_{CC}-U_{CO}}$$

**放电阶段 $T_2$**：电容从 $U_{CO}$ 经 $R_2$ 与放电管向 $0$ 放电至 $\tfrac{1}{2}U_{CO}$：
$$T_2=R_2 C\ln\frac{0-U_{CO}}{0-\tfrac{1}{2}U_{CO}}=R_2 C\ln 2$$

> [!tip] 关键结论
> $T_2=R_2 C\ln 2$ **与 $U_{CO}$ 无关**（放电比值恒为 2），调节 $U_{CO}$ 只改变 $T_1$。验证默认值：取 $U_{CO}=\tfrac{2}{3}V_{CC}=8\,\text{V}$ 时 $T_1=(R_1+R_2)C\ln\tfrac{12-4}{12-8}=(R_1+R_2)C\ln 2$，与默认公式一致 ✓。

**默认周期各分量**（$U_{CO}=8\,\text{V}$）：
- $T_1=(R_1+R_2)C\ln 2=40\times0.693=27.72\,\text{ms}$
- $T_2=R_2 C\ln 2=20\times0.693=13.86\,\text{ms}$
- $T=T_1+T_2=41.58\,\text{ms}$ ✓

**频率减半即周期加倍**：$T'=2T=83.16\,\text{ms}$。因 $T_2$ 不变，故：
$$T_1' = T' - T_2 = 83.16 - 13.86 = 69.30\,\text{ms}$$

代入 $T_1$ 公式（$(R_1+R_2)C=40\,\text{ms}$）：
$$40\,\text{ms}\times\ln\frac{12-\tfrac{1}{2}U_{CO}}{12-U_{CO}} = 69.30\,\text{ms}$$

$$\ln\frac{12-\tfrac{1}{2}U_{CO}}{12-U_{CO}} = \frac{69.30}{40} = 1.7325$$

$$\frac{12-\tfrac{1}{2}U_{CO}}{12-U_{CO}} = e^{1.7325} \approx 5.653$$

$$12-\tfrac{1}{2}U_{CO} = 5.653\times(12-U_{CO}) = 67.84 - 5.653\,U_{CO}$$

$$(5.653-0.5)\,U_{CO} = 67.84 - 12 = 55.84$$

$$U_{CO} = \frac{55.84}{5.153} \approx 10.84\,\text{V}$$

$$\boxed{U_{CO}\approx 10.84\,\text{V}\;(\text{升高，使频率减半})}$$

**验证**：
- $U_{CO}=10.84\,\text{V}$、$\tfrac{1}{2}U_{CO}=5.42\,\text{V}$
- $T_1'=40\times\ln\dfrac{12-5.42}{12-10.84}=40\times\ln\dfrac{6.58}{1.16}=40\times\ln 5.672\approx40\times1.7356\approx69.4\,\text{ms}$ ✓
- $T_2=13.86\,\text{ms}$
- $T'=69.4+13.86=83.3\,\text{ms}\approx 2\times41.58=83.16\,\text{ms}$ ✓
- $f'=1/83.3\,\text{ms}\approx 12.0\,\text{Hz}\approx 24.05/2$ ✓

**原理**：升高 $U_{CO}$ 拉大充电阈值跨度（$\tfrac{1}{2}U_{CO}\to U_{CO}$），且 $U_{CO}$ 越接近 $V_{CC}$，分母 $V_{CC}-U_{CO}$ 越小、对数项越大，$T_1$ 越长，周期增大、频率降低。反之降低 $U_{CO}$ 使频率升高。工程上常用电位器调节 5 脚电压实现频率微调。

**单位检验**：$U_{CO}$ 单位 $\text{V}$，与 $V_{CC}=12\,\text{V}$ 同量纲；$T_1$ 公式中 $(R_1+R_2)C$ 单位 $\text{ms}$、对数项无量纲，结果为 $\text{ms}$ ✓

</details>

---

## 考点统计表

| 知识点 | 涉及题号 | 题数 | 难度分布 |
| :--- | :--- | :---: | :--- |
| [[6.1 施密特触发器\|施密特回差计算]] | 选择1、选择5、填空1、分析1 | 4 | 易-中 |
| [[6.2 单稳态触发器\|单稳态时间计算]] | 选择2、选择3、填空2、分析2 | 4 | 中 |
| [[6.2 单稳态触发器\|74LS121 应用]] | 填空2 | 1 | 中 |
| [[6.3 多谐振荡器\|多谐振荡周期]] | 选择1、填空3、分析3 | 3 | 中 |
| [[6.3 多谐振荡器\|石英晶体特性]] | 选择6 | 1 | 易 |
| [[6.4 555 定时器原理与应用\|555 施密特应用]] | 选择5、填空1、分析4 | 3 | 中 |
| [[6.4 555 定时器原理与应用\|555 单稳态设计]] | 分析5 | 1 | 中 |
| [[6.4 555 定时器原理与应用\|555 多谐计算]] | 选择4、填空4、分析6、分析7、分析8 | 5 | 中-难 |
| [[6.4 555 定时器原理与应用\|555 占空比与控制电压]] | 选择4、分析4、分析8 | 3 | 难 |
| 合计 | — | 18 | — |

> [!tip] 复习建议
> - **公式速记卡**：施密特 $\Delta U_T=U_{T+}-U_{T-}$；单稳态微分 $0.7RC$/积分 $1.1RC$/555 $1.1RC$；多谐对称 $1.4RC$/非对称 $2.2RC$/555 $0.693(R_1+2R_2)C$；
> - **555 阈值**是必考点：$\tfrac{1}{3}V_{CC}$ 置位、$\tfrac{2}{3}V_{CC}$ 复位，回差 $\tfrac{1}{3}V_{CC}$；5 脚加 $U_{CO}$ 可线性调阈值与频率；
> - **占空比**注意基本型 $q>50\%$，要 $q<50\%$ 必须加二极管引导充放电路径；
> - **单位换算**统一用 $\text{k}\Omega\cdot\mu\text{F}=\text{ms}$ 最不易错，计算后务必回代验证；
> - **设计题**（分析5、分析7）先由目标 $t_w$/$f$/$q$ 反解 $R$、$C$，再取标称值核算；
> - **综合题**（分析8）注意 5 脚控制电压改变阈值跨度的原理，会定性分析与定量联立。

## 章节导航

> [!nav] 导航
> [[MOC - 第6章|第6章 知识点目录]] · [[MOC - 数字逻辑电路|课程总览]] · 下一章习题：[[MOC - 第7章习题|第7章 半导体存储器习题]]
