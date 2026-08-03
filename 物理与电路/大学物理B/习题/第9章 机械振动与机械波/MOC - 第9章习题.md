---
domain: 物理与电路
subject: 大学物理B
type: exercise
chapter: 第9章 机械振动与机械波
tags: [大学物理,习题,简谐振动,波动方程,干涉,驻波,多普勒效应]
prerequisites: ["第4章 刚体的转动"]
aliases: [第9章习题, 振动波动习题]
---

# MOC - 第9章习题 机械振动与机械波

> [!abstract] 本章习题概览
> 本章习题共 **28 题**，覆盖 [[9.1 简谐振动、旋转矢量|简谐振动方程与旋转矢量]]、[[9.2 简谐振动能量、阻尼振动、受迫振动|能量与受迫振动]]、[[9.3 平面简谐波波动方程|波动方程建立与波的能量]]、[[9.4 波的干涉、驻波|干涉与驻波]]、[[9.5 多普勒效应|多普勒效应]] 五个知识板块。题型分布：填空 6 题、选择 6 题、计算 12 题、证明/讨论 4 题。答案与详解折叠于 `<details>` 中，建议先独立作答再核对。所有物理量采用 SI 单位，声速取 $v=340\,\text{m/s}$，光速 $c=3.0\times10^8\,\text{m/s}$，重力加速度 $g=9.8\,\text{m/s}^2$。

---

## 一、填空题（6 题）

**1.** 一弹簧振子劲度系数 $k=18\,\text{N/m}$、质量 $m=0.50\,\text{kg}$，其振动周期 $T=$ ______ s，频率 $\nu=$ ______ Hz。

**2.** 简谐振动 $x=0.05\cos(4\pi t+\pi/3)$（SI）的振幅 $A=$ ______ m，角频率 $\omega=$ ______ rad/s，初相 $\varphi=$ ______ rad，$t=0$ 时速度 $v_0=$ ______ m/s。

**3.** 一平面简谐波沿 $+x$ 方向传播，波速 $v=100\,\text{m/s}$，频率 $\nu=50\,\text{Hz}$，则波长 $\lambda=$ ______ m，波数 $k=$ ______ rad/m。

**4.** 两同向同频简谐振动，振幅均为 $A_0$，相位差 $\Delta\varphi=\pi/2$，合振幅 $A=$ ______ $A_0$；若 $\Delta\varphi=\pi$，则 $A=$ ______ $A_0$。

**5.** 驻波方程 $y=0.06\cos(0.5\pi x)\cos(40\pi t)$（SI），相邻波节距离为 ______ m，相邻波腹距离为 ______ m。

**6.** 静止观察者测得迎面驶来汽车喇叭频率 $\nu'=600\,\text{Hz}$，汽车速度 $v_s=30\,\text{m/s}$，声速 $v=340\,\text{m/s}$，则喇叭实际频率 $\nu_0=$ ______ Hz（保留三位有效数字）。

<details>
<summary>填空题答案</summary>

1. $T=2\pi\sqrt{m/k}=2\pi\sqrt{0.50/18}=2\pi\sqrt{0.0278}\approx 2\pi\times0.1667\approx 1.05\,\text{s}$；$\nu=1/T\approx 0.952\,\text{Hz}$。
2. $A=0.05\,\text{m}$；$\omega=4\pi\,\text{rad/s}$；$\varphi=\pi/3\,\text{rad}$；$v_0=-A\omega\sin\varphi=-0.05\times4\pi\times\sin(\pi/3)=-0.05\times4\pi\times0.866\approx-0.544\,\text{m/s}$。
3. $\lambda=v/\nu=100/50=2.0\,\text{m}$；$k=2\pi/\lambda=\pi\,\text{rad/m}\approx 3.14\,\text{rad/m}$。
4. $\Delta\varphi=\pi/2$：$A=\sqrt{A_0^2+A_0^2+2A_0^2\cos(\pi/2)}=\sqrt{2}A_0$；$\Delta\varphi=\pi$：$A=|A_0-A_0|=0$。
5. 与 $y=2A\cos\dfrac{2\pi x}{\lambda}\cos\omega t$ 比较：$\dfrac{2\pi}{\lambda}=0.5\pi\Rightarrow\lambda=4.0\,\text{m}$。相邻波节距 $\lambda/2=2.0\,\text{m}$；相邻波腹距 $\lambda/2=2.0\,\text{m}$。
6. $\nu'=\nu_0\dfrac{v}{v-v_s}$，$\nu_0=\nu'\dfrac{v-v_s}{v}=600\times\dfrac{340-30}{340}=600\times\dfrac{310}{340}\approx 547\,\text{Hz}$。

