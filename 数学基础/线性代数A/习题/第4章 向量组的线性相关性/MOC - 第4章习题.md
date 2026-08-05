---
domain: 数学基础
subject: 线性代数A
type: exercise
chapter: 第4章 向量组的线性相关性
tags: [线性代数,习题,线性相关,极大无关组,基础解系,通解结构]
prerequisites: ["第3章 矩阵初等变换与线性方程组"]
aliases: [第4章习题, 向量组习题]
---

# MOC - 第4章习题 向量组的线性相关性

> [!info] 习题说明
> 本章习题共 **30 题**，覆盖填空、选择、计算、证明四类。重点考查：线性相关判定、极大无关组求法、基础解系求解、通解结构、含参数讨论、抽象向量组证明。
>
> 相关知识点：[[4.1 n维向量概念、线性表示]]、[[4.2 向量组线性相关与无关]]、[[4.3 向量组极大无关组、向量组的秩]]、[[4.4 齐次线性方程组解空间、基础解系]]、[[4.5 非齐次线性方程组通解结构]]、[[MOC - 第4章]]。

## 一、填空题（6 题）

**1.** 设 $\boldsymbol\alpha_1,\boldsymbol\alpha_2,\boldsymbol\alpha_3$ 线性无关，则 $\boldsymbol\alpha_1+\boldsymbol\alpha_2,\boldsymbol\alpha_2+\boldsymbol\alpha_3,\boldsymbol\alpha_3+\boldsymbol\alpha_1$ 的线性相关性是 ______。

<details>
<summary>答案</summary>

**线性无关**。设 $k_1(\boldsymbol\alpha_1+\boldsymbol\alpha_2)+k_2(\boldsymbol\alpha_2+\boldsymbol\alpha_3)+k_3(\boldsymbol\alpha_3+\boldsymbol\alpha_1)=\boldsymbol0$，整理得 $(k_1+k_3)\boldsymbol\alpha_1+(k_1+k_2)\boldsymbol\alpha_2+(k_2+k_3)\boldsymbol\alpha_3=\boldsymbol0$。由 $\boldsymbol\alpha_i$ 无关，解方程组 $\begin{cases}k_1+k_3=0\\k_1+k_2=0\\k_2+k_3=0\end{cases}$ 得 $k_1=k_2=k_3=0$（系数行列式 $=2\ne0$）。
</details>

**2.** 设 $A$ 为 $3\times 5$ 矩阵，$r(A)=2$，则齐次方程组 $A\boldsymbol x=\boldsymbol0$ 的基础解系含 ______ 个解向量。

<details>
<summary>答案</summary>

$n-r(A)=5-2=3$ 个。
</details>

**3.** 设 $\boldsymbol\alpha_1=(1,2,3)^\top,\boldsymbol\alpha_2=(2,4,6)^\top,\boldsymbol\alpha_3=(3,6,9)^\top$，则该向量组的秩为 ______。

<details>
<summary>答案</summary>

$r=1$。三个向量都是 $(1,2,3)^\top$ 的倍数，互相共线。
</details>

**4.** 设 $A\boldsymbol x=\boldsymbol0$ 的基础解系为 $\boldsymbol\xi_1,\boldsymbol\xi_2$，则 $A\boldsymbol x=\boldsymbol0$ 的通解为 ______。

<details>
<summary>答案</summary>

$\boldsymbol x=k_1\boldsymbol\xi_1+k_2\boldsymbol\xi_2,\ k_1,k_2\in\mathbb{R}$。
</details>

**5.** 设 $A\boldsymbol x=\boldsymbol b$ 有特解 $\boldsymbol\eta^*$，导出组基础解系为 $\boldsymbol\xi_1,\boldsymbol\xi_2,\boldsymbol\xi_3$，则 $A\boldsymbol x=\boldsymbol b$ 的通解为 ______。

<details>
<summary>答案</summary>

$\boldsymbol\eta=\boldsymbol\eta^*+k_1\boldsymbol\xi_1+k_2\boldsymbol\xi_2+k_3\boldsymbol\xi_3,\ k_i\in\mathbb{R}$。
</details>

