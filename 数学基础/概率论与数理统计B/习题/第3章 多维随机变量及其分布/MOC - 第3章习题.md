---
domain: 数学基础
subject: 概率论与数理统计B
type: exercise
chapter: 第3章 多维随机变量及其分布
tags: [概率论,数理统计,习题,多维随机变量,联合分布,边缘分布,条件分布,独立性]
prerequisites: ["高等数学", "概率论与数理统计B/第3章 多维随机变量及其分布"]
aliases: [第3章习题, 多维随机变量习题]
---

# MOC - 第3章习题：多维随机变量及其分布

> [!abstract] 本章习题导航
> 本组习题覆盖 [[MOC - 第3章]] 全部内容，分四类共 32 题：
>
> - **填空题**（10 题）：边缘密度、条件概率、独立性判定、卷积
> - **选择题**（10 题）：分布函数性质、边缘与联合关系、正态可加性、极值分布
> - **计算题**（8 题）：联合/边缘/条件密度计算、卷积、极值
> - **证明题**（4 题）：独立性证明、边缘不能决定联合、正态独立充要条件

---

## 一、填空题（10 题）

### 填空 1

> [!question] 题目
> 设 $(X,Y)$ 的联合分布函数为 $F(x,y)$，则 $X$ 的边缘分布函数 $F_X(x)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$F_X(x)=F(x,+\infty)=\lim_{y\to+\infty}F(x,y)$$

</details>

---

### 填空 2

> [!question] 题目
> 设离散型 $(X,Y)$ 的联合分布律为 $p_{ij}$，则 $Y$ 的边缘分布律 $P\{Y=y_j\}=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$p_{\cdot j}=\sum_{i}p_{ij}$$

即对第 $j$ 列求和。

</details>

---

### 填空 3

> [!question] 题目
> 设连续型 $(X,Y)$ 的联合密度为 $f(x,y)$，则 $X$ 的边缘密度 $f_X(x)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$f_X(x)=\int_{-\infty}^{+\infty}f(x,y)\,dy$$

</details>

---

### 填空 4

> [!question] 题目
> 设连续型 $(X,Y)$ 的联合密度为 $f(x,y)$，$Y$ 的边缘密度为 $f_Y(y)>0$，则条件密度 $f_{X|Y}(x\mid y)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$f_{X|Y}(x\mid y)=\frac{f(x,y)}{f_Y(y)}$$

</details>

---

### 填空 5

> [!question] 题目
> 设 $X,Y$ 独立，$X\sim N(0,1)$，$Y\sim N(0,1)$，则 $X+Y\sim$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

由正态可加性：$X+Y\sim N(0,1+1)=N(0,2)$。

</details>

---

### 填空 6

> [!question] 题目
> 设 $X,Y$ 独立同分布，分布函数为 $F(x)$，则 $\max(X,Y)$ 的分布函数为 $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$F_{\max}(z)=[F(z)]^2$$

</details>

---

### 填空 7

> [!question] 题目
> 设 $X,Y$ 独立同分布，分布函数为 $F(x)$，则 $\min(X,Y)$ 的分布函数为 $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$F_{\min}(z)=1-[1-F(z)]^2$$

</details>

---

### 填空 8

> [!question] 题目
> 设 $X,Y$ 独立，$f_X(x)$ 和 $f_Y(y)$ 分别为其密度，则 $Z=X+Y$ 的密度 $f_Z(z)=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$f_Z(z)=\int_{-\infty}^{+\infty}f_X(x)\cdot f_Y(z-x)\,dx$$

</details>

---

### 填空 9

> [!question] 题目
> 二维正态分布 $N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$ 中，$X,Y$ 独立的充要条件是 $\underline{\qquad}$。

<details>
<summary>答案</summary>

$$\rho=0$$

</details>

---

### 填空 10

> [!question] 题目
> 设 $(X,Y)$ 在区域 $D=\{(x,y)\mid 0<x<2,0<y<2\}$ 上服从均匀分布，则 $P\{0<X<1,0<Y<1\}=$ $\underline{\qquad}$。

<details>
<summary>答案</summary>

区域面积 $A=4$，联合密度 $f=\frac{1}{4}$。所求子区域面积为 $1$，故

$$P=\frac{1}{4}$$

</details>

---

