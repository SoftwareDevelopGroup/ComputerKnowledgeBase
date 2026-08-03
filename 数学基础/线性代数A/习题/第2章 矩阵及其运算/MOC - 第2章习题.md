---
domain: 数学基础
subject: 线性代数A
type: exercise
chapter: 第2章 矩阵及其运算
tags: [线性代数,习题,矩阵乘法,逆矩阵,伴随矩阵,分块矩阵]
prerequisites: ["第1章 行列式"]
aliases: [第2章习题, 矩阵习题]
---

# MOC - 第2章习题

> [!info] 习题说明
> 本习题集对应 [[MOC - 第2章|第2章 矩阵及其运算]]，共 30 题，分为填空（8）、选择（6）、计算（10）、证明（6）四类，覆盖矩阵乘法、逆矩阵求解、伴随矩阵性质、分块矩阵运算四大主线。答案以 `<details>` 折叠，计算题给出完整步骤。建议先独立完成，再展开核对。

## 一、填空题（8 题）

**1.** 设 $A$ 为 3 阶方阵，$|A|=2$，则 $|2A|=$ $\rule{2cm}{0.15mm}$，$|-A|=$ $\rule{2cm}{0.15mm}$，$|A^*|=$ $\rule{2cm}{0.15mm}$。

<details><summary>答案</summary>

- $|2A|=2^3|A|=8\times2=16$；
- $|-A|=(-1)^3|A|=-2$；
- $|A^*|=|A|^{n-1}=|A|^2=4$。
</details>

**2.** 设 $A$ 为 3 阶方阵，$|A|=-2$，则 $|A^{-1}|=$ $\rule{2cm}{0.15mm}$，$|A^{*}|=$ $\rule{2cm}{0.15mm}$，$|(A^*)^*|=$ $\rule{2cm}{0.15mm}$。

<details><summary>答案</summary>

- $|A^{-1}|=\dfrac{1}{|A|}=-\dfrac12$；
- $|A^*|=|A|^{n-1}=|A|^2=4$；
- $(A^*)^*=|A|^{n-2}A=|A|A=-2A$，故 $|(A^*)^*|=|-2A|=(-2)^3|A|=-8\times(-2)=16$。
</details>

**3.** 设 $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$，$B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$，则 $AB-BA=$ $\rule{3cm}{0.15mm}$。

<details><summary>答案</summary>

$AB=\begin{pmatrix}2&1\\4&3\end{pmatrix}$，$BA=\begin{pmatrix}3&4\\1&2\end{pmatrix}$，$AB-BA=\begin{pmatrix}-1&-3\\3&1\end{pmatrix}$。
</details>

**4.** 设 $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$，则 $A^{10}=$ $\rule{3cm}{0.15mm}$。

<details><summary>答案</summary>

由 [[2.2 矩阵线性运算、乘法|例题 3]]，$\begin{pmatrix}1&1\\0&1\end{pmatrix}^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}$，故 $A^{10}=\begin{pmatrix}1&10\\0&1\end{pmatrix}$。
</details>

**5.** 设 $A$ 为 $n$ 阶方阵，且 $A^2-3A+2E=O$，则 $A^{-1}=$ $\rule{3cm}{0.15mm}$（用 $A$ 表示）。

<details><summary>答案</summary>

由 $A^2-3A+2E=O$ 得 $A(A-3E)=-2E$，即 $A\cdot\dfrac{3E-A}{2}=E$，故 $A^{-1}=\dfrac{3E-A}{2}$。
</details>

**6.** 设 $A=\begin{pmatrix}2&0&0\\0&1&0\\0&0&3\end{pmatrix}$，则 $A^{-1}=$ $\rule{3cm}{0.15mm}$。

<details><summary>答案</summary>

对角矩阵的逆为对角元取倒数：$A^{-1}=\begin{pmatrix}\frac12&0&0\\0&1&0\\0&0&\frac13\end{pmatrix}$。
</details>