**6.** 设 $\boldsymbol\alpha_1=(1,0,0)^\top,\boldsymbol\alpha_2=(0,1,0)^\top,\boldsymbol\alpha_3=(0,0,1)^\top,\boldsymbol\alpha_4=(1,1,1)^\top$，则该向量组线性 ______（填"相关"或"无关"）。

<details>
<summary>答案</summary>

**相关**。4 个 3 维向量，$m=4>n=3$，必线性相关。
</details>

## 二、选择题（6 题）

**7.** 下列命题正确的是（$\quad$）。

A. 若 $\boldsymbol\alpha_1,\boldsymbol\alpha_2,\boldsymbol\alpha_3$ 线性相关，则其中任一向量都可由其余两个线性表示
B. 若 $\boldsymbol\alpha_1,\boldsymbol\alpha_2,\boldsymbol\alpha_3$ 线性无关，则 $\boldsymbol\alpha_1-\boldsymbol\alpha_2,\boldsymbol\alpha_2-\boldsymbol\alpha_3,\boldsymbol\alpha_3-\boldsymbol\alpha_1$ 线性无关
C. 含零向量的向量组必线性相关
D. 若 $\boldsymbol\alpha_1$ 不能由 $\boldsymbol\alpha_2,\dots,\boldsymbol\alpha_m$ 线性表示，则 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_m$ 线性无关

<details>
<summary>答案</summary>

**C**。

- A 错：线性相关只保证"**至少一个**向量可由其余表示"，并非"每一个"。反例 $\boldsymbol\alpha_1=(1,0),\boldsymbol\alpha_2=(2,0),\boldsymbol\alpha_3=(0,1)$，整体相关（$\boldsymbol\alpha_2=2\boldsymbol\alpha_1$），但 $\boldsymbol\alpha_3$ 不能由 $\boldsymbol\alpha_1,\boldsymbol\alpha_2$ 表示。
- B 错：$(\boldsymbol\alpha_1-\boldsymbol\alpha_2)+(\boldsymbol\alpha_2-\boldsymbol\alpha_3)+(\boldsymbol\alpha_3-\boldsymbol\alpha_1)=\boldsymbol0$，三向量之和为零，故线性相关。
- C 正确：若 $\boldsymbol\alpha_i=\boldsymbol0$，取 $k_i=1$、其余系数为 $0$，即得 $\sum k_j\boldsymbol\alpha_j=\boldsymbol0$ 且系数不全零。
- D 错：反例 $\boldsymbol\alpha_1=(1,0),\boldsymbol\alpha_2=(0,0),\boldsymbol\alpha_3=(2,0)$，$\boldsymbol\alpha_1$ 不能由 $\boldsymbol\alpha_2,\boldsymbol\alpha_3$ 表示，但整体含零向量故线性相关。
</details>

**8.** 向量组 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_m$ 线性无关的充要条件是（$\quad$）。

A. 其中任一向量都不能由其他向量线性表示
B. 其中没有两个向量成比例
C. 其中存在一个非空部分组线性无关
D. $\sum k_i\boldsymbol\alpha_i=\boldsymbol0$ 必有 $k_i$ 全为零

<details>
<summary>答案</summary>

**D**。这是线性无关定义的直接表述。

- A 在 $m\ge2$ 时是等价刻画，但 $m=1$ 时"无其他向量可言"，表述不严密，不作为通用充要条件；
- B 错：仅"两两不成比例"不能保证整体无关。反例 $\boldsymbol\alpha_1=(1,0),\boldsymbol\alpha_2=(0,1),\boldsymbol\alpha_3=(1,1)$ 两两不成比例但 $\boldsymbol\alpha_3=\boldsymbol\alpha_1+\boldsymbol\alpha_2$ 使整体相关；
- C 错：仅"存在"一个无关部分组不能保证整体无关（任一含非零向量的组都存在单向量无关部分组）。反例 $\boldsymbol\alpha_1=(1,0),\boldsymbol\alpha_2=(2,0)$ 相关，但 $\{\boldsymbol\alpha_1\}$ 是无关部分组；
- D 是定义，正确。
</details>

**9.** 设 $A$ 为 $m\times n$ 矩阵，$r(A)=r<n$，则 $A\boldsymbol x=\boldsymbol0$ 的基础解系中解向量个数是（$\quad$）。

