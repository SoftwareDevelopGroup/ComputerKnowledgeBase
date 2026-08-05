---
domain: 数学基础
subject: 概率论与数理统计B
type: exercise
chapter: 第4章 随机变量的数字特征
tags: [概率论,数理统计,习题,数字特征,期望,方差,协方差,相关系数]
prerequisites: ["高等数学", "概率论与数理统计B/第4章 随机变量的数字特征"]
aliases: [第4章习题, 数字特征习题]
---

# MOC - 第4章习题：随机变量的数字特征

> [!abstract] 本章习题导航
> 本组习题覆盖 [[MOC - 第4章]] 全部内容，分四类共 32 题：
>
> - **填空题**（10 题）：六大分布期望方差、方差公式、协方差计算、标准化
> - **选择题**（10 题）：期望性质辨析、独立与不相关、相关系数含义、方差性质
> - **计算题**（8 题）：期望方差计算、协方差相关系数计算、函数期望、综合
> - **证明题**（4 题）：方差性质证明、不相关不独立反例、不等式证明

---

## 一、填空题（10 题）

### 填空 1

> [!question] 题目
> 设 $X\sim B(n,p)$，则 $E(X)=$ $\underline{\qquad}$，$D(X)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$E(X)=np,\qquad D(X)=np(1-p)$$

</details>

---

### 填空 2

> [!question] 题目
> 设 $X\sim\Pi(\lambda)$，则 $E(X)=$ $\underline{\qquad}$，$D(X)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$E(X)=\lambda,\qquad D(X)=\lambda$$

泊松分布期望等于方差。

</details>

---

### 填空 3

> [!question] 题目
> 设 $X\sim U(a,b)$，则 $E(X)=$ $\underline{\qquad}$，$D(X)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$E(X)=\frac{a+b}{2},\qquad D(X)=\frac{(b-a)^2}{12}$$

</details>

---

### 填空 4

> [!question] 题目
> 设 $X\sim\mathrm{Exp}(\lambda)$，则 $E(X)=$ $\underline{\qquad}$，$D(X)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$E(X)=\frac{1}{\lambda},\qquad D(X)=\frac{1}{\lambda^2}$$

</details>

---

### 填空 5

> [!question] 题目
> 设 $X\sim N(\mu,\sigma^2)$，则 $E(X)=$ $\underline{\qquad}$，$D(X)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$E(X)=\mu,\qquad D(X)=\sigma^2$$

</details>

---

### 填空 6

> [!question] 题目
> 方差计算公式 $D(X)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$D(X)=E(X^2)-[E(X)]^2$$

</details>

---

### 填空 7

> [!question] 题目
> 协方差计算公式 $\mathrm{Cov}(X,Y)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$\mathrm{Cov}(X,Y)=E(XY)-E(X)E(Y)$$

</details>

---

### 填空 8

> [!question] 题目
> 相关系数 $\rho_{XY}=$ $\underline{\qquad}$，取值范围为 $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$\rho_{XY}=\frac{\mathrm{Cov}(X,Y)}{\sqrt{D(X)}\sqrt{D(Y)}},\qquad \rho_{XY}\in[-1,1]$$

</details>

---

### 填空 9

> [!question] 题目
> 设 $X,Y$ 独立，$D(X)=2$，$D(Y)=3$，则 $D(X-Y)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$D(X-Y)=D(X)+D(Y)=2+3=5$$

独立时加减号结果相同。

</details>

---

### 填空 10

> [!question] 题目
> 设 $E(X)=2$，$D(X)=4$，则 $X$ 的标准化随机变量为 $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$X^*=\frac{X-E(X)}{\sqrt{D(X)}}=\frac{X-2}{2}$$

满足 $E(X^*)=0$，$D(X^*)=1$。

</details>

---

## 二、选择题（10 题）

### 选择 1

> [!question] 题目
> 下列等式中需要 $X,Y$ 独立才成立的是：
>
> A. $E(X+Y)=E(X)+E(Y)$
> B. $E(XY)=E(X)E(Y)$
> C. $D(X+Y)=D(X)+D(Y)+2\mathrm{Cov}(X,Y)$
> D. $D(c)=0$

<details>
<summary>答案</summary>

**B**。$E(XY)=E(X)E(Y)$ 需要独立性；$E(X+Y)=E(X)+E(Y)$ 不需要（线性性质）；C 是一般公式；D 总成立。

</details>

---

### 选择 2

> [!question] 题目
> 设 $X,Y$ 独立，则下列正确的是：
>
> A. $D(X-Y)=D(X)-D(Y)$
> B. $D(X-Y)=D(X)+D(Y)$
> C. $D(X-Y)=D(X)+D(Y)-2\mathrm{Cov}(X,Y)$
> D. $D(X-Y)=D(X)-2\mathrm{Cov}(X,Y)+D(Y)$