**7.** 设 $A$ 为 3 阶方阵，$|A|=2$，则 $|(2A)^{-1}|=$ $\rule{2cm}{0.15mm}$，$|2A^{-1}|=$ $\rule{2cm}{0.15mm}$。

<details><summary>答案</summary>

- $(2A)^{-1}=\dfrac12 A^{-1}$，$|(2A)^{-1}|=\Big(\dfrac12\Big)^3|A^{-1}|=\dfrac18\cdot\dfrac12=\dfrac{1}{16}$；
- $|2A^{-1}|=2^3|A^{-1}|=8\cdot\dfrac12=4$。
</details>

**8.** 设 $A=\operatorname{diag}(A_1,A_2)$，$A_1=\begin{pmatrix}1&2\\3&4\end{pmatrix}$，$A_2=\begin{pmatrix}2&0\\1&2\end{pmatrix}$，则 $|A|=$ $\rule{2cm}{0.15mm}$。

<details><summary>答案</summary>

$|A|=|A_1|\cdot|A_2|=(-2)\cdot(4-0)=-2\times4=-8$。（$|A_1|=4-6=-2$，$|A_2|=4$。）
</details>

## 二、选择题（6 题）

**9.** 设 $A,B$ 均为 $n$ 阶方阵，则下列结论正确的是（　）。
- (A) $AB=O\Rightarrow A=O$ 或 $B=O$
- (B) $|AB|=0\Rightarrow |A|=0$ 或 $|B|=0$
- (C) $(AB)^T=A^TB^T$
- (D) $(A+B)^2=A^2+2AB+B^2$

<details><summary>答案</summary>

**B**。$|AB|=|A||B|=0\Rightarrow |A|=0$ 或 $|B|=0$。A 错（零因子），C 错（应为 $B^TA^T$），D 错（缺 $BA$，除非可交换）。
</details>

**10.** 设 $A$ 为 $n$ 阶可逆矩阵，则下列不正确的是（　）。
- (A) $(A^{-1})^{-1}=A$
- (B) $(A^T)^{-1}=(A^{-1})^T$
- (C) $(AB)^{-1}=A^{-1}B^{-1}$
- (D) $|A^{-1}|=|A|^{-1}$

<details><summary>答案</summary>

**C**。应为 $(AB)^{-1}=B^{-1}A^{-1}$（反序）。
</details>

**11.** 设 $A$ 为 3 阶方阵，$|A|=a\ne0$，则 $|2A^*|=$（　）。
- (A) $2a^2$
- (B) $4a^2$
- (C) $8a^2$
- (D) $16a^2$

<details><summary>答案</summary>

**C**。$|A^*|=|A|^{n-1}=a^2$，$|2A^*|=2^3|A^*|=8a^2$。
</details>

**12.** 设 $A,B,C$ 均为 $n$ 阶方阵，且 $ABC=E$，则下列必定成立的是（　）。
- (A) $ACB=E$
- (B) $BCA=E$
- (C) $BAC=E$
- (D) $CBA=E$

<details><summary>答案</summary>

**B**。$ABC=E\Rightarrow A$ 可逆且 $A^{-1}=BC$，故 $BC\cdot A=E$，即 $BCA=E$。这是"循环移位不变"性质。
</details>

**13.** 设 $A$ 为 $n$ 阶方阵，且 $A^2=A$，则下列正确的是（　）。
- (A) $A=E$
- (B) $A=O$
- (C) $|A|=0$ 或 $|A|=1$
- (D) $A$ 一定可逆

<details><summary>答案</summary>

**C**。$A^2=A\Rightarrow |A|^2=|A|\Rightarrow |A|(|A|-1)=0\Rightarrow |A|=0$ 或 $|A|=1$。A、B 错（幂等矩阵不唯一），D 错（$A=O$ 不可逆）。
</details>

