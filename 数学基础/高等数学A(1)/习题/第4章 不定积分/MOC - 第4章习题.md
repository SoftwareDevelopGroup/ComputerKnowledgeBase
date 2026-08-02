---
domain: 数学基础
subject: 高等数学A(1)
type: exercise
chapter: 第4章 不定积分
tags: [高等数学,习题,不定积分,换元法,分部积分,有理函数积分]
prerequisites: ["第2章 一元函数微分学"]
aliases: [第4章习题, 不定积分习题]
---

# MOC - 第4章习题

> [!info] 本MOC定位
> 本MOC汇集第4章"不定积分"的典型习题，按**填空（6）、选择（6）、计算（12）、证明（4）**四类组织。重点训练：
> 1. **凑微分法**（填空1—3、计算1—4）：识别 $\varphi'(x)\mathrm dx$ 结构，熟记十二类凑微分模式。
> 2. **第二类换元法**（计算5—7）：三角换元、根式换元、倒代换。
> 3. **分部积分法**（计算8—10）：LIATE 顺序、循环型、递推型。
> 4. **有理函数积分**（计算11—12、证明2）：部分分式分解、待定系数法、递推公式。
>
> 答案统一用 `<details>` 折叠，建议先独立完成再核对。涉及知识点链接到对应小节：[[4.1 不定积分概念与性质]]、[[4.2 换元积分法]]、[[4.3 分部积分法]]、[[4.4 有理函数积分]]、[[4.5 三角函数有理式积分]]。

## 一、填空题（6题）

### 填1
$\displaystyle\int \dfrac{\mathrm dx}{(2x-3)^5}=$ ____。

<details>
<summary>答案</summary>

令 $u=2x-3$，$\mathrm du=2\mathrm dx$：
$$\int \frac{\mathrm dx}{(2x-3)^5}=\frac{1}{2}\int u^{-5}\,\mathrm du=\frac{1}{2}\cdot\frac{u^{-4}}{-4}+C=-\frac{1}{8(2x-3)^4}+C$$

</details>

### 填2
$\displaystyle\int x\sqrt{1+x^2}\,\mathrm dx=$ ____。

<details>
<summary>答案</summary>

令 $u=1+x^2$，$\mathrm du=2x\,\mathrm dx$：
$$\int x\sqrt{1+x^2}\,\mathrm dx=\frac{1}{2}\int u^{1/2}\,\mathrm du=\frac{1}{2}\cdot\frac{u^{3/2}}{3/2}+C=\frac{1}{3}(1+x^2)^{3/2}+C$$

</details>

### 填3
$\displaystyle\int \dfrac{e^{\arctan x}}{1+x^2}\,\mathrm dx=$ ____。

<details>
<summary>答案</summary>

令 $u=\arctan x$，$\mathrm du=\dfrac{\mathrm dx}{1+x^2}$：
$$\int \frac{e^{\arctan x}}{1+x^2}\,\mathrm dx=\int e^u\,\mathrm du=e^u+C=e^{\arctan x}+C$$

</details>

### 填4
$\displaystyle\int \ln x\,\mathrm dx=$ ____。

<details>
<summary>答案</summary>

用 [[4.3 分部积分法|分部积分]]：$u=\ln x$，$\mathrm dv=\mathrm dx$，$v=x$，$\mathrm du=\dfrac{\mathrm dx}{x}$：
$$\int \ln x\,\mathrm dx=x\ln x-\int x\cdot\frac{1}{x}\,\mathrm dx=x\ln x-x+C=x(\ln x-1)+C$$

</details>

### 填5
$\displaystyle\int \dfrac{\mathrm dx}{x^2+4x+5}=$ ____。

<details>
<summary>答案</summary>

$x^2+4x+5=(x+2)^2+1$，令 $u=x+2$：
$$\int \frac{\mathrm dx}{x^2+4x+5}=\int \frac{\mathrm du}{u^2+1}=\arctan u+C=\arctan(x+2)+C$$

</details>

