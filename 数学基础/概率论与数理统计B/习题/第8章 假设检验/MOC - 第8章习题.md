---
domain: 数学基础
subject: 概率论与数理统计B
type: exercise
chapter: 第8章 假设检验
tags: [概率论, 数理统计, 习题, 假设检验, Z检验, t检验, χ²检验, F检验, P值]
prerequisites: ["高等数学", "第8章 假设检验"]
aliases: [第8章习题, 假设检验习题]
---

# MOC - 第8章习题

> [!info] 习题说明
> 本章习题覆盖 [[MOC - 第8章|假设检验]] 全部考点，分填空、选择、计算、证明四类，共 32 题。计算题含 $Z$、$t$、$\chi^2$、$F$ 四类检验的完整步骤；证明题聚焦两类错误关系。答案置于 `<details>` 折叠区。

## 一、填空题（10 题）

**1.** 假设检验中，第一类错误（弃真）的概率为 ＿＿＿，第二类错误（取伪）的概率为 ＿＿＿。

**2.** 显著性水平 $\alpha$ 是预先控制的犯第 ＿＿＿ 类错误的概率。

**3.** 检验 $H_0:\mu=\mu_0$ vs $H_1:\mu\neq\mu_0$（$\sigma^2$ 已知），统计量 $Z=$ ＿＿＿，服从 ＿＿＿ 分布，拒绝域为 ＿＿＿。

**4.** $\sigma^2$ 未知时检验 $\mu$，用统计量 $T=\dfrac{\bar X-\mu_0}{S/\sqrt n}\sim$ ＿＿＿，自由度为 ＿＿＿。

**5.** 检验 $H_0:\sigma^2=\sigma_0^2$（$\mu$ 未知），统计量 $\chi^2=$ ＿＿＿，服从 ＿＿＿ 分布。

**6.** 双边 $\chi^2$ 检验的拒绝域为 ＿＿＿ 或 ＿＿＿。

**7.** 两正态总体方差齐性检验用统计量 $F=$ ＿＿＿，服从 ＿＿＿ 分布。

**8.** 设 $H_0$ 中必须含 ＿＿＿ 号，以保证检验统计量在 $H_0$ 下分布确定。

**9.** 单边检验由备择假设 $H_1$ 的方向决定，$H_1:\mu>\mu_0$ 对应 ＿＿＿ 侧检验。

**10.** P 值法判据：$P$ ＿＿＿ $\alpha$ 时拒绝 $H_0$。

<details><summary>填空题答案</summary>

1. $\alpha=P\{\text{拒}H_0|H_0\text{真}\}$；$\beta=P\{\text{接}H_0|H_0\text{假}\}$
2. 一
3. $Z=\dfrac{\bar X-\mu_0}{\sigma/\sqrt n}$；$N(0,1)$；$|Z|>z_{\alpha/2}$
4. $t(n-1)$；$n-1$
5. $\dfrac{(n-1)S^2}{\sigma_0^2}$；$\chi^2(n-1)$
6. $\chi^2>\chi_{\alpha/2}^2(n-1)$；$\chi^2<\chi_{1-\alpha/2}^2(n-1)$
7. $F=\dfrac{S_1^2}{S_2^2}$；$F(n_1-1,n_2-1)$
8. 等
9. 右
10. $<$

</details>

## 二、选择题（10 题）

**1.** 在样本量固定时，减小 $\alpha$ 则 $\beta$（　）。
A. 减小　B. 增大　C. 不变　D. 为零

**2.** 实际检验中通常控制第一类错误的原因是（　）。
A. $\beta$ 更重要　B. $\alpha$ 可由拒绝域精确控制　C. $\beta$ 无关　D. 习惯

**3.** $\sigma^2$ 已知检验 $\mu$，应选（　）检验。
A. $Z$　B. $t$　C. $\chi^2$　D. $F$

**4.** $\sigma^2$ 未知检验 $\mu$，统计量服从（　）。
A. $N(0,1)$　B. $t(n-1)$　C. $\chi^2(n-1)$　D. $F(n-1,1)$

**5.** 检验 $H_0:\mu\geq\mu_0$ vs $H_1:\mu<\mu_0$ 是（　）。
A. 双边　B. 右侧单边　C. 左侧单边　D. 无法确定

