---
domain: 数学基础
subject: 线性代数A
type: exercise
chapter: 第3章 矩阵初等变换与线性方程组
tags: [线性代数,习题,初等变换,矩阵秩,线性方程组,高斯消元]
prerequisites: ["第2章 矩阵及其运算"]
aliases: [第3章习题, 初等变换与方程组习题]
---

# MOC - 第3章习题 矩阵初等变换与线性方程组

> [!info] 习题说明
> 本章习题共 **30 题**，覆盖填空、选择、计算、证明四类。重点考查：初等变换求秩、解的判定、高斯消元求解、含参数方程组讨论、初等变换求逆、秩的不等式应用。
>
> 相关知识点：[[3.1 初等变换、初等矩阵]]、[[3.2 矩阵的秩]]、[[3.3 线性方程组解的判定]]、[[3.4 高斯消元求解方程组]]、[[3.5 矩阵等价标准形]]、[[MOC - 第3章]]。

## 一、填空题（6 题）

**1.** 设 $A$ 为 $3\times 4$ 矩阵且 $r(A)=2$，则齐次方程组 $A\boldsymbol x=\boldsymbol 0$ 的基础解系含 ______ 个解向量。

<details>
<summary>答案</summary>

$n-r=4-2=2$ 个。
</details>

**2.** 设 $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$，把 $A$ 化为 $E$ 的过程中，$E(21(-3))A=$ ______。

<details>
<summary>答案</summary>

$E(21(-3))=\begin{pmatrix}1&0\\-3&1\end{pmatrix}$，故 $E(21(-3))A=\begin{pmatrix}1&2\\0&-2\end{pmatrix}$（相当于 $r_2-3r_1$）。
</details>

**3.** 设 $A$ 为 $n$ 阶方阵，若 $A\boldsymbol x=\boldsymbol 0$ 有非零解，则 $|A|=$ ______。

<details>
<summary>答案</summary>

$|A|=0$。因 $A\boldsymbol x=\boldsymbol 0$ 有非零解 $\iff r(A)<n\iff A$ 不可逆 $\iff |A|=0$。
</details>

**4.** 设 $r(A)=3$，$A$ 为 $4\times 5$ 矩阵，则 $A^\top$ 的秩为 ______。

<details>
<summary>答案</summary>

$r(A^\top)=r(A)=3$（转置不改变秩）。
</details>

**5.** 设方程组 $A\boldsymbol x=\boldsymbol b$ 的增广矩阵经初等行变换化为 $\begin{pmatrix}1&0&2&1\\0&1&-1&2\\0&0&0&0\end{pmatrix}$，则该方程组的自由变量个数是 ______。

<details>
<summary>答案</summary>

主元在第 1、2 列，自由变量为 $x_3$，共 $1$ 个。（$n-r=3-2=1$）
</details>

**6.** 用初等行变换求逆时，构造分块矩阵 ______，若左侧能化为单位矩阵，则右侧即为 $A^{-1}$。

<details>
<summary>答案</summary>

$(A\mid E)$（$n$ 阶方阵 $A$ 时构造 $n\times 2n$ 矩阵）。
</details>

## 二、选择题（6 题）

**7.** 下列矩阵中不是初等矩阵的是（$\quad$）。

A. $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ $\quad$ B. $\begin{pmatrix}1&0\\0&2\end{pmatrix}$ $\quad$ C. $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ $\quad$ D. $\begin{pmatrix}1&1\\1&1\end{pmatrix}$

<details>
<summary>答案</summary>

**D**。初等矩阵由单位阵经**一次**初等变换得到。A 是换行（$E(1,2)$），B 是倍乘（$E(2(2))$），C 是倍加（$E(12(1))$）。D 的行列式 $=0$ 不可逆，而初等矩阵必可逆，故 D 不是。
</details>

**8.** 设 $A$ 为 $m\times n$ 矩阵，$r(A)=r$，则下列命题错误的是（$\quad$）。

A. $r\le\min(m,n)$ $\quad$ B. $r(A^\top)=r$ $\quad$ C. $r(A^2)=r$ $\quad$ D. $r(kA)=r$（$k\ne0$）

<details>
<summary>答案</summary>

**C**。$A^2$ 要求 $A$ 为方阵，且 $r(A^2)$ 未必等于 $r(A)$（如 $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$，$r(A)=1$ 但 $A^2=O$，$r(A^2)=0$）。其余均为秩的基本性质。
</details>