A. $r$ $\quad$ B. $n-r$ $\quad$ C. $m-r$ $\quad$ D. $n$

<details>
<summary>答案</summary>

**B**。基础解系向量个数 $=n-r(A)=n-r$。
</details>

**10.** 设 $\boldsymbol\alpha_1,\boldsymbol\alpha_2,\boldsymbol\alpha_3,\boldsymbol\alpha_4$ 是 $A\boldsymbol x=\boldsymbol0$ 的基础解系，则下列也是基础解系的是（$\quad$）。

A. $\boldsymbol\alpha_1+\boldsymbol\alpha_2,\boldsymbol\alpha_2+\boldsymbol\alpha_3,\boldsymbol\alpha_3+\boldsymbol\alpha_4,\boldsymbol\alpha_4+\boldsymbol\alpha_1$
B. $\boldsymbol\alpha_1-\boldsymbol\alpha_2,\boldsymbol\alpha_2-\boldsymbol\alpha_3,\boldsymbol\alpha_3-\boldsymbol\alpha_4,\boldsymbol\alpha_4-\boldsymbol\alpha_1$
C. $\boldsymbol\alpha_1,\boldsymbol\alpha_1+\boldsymbol\alpha_2,\boldsymbol\alpha_1+\boldsymbol\alpha_2+\boldsymbol\alpha_3,\boldsymbol\alpha_1+\boldsymbol\alpha_2+\boldsymbol\alpha_3+\boldsymbol\alpha_4$
D. $\boldsymbol\alpha_1+\boldsymbol\alpha_2,\boldsymbol\alpha_2+\boldsymbol\alpha_3,\boldsymbol\alpha_3+\boldsymbol\alpha_4$

<details>
<summary>答案</summary>

**C**。基础解系需含 4 个无关解。B 中四向量之和为 $\boldsymbol0$（相关），错；D 只有 3 个向量，错；A 中 $\boldsymbol\alpha_1+\boldsymbol\alpha_2+\boldsymbol\alpha_3+\boldsymbol\alpha_4$ 各出现两次，相加为零，故 $(\boldsymbol\alpha_1+\boldsymbol\alpha_2)+(\boldsymbol\alpha_3+\boldsymbol\alpha_4)=(\boldsymbol\alpha_2+\boldsymbol\alpha_3)+(\boldsymbol\alpha_4+\boldsymbol\alpha_1)$，相关，错。C 是上三角变换（系数矩阵 $\begin{pmatrix}1&0&0&0\\1&1&0&0\\1&1&1&0\\1&1&1&1\end{pmatrix}$，行列式 $=1\ne0$），与原基础解系等价且无关，是基础解系。
</details>

**11.** 设 $A\boldsymbol x=\boldsymbol b$ 有两个解 $\boldsymbol\eta_1,\boldsymbol\eta_2$，则下列是 $A\boldsymbol x=\boldsymbol0$ 的解的是（$\quad$）。

A. $\boldsymbol\eta_1+\boldsymbol\eta_2$ $\quad$ B. $\boldsymbol\eta_1-\boldsymbol\eta_2$ $\quad$ C. $2\boldsymbol\eta_1$ $\quad$ D. $\boldsymbol\eta_1\boldsymbol\eta_2$

<details>
<summary>答案</summary>

**B**。由非齐次解性质 1，$\boldsymbol\eta_1-\boldsymbol\eta_2$ 是导出组的解。$A(\boldsymbol\eta_1+\boldsymbol\eta_2)=2\boldsymbol b\ne\boldsymbol0$；$A(2\boldsymbol\eta_1)=2\boldsymbol b\ne\boldsymbol0$；D 无意义（向量无乘积）。
</details>

**12.** 设 $A$ 为 $n$ 阶方阵，$|A|=0$，则（$\quad$）。

A. $A$ 的列向量组线性无关
B. $A\boldsymbol x=\boldsymbol0$ 只有零解
C. $A$ 的列向量组线性相关
D. $A$ 的秩为 $n$

<details>
<summary>答案</summary>

**C**。$|A|=0\iff r(A)<n\iff A$ 的列向量组（$n$ 个 $n$ 维向量）线性相关。B 错（应有非零解）；D 错（秩 $<n$）；A 错。
</details>

## 三、计算题（12 题）