</details>

---

## 二、选择题（6 题）

**1.** 一质点作简谐振动，下列说法正确的是（ ）
A. 振幅由系统本身决定，与初条件无关
B. 周期由系统本身决定，与振幅无关
C. 初相由系统本身决定，与初条件无关
D. 频率与振幅成正比

**2.** 简谐振动 $x=A\cos(\omega t+\varphi)$，当 $x=A/2$ 且向正方向运动时，相位（$\omega t+\varphi$，归约到 $[0,2\pi)$）为（ ）
A. $\pi/3$
B. $-\pi/3$ 即 $5\pi/3$
C. $2\pi/3$
D. $4\pi/3$

**3.** 关于简谐振动的能量，下列正确的是（ ）
A. 动能、势能频率均为 $\omega$
B. 动能、势能频率均为 $2\omega$，二者同相
C. 动能、势能频率均为 $2\omega$，二者反相
D. 总能量随时间周期性变化

**4.** 平面简谐波 $y=A\cos[\omega(t-x/v)+\varphi]$ 中，下列正确的是（ ）
A. 波沿 $-x$ 方向传播
B. $x$ 处质点比 $O$ 处相位超前 $\omega x/v$
C. $x$ 处质点比 $O$ 处相位滞后 $\omega x/v$
D. 各质点振动频率不同

**5.** 两相干波源同相，在相遇点波程差 $\delta=3.5\lambda$，则该点干涉结果为（ ）
A. 加强
B. 减弱
C. 既不最大加强也不完全抵消
D. 无法判定

**6.** 关于多普勒效应，下列正确的是（ ）
A. 机械波多普勒公式与电磁波多普勒公式完全相同
B. 机械波多普勒效应只与波源和观察者的相对速度有关
C. 电磁波多普勒效应用相对论公式，且只依赖相对速度
D. 当波源速度超过波速时机械波多普勒公式仍适用

<details>
<summary>选择题答案</summary>

1. **B**。周期（角频率）由系统决定（等时性），与振幅无关；振幅、初相由初条件决定（A、C 错）；频率与振幅无关（D 错）。
2. **B**。$\cos\theta=1/2$ 给 $\theta=\pm\pi/3$；向正方向运动 $v=-A\omega\sin\theta>0\Rightarrow\sin\theta<0$，故 $\theta=-\pi/3$，归约到 $[0,2\pi)$ 为 $5\pi/3$。
3. **C**。动能、势能频率均为 $2\omega$（由 $\sin^2$、$\cos^2$ 倍频），且反相（一最大时另一为零）；总能量守恒（D 错）。
4. **C**。$\omega(t-x/v)$ 中 $x$ 前为负，波沿 $+x$ 传播，$x$ 处相位比 $O$ 滞后 $\omega x/v$（A、B 错）；各质点频率相同（D 错）。
5. **B**。同相波源用波程差判据：$\delta=k\lambda$ 加强，$\delta=(2k+1)\lambda/2$ 减弱。$3.5\lambda=7\lambda/2=(2\times3+1)\lambda/2$，$k=3$，减弱。
6. **C**。电磁波多普勒用相对论公式 $\sqrt{\dfrac{c-u}{c+u}}$，只依赖相对速度 $u$（A 错）；机械波需分别考虑波源、观察者相对介质的速度（B 错）；$v_s\ge v$ 时机械波公式失效（D 错）。

</details>

---

## 三、计算题（12 题）