**9.** 设 $A$ 为 $4\times 3$ 矩阵，$r(A)=2$，$\boldsymbol b\in\mathbb{R}^4$，则 $A\boldsymbol x=\boldsymbol b$（$\quad$）。

A. 必有唯一解 $\quad$ B. 必有无穷多解 $\quad$ C. 必无解 $\quad$ D. 解的情况取决于 $r(\bar A)$

<details>
<summary>答案</summary>

**D**。$r(A)=2$，但 $r(\bar A)$ 可能等于 $2$（有解，且 $r<n=3$，无穷多解）或 $3$（无解）。需看 $\boldsymbol b$ 是否落入 $A$ 的列空间。
</details>

**10.** 设 $A,B$ 均为 $n$ 阶方阵，$AB=O$，则下列正确的是（$\quad$）。

A. $A=O$ 或 $B=O$ $\quad$ B. $|A|=0$ 或 $|B|=0$ $\quad$ C. $r(A)+r(B)\ge n$ $\quad$ D. $r(A)=r(B)$

<details>
<summary>答案</summary>

**B**。由 $AB=O$ 得 $|AB|=|A||B|=0$，故 $|A|=0$ 或 $|B|=0$。A 错（如 $A=\begin{pmatrix}1&0\\0&0\end{pmatrix},B=\begin{pmatrix}0&0\\0&1\end{pmatrix}$）；C 错，正确不等式为 $r(A)+r(B)\le n$（见 [[3.2 矩阵的秩|例 3]]）；D 错。
</details>

**11.** 用初等变换求 $A^{-1}$ 时，若 $(A\mid E)\xrightarrow{\text{行变换}}(B\mid C)$，且 $B$ 中出现全零行，则（$\quad$）。

A. $A^{-1}=C$ $\quad$ B. $A$ 可逆 $\quad$ C. $A$ 不可逆 $\quad$ D. 需继续做列变换

<details>
<summary>答案</summary>

**C**。出现全零行说明 $r(A)<n$，$A$ 不可逆，左侧无法化为 $E$。
</details>

**12.** 矩阵 $A$ 与 $B$ 等价的充要条件是（$\quad$）。

A. $r(A)=r(B)$ 且同型 $\quad$ B. $|A|=|B|$ $\quad$ C. $A,B$ 都是方阵 $\quad$ D. 存在矩阵 $P,Q$ 使 $PAQ=B$

<details>
<summary>答案</summary>

**A**。等价充要条件为同型且秩相等。B 仅对方阵有意义且不充分；C 错，等价不要求方阵；D 缺"可逆"条件（$P,Q$ 必须可逆）。
</details>

## 三、计算题（12 题）

**13.** 求矩阵 $A=\begin{pmatrix}1&2&3&4\\2&4&6&8\\1&0&1&2\end{pmatrix}$ 的秩。

<details>
<summary>解答</summary>

$$A\xrightarrow{\substack{r_2-2r_1\\r_3-r_1}}\begin{pmatrix}1&2&3&4\\0&0&0&0\\0&-2&-2&-2\end{pmatrix}\xrightarrow{r_2\leftrightarrow r_3}\begin{pmatrix}1&2&3&4\\0&-2&-2&-2\\0&0&0&0\end{pmatrix}$$
阶梯形非零行数 $=2$，故 $\boxed{r(A)=2}$。
</details>

**14.** 设 $A=\begin{pmatrix}1&1&1\\1&2&a\\1&4&a^2\end{pmatrix}$，讨论 $r(A)$ 随 $a$ 的变化。

<details>
<summary>解答</summary>

$$A\xrightarrow{\substack{r_2-r_1\\r_3-r_1}}\begin{pmatrix}1&1&1\\0&1&a-1\\0&3&a^2-1\end{pmatrix}\xrightarrow{r_3-3r_2}\begin{pmatrix}1&1&1\\0&1&a-1\\0&0&a^2-3a+2\end{pmatrix}$$
其中 $a^2-3a+2=(a-1)(a-2)$。
- $a\ne 1$ 且 $a\ne 2$：$r(A)=3$；
- $a=1$ 或 $a=2$：第三行变零，$r(A)=2$。

故 $\boxed{r(A)=\begin{cases}3,&a\notin\{1,2\}\\2,&a\in\{1,2\}\end{cases}}$。
</details>