**13.** 判断向量组 $\boldsymbol\alpha_1=(1,1,1)^\top,\boldsymbol\alpha_2=(1,2,3)^\top,\boldsymbol\alpha_3=(1,3,6)^\top$ 的线性相关性。

<details>
<summary>解答</summary>

3 个 3 维向量，算行列式：
$$|A|=\begin{vmatrix}1&1&1\\1&2&3\\1&3&6\end{vmatrix}=1(12-9)-1(6-3)+1(3-2)=3-3+1=1\ne0$$
$|A|\ne0$，故 $\boxed{\text{线性无关}}$。
</details>

**14.** 判断向量组 $\boldsymbol\alpha_1=(1,2,3)^\top,\boldsymbol\alpha_2=(2,3,1)^\top,\boldsymbol\alpha_3=(3,5,4)^\top$ 的线性相关性。

<details>
<summary>解答</summary>

$$|A|=\begin{vmatrix}1&2&3\\2&3&1\\3&5&4\end{vmatrix}=1(12-5)-2(8-3)+3(10-9)=7-10+3=0$$
$|A|=0$，故 $\boxed{\text{线性相关}}$（事实上 $\boldsymbol\alpha_3=\boldsymbol\alpha_1+\boldsymbol\alpha_2$）。
</details>

**15.** 求向量组 $\boldsymbol\alpha_1=(1,1,1,1)^\top,\boldsymbol\alpha_2=(1,2,3,4)^\top,\boldsymbol\alpha_3=(2,3,4,5)^\top,\boldsymbol\alpha_4=(1,0,1,0)^\top$ 的一个极大无关组，并求其秩。

<details>
<summary>解答</summary>

按列拼成矩阵做行变换：
$$A=\begin{pmatrix}1&1&2&1\\1&2&3&0\\1&3&4&1\\1&4&5&0\end{pmatrix}\xrightarrow{\substack{r_2-r_1\\r_3-r_1\\r_4-r_1}}\begin{pmatrix}1&1&2&1\\0&1&1&-1\\0&2&2&0\\0&3&3&-1\end{pmatrix}\xrightarrow{\substack{r_3-2r_2\\r_4-3r_2}}\begin{pmatrix}1&1&2&1\\0&1&1&-1\\0&0&0&2\\0&0&0&2\end{pmatrix}\xrightarrow{r_4-r_3}\begin{pmatrix}1&1&2&1\\0&1&1&-1\\0&0&0&2\\0&0&0&0\end{pmatrix}$$
$r(A)=3$，秩为 $3$。主元列在第 $1,2,4$ 列，极大无关组为 $\boxed{\boldsymbol\alpha_1,\boldsymbol\alpha_2,\boldsymbol\alpha_4}$（也可取 $\boldsymbol\alpha_1,\boldsymbol\alpha_3,\boldsymbol\alpha_4$ 等）。
</details>

**16.** 求向量组 $\boldsymbol\alpha_1=(1,1,1)^\top,\boldsymbol\alpha_2=(1,2,3)^\top,\boldsymbol\alpha_3=(1,3,6)^\top,\boldsymbol\alpha_4=(2,3,4)^\top$ 的一个极大无关组，并把其余向量用该极大无关组线性表示。

<details>
<summary>解答</summary>

参见 [[4.3 向量组极大无关组、向量组的秩|4.3 节例 1]]，行最简形为 $\begin{pmatrix}1&0&0&1\\0&1&0&1\\0&0&1&0\end{pmatrix}$。
- 极大无关组：$\boldsymbol\alpha_1,\boldsymbol\alpha_2,\boldsymbol\alpha_3$；
- $\boldsymbol\alpha_4=\boldsymbol\alpha_1+\boldsymbol\alpha_2$（第 4 列 $(1,1,0)^\top$ 读出）。
</details>

**17.** 设 $\boldsymbol\alpha_1=(1,2,3)^\top,\boldsymbol\alpha_2=(2,3,1)^\top,\boldsymbol\beta=(3,5,4)^\top$。问 $\boldsymbol\beta$ 能否由 $\boldsymbol\alpha_1,\boldsymbol\alpha_2$ 线性表示？

<details>
<summary>解答</summary>