**1.（建立简谐振动方程）** 劲度系数 $k=12\,\text{N/m}$ 的轻弹簧下挂 $m=0.30\,\text{kg}$ 物体。将物体自平衡位置向右拉 $0.040\,\text{m}$ 后由静止释放，$t=0$ 为释放时刻，取右为正。写出振动方程，并求物体从释放到第一次到达 $x=-A/2$ 所用时间。

<details>
<summary>解答</summary>

$\omega=\sqrt{k/m}=\sqrt{12/0.30}=\sqrt{40}\approx 6.32\,\text{rad/s}$。$x_0=0.040\,\text{m}$、$v_0=0$，故 $A=0.040\,\text{m}$、$\varphi=0$。
$$x=0.040\cos(6.32t)\,\text{m}$$
第一次到 $x=-A/2=-0.020\,\text{m}$ 且向负方向运动（第一次到达必为向负方向），相位 $\omega t=2\pi/3$：
$$t=\frac{2\pi/3}{\omega}=\frac{2\pi/3}{6.32}\approx 0.331\,\text{s}$$

**单位检验**：$\omega$ 单位 s⁻¹，$t$ 单位 s，正确。

</details>

**2.（初相与旋转矢量）** 弹簧振子 $A=0.060\,\text{m}$、$\omega=5.0\,\text{rad/s}$。$t=0$ 时 $x_0=0.030\,\text{m}$ 且向负方向运动。用旋转矢量法求初相并写出振动方程，再求 $t=0.10\,\text{s}$ 时位移与速度。

<details>
<summary>解答</summary>

$\cos\varphi=x_0/A=0.030/0.060=0.5$，$\varphi=\pm\pi/3$；$v_0=-A\omega\sin\varphi<0\Rightarrow\sin\varphi>0$，故 $\varphi=\pi/3$（旋转矢量在第一象限，下一刻投影减小）。
$$x=0.060\cos(5.0t+\pi/3)\,\text{m}$$
$t=0.10\,\text{s}$：相位 $5.0\times0.10+\pi/3=0.5+\pi/3\approx 0.5+1.047=1.547\,\text{rad}$。
$$x=0.060\cos(1.547)\approx 0.060\times0.0243\approx 1.46\times10^{-3}\,\text{m}$$
$$v=-A\omega\sin(\text{相位})=-0.060\times5.0\times\sin(1.547)\approx-0.300\times0.9997\approx-0.300\,\text{m/s}$$

**单位检验**：位移 m，速度 m/s，正确。

</details>

**3.（振动合成）** 两同向同频简谐振动 $x_1=0.05\cos(8\pi t+\pi/4)$、$x_2=0.05\cos(8\pi t-3\pi/4)$（SI）。求合振幅、合初相，并判断加强或减弱。

<details>
<summary>解答</summary>

$\Delta\varphi=\varphi_2-\varphi_1=-3\pi/4-\pi/4=-\pi$，反相，故合振幅 $A=|A_1-A_2|=|0.05-0.05|=0$，完全抵消。合振动 $x=0$。合初相无意义（振幅为零）。

**单位检验**：$A$ 单位 m，$\Delta\varphi$ 单位 rad，正确。

</details>

**4.（能量计算）** 弹簧振子 $m=0.40\,\text{kg}$、$k=16\,\text{N/m}$、$A=0.080\,\text{m}$。求：(1) 总能量；(2) $x=0.040\,\text{m}$ 处动能与势能；(3) 动能等于势能的位置。

<details>
<summary>解答</summary>

(1) $E=\tfrac12 kA^2=\tfrac12\times16\times0.080^2=0.0512\,\text{J}$。
(2) $E_p=\tfrac12 kx^2=\tfrac12\times16\times0.040^2=0.0128\,\text{J}$；$E_k=E-E_p=0.0512-0.0128=0.0384\,\text{J}$。
(3) $E_k=E_p$ 即 $E_p=\tfrac12 E=\tfrac14 kA^2$，$\tfrac12 kx^2=\tfrac14 kA^2\Rightarrow x=\pm A/\sqrt2=\pm0.0566\,\text{m}$。

**单位检验**：$\text{N/m}\cdot\text{m}^2=\text{J}$，正确。

</details>