**15.** 判定方程组 $\begin{cases}x_1+2x_2-x_3=1\\2x_1+4x_2-2x_3=3\\x_1+x_2+x_3=0\end{cases}$ 是否有解。

<details>
<summary>解答</summary>

增广矩阵
$$\bar A=\begin{pmatrix}1&2&-1&1\\2&4&-2&3\\1&1&1&0\end{pmatrix}\xrightarrow{\substack{r_2-2r_1\\r_3-r_1}}\begin{pmatrix}1&2&-1&1\\0&0&0&1\\0&-1&2&-1\end{pmatrix}\xrightarrow{r_2\leftrightarrow r_3}\begin{pmatrix}1&2&-1&1\\0&-1&2&-1\\0&0&0&1\end{pmatrix}$$
$r(A)=2$，$r(\bar A)=3$，$r(A)<r(\bar A)$，**无解**。
</details>

**16.** 求齐次方程组 $\begin{cases}x_1-x_2-x_3+x_4=0\\x_1-x_2+x_3-3x_4=0\\x_1-x_2-2x_3+3x_4=0\end{cases}$ 的通解与基础解系。

<details>
<summary>解答</summary>

对系数矩阵 $A$ 做行变换：
$$A=\begin{pmatrix}1&-1&-1&1\\1&-1&1&-3\\1&-1&-2&3\end{pmatrix}\xrightarrow{\substack{r_2-r_1\\r_3-r_1}}\begin{pmatrix}1&-1&-1&1\\0&0&2&-4\\0&0&-1&2\end{pmatrix}\xrightarrow{\substack{r_2\div2\\r_3+r_2}}\begin{pmatrix}1&-1&-1&1\\0&0&1&-2\\0&0&0&0\end{pmatrix}\xrightarrow{r_1+r_2}\begin{pmatrix}1&-1&0&-1\\0&0&1&-2\\0&0&0&0\end{pmatrix}$$
$r(A)=2$，主元在第 1、3 列。令自由变量 $x_2=c_1,\ x_4=c_2$，则 $x_1=c_1+c_2,\ x_3=2c_2$。
$$\boldsymbol x=c_1(1,1,0,0)^\top+c_2(1,0,2,1)^\top$$
基础解系：$\boldsymbol\xi_1=(1,1,0,0)^\top,\boldsymbol\xi_2=(1,0,2,1)^\top$。
</details>

**17.** 求非齐次方程组 $\begin{cases}x_1+x_2+x_3+x_4=4\\x_1+2x_2-x_3+4x_4=5\\2x_1+3x_2+0x_3+5x_4=9\end{cases}$ 的通解。

<details>
<summary>解答</summary>

增广矩阵
$$\bar A=\begin{pmatrix}1&1&1&1&4\\1&2&-1&4&5\\2&3&0&5&9\end{pmatrix}\xrightarrow{\substack{r_2-r_1\\r_3-2r_1}}\begin{pmatrix}1&1&1&1&4\\0&1&-2&3&1\\0&1&-2&3&1\end{pmatrix}\xrightarrow{r_3-r_2}\begin{pmatrix}1&1&1&1&4\\0&1&-2&3&1\\0&0&0&0&0\end{pmatrix}\xrightarrow{r_1-r_2}\begin{pmatrix}1&0&3&-2&3\\0&1&-2&3&1\\0&0&0&0&0\end{pmatrix}$$
$r(A)=r(\bar A)=2<n=4$，自由变量 $x_3=c_1,\ x_4=c_2$。读出 $x_1=3-3c_1+2c_2,\ x_2=1+2c_1-3c_2$。
$$\boxed{\boldsymbol x=(3,1,0,0)^\top+c_1(-3,2,1,0)^\top+c_2(2,-3,0,1)^\top}$$
</details>

**18.** 用初等行变换求 $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ 的逆。

<details>
<summary>解答</summary>

$$\begin{pmatrix}1&2&1&0\\3&4&0&1\end{pmatrix}\xrightarrow{r_2-3r_1}\begin{pmatrix}1&2&1&0\\0&-2&-3&1\end{pmatrix}\xrightarrow{-\tfrac12 r_2}\begin{pmatrix}1&2&1&0\\0&1&3/2&-1/2\end{pmatrix}\xrightarrow{r_1-2r_2}\begin{pmatrix}1&0&-2&1\\0&1&3/2&-1/2\end{pmatrix}$$
$$\boxed{A^{-1}=\begin{pmatrix}-2&1\\3/2&-1/2\end{pmatrix}}$$
</details>