### 填6
$\displaystyle\int \sin^3 x\cos x\,\mathrm dx=$ ____。

<details>
<summary>答案</summary>

令 $u=\sin x$，$\mathrm du=\cos x\,\mathrm dx$：
$$\int \sin^3 x\cos x\,\mathrm dx=\int u^3\,\mathrm du=\frac{u^4}{4}+C=\frac{\sin^4 x}{4}+C$$

</details>

## 二、选择题（6题）

### 选1
下列等式中正确的是（  ）。
- (A) $\int f'(x)\,\mathrm dx=f(x)$
- (B) $\dfrac{\mathrm d}{\mathrm dx}\int f(x)\,\mathrm dx=f(x)+C$
- (C) $\int \mathrm df(x)=f(x)+C$
- (D) $\mathrm d\!\left[\int f(x)\,\mathrm dx\right]=f(x)$

<details>
<summary>答案</summary>

**C**。

由 [[4.1 不定积分概念与性质|积分与微分互逆]]：$\int \mathrm df(x)=f(x)+C$（先微后积差常数）。

- (A) 缺常数 $C$；
- (B) $\dfrac{\mathrm d}{\mathrm dx}\int f\,\mathrm dx=f(x)$，无 $C$；
- (D) $\mathrm d\!\left[\int f\,\mathrm dx\right]=f(x)\,\mathrm dx$，是微分式不是函数。

</details>

### 选2
设 $f(x)=e^{-x}$，则 $\int f'(x)\,\mathrm dx=$（  ）。
- (A) $-e^{-x}+C$
- (B) $e^{-x}+C$
- (C) $-e^{-x}$
- (D) $e^{-x}$

<details>
<summary>答案</summary>

**B**。

由 [[4.1 不定积分概念与性质|积分与微分的互逆关系]]：$\int f'(x)\,\mathrm dx=f(x)+C$。

这里 $f(x)=e^{-x}$，故 $\int f'(x)\,\mathrm dx=e^{-x}+C$。

> [!tip] 直接验证
> 对 $e^{-x}+C$ 求导：$\dfrac{\mathrm d}{\mathrm dx}(e^{-x}+C)=-e^{-x}=f'(x)$，验证无误。注意不要因为 $f'(x)=-e^{-x}$ 中有负号而误选 (A)——求原函数时负号已包含在 $e^{-x}$ 中。

</details>

### 选3
$\displaystyle\int \dfrac{\mathrm dx}{\sqrt{4-x^2}}=$（  ）。
- (A) $\arcsin\dfrac{x}{2}+C$
- (B) $\dfrac{1}{2}\arcsin\dfrac{x}{2}+C$
- (C) $\arcsin 2x+C$
- (D) $2\arcsin\dfrac{x}{2}+C$

<details>
<summary>答案</summary>

**A**。

由 [[4.1 不定积分概念与性质|公式14]]：$\int \dfrac{\mathrm dx}{\sqrt{a^2-x^2}}=\arcsin\dfrac{x}{a}+C$，$a=2$。

</details>

### 选4
计算 $\displaystyle\int \dfrac{\mathrm dx}{x\sqrt{x^2-1}}$（$x>1$）的结果是（  ）。
- (A) $\arccos\dfrac{1}{x}+C$
- (B) $-\arcsin\dfrac{1}{x}+C$
- (C) $\ln|x+\sqrt{x^2-1}|+C$
- (D) (A) 与 (B) 都对

<details>
<summary>答案</summary>

**D**。

由 [[4.2 换元积分法|例8]]：
- 倒代换 $x=\dfrac{1}{t}$ 得 $-\arcsin\dfrac{1}{x}+C$（B）；
- 三角换元 $x=\sec t$ 得 $\arccos\dfrac{1}{x}+C$（A）。

由恒等式 $\arcsin\theta+\arccos\theta=\dfrac{\pi}{2}$，二者相差常数，合并到 $C$ 中即一致。

</details>