<details>
<summary>答案</summary>

**B**。独立时 $\mathrm{Cov}=0$，$D(X\pm Y)=D(X)+D(Y)$，加减号结果相同。

</details>

---

### 选择 3

> [!question] 题目
> 设 $D(X)=4$，$D(Y)=9$，$\mathrm{Cov}(X,Y)=6$，则 $\rho_{XY}=$：
>
> A. $\frac{2}{3}$
> B. $1$
> C. $\frac{1}{2}$
> D. $\frac{3}{2}$

<details>
<summary>答案</summary>

**B**。$\rho=\frac{6}{\sqrt{4\times9}}=\frac{6}{6}=1$，$X,Y$ 完全正线性相关。

</details>

---

### 选择 4

> [!question] 题目
> 关于独立与不相关，下列正确的是：
>
> A. 不相关则独立
> B. 独立则不相关，且反之亦然
> C. 独立则不相关，但反之一般不成立
> D. 二者无关系

<details>
<summary>答案</summary>

**C**。独立 $\Rightarrow$ 不相关（$\rho=0$），但 $\rho=0$ 一般推不出独立，除非二维正态。

</details>

---

### 选择 5

> [!question] 题目
> 设 $X\sim N(2,9)$，则 $E(X^2)=$：
>
> A. $4$
> B. $13$
> C. $9$
> D. $11$

<details>
<summary>答案</summary>

**B**。$E(X^2)=D(X)+[E(X)]^2=9+4=13$。

</details>

---

### 选择 6

> [!question] 题目
> $|\rho_{XY}|=1$ 等价于：
>
> A. $X,Y$ 独立
> B. $X,Y$ 存在线性关系 $Y=aX+b$ a.s.
> C. $\mathrm{Cov}(X,Y)=0$
> D. $D(X)=D(Y)$

<details>
<summary>答案</summary>

**B**。$|\rho|=1 \Leftrightarrow$ 几乎处处线性关系 $Y=aX+b$；$\rho=1$ 时 $a>0$，$\rho=-1$ 时 $a<0$。

</details>

---

### 选择 7

> [!question] 题目
> 设 $X\sim B(10,0.3)$，则 $D(X)=$：
>
> A. $3$
> B. $2.1$
> C. $0.21$
> D. $30$

<details>
<summary>答案</summary>

**B**。$D(X)=np(1-p)=10\times0.3\times0.7=2.1$。

</details>

---

### 选择 8

> [!question] 题目
> 设 $X\sim\mathrm{Exp}(2)$，则 $E(X^2)=$：
>
> A. $\frac{1}{2}$
> B. $\frac{1}{4}$
> C. $\frac{1}{2}$
> D. $1$

<details>
<summary>答案</summary>

**D**。$E(X)=\frac{1}{2}$，$D(X)=\frac{1}{4}$，$E(X^2)=D(X)+[E(X)]^2=\frac{1}{4}+\frac{1}{4}=\frac{1}{2}$。修正：$E(X^2)=\frac{1}{4}+\frac{1}{4}=\frac{1}{2}$，选 **D**（$\frac{1}{2}$）。

</details>

---

### 选择 9

> [!question] 题目
> 协方差矩阵的性质不包括：
>
> A. 对称性
> B. 半正定性
> C. 对角元非负
> D. 行列式非零

<details>
<summary>答案</summary>

**D**。协方差矩阵对称且半正定，但行列式可以为零（例如各分量完全线性相关时）。

</details>

---

### 选择 10

> [!question] 题目
> 设 $X\sim U(-1,1)$，则 $E(X)=$，$D(X)=$：
>
> A. $0,\;\frac{1}{3}$
> B. $0,\;\frac{1}{12}$
> C. $0,\;\frac{4}{3}$
> D. $1,\;\frac{1}{3}$

<details>
<summary>答案</summary>

**A**。$E=\frac{-1+1}{2}=0$，$D=\frac{(1-(-1))^2}{12}=\frac{4}{12}=\frac{1}{3}$。

</details>

---

## 三、计算题（8 题）

### 计算 1

> [!question] 题目
> 设 $X$ 的密度 $f(x)=\begin{cases}2x,&0<x<1\\0,&\text{其他}\end{cases}$，求 $E(X)$、$D(X)$。

<details>
<summary>解答</summary>

$$E(X)=\int_0^1 x\cdot2x\,dx=\frac{2}{3}$$

$$E(X^2)=\int_0^1 x^2\cdot2x\,dx=\frac{1}{2}$$