**5.（受迫振动共振）** 受迫振动系统 $\omega_0=10\,\text{rad/s}$、$\delta=1.0\,\text{s}^{-1}$、$f_m=2.0\,\text{m/s}^2$。求共振频率与共振振幅，并估算 $\omega_d=8.0\,\text{rad/s}$ 时振幅。

<details>
<summary>解答</summary>

$\omega_r=\sqrt{\omega_0^2-2\delta^2}=\sqrt{100-2}=\sqrt{98}\approx 9.90\,\text{rad/s}$。
$A_{\max}\approx\dfrac{f_m}{2\delta\omega_0}=\dfrac{2.0}{2\times1.0\times10}=0.10\,\text{m}$。
$\omega_d=8.0$：
$$A=\frac{2.0}{\sqrt{(100-64)^2+(2\times1.0\times8.0)^2}}=\frac{2.0}{\sqrt{36^2+16^2}}=\frac{2.0}{\sqrt{1296+256}}=\frac{2.0}{\sqrt{1552}}\approx\frac{2.0}{39.4}\approx 0.0508\,\text{m}$$

**单位检验**：$A$ 单位 $\text{m/s}^2/\text{s}^{-2}=\text{m}$，正确。

</details>

**6.（波动方程建立）** 横波沿 $+x$ 传播，$v=80\,\text{m/s}$、$A=0.020\,\text{m}$、$\nu=40\,\text{Hz}$。$t=0$ 时 $O$ 点在 $y=0$ 且向 $+y$ 运动。写出波动方程，并求 $x=1.0\,\text{m}$ 处 $t=0.025\,\text{s}$ 时的位移。

<details>
<summary>解答</summary>

$\omega=2\pi\nu=80\pi\,\text{rad/s}$，$\lambda=v/\nu=2.0\,\text{m}$。$O$ 点 $y_0=A\cos(\omega t+\varphi)$：$t=0$ 时 $A\cos\varphi=0$，$\varphi=\pm\pi/2$；$v_{y0}=-A\omega\sin\varphi>0\Rightarrow\sin\varphi<0$，故 $\varphi=-\pi/2$。
$$y=0.020\cos[80\pi(t-x/80)-\pi/2]\,\text{m}$$
$x=1.0\,\text{m}$、$t=0.025\,\text{s}$：相位 $80\pi(0.025-1.0/80)-\pi/2=80\pi\times0.0125-\pi/2=\pi-\pi/2=\pi/2$。
$$y=0.020\cos(\pi/2)=0$$

**单位检验**：$\omega x/v$ 单位 rad，$y$ 单位 m，正确。

</details>

**7.（由波形图求方程）** $t=0$ 波形为 $y=0.04\cos(0.5\pi x-\pi/6)$（SI），波沿 $-x$ 方向传播，$v=10\,\text{m/s}$。求波动方程及 $x=2.0\,\text{m}$ 处振动方程。

<details>
<summary>解答</summary>

$t=0$：$y(x,0)=0.04\cos(0.5\pi x-\pi/6)$。沿 $-x$ 传播形式 $A\cos(\omega t+kx+\varphi)$，$t=0$ 得 $A\cos(kx+\varphi)=0.04\cos(0.5\pi x-\pi/6)$，故 $A=0.04\,\text{m}$、$k=0.5\pi\,\text{rad/m}$、$\varphi=-\pi/6$。$\omega=kv=0.5\pi\times10=5\pi\,\text{rad/s}$。
$$y=0.04\cos(5\pi t+0.5\pi x-\pi/6)\,\text{m}$$
$x=2.0\,\text{m}$：相位 $0.5\pi\times2.0=\pi$，振动方程
$$y(2.0,t)=0.04\cos(5\pi t+\pi-\pi/6)=0.04\cos(5\pi t+5\pi/6)\,\text{m}$$

**单位检验**：$k$ 单位 rad/m，$\omega$ 单位 rad/s，正确。

</details>

**8.（波强与振幅）** 空气中声波 $\nu=500\,\text{Hz}$、$v=340\,\text{m/s}$、$\rho=1.29\,\text{kg/m}^3$，距点声源 $r=4.0\,\text{m}$ 处声强 $I=2.0\times10^{-4}\,\text{W/m}^2$。求该处空气质元振幅与声源平均功率。