### 选5
设 $I_n=\displaystyle\int x^n e^x\,\mathrm dx$（$n\ge 1$），则递推公式为（  ）。
- (A) $I_n=x^n e^x-nI_{n-1}$
- (B) $I_n=x^n e^x+I_{n-1}$
- (C) $I_n=x^n e^x-nI_{n+1}$
- (D) $I_n=x^n e^x-1$

<details>
<summary>答案</summary>

**A**。

用 [[4.3 分部积分法|分部]]：$u=x^n$，$\mathrm dv=e^x\mathrm dx$，$v=e^x$，$\mathrm du=n x^{n-1}\mathrm dx$：
$$I_n=x^n e^x-\int n x^{n-1} e^x\,\mathrm dx=x^n e^x-nI_{n-1}$$

</details>

### 选6
$\displaystyle\int \dfrac{\mathrm dx}{x^2-1}=$（  ）。
- (A) $\dfrac{1}{2}\ln\left|\dfrac{x-1}{x+1}\right|+C$
- (B) $\ln\left|\dfrac{x-1}{x+1}\right|+C$
- (C) $\ln|x-1|+\ln|x+1|+C$
- (D) $\ln|x-1|-\ln|x+1|+C$

<details>
<summary>答案</summary>

**A**。

$x^2-1=(x-1)(x+1)$，[[4.4 有理函数积分|部分分式]]：
$$\frac{1}{(x-1)(x+1)}=\frac{A}{x-1}+\frac{B}{x+1}$$
$1=A(x+1)+B(x-1)$。代 $x=1$ 得 $A=\dfrac{1}{2}$；代 $x=-1$ 得 $B=-\dfrac{1}{2}$。
$$\int \frac{\mathrm dx}{x^2-1}=\frac{1}{2}\ln|x-1|-\frac{1}{2}\ln|x+1|+C=\frac{1}{2}\ln\left|\frac{x-1}{x+1}\right|+C$$

> [!tip] 干扰项辨析
> (B) 缺少 $\dfrac{1}{2}$ 因子；(D) 同样缺少 $\dfrac{1}{2}$ 因子；(C) 符号错误（应相减而非相加）。

</details>

## 三、计算题（12题）

### 计1
计算 $\displaystyle\int \dfrac{x}{(1+x^2)^2}\,\mathrm dx$。

<details>
<summary>解答</summary>

[[4.2 换元积分法|凑微分]]：$x\,\mathrm dx=\dfrac{1}{2}\mathrm d(1+x^2)$，令 $u=1+x^2$：
$$\int \frac{x}{(1+x^2)^2}\,\mathrm dx=\frac{1}{2}\int u^{-2}\,\mathrm du=-\frac{1}{2u}+C=-\frac{1}{2(1+x^2)}+C$$

</details>

### 计2
计算 $\displaystyle\int \dfrac{\mathrm dx}{x(1+\ln x)}$（$x>0$，$x\ne e^{-1}$）。

<details>
<summary>解答</summary>

令 $u=1+\ln x$，$\mathrm du=\dfrac{\mathrm dx}{x}$：
$$\int \frac{\mathrm dx}{x(1+\ln x)}=\int \frac{\mathrm du}{u}=\ln|u|+C=\ln|1+\ln x|+C$$

</details>

### 计3
计算 $\displaystyle\int \tan x\,\mathrm dx$ 并验证 [[4.1 不定积分概念与性质|公式18]]。

<details>
<summary>解答</summary>

$\tan x=\dfrac{\sin x}{\cos x}$，注意到 $\mathrm d(\cos x)=-\sin x\,\mathrm dx$：
$$\int \tan x\,\mathrm dx=-\int \frac{\mathrm d(\cos x)}{\cos x}=-\ln|\cos x|+C$$

这正是 [[4.1 不定积分概念与性质|公式18]]。

</details>

### 计4
计算 $\displaystyle\int \dfrac{x^2}{\sqrt{1-x^2}}\,\mathrm dx$。

<details>
<summary>解答</summary>