注意到 $\boldsymbol\beta=\boldsymbol\alpha_1+\boldsymbol\alpha_2$（分量验证：$1+2=3,2+3=5,3+1=4$ ✓），能表示：
$$\boxed{\boldsymbol\beta=\boldsymbol\alpha_1+\boldsymbol\alpha_2}$$
也可解方程组 $\begin{pmatrix}1&2\\2&3\\3&1\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}3\\5\\4\end{pmatrix}$，得 $x_1=x_2=1$，表示唯一。
</details>

**18.** 求齐次方程组 $\begin{cases}x_1+x_2-x_3-x_4=0\\x_1-2x_2+x_3-2x_4=0\end{cases}$ 的基础解系与通解。

<details>
<summary>解答</summary>

参见 [[4.4 齐次线性方程组解空间、基础解系|4.4 节例 1]]，行最简形 $\begin{pmatrix}1&0&-1/3&-4/3\\0&1&-2/3&1/3\end{pmatrix}$。
- 基础解系：$\boldsymbol\xi_1=(1,2,3,0)^\top,\boldsymbol\xi_2=(4,-1,0,3)^\top$；
- 通解：$\boldsymbol x=k_1(1,2,3,0)^\top+k_2(4,-1,0,3)^\top$。
</details>

**19.** 求齐次方程组 $\begin{cases}x_1-2x_2+x_3+x_4=0\\2x_1-4x_2+2x_3+2x_4=0\end{cases}$ 的基础解系。

<details>
<summary>解答</summary>

第二方程是第一方程的 2 倍，等价于一个方程 $x_1-2x_2+x_3+x_4=0$，行最简形 $\begin{pmatrix}1&-2&1&1\\0&0&0&0\end{pmatrix}$。
$r=1,n-r=3$，自由变量 $x_2,x_3,x_4$，由 $x_1=2x_2-x_3-x_4$。
- 取 $(x_2,x_3,x_4)=(1,0,0)$：$\boldsymbol\xi_1=(2,1,0,0)^\top$；
- 取 $(0,1,0)$：$\boldsymbol\xi_2=(-1,0,1,0)^\top$；
- 取 $(0,0,1)$：$\boldsymbol\xi_3=(-1,0,0,1)^\top$。

基础解系：$\boxed{\boldsymbol\xi_1=(2,1,0,0)^\top,\boldsymbol\xi_2=(-1,0,1,0)^\top,\boldsymbol\xi_3=(-1,0,0,1)^\top}$。
</details>

**20.** 求非齐次方程组 $\begin{cases}x_1+x_2+x_3+x_4=4\\x_1+2x_2-x_3+4x_4=5\\2x_1+3x_2+5x_4=9\end{cases}$ 的通解。

<details>
<summary>解答</summary>

参见 [[4.5 非齐次线性方程组通解结构|4.5 节例 1]]。
行最简形 $\begin{pmatrix}1&0&3&-2&3\\0&1&-2&3&1\\0&0&0&0&0\end{pmatrix}$，$r=2,n-r=2$，自由变量 $x_3,x_4$。
- 特解 $\boldsymbol\eta^*=(3,1,0,0)^\top$（令 $x_3=x_4=0$）；
- 基础解系 $\boldsymbol\xi_1=(-3,2,1,0)^\top,\boldsymbol\xi_2=(2,-3,0,1)^\top$。

通解：$\boxed{\boldsymbol\eta=(3,1,0,0)^\top+k_1(-3,2,1,0)^\top+k_2(2,-3,0,1)^\top}$。
</details>

**21.** 求非齐次方程组 $\begin{cases}x_1+2x_2+3x_3=6\\2x_1+4x_2+5x_3=11\\x_1+3x_2+4x_3=8\end{cases}$ 的通解。

<details>
<summary>解答</summary>