<details>
<summary>解答</summary>

$A=\sqrt{\dfrac{2I}{\rho\omega^2 v}}$，$\omega=2\pi\times500=1000\pi\approx 3142\,\text{rad/s}$，$\omega^2\approx 9.87\times10^6$。
分母 $\rho\omega^2 v=1.29\times9.87\times10^6\times340\approx 4.33\times10^9$。
$$A=\sqrt{\frac{2\times2.0\times10^{-4}}{4.33\times10^9}}=\sqrt{9.24\times10^{-14}}\approx 3.04\times10^{-7}\,\text{m}$$
声源功率 $P=4\pi r^2 I=4\pi\times4.0^2\times2.0\times10^{-4}\approx 4.02\times10^{-2}\,\text{W}$。

**单位检验**：$A$ 单位 m，$P$ 单位 W，正确。

</details>

**9.（干涉判定）** 两相干波源 $S_1$、$S_2$ 同相、同频 $\nu=200\,\text{Hz}$，$v=400\,\text{m/s}$，$S_1S_2=12\,\text{m}$。在 $S_1S_2$ 连线上 $S_2$ 外侧距 $S_2$ 为 $r=5.0\,\text{m}$ 的 $P$ 点，干涉加强还是减弱？

<details>
<summary>解答</summary>

$\lambda=v/\nu=2.0\,\text{m}$。$P$ 到 $S_2$ 距 $r_2=5.0\,\text{m}$，到 $S_1$ 距 $r_1=r+12=17.0\,\text{m}$。波程差 $\delta=r_1-r_2=12.0\,\text{m}$。
$\delta/\lambda=12/2.0=6$，整数倍，故**加强**。

**单位检验**：$\delta$ 单位 m，正确。

</details>

**10.（驻波计算）** 驻波方程 $y=0.05\cos(0.4\pi x)\cos(50\pi t)$（SI）。求波长、波节坐标（$0\le x\le10\,\text{m}$ 范围内列出）、波腹坐标，并写出形成该驻波的两列行波。

<details>
<summary>解答</summary>

与 $2A\cos\dfrac{2\pi x}{\lambda}\cos\omega t$ 比较：$2A=0.05\Rightarrow A=0.025\,\text{m}$；$\omega=50\pi\,\text{rad/s}$；$\dfrac{2\pi}{\lambda}=0.4\pi\Rightarrow\lambda=5.0\,\text{m}$。

波节：$\cos(0.4\pi x)=0\Rightarrow 0.4\pi x=(2k+1)\pi/2\Rightarrow x=(2k+1)\times1.25\,\text{m}$。$0\le x\le10$ 内：$x=1.25,3.75,6.25,8.75\,\text{m}$（$k=0,1,2,3$）。

波腹：$0.4\pi x=k\pi\Rightarrow x=2.5k\,\text{m}$，$0\le x\le10$ 内：$x=0,2.5,5.0,7.5,10\,\text{m}$。

两列行波：$y_1=0.025\cos(50\pi t-0.4\pi x)$、$y_2=0.025\cos(50\pi t+0.4\pi x)$（SI）。

**单位检验**：$\lambda$ 单位 m，$x$ 单位 m，正确。

</details>

**11.（弦的驻波模式）** 长 $L=0.80\,\text{m}$ 的弦线质量 $m=2.0\times10^{-3}\,\text{kg}$，张力 $F_T=50\,\text{N}$，两端固定。求基频与第三次谐频。

<details>
<summary>解答</summary>

$\mu=m/L=2.0\times10^{-3}/0.80=2.5\times10^{-3}\,\text{kg/m}$。$v=\sqrt{F_T/\mu}=\sqrt{50/(2.5\times10^{-3})}=\sqrt{2.0\times10^4}\approx 141\,\text{m/s}$。
基频 $\nu_1=v/(2L)=141/(2\times0.80)\approx 88.4\,\text{Hz}$。
第三次谐频 $\nu_3=3\nu_1\approx 265\,\text{Hz}$。