含 $\sqrt{1-x^2}$，用 [[4.2 换元积分法|三角换元]] $x=\sin t$，$t\in(-\pi/2,\pi/2)$，$\mathrm dx=\cos t\,\mathrm dt$，$\sqrt{1-x^2}=\cos t$：
$$\int \frac{x^2}{\sqrt{1-x^2}}\,\mathrm dx=\int \frac{\sin^2 t}{\cos t}\cdot\cos t\,\mathrm dt=\int \sin^2 t\,\mathrm dt=\int \frac{1-\cos 2t}{2}\,\mathrm dt$$
$$=\frac{t}{2}-\frac{\sin 2t}{4}+C=\frac{1}{2}\arcsin x-\frac{1}{2}x\sqrt{1-x^2}+C$$

回代用 $\sin 2t=2\sin t\cos t=2x\sqrt{1-x^2}$。

</details>

### 计5
计算 $\displaystyle\int \dfrac{\mathrm dx}{x^2\sqrt{x^2+1}}$。

<details>
<summary>解答</summary>

**法1（倒代换）**：令 $x=\dfrac{1}{t}$，$\mathrm dx=-\dfrac{1}{t^2}\mathrm dt$，$\sqrt{x^2+1}=\dfrac{\sqrt{1+t^2}}{|t|}$（$x>0\Rightarrow t>0$）：
$$\int \frac{\mathrm dx}{x^2\sqrt{x^2+1}}=\int \frac{-\frac{1}{t^2}\mathrm dt}{\frac{1}{t^2}\cdot\frac{\sqrt{1+t^2}}{t}}=-\int \frac{t\,\mathrm dt}{\sqrt{1+t^2}}=-\sqrt{1+t^2}+C=-\frac{\sqrt{x^2+1}}{x}+C$$

**法2（三角换元）**：令 $x=\tan t$，$\mathrm dx=\sec^2 t\,\mathrm dt$，$\sqrt{x^2+1}=\sec t$：
$$\int \frac{\mathrm dx}{x^2\sqrt{x^2+1}}=\int \frac{\sec^2 t\,\mathrm dt}{\tan^2 t\cdot\sec t}=\int \frac{\sec t}{\tan^2 t}\,\mathrm dt=\int \frac{\cos t}{\sin^2 t}\,\mathrm dt$$
令 $u=\sin t$：$=\int u^{-2}\,\mathrm du=-\dfrac{1}{u}+C=-\csc t+C=-\dfrac{\sqrt{x^2+1}}{x}+C$（由 $\csc t=\dfrac{\sec t}{\tan t}=\dfrac{\sqrt{x^2+1}}{x}$）。

**答案**：$-\dfrac{\sqrt{x^2+1}}{x}+C$。

</details>

### 计6
计算 $\displaystyle\int \dfrac{\sqrt{x}}{\sqrt{x}-1}\,\mathrm dx$。

<details>
<summary>解答</summary>

用 [[4.2 换元积分法|根式换元]] $t=\sqrt{x}$，$x=t^2$，$\mathrm dx=2t\,\mathrm dt$：
$$\int \frac{\sqrt{x}}{\sqrt{x}-1}\,\mathrm dx=\int \frac{t}{t-1}\cdot 2t\,\mathrm dt=2\int \frac{t^2}{t-1}\,\mathrm dt$$
化简：$\dfrac{t^2}{t-1}=\dfrac{t^2-1+1}{t-1}=\dfrac{(t-1)(t+1)+1}{t-1}=t+1+\dfrac{1}{t-1}$：
$$=2\int \left(t+1+\frac{1}{t-1}\right)\mathrm dt=2\left(\frac{t^2}{2}+t+\ln|t-1|\right)+C$$
$$=t^2+2t+2\ln|t-1|+C=x+2\sqrt{x}+2\ln|\sqrt{x}-1|+C$$

</details>

### 计7
计算 $\displaystyle\int \sqrt{4-x^2}\,\mathrm dx$（$a=2$ 的标准三角换元）。

<details>
<summary>解答</summary>