**14.** 设 $A$ 为 $n$ 阶方阵（$n\ge3$），$|A|=0$，则下列正确的是（　）。
- (A) $A^*=O$
- (B) $|A^*|=0$
- (C) $A^*$ 一定不可逆
- (D) B、C 都对

<details><summary>答案</summary>

**D**。$|A^*|=|A|^{n-1}=0$（$n\ge3$），故 $A^*$ 不可逆。A 错：当 $\operatorname{rank}A=n-1$ 时 $A^*\ne O$（秩为 1），见 [[2.6 伴随矩阵|伴随矩阵]] 与 [[MOC - 第3章]] 秩关系。
</details>

## 三、计算题（10 题）

**15.** 设 $A=\begin{pmatrix}1&2&3\\2&1&-1\end{pmatrix}$，$B=\begin{pmatrix}1&0\\0&1\\-1&2\end{pmatrix}$，求 $AB$ 与 $BA$，并说明是否相等。

<details><summary>解答</summary>

$A$ 为 $2\times3$，$B$ 为 $3\times2$，$AB$ 为 $2\times2$：
$$(AB)_{11}=1+0-3=-2,\ (AB)_{12}=0+2+6=8,$$
$$(AB)_{21}=2+0+1=3,\ (AB)_{22}=0+1-2=-1.$$
$$AB=\begin{pmatrix}-2&8\\3&-1\end{pmatrix}.$$

$BA$ 为 $3\times3$：
$$(BA)_{11}=1,\ (BA)_{12}=2,\ (BA)_{13}=3;$$
$$(BA)_{21}=2,\ (BA)_{22}=1,\ (BA)_{23}=-1;$$
$$(BA)_{31}=-1+0+2=1,\ (BA)_{32}=-2+0-2=-4,\ (BA)_{33}=-3+0-2=-5.$$
$$BA=\begin{pmatrix}1&2&3\\2&1&-1\\1&-4&-5\end{pmatrix}.$$

二者型不同（$2\times2$ 与 $3\times3$），$AB\ne BA$，再次说明矩阵乘法不满足交换律。
</details>

**16.** 用伴随矩阵法求 $A=\begin{pmatrix}1&0&1\\2&1&0\\0&0&2\end{pmatrix}$ 的逆矩阵。

<details><summary>解答</summary>

**第 1 步**：$|A|=1\cdot(2-0)+0+1\cdot(0-0)=2$（按第 1 行展开，余子式 $M_{13}=\begin{vmatrix}2&1\\0&0\end{vmatrix}=0$）。$|A|=2\ne0$，可逆。

**第 2 步**：求代数余子式。
$A_{11}=2,\ A_{12}=-4,\ A_{13}=0$；
$A_{21}=0,\ A_{22}=2,\ A_{23}=0$；
$A_{31}=-1,\ A_{32}=2,\ A_{33}=1$。

代数余子式矩阵 $\begin{pmatrix}2&-4&0\\0&2&0\\-1&2&1\end{pmatrix}$，转置得
$$A^*=\begin{pmatrix}2&0&-1\\-4&2&2\\0&0&1\end{pmatrix}.$$

**第 3 步**：$A^{-1}=\dfrac{1}{2}A^*=\begin{pmatrix}1&0&-\frac12\\-2&1&1\\0&0&\frac12\end{pmatrix}$。
</details>

**17.** 设 $A=\begin{pmatrix}3&0\\0&2\end{pmatrix}$，$B=\begin{pmatrix}1&2\\3&4\end{pmatrix}$，求 $(AB)^{-1}$。

<details><summary>解答</summary>

$AB=\begin{pmatrix}3&0\\0&2\end{pmatrix}\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}3&6\\6&8\end{pmatrix}$，$|AB|=24-36=-12$。
$$(AB)^{-1}=\frac{1}{-12}\begin{pmatrix}8&-6\\-6&3\end{pmatrix}=\begin{pmatrix}-\frac23&\frac12\\\frac12&-\frac14\end{pmatrix}.$$
也可用反序律 $(AB)^{-1}=B^{-1}A^{-1}$ 验证。
</details>