**单位检验**：$v$ 单位 m/s，$\nu$ 单位 Hz，正确。

</details>

**12.（多普勒效应综合）** 声源 $\nu_0=400\,\text{Hz}$ 以 $v_s=20\,\text{m/s}$ 朝静止观察者驶来，观察者又以 $v_o=10\,\text{m/s}$ 朝声源跑去，$v=340\,\text{m/s}$。求观察者听到的频率。若该声源改为以 $u=0.20c$ 远离地球的恒星，发射 $\lambda_0=600\,\text{nm}$ 谱线，地球观测波长为多少？

<details>
<summary>解答</summary>

(1) 二者相向，$v_o$、$v_s$ 均取正：
$$\nu'=\nu_0\frac{v+v_o}{v-v_s}=400\times\frac{340+10}{340-20}=400\times\frac{350}{320}\approx 438\,\text{Hz}$$

(2) 电磁波多普勒，远离 $u=0.20c$：
$$\frac{\nu'}{\nu_0}=\sqrt{\frac{c-u}{c+u}}=\sqrt{\frac{0.80}{1.20}}=\sqrt{0.6667}\approx 0.8165$$
$\lambda'/\lambda_0=\nu_0/\nu'=1/0.8165\approx 1.225$：
$$\lambda'=1.225\times600\approx 735\,\text{nm}$$（红移，向红外偏移）

**单位检验**：(1) Hz；(2) nm，正确。

</details>

---

## 四、证明题与讨论题（4 题）

**1.（证明：弹簧振子机械能守恒）** 弹簧振子 $m\ddot x=-kx$，$x=A\cos(\omega t+\varphi)$，$\omega=\sqrt{k/m}$。证明其动能与势能之和为常量 $\tfrac12 kA^2$，并说明动能、势能频率为何是 $2\omega$。

<details>
<summary>证明</summary>

$E_k=\tfrac12 m\dot x^2=\tfrac12 mA^2\omega^2\sin^2(\omega t+\varphi)=\tfrac12 kA^2\sin^2(\omega t+\varphi)$（用 $m\omega^2=k$）。
$E_p=\tfrac12 kx^2=\tfrac12 kA^2\cos^2(\omega t+\varphi)$。
$$E=E_k+E_p=\tfrac12 kA^2[\sin^2(\omega t+\varphi)+\cos^2(\omega t+\varphi)]=\tfrac12 kA^2$$
与时间无关，守恒。

利用降幂公式 $\sin^2\theta=\tfrac12[1-\cos2\theta]$、$\cos^2\theta=\tfrac12[1+\cos2\theta]$：
$$E_k=\tfrac14 kA^2[1-\cos(2\omega t+2\varphi)],\quad E_p=\tfrac14 kA^2[1+\cos(2\omega t+2\varphi)]$$
二者均以 $2\omega$ 为角频率变化，且 $\cos$ 项符号相反故**反相**。物理上，每经过 $T/2$ 振子从一端到另一端，动能、势能各经历一次完整的最大↔最小循环，故频率翻倍。$\blacksquare$

</details>

**2.（证明：波动方程满足 $\partial^2 y/\partial t^2=v^2\partial^2 y/\partial x^2$）** 设 $y=A\cos[\omega(t-x/v)+\varphi]$，$v=\omega/k$。证明 $y$ 满足一维波动方程，并说明 $f(t-x/v)$ 形式的函数都是其解的物理意义。

<details>
<summary>证明</summary>

令 $\theta=\omega(t-x/v)+\varphi$。
$$\frac{\partial y}{\partial t}=-A\omega\sin\theta,\quad \frac{\partial^2 y}{\partial t^2}=-A\omega^2\cos\theta=-\omega^2 y$$
$$\frac{\partial y}{\partial x}=-A\omega\cdot(-1/v)\sin\theta=\frac{A\omega}{v}\sin\theta,\quad \frac{\partial^2 y}{\partial x^2}=-\frac{A\omega^2}{v^2}\cos\theta=-\frac{\omega^2}{v^2}y$$
比较：$\dfrac{\partial^2 y}{\partial t^2}=v^2\dfrac{\partial^2 y}{\partial x^2}$（均等于 $-\omega^2 y$，差因子 $v^2$），证毕。

一般地，对 $y=f(\theta)$，$\theta=t-x/v$，$\dfrac{\partial^2 y}{\partial t^2}=f''$、$\dfrac{\partial^2 y}{\partial x^2}=\dfrac{1}{v^2}f''$，恒满足波动方程。物理意义：$f(t-x/v)$ 描述"以速度 $v$ 沿 $+x$ 传播、形状不变"的行波——某 $t$ 时刻 $x$ 处的波形，等于 $t-\Delta t$ 时刻 $x-v\Delta t$ 处的波形，即波形以 $v$ 平移而不变形。$f(t+x/v)$ 对应沿 $-x$ 传播的行波。$\blacksquare$

</details>

**3.（证明：驻波波节波腹位置）** 由两列反向行波 $y_1=A\cos(\omega t-kx)$、$y_2=A\cos(\omega t+kx)$ 叠加，导出驻波方程，并证明波节位于 $x=(2k+1)\lambda/4$、波腹位于 $x=k\lambda/2$（$k$ 为整数）。

<details>
<summary>证明</summary>

由和差化积 $\cos\alpha+\cos\beta=2\cos\dfrac{\alpha+\beta}{2}\cos\dfrac{\alpha-\beta}{2}$：
$$y=y_1+y_2=2A\cos\frac{(\omega t-kx)+(\omega t+kx)}{2}\cos\frac{(\omega t-kx)-(\omega t+kx)}{2}=2A\cos\omega t\cos kx$$
即 $y=2A\cos\dfrac{2\pi x}{\lambda}\cos\omega t$，空间因子 $\cos\dfrac{2\pi x}{\lambda}$ 与时间因子 $\cos\omega t$ 分离，故为驻波。

振幅 $|2A\cos\dfrac{2\pi x}{\lambda}|$：
- 波节（振幅为零）：$\cos\dfrac{2\pi x}{\lambda}=0\Rightarrow\dfrac{2\pi x}{\lambda}=(2k+1)\dfrac{\pi}{2}\Rightarrow x=(2k+1)\dfrac{\lambda}{4}$，$k\in\mathbb Z$；
- 波腹（振幅最大 $2A$）：$\left|\cos\dfrac{2\pi x}{\lambda}\right|=1\Rightarrow\dfrac{2\pi x}{\lambda}=k\pi\Rightarrow x=k\dfrac{\lambda}{2}$，$k\in\mathbb Z$。

相邻波节间距 $\Delta x=[(2k+3)-(2k+1)]\lambda/4=\lambda/2$；相邻波腹间距 $\Delta x=\lambda/2$；相邻波节波腹间距 $\lambda/4$。$\blacksquare$

</details>

**4.（讨论：机械波与电磁波的异同）** 从产生条件、传播介质、波的类型（横/纵）、波速决定因素、能量是否传播、多普勒公式六个方面系统比较机械波与电磁波，并说明二者数学结构为何相同。

<details>
<summary>讨论</summary>

| 比较项 | 机械波 | 电磁波 |
| ---- | ---- | ---- |
| 产生条件 | 波源 + 弹性介质 | 加速电荷（变化电流） |
| 传播介质 | 必须有弹性介质（真空不能传播） | 无需介质，可在真空传播 |
| 波的类型 | 有横波有纵波 | 横波（$\vec E\perp\vec B\perp\vec k$） |
| 波速决定 | 由介质性质决定（$v=\sqrt{Y/\rho}$ 等） | 真空中 $c=1/\sqrt{\mu_0\varepsilon_0}$，介质中 $v=1/\sqrt{\mu\varepsilon}$ |
| 能量传播 | 传播（能流密度 $I=\tfrac12\rho\omega^2A^2v$） | 传播（坡印亭矢量 $\vec S=\vec E\times\vec H$） |
| 多普勒公式 | $\nu'=\nu_0\dfrac{v+v_o}{v-v_s}$（分别考虑） | $\nu'=\nu_0\sqrt{\dfrac{c-u}{c+u}}$（相对论，仅相对速度） |

**数学结构相同的原因**：机械波由介质质元的牛顿运动方程 $\rho\dfrac{\partial^2 u}{\partial t^2}=Y\dfrac{\partial^2 u}{\partial x^2}$（弹性回复耦合）导出；电磁波由麦克斯韦方程组在无源区 $\nabla\times\vec E=-\dfrac{\partial\vec B}{\partial t}$、$\nabla\times\vec B=\mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ 联立得 $\nabla^2\vec E=\mu_0\varepsilon_0\dfrac{\partial^2\vec E}{\partial t^2}$。两者都归结为**线性波动方程** $\nabla^2 u=\dfrac{1}{v^2}\dfrac{\partial^2 u}{\partial t^2}$，因此叠加原理、干涉、驻波、衍射等数学结论完全平行——这正是把力学波动的结论类比到光学（[[MOC - 第10章|第10章]] 波动光学）的理论基础。

但物理本质不同：机械波是介质质元的机械振动，能量为动能与弹性势能；电磁波是 $\vec E$、$\vec B$ 场的振荡，能量由坡印亭矢量描述，且电场磁场相互激发、自维持，无需介质。$\blacksquare$

</details>

---

## 考点统计表

| 知识点 | 涉及题号 | 题数 | 难度分布 |
| :--- | :--- | :---: | :--- |
| [[9.1 简谐振动、旋转矢量\|简谐振动方程建立]] | 填空1、选择1、计算1、计算2 | 4 | 易-中 |
| [[9.1 简谐振动、旋转矢量\|相位与旋转矢量]] | 填空2、选择2、计算2 | 3 | 中 |
| [[9.1 简谐振动、旋转矢量\|同向同频合成]] | 填空4、计算3 | 2 | 中 |
| [[9.2 简谐振动能量、阻尼振动、受迫振动\|振动能量]] | 填空2、选择3、计算4、证明1 | 4 | 中 |
| [[9.2 简谐振动能量、阻尼振动、受迫振动\|受迫振动与共振]] | 计算5 | 1 | 中-难 |
| [[9.3 平面简谐波波动方程\|波动方程建立]] | 填空3、选择4、计算6、计算7、证明2 | 5 | 中 |
| [[9.3 平面简谐波波动方程\|波的能量与能流密度]] | 计算8 | 1 | 中-难 |
| [[9.4 波的干涉、驻波\|干涉加强减弱]] | 选择5、计算9 | 2 | 中 |
| [[9.4 波的干涉、驻波\|驻波计算]] | 填空5、计算10、计算11、证明3 | 4 | 中 |
| [[9.5 多普勒效应\|机械波多普勒]] | 填空6、选择6、计算12 | 3 | 中 |
| [[9.5 多普勒效应\|电磁波多普勒]] | 选择6、计算12 | 2 | 难 |
| 机械波与电磁波比较 | 讨论4 | 1 | 难 |
| 合计 | — | 32（含分点） | — |

> [!tip] 复习建议
> - **简谐振动方程**（计算1、2）是基础，确保 $\omega=\sqrt{k/m}$、$A$、$\varphi$ 由初条件确定熟练，旋转矢量法求初相是重点；
> - **波动方程**（计算6、7）注意传播方向符号与初相判定，波形图与振动图不要混用；
> - **能量**（计算4、证明1）区分振子能量守恒与介质质元能量不守恒；
> - **干涉与驻波**（计算9、10、11）相位差/波程差判据要熟练，波节波腹公式必背；
> - **多普勒效应**（计算12）分清机械波（$v_o$、$v_s$ 分别代入）与电磁波（相对论公式）；
> - 证明题注意波动方程、驻波方程的推导步骤，是高分点。

## 章节导航

> [!nav] 导航
> [[MOC - 第9章|第9章 知识点目录]] · [[MOC - 大学物理B|课程总览]] · 上一章习题：[[MOC - 第8章习题|第8章 电磁感应与电磁场习题]] · 下一章习题：[[MOC - 第10章习题|第10章 波动光学习题]]