令 $x=2\sin t$，$\mathrm dx=2\cos t\,\mathrm dt$，$\sqrt{4-x^2}=2\cos t$：
$$\int \sqrt{4-x^2}\,\mathrm dx=\int 2\cos t\cdot 2\cos t\,\mathrm dt=4\int \cos^2 t\,\mathrm dt=4\int \frac{1+\cos 2t}{2}\,\mathrm dt$$
$$=2(t+\sin t\cos t)+C$$
回代：$\sin t=\dfrac{x}{2}$，$t=\arcsin\dfrac{x}{2}$，$\cos t=\dfrac{\sqrt{4-x^2}}{2}$，$\sin t\cos t=\dfrac{x\sqrt{4-x^2}}{4}$：
$$\int \sqrt{4-x^2}\,\mathrm dx=\frac{x\sqrt{4-x^2}}{2}+2\arcsin\frac{x}{2}+C$$

</details>

### 计8（分部积分——循环型）
计算 $\displaystyle\int e^{2x}\cos 3x\,\mathrm dx$。

<details>
<summary>解答</summary>

[[4.3 分部积分法|循环型]]。取 $u=\cos 3x$，$\mathrm dv=e^{2x}\mathrm dx$，$v=\dfrac{1}{2}e^{2x}$，$\mathrm du=-3\sin 3x\,\mathrm dx$：
$$I=\int e^{2x}\cos 3x\,\mathrm dx=\frac{1}{2}e^{2x}\cos 3x+\frac{3}{2}\int e^{2x}\sin 3x\,\mathrm dx$$
对 $\int e^{2x}\sin 3x\,\mathrm dx$ 再分部，取 $u=\sin 3x$，$\mathrm dv=e^{2x}\mathrm dx$，$v=\dfrac{1}{2}e^{2x}$，$\mathrm du=3\cos 3x\,\mathrm dx$：
$$\int e^{2x}\sin 3x\,\mathrm dx=\frac{1}{2}e^{2x}\sin 3x-\frac{3}{2}I$$
代回：$I=\dfrac{1}{2}e^{2x}\cos 3x+\dfrac{3}{2}\left(\dfrac{1}{2}e^{2x}\sin 3x-\dfrac{3}{2}I\right)$，$I=\dfrac{1}{2}e^{2x}\cos 3x+\dfrac{3}{4}e^{2x}\sin 3x-\dfrac{9}{4}I$，$\dfrac{13}{4}I=\dfrac{e^{2x}(2\cos 3x+3\sin 3x)}{4}$：
$$\boxed{\int e^{2x}\cos 3x\,\mathrm dx=\frac{e^{2x}(2\cos 3x+3\sin 3x)}{13}+C}$$

</details>

### 计9（分部积分——递推型）
计算 $\displaystyle\int \sin^3 x\,\mathrm dx$。

<details>
<summary>解答</summary>

**法1（降次）**：$\sin^3 x=\sin x(1-\cos^2 x)=\sin x-\sin x\cos^2 x$：
$$\int \sin^3 x\,\mathrm dx=-\cos x+\frac{\cos^3 x}{3}+C$$
（第二项用 $\sin x\,\mathrm dx=-\mathrm d(\cos x)$，$\int -u^2\,\mathrm du=-\dfrac{u^3}{3}$，其中 $u=\cos x$。）

**法2（[[4.3 分部积分法|递推公式]]）**：$I_3=\dfrac{2}{3}I_1-\dfrac{\sin^2 x\cos x}{3}+C=-\dfrac{2}{3}\cos x-\dfrac{\sin^2 x\cos x}{3}+C$，用 $\sin^2 x=1-\cos^2 x$ 化简即得上式。

**答案**：$-\cos x+\dfrac{\cos^3 x}{3}+C$。

</details>

### 计10（分部 + 换元综合）
计算 $\displaystyle\int e^{\sqrt{2x-1}}\,\mathrm dx$。

<details>
<summary>解答</summary>