**19.** 用初等行变换求 $A=\begin{pmatrix}1&0&1\\2&1&0\\1&1&1\end{pmatrix}$ 的逆。

<details>
<summary>解答</summary>

$$\begin{pmatrix}1&0&1&1&0&0\\2&1&0&0&1&0\\1&1&1&0&0&1\end{pmatrix}\xrightarrow{\substack{r_2-2r_1\\r_3-r_1}}\begin{pmatrix}1&0&1&1&0&0\\0&1&-2&-2&1&0\\0&1&0&-1&0&1\end{pmatrix}\xrightarrow{r_3-r_2}\begin{pmatrix}1&0&1&1&0&0\\0&1&-2&-2&1&0\\0&0&2&1&-1&1\end{pmatrix}$$
$$\xrightarrow{r_3\div2}\begin{pmatrix}1&0&1&1&0&0\\0&1&-2&-2&1&0\\0&0&1&1/2&-1/2&1/2\end{pmatrix}\xrightarrow{\substack{r_2+2r_3\\r_1-r_3}}\begin{pmatrix}1&0&0&1/2&1/2&-1/2\\0&1&0&-1&0&1\\0&0&1&1/2&-1/2&1/2\end{pmatrix}$$
$$\boxed{A^{-1}=\dfrac12\begin{pmatrix}1&1&-1\\-2&0&2\\1&-1&1\end{pmatrix}}$$
可验算 $|A|=2\ne0$，$AA^{-1}=E$。
</details>

**20.** 讨论 $\lambda$ 取何值时方程组 $\begin{cases}\lambda x_1+x_2+x_3=1\\x_1+\lambda x_2+x_3=\lambda\\x_1+x_2+\lambda x_3=\lambda^2\end{cases}$ 有唯一解、无解、无穷多解。

<details>
<summary>解答</summary>

参见 [[3.4 高斯消元求解方程组|3.4 节例 4]]，化简得：
$$\bar A\to\begin{pmatrix}1&1&\lambda&\lambda^2\\0&\lambda-1&1-\lambda&\lambda(1-\lambda)\\0&0&(1-\lambda)(2+\lambda)&(1-\lambda)(1+\lambda)^2\end{pmatrix}$$
- $\lambda\ne 1$ 且 $\lambda\ne -2$：$r(A)=r(\bar A)=3$，**唯一解**；
- $\lambda=-2$：第三行变 $(0,0,0\mid 9)$ 矛盾，$r(A)=2<r(\bar A)=3$，**无解**；
- $\lambda=1$：三方程同为 $x_1+x_2+x_3=1$，$r(A)=r(\bar A)=1<3$，**无穷多解**，通解 $\boldsymbol x=(1,0,0)^\top+c_1(-1,1,0)^\top+c_2(-1,0,1)^\top$。
</details>

**21.** 求矩阵 $A=\begin{pmatrix}2&-1&-1\\1&1&-2\\4&-6&2\end{pmatrix}$ 的秩与等价标准形。

<details>
<summary>解答</summary>

$$A\xrightarrow{r_1\leftrightarrow r_2}\begin{pmatrix}1&1&-2\\2&-1&-1\\4&-6&2\end{pmatrix}\xrightarrow{\substack{r_2-2r_1\\r_3-4r_1}}\begin{pmatrix}1&1&-2\\0&-3&3\\0&-10&10\end{pmatrix}\xrightarrow{\substack{r_2\div(-3)\\r_3+10r_2}}\begin{pmatrix}1&1&-2\\0&1&-1\\0&0&0\end{pmatrix}$$
$r(A)=2$。等价标准形为 $\boxed{\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}}$。
</details>

**22.** 设 $A=\begin{pmatrix}1&1&1\\2&1&3\\1&0&2\end{pmatrix}$，把 $A$ 的第 2 行的 $-2$ 倍加到第 3 行得到 $B$，求初等矩阵 $P$ 使 $B=PA$，并求 $P^{-1}$。

<details>
<summary>解答</summary>

变换 $r_3-2r_2$ 对应左乘 $P=E(32(-2))=\begin{pmatrix}1&0&0\\0&1&0\\0&-2&1\end{pmatrix}$。
$$B=PA=\begin{pmatrix}1&1&1\\2&1&3\\-3&-2&-4\end{pmatrix}$$
$P^{-1}=E(32(2))=\begin{pmatrix}1&0&0\\0&1&0\\0&2&1\end{pmatrix}$（倍加的逆是把 $-k$ 换成 $k$）。
</details>