**6.** $H_0$ 中含等号的原因是（　）。
A. 习惯　B. 取等号时统计量分布确定　C. 美观　D. 必须

**7.** 双边 $t$ 检验的拒绝域为（　）。
A. $|T|>t_\alpha(n-1)$　B. $|T|>t_{\alpha/2}(n-1)$　C. $T>t_{\alpha/2}(n-1)$　D. $T<-t_{\alpha/2}(n-1)$

**8.** 两样本 pooled $t$ 检验的前提是（　）。
A. $\sigma_1^2,\sigma_2^2$ 已知　B. $\sigma_1^2=\sigma_2^2$　C. $\mu_1=\mu_2$　D. $n_1=n_2$

**9.** 关于 P 值，下列正确的是（　）。
A. P 值是 $H_0$ 为真的概率
B. $P<\alpha$ 拒绝 $H_0$
C. P 值越大越拒绝
D. P 值与 $\alpha$ 无关

**10.** $\mu$ 未知检验 $\sigma^2$，$\chi^2$ 统计量的自由度为（　）。
A. $n$　B. $n-1$　C. $n-2$　D. $2n-2$

<details><summary>选择题答案</summary>

1. **B**
2. **B**
3. **A**
4. **B**
5. **C**
6. **B**
7. **B**
8. **B**
9. **B**
10. **B**

</details>

## 三、计算题（8 题）

**1.（Z 检验）** 某车间铜丝折断力 $X\sim N(\mu,64)$，$\mu_0=570$。抽 $n=9$ 得 $\bar x=575$。问折断力是否显著提高（$\alpha=0.05$）？

<details><summary>解答</summary>

1. 右侧单边：$H_0:\mu\leq570$，$H_1:\mu>570$。
2. $\sigma^2=64$ 已知，$Z=\dfrac{\bar X-\mu_0}{\sigma/\sqrt n}\sim N(0,1)$。
3. 拒绝域 $Z>z_{0.05}=1.645$。
4. $Z=\dfrac{575-570}{8/3}=\dfrac{15}{8}=1.875$。
5. $1.875>1.645$，**拒绝 $H_0$**，折断力显著提高。

</details>

**2.（t 检验）** 元件寿命 $X\sim N(\mu,\sigma^2)$，$\sigma^2$ 未知，标准 $\mu_0=1000$。抽 $n=9$ 得 $\bar x=980$，$s=30$。问寿命是否显著低于标准（$\alpha=0.05$）？

<details><summary>解答</summary>

1. 左侧单边：$H_0:\mu\geq1000$，$H_1:\mu<1000$。
2. $\sigma^2$ 未知，$T=\dfrac{\bar X-\mu_0}{S/\sqrt n}\sim t(8)$。
3. 拒绝域 $T<-t_{0.05}(8)=-1.860$。
4. $T=\dfrac{980-1000}{30/3}=-2$。
5. $-2<-1.860$，**拒绝 $H_0$**，寿命显著低于标准。

</details>

**3.（t 检验 双边）** 正态总体 $n=16$，$\bar x=24$，$s=4$，检验 $H_0:\mu=25$ vs $H_1:\mu\neq25$（$\alpha=0.05$）。

<details><summary>解答</summary>

1. 双边：$H_0:\mu=25$，$H_1:\mu\neq25$。
2. $\sigma^2$ 未知，$T=\dfrac{\bar X-25}{S/\sqrt n}\sim t(15)$。
3. 拒绝域 $|T|>t_{0.025}(15)=2.131$。
4. $T=\dfrac{24-25}{4/4}=-1$。
5. $|-1|=1<2.131$，**接受 $H_0$**。

</details>

**4.（两样本 t 检验）** 两机床加工直径 $N(\mu_1,\sigma^2),N(\mu_2,\sigma^2)$，$n_1=n_2=8$，$\bar x=20.0,\bar y=19.5$，$s_1^2=0.10,s_2^2=0.14$。问有无显著差异（$\alpha=0.05$）？

<details><summary>解答</summary>