令 $t=\sqrt{2x-1}$，$x=\dfrac{t^2+1}{2}$，$\mathrm dx=t\,\mathrm dt$：
$$\int e^{\sqrt{2x-1}}\,\mathrm dx=\int e^t\cdot t\,\mathrm dt$$
[[4.3 分部积分法|分部]]：$u=t$，$\mathrm dv=e^t\mathrm dt$，$v=e^t$：
$$\int t e^t\,\mathrm dt=t e^t-e^t+C_1=e^t(t-1)+C_1$$
回代 $t=\sqrt{2x-1}$：
$$\int e^{\sqrt{2x-1}}\,\mathrm dx=e^{\sqrt{2x-1}}(\sqrt{2x-1}-1)+C$$

</details>

### 计11（有理函数部分分式）
计算 $\displaystyle\int \dfrac{x+3}{x^2-5x+6}\,\mathrm dx$。

<details>
<summary>解答</summary>

$x^2-5x+6=(x-2)(x-3)$，[[4.4 有理函数积分|部分分式]]：
$$\frac{x+3}{(x-2)(x-3)}=\frac{A}{x-2}+\frac{B}{x-3}$$
$x+3=A(x-3)+B(x-2)$。
- $x=2$：$5=-A$，$A=-5$；
- $x=3$：$6=B$，$B=6$。

$$\int \frac{x+3}{x^2-5x+6}\,\mathrm dx=-5\ln|x-2|+6\ln|x-3|+C$$

</details>

### 计12（含二次不可约因式）
计算 $\displaystyle\int \dfrac{2x+1}{x^2+2x+5}\,\mathrm dx$。

<details>
<summary>解答</summary>

$x^2+2x+5=(x+1)^2+4$。令 $u=x+1$，$2x+1=2u-1$，$\mathrm dx=\mathrm du$：
$$\int \frac{2x+1}{x^2+2x+5}\,\mathrm dx=\int \frac{2u-1}{u^2+4}\,\mathrm du=2\int \frac{u\,\mathrm du}{u^2+4}-\int \frac{\mathrm du}{u^2+4}$$
$$=\ln(u^2+4)-\frac{1}{2}\arctan\frac{u}{2}+C=\ln(x^2+2x+5)-\frac{1}{2}\arctan\frac{x+1}{2}+C$$

</details>

## 四、证明题（4题）

### 证1（原函数结构）
设 $F(x)$、$G(x)$ 都是 $f(x)$ 在区间 $I$ 上的原函数，证明 $G(x)-F(x)\equiv C$（常数）。

<details>
<summary>证明</summary>

由 [[4.1 不定积分概念与性质|原函数定义]]：$F'(x)=f(x)$，$G'(x)=f(x)$（$x\in I$）。令 $\Phi(x)=G(x)-F(x)$，则
$$\Phi'(x)=G'(x)-F'(x)=f(x)-f(x)=0,\quad x\in I$$
由 [[3.1 罗尔定理、拉格朗日中值定理|拉格朗日定理的推论]]（导数恒为零的函数为常数），$\Phi(x)\equiv C$，即 $G(x)-F(x)=C$。$\blacksquare$

</details>

### 证2（分部积分递推公式）
设 $I_n=\displaystyle\int \dfrac{\mathrm dx}{(x^2+a^2)^n}$（$n\ge 2$，$a>0$）。证明递推公式：
$$I_n=\frac{x}{2a^2(n-1)(x^2+a^2)^{n-1}}+\frac{2n-3}{2a^2(n-1)}I_{n-1}$$

<details>
<summary>证明</summary>