**23.** 求方程组 $\begin{cases}x_1+2x_2+3x_3=6\\2x_1+4x_2+5x_3=11\\x_1+3x_2+4x_3=8\end{cases}$ 的解。

<details>
<summary>解答</summary>

参见 [[3.4 高斯消元求解方程组|3.4 节例 1]]，化行最简形后唯一解 $\boxed{\boldsymbol x=(1,1,1)^\top}$。
</details>

**24.** 设 $A=\begin{pmatrix}1&2&3\\2&3&4\\3&5&7\end{pmatrix}$，用初等行变换判定 $A$ 是否可逆，若可逆则求 $A^{-1}$。

<details>
<summary>解答</summary>

$$\begin{pmatrix}1&2&3&1&0&0\\2&3&4&0&1&0\\3&5&7&0&0&1\end{pmatrix}\xrightarrow{\substack{r_2-2r_1\\r_3-3r_1}}\begin{pmatrix}1&2&3&1&0&0\\0&-1&-2&-2&1&0\\0&-1&-2&-3&0&1\end{pmatrix}\xrightarrow{r_3-r_2}\begin{pmatrix}1&2&3&1&0&0\\0&-1&-2&-2&1&0\\0&0&0&-1&-1&1\end{pmatrix}$$
第三行左侧全零而右侧非零，说明 $r(A)=2<3$，**$A$ 不可逆**，$A^{-1}$ 不存在。（注：第 3 行 = 第 1 行 + 第 2 行，故 $A$ 奇异。）
</details>

## 四、证明题（6 题）

**25.** 证明：初等矩阵的转置仍是初等矩阵。

<details>
<summary>证明</summary>

逐一验证：
- $E(i,j)^\top=E(i,j)$（对称阵，仍为换行初等矩阵）；
- $E(i(k))^\top=E(i(k))$（对角阵，对称）；
- $E(ij(k))^\top=E(ji(k))$（因为 $(E+ke_i e_j^\top)^\top=E+ke_j e_i^\top$，是"把第 $i$ 行的 $k$ 倍加到第 $j$ 行"对应的初等矩阵）。

三种情形均为初等矩阵，证毕。
</details>

**26.** 设 $A$ 为 $n$ 阶方阵，证明 $A$ 可逆 $\iff A$ 可表示为若干初等矩阵之积。

<details>
<summary>证明</summary>

($\Leftarrow$) 初等矩阵都可逆，可逆矩阵之积仍可逆，故 $A$ 可逆。

($\Rightarrow$) 设 $A$ 可逆。由 [[3.5 矩阵等价标准形]] 推论，$A\cong E_n$，即存在初等矩阵 $P_1,\dots,P_s,Q_1,\dots,Q_t$ 使 $P_s\cdots P_1\,A\,Q_1\cdots Q_t=E_n$。于是 $A=P_1^{-1}\cdots P_s^{-1}\,Q_1^{-1}\cdots Q_t^{-1}$。由 [[3.1 初等变换、初等矩阵|3.1 节定理]]，初等矩阵的逆仍为初等矩阵，故 $A$ 是初等矩阵之积。
</details>

**27.** 设 $A,B$ 为 $n$ 阶方阵，证明 $r(AB)\le\min(r(A),r(B))$。

<details>
<summary>证明</summary>

设 $r(A)=r$。由 [[3.5 矩阵等价标准形|例 3]]，$A=P\begin{pmatrix}E_r&O\\O&O\end{pmatrix}Q$，其中 $P,Q$ 可逆。则
$$AB=P\begin{pmatrix}E_r&O\\O&O\end{pmatrix}QB$$
记 $QB=\begin{pmatrix}C_1\\C_2\end{pmatrix}$（$C_1$ 为 $QB$ 的前 $r$ 行），则 $\begin{pmatrix}E_r&O\\O&O\end{pmatrix}QB=\begin{pmatrix}C_1\\O\end{pmatrix}$。左乘可逆 $P$ 不改变秩，故
$$r(AB)=r\begin{pmatrix}C_1\\O\end{pmatrix}=r(C_1)\le r(QB)=r(B)$$
同理 $r(AB)=r((AB)^\top)=r(B^\top A^\top)\le r(A^\top)=r(A)$。综上 $r(AB)\le\min(r(A),r(B))$。
</details>