1. 双边：$H_0:\mu_1=\mu_2$，$H_1:\mu_1\neq\mu_2$。
2. 方差相等未知，$T=\dfrac{\bar X-\bar Y}{S_w\sqrt{1/8+1/8}}\sim t(14)$。
3. 拒绝域 $|T|>t_{0.025}(14)=2.145$。
4. $S_w^2=\dfrac{7(0.10+0.14)}{14}=0.12$，$S_w=\sqrt{0.12}$。
   $T=\dfrac{0.5}{\sqrt{0.12}\sqrt{0.25}}=\dfrac{0.5}{\sqrt{0.03}}\approx2.887$。
5. $2.887>2.145$，**拒绝 $H_0$**，有显著差异。

</details>

**5.（χ² 检验）** $X\sim N(\mu,\sigma^2)$，$n=10$，$s^2=75.4$，检验 $H_0:\sigma^2=64$ vs $H_1:\sigma^2\neq64$（$\alpha=0.05$）。

<details><summary>解答</summary>

1. 双边：$H_0:\sigma^2=64$，$H_1:\sigma^2\neq64$。
2. $\mu$ 未知，$\chi^2=\dfrac{(n-1)S^2}{\sigma_0^2}\sim\chi^2(9)$。
3. 拒绝域 $\chi^2>\chi_{0.025}^2(9)=19.023$ 或 $\chi^2<\chi_{0.975}^2(9)=2.700$。
4. $\chi^2=\dfrac{9\times75.4}{64}\approx10.603$。
5. $2.700<10.603<19.023$，**接受 $H_0$**，方差无显著变化。

</details>

**6.（F 检验）** $n_1=8,n_2=10$，$s_1^2=0.81,s_2^2=0.36$，检验方差齐性（$\alpha=0.05$）。

<details><summary>解答</summary>

1. 双边：$H_0:\sigma_1^2=\sigma_2^2$，$H_1:\sigma_1^2\neq\sigma_2^2$。
2. $F=\dfrac{S_1^2}{S_2^2}\sim F(7,9)$。
3. 拒绝域 $F>F_{0.025}(7,9)=4.20$ 或 $F<F_{0.975}(7,9)\approx0.207$。
4. $F=\dfrac{0.81}{0.36}=2.25$。
5. $0.207<2.25<4.20$，**接受 $H_0$**，方差齐性成立。

</details>

**7.（P 值法）** $\sigma^2=1$ 已知，检验 $H_0:\mu=0$ vs $H_1:\mu\neq0$，$n=9$，$\bar x=0.6$。计算 P 值并就 $\alpha=0.05$ 判断。

<details><summary>解答</summary>

$Z=\dfrac{0.6}{1/3}=1.8$。双边 P 值 $P=2P\{Z>1.8\}=2(1-\Phi(1.8))=2(1-0.9641)=0.0718$。
$0.0718>0.05$，**接受 $H_0$**。拒绝的最小水平约为 $0.0718$。

</details>

**8.（综合）** 某糖果包装机额定每袋 500g，设袋重 $X\sim N(\mu,\sigma^2)$。抽 $n=16$ 得 $\bar x=498$，$s=4$。问机器是否正常（$\alpha=0.05$）？

<details><summary>解答</summary>

1. 双边：$H_0:\mu=500$，$H_1:\mu\neq500$。
2. $\sigma^2$ 未知，$T=\dfrac{\bar X-500}{S/\sqrt n}\sim t(15)$。
3. 拒绝域 $|T|>t_{0.025}(15)=2.131$。
4. $T=\dfrac{498-500}{4/4}=-2$。
5. $|-2|=2<2.131$，**接受 $H_0$**，机器正常。

</details>

## 四、证明题（4 题）

**1.** 证明：在样本量 $n$ 固定时，减小 $\alpha$ 必增大 $\beta$。

<details><summary>证明</summary>

记检验统计量为 $T$，拒绝域 $W$，接受域 $\bar W$。$\alpha=P\{T\in W|H_0\}$，$\beta=P\{T\in\bar W|H_1\}$（$H_1$ 真时）。
缩小拒绝域 $W$（使 $\alpha\downarrow$）$\Rightarrow$ 接受域 $\bar W$ 变大 $\Rightarrow$ 在 $H_1$ 真时落入 $\bar W$（取伪）的概率 $\beta$ 增大。
直观上：判断更"保守"（更不易拒绝）$\Rightarrow$ 更易放过假的 $H_0$ $\Rightarrow$ $\beta\uparrow$。$\square$