**18.** 设 $A$ 为 3 阶方阵，$|A|=\dfrac12$，求 $(2A)^{-1}-3A^*$。

<details><summary>解答</summary>

$(2A)^{-1}=\dfrac12 A^{-1}=\dfrac12\cdot\dfrac{A^*}{|A|}=\dfrac12\cdot\dfrac{A^*}{1/2}=A^*$。故 $(2A)^{-1}-3A^*=A^*-3A^*=-2A^*$。

如需进一步，$|-2A^*|=(-2)^3|A^*|=-8\cdot|A|^2=-8\cdot\dfrac14=-2$。答案矩阵形式为 $-2A^*$。
</details>

**19.** 设 $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$，$B=\begin{pmatrix}5&6\\7&8\end{pmatrix}$，求 $(A+B)^2$，并验证 $(A+B)^2\ne A^2+2AB+B^2$。

<details><summary>解答</summary>

$A+B=\begin{pmatrix}6&8\\10&12\end{pmatrix}$，$(A+B)^2=\begin{pmatrix}6&8\\10&12\end{pmatrix}^2=\begin{pmatrix}36+80&48+96\\60+120&80+144\end{pmatrix}=\begin{pmatrix}116&144\\180&224\end{pmatrix}$。

$A^2=\begin{pmatrix}7&10\\15&22\end{pmatrix}$，$B^2=\begin{pmatrix}67&78\\91&106\end{pmatrix}$，$2AB=2\begin{pmatrix}19&22\\43&50\end{pmatrix}=\begin{pmatrix}38&44\\86&100\end{pmatrix}$。
$A^2+2AB+B^2=\begin{pmatrix}7+38+67&10+44+78\\15+86+91&22+100+106\end{pmatrix}=\begin{pmatrix}112&132\\192&228\end{pmatrix}$。

二者不等：$AB\ne BA$，故不能套用数的二项式公式。正确展开为 $(A+B)^2=A^2+AB+BA+B^2$。
</details>

**20.** 设 $A=\begin{pmatrix}1&1&0\\0&1&1\\0&0&1\end{pmatrix}$，求 $A^n$（$n$ 为正整数）。

<details><summary>解答</summary>

记 $N=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}$，则 $A=E+N$，且 $N^2=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}$，$N^3=O$。因 $E$ 与 $N$ 可交换，由二项式定理：
$$A^n=(E+N)^n=\sum_{k=0}^{n}\binom{n}{k}N^k=E+nN+\binom{n}{2}N^2.$$
$$A^n=\begin{pmatrix}1&n&\binom{n}{2}\\0&1&n\\0&0&1\end{pmatrix}=\begin{pmatrix}1&n&\frac{n(n-1)}2\\0&1&n\\0&0&1\end{pmatrix}.$$
</details>

**21.** 解矩阵方程 $AX=A+X$，其中 $A=\begin{pmatrix}1&2\\1&3\end{pmatrix}$。

<details><summary>解答</summary>

$AX-X=A\Rightarrow (A-E)X=A$。$A-E=\begin{pmatrix}0&2\\1&2\end{pmatrix}$，$|A-E|=0-2=-2\ne0$，可逆。
$$(A-E)^{-1}=\frac{1}{-2}\begin{pmatrix}2&-2\\-1&0\end{pmatrix}=\begin{pmatrix}-1&1\\\frac12&0\end{pmatrix}.$$
$$X=(A-E)^{-1}A=\begin{pmatrix}-1&1\\\frac12&0\end{pmatrix}\begin{pmatrix}1&2\\1&3\end{pmatrix}=\begin{pmatrix}0&1\\\frac12&1\end{pmatrix}.$$
验证：$AX=\begin{pmatrix}1&2\\1&3\end{pmatrix}\begin{pmatrix}0&1\\\frac12&1\end{pmatrix}=\begin{pmatrix}1&3\\\frac32&4\end{pmatrix}$，$A+X=\begin{pmatrix}1&3\\\frac32&4\end{pmatrix}$ ✓。
</details>