## 二、选择题（10 题）

### 选择 1

> [!question] 题目
> 设 $F(x,y)$ 为二维随机变量的联合分布函数，下列性质不成立的是：
>
> A. $F(-\infty,y)=0$
> B. $F(+\infty,+\infty)=1$
> C. $F$ 关于 $x,y$ 分别单调不减
> D. $F(x,y)$ 关于 $x$ 和 $y$ 都左连续

<details>
<summary>答案</summary>

**D**。联合分布函数关于 $x$ 和 $y$ 都是**右连续**，而非左连续。

</details>

---

### 选择 2

> [!question] 题目
> 设 $(X,Y)$ 的联合密度 $f(x,y)$ 在全平面连续，则下列正确的是：
>
> A. 边缘密度可唯一确定联合密度
> B. 联合密度可唯一确定边缘密度
> C. 边缘密度与联合密度相互唯一确定
> D. 以上都不对

<details>
<summary>答案</summary>

**B**。联合密度积分得边缘密度（唯一），但边缘密度一般不能唯一确定联合密度（丢失相依结构）。

</details>

---

### 选择 3

> [!question] 题目
> 设 $X\sim N(1,4)$，$Y\sim N(2,9)$ 且 $X,Y$ 独立，则 $X+Y\sim$：
>
> A. $N(3,13)$
> B. $N(3,5)$
> C. $N(3,36)$
> D. $N(2,13)$

<details>
<summary>答案</summary>

**A**。$\mu=1+2=3$，$\sigma^2=4+9=13$，故 $X+Y\sim N(3,13)$。

</details>

---

### 选择 4

> [!question] 题目
> 关于二维正态分布 $N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$，下列正确的是：
>
> A. $\rho=0$ 时 $X,Y$ 不相关但不一定独立
> B. $\rho=0 \Leftrightarrow X,Y$ 独立
> C. $X,Y$ 独立 $\Rightarrow \rho\neq0$
> D. $\rho$ 可取任意实数

<details>
<summary>答案</summary>

**B**。二维正态中 $\rho=0 \Leftrightarrow$ 独立（不相关即独立，这是正态特有性质）。$\rho\in(-1,1)$。

</details>

---

### 选择 5

> [!question] 题目
> 设 $X,Y$ 独立，分布函数分别为 $F_X,F_Y$，则 $M=\max(X,Y)$ 的分布函数为：
>
> A. $F_X(z)+F_Y(z)$
> B. $F_X(z)\cdot F_Y(z)$
> C. $1-[1-F_X(z)][1-F_Y(z)]$
> D. $[F_X(z)+F_Y(z)]/2$

<details>
<summary>答案</summary>

**B**。$\max(X,Y)\leq z \Leftrightarrow X\leq z$ 且 $Y\leq z$，独立时概率相乘。

</details>

---

### 选择 6

> [!question] 题目
> 设 $X,Y$ 独立，$X\sim U(0,1)$，$Y\sim U(0,1)$，则 $Z=X+Y$ 的密度在 $z=0.5$ 处的值为：
>
> A. $0.5$
> B. $1$
> C. $0.5$（即 $z$）
> D. $1.5$

<details>
<summary>答案</summary>

**A**。$0<z<1$ 时 $f_Z(z)=z$，故 $f_Z(0.5)=0.5$。

</details>

---

### 选择 7

> [!question] 题目
> 下列说法正确的是：
>
> A. $X,Y$ 独立则 $f(x,y)=f_X(x)f_Y(y)$
> B. $f(x,y)=f_X(x)f_Y(y)$ 不一定推出独立
> C. 独立的定义是 $f(x,y)=f_X(x)+f_Y(y)$
> D. 独立要求 $f_X(x)$ 和 $f_Y(y)$ 相等

<details>
<summary>答案</summary>

**A**。独立 $\Leftrightarrow$ 联合密度 = 边缘密度之积（几乎处处）。

</details>

---

### 选择 8

> [!question] 题目
> 设 $X_1,\ldots,X_n$ 独立同分布，$F(x)$ 为公共分布函数，$N=\min(X_1,\ldots,X_n)$，则 $F_N(z)=$：
>
> A. $[F(z)]^n$
> B. $1-[1-F(z)]^n$
> C. $nF(z)$
> D. $F(z)^n$