**28.** 设 $A$ 为 $m\times n$ 矩阵，$B$ 为 $n\times s$ 矩阵，$AB=O$，证明 $r(A)+r(B)\le n$。

<details>
<summary>证明</summary>

参见 [[3.2 矩阵的秩|例 3]]。$AB=O$ 表明 $B$ 的每一列 $\boldsymbol b_j$ 都是 $A\boldsymbol x=\boldsymbol 0$ 的解。设 $r(A)=r$，齐次方程组 $A\boldsymbol x=\boldsymbol 0$ 的解空间维数为 $n-r$。

$B$ 的 $s$ 个列都落在 $n-r$ 维解空间中，故 $B$ 的列秩 $\le n-r$，即 $r(B)\le n-r$。移项得 $r(A)+r(B)\le n$。
</details>

**29.** 证明：若 $A^2=A$（幂等矩阵），则 $r(A)+r(E-A)=n$。

<details>
<summary>证明</summary>

由 $A^2=A$ 得 $A(A-E)=O$，即 $A(E-A)=O$。由 28 题，$r(A)+r(E-A)\le n$。

另一方面 $A+(E-A)=E$，由 [[3.2 矩阵的秩|和的秩不等式]] $r(A+B)\le r(A)+r(B)$ 得 $n=r(E)=r(A+(E-A))\le r(A)+r(E-A)$。

两边夹得 $r(A)+r(E-A)=n$。
</details>

**30.** 设 $A$ 为 $n$ 阶方阵，证明 $r(A)=r(A^\top A)$。

<details>
<summary>证明</summary>

只要证 $A\boldsymbol x=\boldsymbol 0$ 与 $A^\top A\,\boldsymbol x=\boldsymbol 0$ 同解（则解空间维数相同，$n-r(A)=n-r(A^\top A)$，秩相等）。

- 若 $A\boldsymbol x=\boldsymbol 0$，左乘 $A^\top$ 得 $A^\top A\boldsymbol x=\boldsymbol 0$。
- 反之若 $A^\top A\boldsymbol x=\boldsymbol 0$，左乘 $\boldsymbol x^\top$ 得 $\boldsymbol x^\top A^\top A\boldsymbol x=0$，即 $(A\boldsymbol x)^\top(A\boldsymbol x)=\|A\boldsymbol x\|^2=0$，故 $A\boldsymbol x=\boldsymbol 0$。

两方程组同解，零空间维数相等，故 $r(A)=r(A^\top A)$。（注：本题在实数域上成立；复数域需用 $A^H A$。）
</details>

## 考点统计表

| 考点 | 题号 | 题数 | 难度 |
| ---- | ---- | ---- | ---- |
| 初等变换与初等矩阵的概念 | 2, 7, 22, 25 | 4 | 易 |
| 初等变换求秩 | 13, 14, 21 | 3 | 中 |
| 解的判定（无解/唯一/无穷） | 9, 15, 20 | 3 | 中 |
| 齐次方程组求解与基础解系 | 1, 16 | 2 | 中 |
| 非齐次方程组求解 | 5, 17, 23 | 3 | 中 |
| 含参数方程组讨论 | 14, 20 | 2 | 较难 |
| 初等变换求逆矩阵 | 6, 11, 18, 19, 24 | 5 | 中 |
| 矩阵等价与等价标准形 | 12, 21, 26 | 3 | 中 |
| 秩的性质与不等式 | 3, 4, 8, 10, 27, 28, 29, 30 | 8 | 较难 |

> [!tip] 复习建议
> - **基础层**：先做填空与选择（1–12），巩固概念与判定；
> - **应用层**：再做计算 13–24，重点是 16、17、20 三类——求秩、求解、含参数讨论；
> - **提升层**：证明题 25–30 集中训练秩的不等式与等价标准形的应用，是高分关键。

## 章节导航

- 上一级：[[MOC - 第3章]]
- 知识点：[[3.1 初等变换、初等矩阵]] · [[3.2 矩阵的秩]] · [[3.3 线性方程组解的判定]] · [[3.4 高斯消元求解方程组]] · [[3.5 矩阵等价标准形]]

## 相关标签

#线性代数 #习题 #初等变换 #矩阵秩 #线性方程组 #高斯消元