**22.** 设 $A=\begin{pmatrix}2&0&0\\0&1&2\\0&3&4\end{pmatrix}$，用分块法求 $A^{-1}$。

<details><summary>解答</summary>

分块为 $A=\begin{pmatrix}2&0\\0&A_1\end{pmatrix}$，$A_1=\begin{pmatrix}1&2\\3&4\end{pmatrix}$。$|A_1|=-2\ne0$，$A_1^{-1}=\begin{pmatrix}-2&1\\\frac32&-\frac12\end{pmatrix}$。
$$A^{-1}=\begin{pmatrix}2^{-1}&0\\0&A_1^{-1}\end{pmatrix}=\begin{pmatrix}\frac12&0&0\\0&-2&1\\0&\frac32&-\frac12\end{pmatrix}.$$
</details>

**23.** 设 $A$ 为 3 阶方阵，$|A|=\dfrac13$，$A^*=\begin{pmatrix}1&0&0\\2&1&0\\0&0&1\end{pmatrix}$，求 $A$。

<details><summary>解答</summary>

由 $A^*=|A|A^{-1}$，$A^{-1}=\dfrac{A^*}{|A|}=3A^*=\begin{pmatrix}3&0&0\\6&3&0\\0&0&3\end{pmatrix}$。
$|A^{-1}|=\dfrac1{|A|}=3$，校验 $|3A^*|=3^3|A^*|=27\cdot|A|^2=27\cdot\frac19=3$ ✓。
$A=(A^{-1})^{-1}$，求 $\begin{pmatrix}3&0&0\\6&3&0\\0&0&3\end{pmatrix}^{-1}$：分块 $=\operatorname{diag}(B,3)$，$B=\begin{pmatrix}3&0\\6&3\end{pmatrix}$，$B^{-1}=\dfrac{1}{9}\begin{pmatrix}3&0\\-6&3\end{pmatrix}=\begin{pmatrix}\frac13&0\\-\frac23&\frac13\end{pmatrix}$。
$$A=\begin{pmatrix}\frac13&0&0\\-\frac23&\frac13&0\\0&0&\frac13\end{pmatrix}.$$
</details>

**24.** 设 $A=\begin{pmatrix}1&-1\\1&1\end{pmatrix}$，已知 $A^2-2A+2E=O$，求 $A^4$ 与 $A^{-1}$。

<details><summary>解答</summary>

- $A^4$：由 $A^2=2A-2E$，
  $A^3=A(2A-2E)=2A^2-2A=2(2A-2E)-2A=2A-4E$；
  $A^4=A\cdot A^3=A(2A-4E)=2A^2-4A=2(2A-2E)-4A=-4E$。

- $A^{-1}$：$|A|=1-(-1)=2\ne0$，可逆。$A^2-2A+2E=O\Rightarrow A(A-2E)=-2E\Rightarrow A\cdot\dfrac{2E-A}{2}=E$，故 $A^{-1}=\dfrac{2E-A}{2}=\dfrac12\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\begin{pmatrix}\frac12&\frac12\\-\frac12&\frac12\end{pmatrix}$。
</details>

## 四、证明题（6 题）

**25.** 设 $A$ 为 $n$ 阶方阵，且 $A^TA=E$（正交矩阵），证明 $|A|=\pm1$。

<details><summary>证明</summary>

$A^TA=E$ 两边取行列式：$|A^T||A|=|E|=1$。由 [[2.3 矩阵转置、方阵行列式|转置不变]] $|A^T|=|A|$，故 $|A|^2=1$，从而 $|A|=\pm1$。
</details>