<details>
<summary>答案</summary>

**B**。$\min\leq z$ 的补事件是所有 $X_i>z$，独立时概率相乘：$P\{\min>z\}=[1-F(z)]^n$，故 $F_N=1-[1-F]^n$。

</details>

---

### 选择 9

> [!question] 题目
> 设 $(X,Y)$ 的联合密度 $f(x,y)=g(x)h(y)$（在矩形区域上），则：
>
> A. $X,Y$ 不一定独立
> B. $X,Y$ 独立
> C. $X,Y$ 一定不独立
> D. 无法判断

<details>
<summary>答案</summary>

**B**。联合密度可因式分解为只含 $x$ 和只含 $y$ 的函数之积，且定义域为矩形，故独立。

</details>

---

### 选择 10

> [!question] 题目
> 设 $X,Y$ 独立，$X\sim\mathrm{Exp}(\lambda)$，$Y\sim\mathrm{Exp}(\lambda)$，则 $\min(X,Y)\sim$：
>
> A. $\mathrm{Exp}(2\lambda)$
> B. $\mathrm{Exp}(\lambda)$
> C. $\mathrm{Exp}(\lambda/2)$
> D. $U(0,2)$

<details>
<summary>答案</summary>

**A**。$F_{\min}(t)=1-e^{-2\lambda t}$，即 $\min\sim\mathrm{Exp}(2\lambda)$，失效率叠加。

</details>

---

## 三、计算题（8 题）

### 计算 1

> [!question] 题目
> 设 $(X,Y)$ 的联合密度为 $f(x,y)=\begin{cases}e^{-y},&0<x<y\\0,&\text{其他}\end{cases}$，求边缘密度 $f_X(x)$、$f_Y(y)$。

<details>
<summary>解答</summary>

当 $x>0$ 时：$f_X(x)=\int_x^{+\infty}e^{-y}\,dy=e^{-x}$，故 $f_X(x)=e^{-x}\;(x>0)$，即 $X\sim\mathrm{Exp}(1)$。

当 $y>0$ 时：$f_Y(y)=\int_0^y e^{-y}\,dx=ye^{-y}$，故 $f_Y(y)=ye^{-y}\;(y>0)$。

</details>

---

### 计算 2

> [!question] 题目
> 设 $(X,Y)$ 的联合密度 $f(x,y)=\begin{cases}2,&0<x<1,0<y<x\\0,&\text{其他}\end{cases}$，求条件密度 $f_{Y|X}(y\mid x)$。

<details>
<summary>解答</summary>

当 $0<x<1$ 时：$f_X(x)=\int_0^x 2\,dy=2x$。

$$f_{Y|X}(y\mid x)=\frac{f(x,y)}{f_X(x)}=\frac{2}{2x}=\frac{1}{x},\qquad 0<y<x$$

即在 $X=x$ 条件下，$Y\sim U(0,x)$。

</details>

---

### 计算 3

> [!question] 题目
> 设 $X,Y$ 独立，$X\sim U(0,1)$，$Y\sim U(0,1)$，求 $Z=X+Y$ 的密度。

<details>
<summary>解答</summary>

由卷积公式 $f_Z(z)=\int f_X(x)f_Y(z-x)\,dx$，需 $0<x<1$ 且 $0<z-x<1$。

- $0<z<1$：$0<x<z$，$f_Z(z)=\int_0^z dx=z$
- $1\leq z<2$：$z-1<x<1$，$f_Z(z)=\int_{z-1}^1 dx=2-z$

$$f_Z(z)=\begin{cases}z,&0<z<1\\2-z,&1\leq z<2\\0,&\text{其他}\end{cases}$$

</details>

---

### 计算 4

> [!question] 题目
> 设 $X,Y$ 独立，$X\sim N(0,1)$，$Y\sim N(0,1)$，求 $P\{X+Y\leq1\}$。

<details>
<summary>解答</summary>

$Z=X+Y\sim N(0,2)$，故

$$P\{Z\leq1\}=\Phi\!\left(\frac{1-0}{\sqrt{2}}\right)=\Phi\!\left(\frac{\sqrt{2}}{2}\right)$$

</details>

---

### 计算 5