增广矩阵
$$\bar A=\begin{pmatrix}1&2&3&6\\2&4&5&11\\1&3&4&8\end{pmatrix}\xrightarrow{\substack{r_2-2r_1\\r_3-r_1}}\begin{pmatrix}1&2&3&6\\0&0&-1&-1\\0&1&1&2\end{pmatrix}\xrightarrow{r_2\leftrightarrow r_3}\begin{pmatrix}1&2&3&6\\0&1&1&2\\0&0&-1&-1\end{pmatrix}\xrightarrow{\substack{r_3\div(-1)\\r_2-r_3\\r_1-3r_3}}\begin{pmatrix}1&2&0&3\\0&1&0&1\\0&0&1&1\end{pmatrix}\xrightarrow{r_1-2r_2}\begin{pmatrix}1&0&0&1\\0&1&0&1\\0&0&1&1\end{pmatrix}$$
$r(A)=r(\bar A)=3=n$，**唯一解** $\boxed{\boldsymbol\eta=(1,1,1)^\top}$（无自由变量，特解即通解）。
</details>

**22.** 设 $A\boldsymbol x=\boldsymbol b$ 是 4 元非齐次方程组，$\boldsymbol\eta_1=(1,2,3,4)^\top,\boldsymbol\eta_2=(0,1,1,0)^\top,\boldsymbol\eta_3=(2,3,5,6)^\top$ 是其三个解，$r(A)=2$。求通解。

<details>
<summary>解答</summary>

参见 [[4.5 非齐次线性方程组通解结构|4.5 节例 2]]。$n-r=2$，需 2 个无关齐次解。
$$\boldsymbol\eta_1-\boldsymbol\eta_2=(1,1,2,4)^\top,\quad \boldsymbol\eta_1-\boldsymbol\eta_3=(-1,-1,-2,-2)^\top$$
二者不成比例（第四分量比 $\frac{4}{-2}=-2$ 与 $\frac{2}{-2}=1$ 不等），线性无关，作基础解系。取 $\boldsymbol\eta^*=\boldsymbol\eta_1$。
$$\boxed{\boldsymbol\eta=(1,2,3,4)^\top+k_1(1,1,2,4)^\top+k_2(-1,-1,-2,-2)^\top}$$
</details>

**23.** 讨论 $\lambda$ 取何值时方程组 $\begin{cases}x_1+x_2+x_3=1\\x_1+\lambda x_2+x_3=\lambda\\x_1+x_2+\lambda x_3=\lambda^2\end{cases}$ 有唯一解、无解、无穷多解；并求无穷多解时的通解。

<details>
<summary>解答</summary>

参见 [[4.5 非齐次线性方程组通解结构|4.5 节例 3]]。
$$\bar A\to\begin{pmatrix}1&1&1&1\\0&\lambda-1&0&\lambda-1\\0&0&\lambda-1&\lambda^2-1\end{pmatrix}$$
- $\lambda\ne 1$：$r(A)=r(\bar A)=3=n$，**唯一解**；
- $\lambda=1$：$r(A)=r(\bar A)=1<3$，**无穷多解**，行最简形 $\begin{pmatrix}1&1&1&1\\0&0&0&0\\0&0&0&0\end{pmatrix}$。

$\lambda=1$ 时通解：$\boxed{\boldsymbol\eta=(1,0,0)^\top+k_1(-1,1,0)^\top+k_2(-1,0,1)^\top}$。

（本题不存在无解情形。）
</details>

**24.** 求矩阵 $A=\begin{pmatrix}1&2&3\\2&3&1\\3&5&4\end{pmatrix}$ 的列向量组的秩与一个极大无关组。

<details>
<summary>解答</summary>

$$|A|=\begin{vmatrix}1&2&3\\2&3&1\\3&5&4\end{vmatrix}=0$$（参见 14 题），故秩 $<3$。又 $\begin{vmatrix}1&2\\2&3\end{vmatrix}=3-4=-1\ne0$，故秩 $=2$。
极大无关组可取前两列 $\boxed{\boldsymbol\alpha_1,\boldsymbol\alpha_2}$（秩 $2$），且 $\boldsymbol\alpha_3=\boldsymbol\alpha_1+\boldsymbol\alpha_2$。
</details>

## 四、证明题（6 题）

**25.** 证明：若 $\boldsymbol\alpha_1,\boldsymbol\alpha_2,\dots,\boldsymbol\alpha_m$ 线性无关，而 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_m,\boldsymbol\beta$ 线性相关，则 $\boldsymbol\beta$ 可由 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_m$ 线性表示，且表示唯一。

<details>
<summary>证明</summary>