**26.** 设 $A$ 为 $n$ 阶方阵，且存在正整数 $k$ 使 $A^k=O$（幂零矩阵），证明 $A$ 不可逆。

<details><summary>证明</summary>

反证。设 $A$ 可逆，则 $A^k$ 可逆（可逆矩阵之积可逆），但 $A^k=O$ 不可逆，矛盾。故 $A$ 不可逆。

或直接取行列式：$|A^k|=|A|^k=|O|=0\Rightarrow |A|=0$，由 [[2.4 逆矩阵|可逆充要条件]] 知 $A$ 不可逆。
</details>

**27.** 设 $A$ 为 $n$ 阶对称矩阵，$B$ 为 $n$ 阶反对称矩阵，证明 $AB-BA$ 为对称矩阵。

<details><summary>证明</summary>

由题 $A^T=A$，$B^T=-B$。计算 $(AB-BA)^T$：
$$(AB-BA)^T=(AB)^T-(BA)^T=B^T A^T-A^T B^T=(-B)A-A(-B)=-BA+AB=AB-BA.$$
故 $AB-BA$ 对称。

> [!note] 关键依据
> [[2.3 矩阵转置、方阵行列式|转置反序律]] $(AB)^T=B^T A^T$，以及对称、反对称的转置刻画。
</details>

**28.** 设 $A,B$ 均为 $n$ 阶方阵，且 $AB=A+B$，证明：
（1）$(A-E)(B-E)=E$；
（2）$AB=BA$。

<details><summary>证明</summary>

（1）$AB=A+B\Rightarrow AB-A-B=O\Rightarrow AB-A-B+E=E\Rightarrow (A-E)(B-E)=E$。

（2）由（1）$(A-E)(B-E)=E$，即 $A-E$ 与 $B-E$ 互为逆矩阵，故 $(B-E)(A-E)=E$（逆的唯一性与双侧性）：
$$BA-B-A+E=E\Rightarrow BA=A+B.$$
又 $AB=A+B$，故 $AB=BA$。
</details>

**29.** 设 $A$ 为 $n$ 阶可逆方阵，证明 $(A^*)^{-1}=(A^{-1})^*$。

<details><summary>证明</summary>

由核心恒等式 $A^*A=|A|E$，$|A|\ne0$，两边除以 $|A|$（或乘以 $\dfrac{1}{|A|}$）：$A^*\cdot\dfrac{A}{|A|}=E$，故 $(A^*)^{-1}=\dfrac{A}{|A|}$。

另一方面，将求逆公式 $A^{-1}=\dfrac{A^*}{|A|}$ 应用于 $A^{-1}$：$(A^{-1})^*=|A^{-1}|(A^{-1})^{-1}=\dfrac{1}{|A|}\cdot A=\dfrac{A}{|A|}$。

故 $(A^*)^{-1}=(A^{-1})^*=\dfrac{A}{|A|}$，证毕。见 [[2.6 伴随矩阵|性质 (8)]]。
</details>

**30.** 设 $A$ 为 $n$ 阶方阵（$n\ge2$），证明：若 $|A|\ne0$，则 $(A^*)^*=|A|^{n-2}A$。

<details><summary>证明</summary>

由核心恒等式应用于 $A^*$：$A^*(A^*)^*=|A^*|E$。由 [[2.6 伴随矩阵|性质 (3)]] $|A^*|=|A|^{n-1}$，故
$$A^*(A^*)^*=|A|^{n-1}E.\quad(\star)$$
当 $|A|\ne0$ 时 $A^*$ 可逆（$|A^*|=|A|^{n-1}\ne0$）。对 $(\star)$ 左乘 $(A^*)^{-1}$：
$$(A^*)^*=(A^*)^{-1}|A|^{n-1}E=|A|^{n-1}(A^*)^{-1}.$$
又 $(A^*)^{-1}=\dfrac{A}{|A|}$（性质 (8)），代入：
$$(A^*)^*=|A|^{n-1}\cdot\frac{A}{|A|}=|A|^{n-2}A.$$
证毕。