> [!question] 题目
> 设 $(X,Y)$ 的联合密度 $f(x,y)=\begin{cases}1,&0<x<1,0<y<1\\0,&\text{其他}\end{cases}$，求 $Z=X/Y$ 的密度。

<details>
<summary>解答</summary>

由商公式：$f_Z(z)=\int|y|\cdot f(zy,y)\,dy$，需 $0<zy<1$ 且 $0<y<1$。

- $z>0$：$y<1$ 且 $zy<1$ 即 $y<\min(1,1/z)$
  - $0<z<1$：$y<1$，$f_Z(z)=\int_0^1 y\,dy=\frac{1}{2}$
  - $z\geq1$：$y<1/z$，$f_Z(z)=\int_0^{1/z}y\,dy=\frac{1}{2z^2}$

$$f_Z(z)=\begin{cases}\frac{1}{2},&0<z<1\\\frac{1}{2z^2},&z\geq1\\0,&\text{其他}\end{cases}$$

</details>

---

### 计算 6

> [!question] 题目
> 设系统由 3 个独立元件串联，各元件寿命 $\sim\mathrm{Exp}(\lambda)$，求系统寿命的分布。

<details>
<summary>解答</summary>

串联系统寿命 $N=\min(T_1,T_2,T_3)$。$F(t)=1-e^{-\lambda t}$，故

$$F_N(t)=1-[1-F(t)]^3=1-e^{-3\lambda t}$$

即 $N\sim\mathrm{Exp}(3\lambda)$。

</details>

---

### 计算 7

> [!question] 题目
> 设 $(X,Y)$ 的联合分布律为
>
> | $X\backslash Y$ | 1 | 2 | 3 |
> |:---:|:---:|:---:|:---:|
> | 1 | $\frac{1}{6}$ | $\frac{1}{9}$ | $\frac{1}{18}$ |
> | 2 | $\frac{1}{3}$ | $\alpha$ | $\beta$ |
>
> 若 $X,Y$ 独立，求 $\alpha,\beta$。

<details>
<summary>解答</summary>

边缘：$p_{1\cdot}=\frac{1}{6}+\frac{1}{9}+\frac{1}{18}=\frac{1}{3}$，$p_{2\cdot}=\frac{2}{3}$。

$p_{\cdot1}=\frac{1}{6}+\frac{1}{3}=\frac{1}{2}$，$p_{\cdot2}=\frac{1}{9}+\alpha$，$p_{\cdot3}=\frac{1}{18}+\beta$。

独立性要求 $p_{ij}=p_{i\cdot}p_{\cdot j}$：

$P\{X=1,Y=1\}=\frac{1}{3}\cdot\frac{1}{2}=\frac{1}{6}$ ✓

$P\{X=1,Y=2\}=\frac{1}{3}\cdot(\frac{1}{9}+\alpha)=\frac{1}{9}$，得 $\frac{1}{9}+\alpha=\frac{1}{3}$，$\alpha=\frac{2}{9}$。

规范性：$\frac{1}{6}+\frac{1}{9}+\frac{1}{18}+\frac{1}{3}+\alpha+\beta=1$，即 $\frac{2}{3}+\alpha+\beta=1$，$\beta=\frac{1}{3}-\alpha=\frac{1}{9}$。

验证：$P\{X=1,Y=3\}=\frac{1}{3}\cdot(\frac{1}{18}+\beta)=\frac{1}{3}\cdot\frac{1}{6}=\frac{1}{18}$ ✓

$$\alpha=\frac{2}{9},\quad\beta=\frac{1}{9}$$

</details>

---

### 计算 8

> [!question] 题目
> 设 $(X,Y)\sim N(0,0,1,1,\rho)$，求条件密度 $f_{X|Y}(x\mid y)$。

<details>
<summary>解答</summary>

边缘 $f_Y(y)=\frac{1}{\sqrt{2\pi}}e^{-y^2/2}$。

$$f_{X|Y}(x\mid y)=\frac{f(x,y)}{f_Y(y)}=\frac{1}{\sqrt{2\pi(1-\rho^2)}}\exp\!\left[-\frac{(x-\rho y)^2}{2(1-\rho^2)}\right]$$

即在 $Y=y$ 条件下，$X\sim N(\rho y,1-\rho^2)$。

</details>

---

## 四、证明题（4 题）

### 证明 1