[[4.3 分部积分法|分部积分]]，取 $u=\dfrac{1}{(x^2+a^2)^n}$，$\mathrm dv=\mathrm dx$，则 $v=x$，$\mathrm du=-\dfrac{2nx\,\mathrm dx}{(x^2+a^2)^{n+1}}$：
$$I_n=\frac{x}{(x^2+a^2)^n}-\int x\cdot\left(-\frac{2nx}{(x^2+a^2)^{n+1}}\right)\mathrm dx=\frac{x}{(x^2+a^2)^n}+2n\int \frac{x^2}{(x^2+a^2)^{n+1}}\,\mathrm dx$$
拆 $x^2=(x^2+a^2)-a^2$：
$$\int \frac{x^2}{(x^2+a^2)^{n+1}}\,\mathrm dx=\int \frac{(x^2+a^2)-a^2}{(x^2+a^2)^{n+1}}\,\mathrm dx=I_n-a^2 I_{n+1}$$
故 $I_n=\dfrac{x}{(x^2+a^2)^n}+2n(I_n-a^2 I_{n+1})$，整理得
$$2na^2 I_{n+1}=\frac{x}{(x^2+a^2)^n}+(2n-1)I_n$$
把 $n$ 换为 $n-1$（要求 $n-1\ge 1$ 即 $n\ge 2$）：
$$I_n=\frac{x}{2a^2(n-1)(x^2+a^2)^{n-1}}+\frac{2n-3}{2a^2(n-1)}I_{n-1}$$
$\blacksquare$

</details>

### 证3（万能代换公式）
证明：对任意三角函数有理式 $\int R(\sin x,\cos x)\,\mathrm dx$，令 $t=\tan\dfrac{x}{2}$ 后必可化为 $t$ 的有理函数积分。

<details>
<summary>证明</summary>

由半角代换公式（[[4.5 三角函数有理式积分|万能代换]]）：
$$\sin x=\frac{2t}{1+t^2},\quad \cos x=\frac{1-t^2}{1+t^2},\quad \mathrm dx=\frac{2\,\mathrm dt}{1+t^2}$$
代入原积分：
$$\int R(\sin x,\cos x)\,\mathrm dx=\int R\!\left(\frac{2t}{1+t^2},\frac{1-t^2}{1+t^2}\right)\cdot\frac{2}{1+t^2}\,\mathrm dt$$
因 $R(u,v)$ 是有理函数（多项式之商），把 $u,v$ 用 $t$ 的有理式代入后，复合 $R\!\left(\dfrac{2t}{1+t^2},\dfrac{1-t^2}{1+t^2}\right)$ 仍是 $t$ 的有理函数；再乘 $\dfrac{2}{1+t^2}$ 也是有理函数。故积分化为 $\int \tilde R(t)\,\mathrm dt$，其中 $\tilde R(t)$ 是 $t$ 的有理函数。由 [[4.4 有理函数积分|有理函数积分理论]]，其原函数必为初等函数。$\blacksquare$

</details>

### 证4（循环型分部积分）
设 $I=\displaystyle\int e^{ax}\sin bx\,\mathrm dx$（$a^2+b^2\ne 0$）。证明：
$$I=\frac{e^{ax}(a\sin bx-b\cos bx)}{a^2+b^2}+C$$

<details>
<summary>证明</summary>

[[4.3 分部积分法|分部]]，取 $u=\sin bx$，$\mathrm dv=e^{ax}\mathrm dx$，$v=\dfrac{1}{a}e^{ax}$，$\mathrm du=b\cos bx\,\mathrm dx$：
$$I=\frac{1}{a}e^{ax}\sin bx-\frac{b}{a}\int e^{ax}\cos bx\,\mathrm dx$$
对 $\int e^{ax}\cos bx\,\mathrm dx$ 再分部，取 $u=\cos bx$，$\mathrm dv=e^{ax}\mathrm dx$，$v=\dfrac{1}{a}e^{ax}$，$\mathrm du=-b\sin bx\,\mathrm dx$：
$$\int e^{ax}\cos bx\,\mathrm dx=\frac{1}{a}e^{ax}\cos bx+\frac{b}{a}I$$
代回：
$$I=\frac{1}{a}e^{ax}\sin bx-\frac{b}{a}\left(\frac{1}{a}e^{ax}\cos bx+\frac{b}{a}I\right)=\frac{e^{ax}\sin bx}{a}-\frac{b e^{ax}\cos bx}{a^2}-\frac{b^2}{a^2}I$$
移项：$I\left(1+\dfrac{b^2}{a^2}\right)=\dfrac{e^{ax}(a\sin bx-b\cos bx)}{a^2}$，即
$$I\cdot\frac{a^2+b^2}{a^2}=\frac{e^{ax}(a\sin bx-b\cos bx)}{a^2}$$
$$\boxed{I=\frac{e^{ax}(a\sin bx-b\cos bx)}{a^2+b^2}+C}$$
$\blacksquare$