由 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_m,\boldsymbol\beta$ 相关，存在不全零的 $k_1,\dots,k_m,k$ 使
$$k_1\boldsymbol\alpha_1+\cdots+k_m\boldsymbol\alpha_m+k\boldsymbol\beta=\boldsymbol0$$
若 $k=0$，则 $k_1\boldsymbol\alpha_1+\cdots+k_m\boldsymbol\alpha_m=\boldsymbol0$ 且 $k_i$ 不全零，与 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_m$ 无关矛盾。故 $k\ne0$，于是
$$\boldsymbol\beta=-\frac{k_1}{k}\boldsymbol\alpha_1-\cdots-\frac{k_m}{k}\boldsymbol\alpha_m$$
即 $\boldsymbol\beta$ 可由 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_m$ 表示。

**唯一性**：设 $\boldsymbol\beta=\sum k_i\boldsymbol\alpha_i=\sum k_i'\boldsymbol\alpha_i$，则 $\sum(k_i-k_i')\boldsymbol\alpha_i=\boldsymbol0$。由无关性 $k_i-k_i'=0$，即 $k_i=k_i'$。表示唯一。$\blacksquare$
</details>

**26.** 设 $\boldsymbol\alpha_1,\boldsymbol\alpha_2,\dots,\boldsymbol\alpha_m$ 线性相关，$\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_{m-1}$ 线性无关，证明 $\boldsymbol\alpha_m$ 可由 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_{m-1}$ 线性表示。

<details>
<summary>证明</summary>

由 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_m$ 相关，存在不全零的 $k_1,\dots,k_m$ 使 $\sum_{i=1}^m k_i\boldsymbol\alpha_i=\boldsymbol0$。若 $k_m=0$，则 $\sum_{i=1}^{m-1}k_i\boldsymbol\alpha_i=\boldsymbol0$ 且 $k_1,\dots,k_{m-1}$ 不全零，与 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_{m-1}$ 无关矛盾。故 $k_m\ne0$，
$$\boldsymbol\alpha_m=-\frac{k_1}{k_m}\boldsymbol\alpha_1-\cdots-\frac{k_{m-1}}{k_m}\boldsymbol\alpha_{m-1}$$
即 $\boldsymbol\alpha_m$ 可由 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_{m-1}$ 线性表示。$\blacksquare$
</details>

**27.** 设 $\boldsymbol\alpha_1,\boldsymbol\alpha_2,\boldsymbol\alpha_3$ 线性无关，证明 $\boldsymbol\alpha_1+\boldsymbol\alpha_2,\boldsymbol\alpha_2+\boldsymbol\alpha_3,\boldsymbol\alpha_3+\boldsymbol\alpha_1$ 也线性无关。

<details>
<summary>证明</summary>

参见 [[4.2 向量组线性相关与无关|4.2 节例 3]]。设 $k_1(\boldsymbol\alpha_1+\boldsymbol\alpha_2)+k_2(\boldsymbol\alpha_2+\boldsymbol\alpha_3)+k_3(\boldsymbol\alpha_3+\boldsymbol\alpha_1)=\boldsymbol0$，整理得 $(k_1+k_3)\boldsymbol\alpha_1+(k_1+k_2)\boldsymbol\alpha_2+(k_2+k_3)\boldsymbol\alpha_3=\boldsymbol0$。由 $\boldsymbol\alpha_1,\boldsymbol\alpha_2,\boldsymbol\alpha_3$ 无关，得方程组 $\begin{cases}k_1+k_3=0\\k_1+k_2=0\\k_2+k_3=0\end{cases}$，系数矩阵行列式 $=2\ne0$，只有零解 $k_1=k_2=k_3=0$。故 $\boldsymbol\alpha_1+\boldsymbol\alpha_2,\boldsymbol\alpha_2+\boldsymbol\alpha_3,\boldsymbol\alpha_3+\boldsymbol\alpha_1$ 线性无关。$\blacksquare$
</details>

**28.** 设 $A$ 为 $m\times n$ 矩阵，$B$ 为 $n\times s$ 矩阵，$AB=O$，证明 $r(A)+r(B)\le n$。

<details>
<summary>证明</summary>