$$D(X)=E(X^2)-[E(X)]^2=\frac{1}{2}-\frac{4}{9}=\frac{1}{18}$$

</details>

---

### 计算 2

> [!question] 题目
> 设 $X,Y$ 独立，$E(X)=1$，$D(X)=4$，$E(Y)=2$，$D(Y)=9$，求 $E(3X-2Y+1)$ 和 $D(3X-2Y+1)$。

<details>
<summary>解答</summary>

$$E(3X-2Y+1)=3E(X)-2E(Y)+1=3-4+1=0$$

$$D(3X-2Y+1)=9D(X)+4D(Y)=36+36=72$$

（常数 $+1$ 不影响方差）

</details>

---

### 计算 3

> [!question] 题目
> 设 $(X,Y)$ 的联合密度 $f(x,y)=\begin{cases}2,&0<x<1,0<y<x\\0,&\text{其他}\end{cases}$，求 $\mathrm{Cov}(X,Y)$ 和 $\rho_{XY}$。

<details>
<summary>解答</summary>

$E(XY)=\int_0^1\int_0^x xy\cdot2\,dy\,dx=\int_0^1 x^3\,dx=\frac{1}{4}$

$E(X)=\int_0^1 2x^2\,dx=\frac{2}{3}$，$E(Y)=\int_0^1 x^2\,dx=\frac{1}{3}$

$D(X)=\frac{1}{18}$，$D(Y)=\frac{1}{18}$（见 [[4.3 协方差、相关系数]] 例2）

$$\mathrm{Cov}(X,Y)=\frac{1}{4}-\frac{2}{3}\cdot\frac{1}{3}=\frac{1}{36}$$

$$\rho_{XY}=\frac{1/36}{1/18}=\frac{1}{2}$$

</details>

---

### 计算 4

> [!question] 题目
> 设 $X\sim N(1,4)$，求 $E(X^2)$ 和 $E(e^X)$（提示：$E(e^X)$ 用矩母函数）。

<details>
<summary>解答</summary>

$E(X^2)=D(X)+[E(X)]^2=4+1=5$

$E(e^X)=\int_{-\infty}^{+\infty}e^x\frac{1}{\sqrt{8\pi}}e^{-\frac{(x-1)^2}{8}}\,dx$

利用正态矩母函数 $M(t)=E(e^{tX})=e^{\mu t+\frac{1}{2}\sigma^2 t^2}$，令 $t=1$：

$$E(e^X)=e^{1\cdot1+\frac{1}{2}\cdot4\cdot1}=e^{1+2}=e^3$$

</details>

---

### 计算 5

> [!question] 题目
> 设 $X\sim B(20,0.5)$，用切比雪夫不等式估计 $P\{|X-10|\geq4\}$ 的上界。

<details>
<summary>解答</summary>

$E(X)=np=10$，$D(X)=np(1-p)=20\times0.5\times0.5=5$。

由切比雪夫不等式，$\varepsilon=4$：

$$P\{|X-10|\geq4\}\leq\frac{D(X)}{\varepsilon^2}=\frac{5}{16}$$

</details>

---

### 计算 6

> [!question] 题目
> 设 $X\sim U(0,2)$，$Y=X^2$，求 $E(Y)$ 和 $D(Y)$。

<details>
<summary>解答</summary>

$f_X(x)=\frac{1}{2}\;(0<x<2)$。

$$E(Y)=E(X^2)=\int_0^2\frac{x^2}{2}\,dx=\frac{4}{3}$$

$$E(Y^2)=E(X^4)=\int_0^2\frac{x^4}{2}\,dx=\frac{16}{5}$$

$$D(Y)=E(Y^2)-[E(Y)]^2=\frac{16}{5}-\frac{16}{9}=\frac{144-80}{45}=\frac{64}{45}$$

</details>

---

### 计算 7

> [!question] 题目
> 设二维 $(X,Y)$，$D(X)=4$，$D(Y)=9$，$\rho_{XY}=0.5$，求 $\mathrm{Cov}(X,Y)$ 和 $D(X+Y)$、$D(X-Y)$。

<details>
<summary>解答</summary>

$$\mathrm{Cov}(X,Y)=\rho\sqrt{D(X)D(Y)}=0.5\times\sqrt{4\times9}=0.5\times6=3$$

$$D(X+Y)=D(X)+D(Y)+2\mathrm{Cov}=4+9+6=19$$

$$D(X-Y)=D(X)+D(Y)-2\mathrm{Cov}=4+9-6=7$$

</details>

---

### 计算 8