> [!note] 推广
> 该公式对 $|A|=0$ 也成立：$n=2$ 时 $(A^*)^*=A=|A|^0 A$；$n\ge3$ 时利用秩可证 $(A^*)^*=O=|A|^{n-2}A$。详见 [[2.6 伴随矩阵]]。
</details>

## 考点统计

| 题型 | 题号 | 主要考点 | 关联小节 |
| ---- | ---- | -------- | -------- |
| 填空 | 1, 2, 7 | $|kA|=k^n|A|$、$\|A^{-1}\|$、$\|A^*\|$ | [[2.3 矩阵转置、方阵行列式]]、[[2.6 伴随矩阵]] |
| 填空 | 3, 4 | 矩阵乘法、矩阵的幂 | [[2.2 矩阵线性运算、乘法]] |
| 填空 | 5, 6 | 抽象求逆、对角阵求逆 | [[2.4 逆矩阵]] |
| 填空 | 8 | 分块对角行列式 | [[2.5 分块矩阵]] |
| 选择 | 9, 13 | 乘法失效律、幂等矩阵 | [[2.2 矩阵线性运算、乘法]] |
| 选择 | 10, 11, 12, 14 | 逆性质反序、伴随行列式、循环移位 | [[2.4 逆矩阵]]、[[2.6 伴随矩阵]] |
| 计算 | 15, 19 | 元素级乘法、$(A+B)^2$ 不成立 | [[2.2 矩阵线性运算、乘法]] |
| 计算 | 16, 17, 21, 23 | 伴随法求逆、解矩阵方程 | [[2.4 逆矩阵]]、[[2.6 伴随矩阵]] |
| 计算 | 18 | $A^*$ 与 $A^{-1}$ 互化 | [[2.6 伴随矩阵]] |
| 计算 | 20, 24 | 矩阵高次幂（二项式、降幂递推） | [[2.2 矩阵线性运算、乘法]]、[[2.3 矩阵转置、方阵行列式]] |
| 计算 | 22 | 分块对角求逆 | [[2.5 分块矩阵]] |
| 证明 | 25, 26 | 正交矩阵行列式、幂零不可逆 | [[2.3 矩阵转置、方阵行列式]]、[[2.4 逆矩阵]] |
| 证明 | 27 | 对称/反对称与转置反序律 | [[2.3 矩阵转置、方阵行列式]] |
| 证明 | 28 | 矩阵方程因子分解、交换性 | [[2.4 逆矩阵]] |
| 证明 | 29, 30 | 伴随矩阵恒等式与双重伴随 | [[2.6 伴随矩阵]] |

> [!summary] 高频考点分布
> - **伴随矩阵性质**（$|A^*|$、$(A^*)^*$、$(A^*)^{-1}$）：题 1、2、7、11、14、18、23、29、30，占比最高。
> - **逆矩阵计算与方程**：题 5、6、16、17、21、22，是必考计算题。
> - **乘法失效律与高次幂**：题 3、4、9、13、15、19、20、24，强调不能套用数的规律。
> - **分块运算**：题 8、22。
> - **转置与对称性证明**：题 25、27。

## 章节导航

- 返回：[[MOC - 第2章]]
- 知识点：[[2.1 矩阵概念与常见特殊矩阵]] · [[2.2 矩阵线性运算、乘法]] · [[2.3 矩阵转置、方阵行列式]] · [[2.4 逆矩阵]] · [[2.5 分块矩阵]] · [[2.6 伴随矩阵]]
- 上一章习题：[[MOC - 第1章习题]]（待建）
- 下一章习题：[[MOC - 第3章习题]]（待建）

## 相关标签

#线性代数 #习题 #矩阵乘法 #逆矩阵 #伴随矩阵 #分块矩阵