参见 [[4.4 齐次线性方程组解空间、基础解系|4.4 节例 3]]。$AB=O$ 表明 $B$ 的每一列都是 $A\boldsymbol x=\boldsymbol0$ 的解，故 $B$ 的列向量组 $\subseteq N(A)$。
$$r(B)=r(B\text{ 的列向量组})\le\dim N(A)=n-r(A)$$
移项得 $r(A)+r(B)\le n$。$\blacksquare$
</details>

**29.** 设 $A$ 为 $n$ 阶方阵且 $A^2=A$（幂等矩阵），证明 $r(A)+r(E-A)=n$。

<details>
<summary>证明</summary>

由 $A^2=A$ 得 $A(E-A)=O$（因 $A-A^2=A-A=O$）。由 28 题，$r(A)+r(E-A)\le n$。
另一方面 $A+(E-A)=E$，由 [[3.2 矩阵的秩|和的秩不等式]] $r(A+B)\le r(A)+r(B)$：
$$n=r(E)=r(A+(E-A))\le r(A)+r(E-A)$$
两边夹得 $r(A)+r(E-A)=n$。$\blacksquare$
</details>

**30.** 设 $\boldsymbol\alpha_1,\boldsymbol\alpha_2,\dots,\boldsymbol\alpha_n$ 是 $n$ 维向量组且线性无关，证明任一 $n$ 维向量 $\boldsymbol\beta$ 都可由 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_n$ 线性表示，且表示唯一。

<details>
<summary>证明</summary>

由 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_n$ 是 $n$ 个 $n$ 维线性无关向量，构成 $\mathbb{F}^n$ 的一组基（[[4.3 向量组极大无关组、向量组的秩|极大无关组]]）。

对任一 $\boldsymbol\beta\in\mathbb{F}^n$，$n+1$ 个 $n$ 维向量 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_n,\boldsymbol\beta$ 必线性相关（向量个数 $n+1>$ 维数 $n$）。由 25 题结论（$\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_n$ 无关而加 $\boldsymbol\beta$ 后相关），$\boldsymbol\beta$ 可由 $\boldsymbol\alpha_1,\dots,\boldsymbol\alpha_n$ 线性表示且表示唯一。$\blacksquare$

> [!tip] 几何意义
> $n$ 维空间中任意 $n$ 个线性无关向量构成"坐标系"（基），空间中任一向量都有唯一"坐标"——这正是 [[MOC - 第6章|第 6 章 线性空间]] 基与坐标概念的具体原型。
</details>

## 考点统计表

| 考点 | 题号 | 题数 | 难度 |
| ---- | ---- | ---- | ---- |
| 线性相关/无关概念与判定 | 1, 6, 7, 8, 12, 13, 14, 27, 30 | 9 | 中 |
| 线性表示判定与求表示式 | 17, 25, 26 | 3 | 中 |
| 极大无关组求法与秩 | 3, 15, 16, 24 | 4 | 中 |
| 基础解系求解与判定 | 2, 4, 9, 10, 18, 19 | 6 | 中 |
| 非齐次通解结构 | 5, 11, 20, 21, 22, 23 | 6 | 中 |
| 含参数方程组讨论 | 23 | 1 | 较难 |
| 抽象向量组证明 | 25, 26, 27, 28, 29, 30 | 6 | 较难 |
| 秩不等式与 $AB=O$ | 28, 29 | 2 | 较难 |

> [!tip] 复习建议
> - **基础层**：先做填空与选择（1–12），巩固相关性判定、基础解系个数、通解结构概念；
> - **应用层**：再做计算 13–24，重点 16、18、20、22、23 五类——极大无关组、基础解系、非齐次通解、由解反推、含参数讨论；
> - **提升层**：证明题 25–30 集中训练"无关 $\Rightarrow$ 表示唯一""$AB=O\Rightarrow$ 秩不等式""幂等矩阵秩等式"三类核心论证，是高分关键。

## 章节导航

- 上一级：[[MOC - 第4章]]
- 知识点：[[4.1 n维向量概念、线性表示]] · [[4.2 向量组线性相关与无关]] · [[4.3 向量组极大无关组、向量组的秩]] · [[4.4 齐次线性方程组解空间、基础解系]] · [[4.5 非齐次线性方程组通解结构]]

## 相关标签

#线性代数 #习题 #线性相关 #极大无关组 #基础解系 #通解结构