</details>

**2.** 设 $\sigma^2$ 已知，检验 $H_0:\mu=\mu_0$ vs $H_1:\mu\neq\mu_0$。证明：$\mu$ 的 $1-\alpha$ 置信区间包含 $\mu_0$ 当且仅当在水平 $\alpha$ 下接受 $H_0$。

<details><summary>证明</summary>

置信区间 $\left(\bar X-z_{\alpha/2}\dfrac{\sigma}{\sqrt n},\bar X+z_{\alpha/2}\dfrac{\sigma}{\sqrt n}\right)$ 包含 $\mu_0$
$\Leftrightarrow \left|\dfrac{\bar X-\mu_0}{\sigma/\sqrt n}\right|<z_{\alpha/2}$
$\Leftrightarrow |Z|<z_{\alpha/2}$（$Z=\dfrac{\bar X-\mu_0}{\sigma/\sqrt n}$）
$\Leftrightarrow$ 统计量观测值落入接受域
$\Leftrightarrow$ 接受 $H_0$。$\square$

（此即假设检验与区间估计的对偶性）

</details>

**3.** 证明 $Z$ 检验统计量 $Z=\dfrac{\bar X-\mu_0}{\sigma/\sqrt n}$ 在 $H_0:\mu=\mu_0$ 下服从 $N(0,1)$。

<details><summary>证明</summary>

$\bar X\sim N(\mu,\sigma^2/n)$。$H_0$ 成立即 $\mu=\mu_0$，故 $\bar X\sim N(\mu_0,\sigma^2/n)$。
$E(Z)=\dfrac{E(\bar X)-\mu_0}{\sigma/\sqrt n}=\dfrac{\mu_0-\mu_0}{\sigma/\sqrt n}=0$，$D(Z)=\dfrac{D(\bar X)}{\sigma^2/n}=\dfrac{\sigma^2/n}{\sigma^2/n}=1$。
又 $\bar X$ 正态，故线性变换 $Z$ 正态，$Z\sim N(0,1)$。$\square$

</details>

**4.** 设检验 $H_0:\mu=\mu_0$（$\sigma^2$ 未知）用 $t$ 检验，自由度为 $n-1$ 而非 $n$。证明其原因。

<details><summary>证明</summary>

$t$ 统计量 $T=\dfrac{\bar X-\mu_0}{S/\sqrt n}$，其中 $S^2=\dfrac{1}{n-1}\sum(X_i-\bar X)^2$。
关键：$\dfrac{(n-1)S^2}{\sigma^2}=\sum\left(\dfrac{X_i-\bar X}{\sigma}\right)^2$。因 $\sum(X_i-\bar X)=0$ 引入一个线性约束，使 $n$ 个 $X_i-\bar X$ 中只有 $n-1$ 个独立，故该平方和服从 $\chi^2(n-1)$ 而非 $\chi^2(n)$。
又 $\bar X$ 与 $S^2$ 独立（正态总体性质），由 $t$ 分布定义 $T=\dfrac{N(0,1)}{\sqrt{\chi^2(n-1)/(n-1)}}\sim t(n-1)$。
即自由度损失一个源于用 $\bar X$ 估计 $\mu$。$\square$

</details>

## 考点统计

| 考点 | 题号 | 题量 |
| ---- | ---- | ---- |
| 两类错误概念 | 填1-2、选1-2、证1 | 5 |
| 显著性水平与拒绝域 | 填3、选6、证2 | 3 |
| 单/双边判定 | 填9、选5、选7 | 3 |
| Z 检验 | 填3、选3、计1、证2-3 | 5 |
| t 检验 | 填4、选4、计2-4、证4 | 6 |
| $\chi^2$ 检验 | 填5-6、选10、计5 | 5 |
| F 检验（方差齐性） | 填7、选8、计6 | 3 |
| P 值法 | 填10、选9、计7 | 3 |
| 估计与检验对偶 | 证2 | 1 |

## 章节导航

- 上一级：[[MOC - 概率论与数理统计B]]
- 本章：[[MOC - 第8章]]
- 上一章习题：[[MOC - 第7章习题]]
- 下一章：课程结束（第8章为本课程最后一章，无后续习题）