> [!question] 题目
> 证明：若 $X,Y$ 独立，则对任意常数 $a,b$（$a\neq0$），$aX$ 与 $bY$ 也独立。

<details>
<summary>证明</summary>

$X,Y$ 独立 $\Rightarrow F(x,y)=F_X(x)F_Y(y)$。设 $U=aX$，$V=bY$。

$$F_{U,V}(u,v)=P\{aX\leq u,bY\leq v\}$$

当 $a>0,b>0$：$=P\{X\leq u/a,Y\leq v/b\}=F_X(u/a)F_Y(v/b)=F_U(u)F_V(v)$。

类似讨论 $a<0$（不等号反向）的情况，均有 $F_{U,V}=F_U\cdot F_V$。故 $aX$ 与 $bY$ 独立。

</details>

---

### 证明 2

> [!question] 题目
> 举例证明：边缘分布不能决定联合分布。

<details>
<summary>证明</summary>

取 $f_X(x)=2x$，$f_Y(y)=2y$（$0<x,y<1$）。

- **情形1**（独立）：$f_1(x,y)=4xy$
- **情形2**（不独立）：取 $f_2(x,y)=\begin{cases}\frac{3}{2}(x^2+y^2),&0<x,y<1\\0,&\text{其他}\end{cases}$

验证 $f_2$ 的规范性：$\int_0^1\int_0^1\frac{3}{2}(x^2+y^2)\,dx\,dy=\frac{3}{2}\cdot\frac{2}{3}=1$ ✓

$f_2$ 的边缘：$f_{2,X}(x)=\int_0^1\frac{3}{2}(x^2+y^2)\,dy=\frac{3}{2}x^2+\frac{1}{2}\neq 2x=f_1$ 的边缘。

故两组联合分布有**不同的**联合密度，说明边缘分布不唯一确定联合分布。

</details>

---

### 证明 3

> [!question] 题目
> 证明：二维正态分布 $N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$ 中，$\rho=0 \Leftrightarrow X,Y$ 独立。

<details>
<summary>证明</summary>

**($\Leftarrow$)** 若 $X,Y$ 独立，则 $f(x,y)=f_X(x)f_Y(y)$。比较联合密度与边缘密度乘积的表达式，交叉项 $\frac{-2\rho(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2}$ 必须消失，故 $\rho=0$。

**($\Rightarrow$)** 若 $\rho=0$，联合密度中 $\frac{1}{2(1-\rho^2)}=\frac{1}{2}$，交叉项消失：

$$f(x,y)=\frac{1}{2\pi\sigma_1\sigma_2}\exp\!\left[-\frac{(x-\mu_1)^2}{2\sigma_1^2}-\frac{(y-\mu_2)^2}{2\sigma_2^2}\right]=f_X(x)\cdot f_Y(y)$$

故 $X,Y$ 独立。

</details>

---

### 证明 4

> [!question] 题目
> 证明：若 $X_1,\ldots,X_n$ 独立同分布，$F(x)$ 为公共分布函数，则 $M=\max(X_1,\ldots,X_n)$ 的分布函数为 $[F(x)]^n$。

<details>
<summary>证明</summary>

$$F_M(z)=P\{M\leq z\}=P\{X_1\leq z,\ldots,X_n\leq z\}$$

由独立性：

$$=\prod_{i=1}^n P\{X_i\leq z\}=\prod_{i=1}^n F(z)=[F(z)]^n$$

</details>

---

## 考点统计

| 题型 | 题数 | 主要考点 |
|:---:|:---:|:---|
| 填空 | 10 | 边缘/条件密度公式、卷积、极值分布、正态可加性、独立充要条件 |
| 选择 | 10 | 分布函数性质、边缘与联合关系、正态独立 $\rho=0$、卷积结果、极值公式 |
| 计算 | 8 | 联合→边缘、条件密度、卷积求和的分布、正态和概率、商分布、极值、独立性反求参数 |
| 证明 | 4 | 独立性的线性变换、边缘不能决定联合、正态独立充要条件、极值分布推导 |

## 章节导航

- 上一级：[[MOC - 概率论与数理统计B]]
- 本章知识点：[[MOC - 第3章]]
- 上一章习题：[[MOC - 第2章习题]]
- 下一章习题：[[MOC - 第4章习题]]