> [!question] 题目
> 设 $X,Y$ 独立，$X\sim\Pi(2)$，$Y\sim\mathrm{Exp}(3)$，求 $E(2X-3Y)$ 和 $D(2X-3Y)$。

<details>
<summary>解答</summary>

$E(X)=D(X)=2$，$E(Y)=\frac{1}{3}$，$D(Y)=\frac{1}{9}$。

$$E(2X-3Y)=2E(X)-3E(Y)=4-1=3$$

$$D(2X-3Y)=4D(X)+9D(Y)=8+1=9$$

</details>

---

## 四、证明题（4 题）

### 证明 1

> [!question] 题目
> 证明：$D(X)=0 \Leftrightarrow P\{X=E(X)\}=1$。

<details>
<summary>证明</summary>

**($\Leftarrow$)** 若 $P\{X=E(X)\}=1$，则 $X$ 几乎处处为常数 $E(X)$，故 $D(X)=E\{[X-E(X)]^2\}=0$。

**($\Rightarrow$)** 若 $D(X)=0$，即 $E\{[X-E(X)]^2\}=0$。令 $Y=[X-E(X)]^2\geq0$，$E(Y)=0$。

由非负随机变量期望为零则几乎处处为零：$P\{Y=0\}=1$，即 $P\{[X-E(X)]^2=0\}=1$，亦即 $P\{X=E(X)\}=1$。

</details>

---

### 证明 2

> [!question] 题目
> 证明：若 $X,Y$ 独立，则 $D(X+Y)=D(X)+D(Y)$。

<details>
<summary>证明</summary>

由和的方差公式：

$$D(X+Y)=D(X)+D(Y)+2\,\mathrm{Cov}(X,Y)$$

由独立性 $\mathrm{Cov}(X,Y)=E(XY)-E(X)E(Y)=E(X)E(Y)-E(X)E(Y)=0$。

故 $D(X+Y)=D(X)+D(Y)$。

</details>

---

### 证明 3

> [!question] 题目
> 设 $\Theta\sim U(0,2\pi)$，$X=\cos\Theta$，$Y=\sin\Theta$。证明 $X,Y$ 不相关但不独立。

<details>
<summary>证明</summary>

$E(X)=\frac{1}{2\pi}\int_0^{2\pi}\cos\theta\,d\theta=0$，$E(Y)=\frac{1}{2\pi}\int_0^{2\pi}\sin\theta\,d\theta=0$。

$E(XY)=\frac{1}{2\pi}\int_0^{2\pi}\cos\theta\sin\theta\,d\theta=\frac{1}{4\pi}\int_0^{2\pi}\sin2\theta\,d\theta=0$

$\mathrm{Cov}(X,Y)=0-0=0$，故不相关。

但 $X^2+Y^2=1$（恒等式），$Y$ 的取值被 $X$ 完全约束（$Y=\pm\sqrt{1-X^2}$），不独立。

</details>

---

### 证明 4

> [!question] 题目
> 证明切比雪夫不等式：$P\{|X-E(X)|\geq\varepsilon\}\leq\frac{D(X)}{\varepsilon^2}$。

<details>
<summary>证明</summary>

设 $\mu=E(X)$。记 $A=\{|X-\mu|\geq\varepsilon\}$，则

$$D(X)=E\{[X-\mu]^2\}=\int_{-\infty}^{+\infty}(x-\mu)^2 f(x)\,dx$$

拆分积分区域为 $A$ 和 $A^c$：

$$\geq\int_A(x-\mu)^2 f(x)\,dx\geq\int_A\varepsilon^2 f(x)\,dx=\varepsilon^2 P(A)=\varepsilon^2 P\{|X-\mu|\geq\varepsilon\}$$

故 $P\{|X-\mu|\geq\varepsilon\}\leq\frac{D(X)}{\varepsilon^2}$。

</details>

---

## 考点统计

| 题型 | 题数 | 主要考点 |
|:---:|:---:|:---|
| 填空 | 10 | 六大分布期望方差、方差/协方差/相关系数公式、标准化、独立和方差 |
| 选择 | 10 | 期望性质辨析、独立和不相关关系、$|\rho|=1$ 含义、$E(X^2)$ 计算、协方差矩阵性质 |
| 计算 | 8 | 密度期望方差、线性组合、协方差相关系数、函数期望、切比雪夫估计、非线性函数 |
| 证明 | 4 | 方差为零充要条件、独立和方差、不相关不独立反例、切比雪夫不等式 |

## 章节导航

- 上一级：[[MOC - 概率论与数理统计B]]
- 本章知识点：[[MOC - 第4章]]
- 上一章习题：[[MOC - 第3章习题]]
- 下一章习题：[[MOC - 第5章习题]]