</details>

## 考点统计表

| 题型 | 题号 | 涉及考点 | 关联小节 |
| ---- | ---- | -------- | -------- |
| 填空 | 填1 | 凑微分（线性换元） | [[4.2 换元积分法]] |
| 填空 | 填2 | 凑微分（$x\,\mathrm dx$ 凑 $x^2$） | [[4.2 换元积分法]] |
| 填空 | 填3 | 凑微分（$\mathrm d\arctan x$） | [[4.2 换元积分法]] |
| 填空 | 填4 | 分部积分（对数） | [[4.3 分部积分法]] |
| 填空 | 填5 | 配方化为 $\arctan$ 标准形 | [[4.4 有理函数积分]] |
| 填空 | 填6 | 凑微分（$\sin x\,\mathrm dx$ 凑 $\mathrm d\cos x$） | [[4.2 换元积分法]] |
| 选择 | 选1 | 积分与微分互逆关系辨析 | [[4.1 不定积分概念与性质]] |
| 选择 | 选2 | $\int f'\,\mathrm dx=f+C$ | [[4.1 不定积分概念与性质]] |
| 选择 | 选3 | $\dfrac{1}{\sqrt{a^2-x^2}}$ 标准形 | [[4.1 不定积分概念与性质]] |
| 选择 | 选4 | 第二类换元（倒代换/三角换元）的等价性 | [[4.2 换元积分法]] |
| 选择 | 选5 | 分部积分递推公式 | [[4.3 分部积分法]] |
| 选择 | 选6 | 有理函数部分分式 | [[4.4 有理函数积分]] |
| 计算 | 计1—计3 | 凑微分法（不同模式） | [[4.2 换元积分法]] |
| 计算 | 计4、计5、计7 | 第二类换元（三角换元、倒代换） | [[4.2 换元积分法]] |
| 计算 | 计6 | 根式换元 | [[4.2 换元积分法]] |
| 计算 | 计8、计9 | 分部积分（循环型、递推型） | [[4.3 分部积分法]] |
| 计算 | 计10 | 分部与换元综合 | [[4.2 换元积分法]]、[[4.3 分部积分法]] |
| 计算 | 计11、计12 | 有理函数部分分式 | [[4.4 有理函数积分]] |
| 证明 | 证1 | 原函数结构定理 | [[4.1 不定积分概念与性质]] |
| 证明 | 证2 | 分部积分递推公式 | [[4.3 分部积分法]]、[[4.4 有理函数积分]] |
| 证明 | 证3 | 万能代换化为有理函数 | [[4.4 有理函数积分]]、[[4.5 三角函数有理式积分]] |
| 证明 | 证4 | 循环型分部积分 | [[4.3 分部积分法]] |

> [!tip] 复习建议
> - **必练**：计4、计7（三角换元）、计8（循环型）、计11（部分分式）、证4（循环型证明）。
> - **易错**：填6（注意 $\mathrm d\cos x=-\sin x\,\mathrm dx$ 的负号）、计6（含 $\ln|\sqrt{x}-1|$）、选4（不同换元答案形式差异）。
> - **速通**：填空1—3、计1—计3（凑微分的标准化流程）。

## 章节导航

- 章节入口：[[MOC - 第4章]]
- 知识点小节：[[4.1 不定积分概念与性质]]、[[4.2 换元积分法]]、[[4.3 分部积分法]]、[[4.4 有理函数积分]]、[[4.5 三角函数有理式积分]]
- 上一级：[[MOC - 高等数学A(1)]]
- 上一章习题：[[MOC - 第3章习题]]
- 下一章习题：[[MOC - 第5章习题]]（待建）

## 相关标签

#高等数学 #习题 #不定积分 #换元法 #分部积分 #有理函数积分
