---
domain: 物理与电路
subject: 大学物理B
type: exercise
chapter: 第1章 质点运动学
tags: [大学物理,习题,运动学,速度,加速度,相对运动]
prerequisites: ["高等数学A(1)"]
aliases: [第1章习题, 质点运动学习题]
---

# MOC - 第1章习题 质点运动学

> [!abstract] 本章习题概览
> 本章习题共 **24 题**，覆盖 [[1.1 参考系、坐标系、位置矢量|位置矢量与运动方程]]、[[1.2 位移、速度、加速度|位移速度加速度]]、[[1.3 直线运动、曲线运动|直线运动/抛体/圆周运动]]、[[1.4 相对运动|伽利略变换]] 四个知识板块。题型分布：填空 6 题、选择 6 题、计算 10 题、证明/讨论 2 题。答案与详解折叠于 `<details>` 中，建议先独立作答再核对。

---

## 一、填空题（6 题）

**1.** 质点运动方程为 $\vec r(t) = (2t^2)\hat i + (3t)\hat j$（SI），则 $t=2\,\text{s}$ 时速度 $\vec v =$ ______，加速度 $\vec a =$ ______。

**2.** 质点沿 $x$ 轴运动，$x = 4t - t^2$（m），$t$ 单位 s。$t=0$ 到 $t=4\,\text{s}$ 内位移为 ______ m，路程为 ______ m。

**3.** 质点做半径 $R=0.5\,\text{m}$ 的匀速圆周运动，速率 $v=3\,\text{m/s}$，则其向心加速度大小 $a_n =$ ______ m/s²，角速度 $\omega =$ ______ rad/s。

**4.** 以 $v_0=20\,\text{m/s}$、$\theta=30°$ 斜抛物体（$g=10\,\text{m/s}^2$，忽略空气阻力），射高 $H=$ ______ m，射程 $R=$ ______ m。

**5.** 河宽 $120\,\text{m}$，水流速度 $4\,\text{m/s}$，船在静水中速度 $5\,\text{m/s}$。船头垂直河岸渡河，到达对岸需 ______ s，将到达对岸下游 ______ m 处。

**6.** 一质点沿直线运动，速度与时间关系为 $v = 6 - 2t$（m/s）。当 $t=$ ______ s 时速度为零；此后加速度方向与速度方向 ______（填"相同"或"相反"）。

<details>
<summary>填空题答案</summary>

1. $\vec v = 8\hat i + 3\hat j$（m/s）；$\vec a = 4\hat i$（m/s²）。
2. 位移 $= x(4)-x(0) = (16-16)-0 = 0$ m；折返点 $v=4-2t=0$，$t=2$ s，$x(2)=8-4=4$ m，路程 $= |4|+|0-4| = 8$ m。
3. $a_n = v^2/R = 9/0.5 = 18$ m/s²；$\omega = v/R = 6$ rad/s。
4. $H = v_0^2\sin^2\theta/(2g) = 400\times 0.25/20 = 5$ m；$R = v_0^2\sin 2\theta/g = 400\times\sin 60°/10 \approx 34.64$ m。
5. $t = 120/5 = 24$ s；下漂 $x = 4\times 24 = 96$ m。
6. $v=0 \Rightarrow 6-2t=0 \Rightarrow t=3$ s；此后 $v<0$，$a=-2$ m/s² 也为负，同向（相同）。

</details>

---

## 二、选择题（6 题）

**1.** 关于质点，下列说法正确的是（ ）
A. 体积很小的物体一定可视为质点
B. 质量很大的物体一定不能视为质点
C. 不论物体多大，只要其形状大小对所研究问题影响可忽略，即可视为质点
D. 作转动的物体也能视为质点

**2.** 质点沿曲线运动，下列说法正确的是（ ）
A. 速度方向沿切线，加速度方向也一定沿切线
B. 速度方向沿法线
C. 加速度方向始终指向曲率中心
D. 加速度可分解为切向分量与法向分量

**3.** 关于位移与路程，下列正确的是（ ）
A. 位移大小恒等于路程
B. 位移是标量，路程是矢量
C. 单向直线运动中位移大小等于路程
D. 闭合运动中位移为零，路程也为零

**4.** 质点做匀速圆周运动，下列物理量中恒定不变的是（ ）
A. 速度 $\vec v$
B. 加速度 $\vec a$
C. 速率 $v$
D. 角速度 $\vec\omega$（方向）

**5.** 伽利略速度变换 $\vec v = \vec v' + \vec u$ 中，$\vec u$ 的物理意义是（ ）
A. 质点相对静系的速度
B. 质点相对动系的速度
C. 动系相对静系的速度
D. 静系相对动系的速度

**6.** 动系相对静系匀速平动时，加速度变换满足（ ）
A. $\vec a' = \vec a$
B. $\vec a' = \vec a - \vec u$
C. $\vec a' = 0$
D. $\vec a' = \vec a + \vec u$

<details>
<summary>选择题答案</summary>

1. **C**。质点条件是形状大小对问题影响可忽略，与绝对大小无关；转动物体一般不可视为质点。
2. **D**。速度沿切线；加速度可分解为切向（改大小）与法向（改方向）。
3. **C**。单向直线运动中 $|\Delta\vec r|=\Delta s$；闭合运动路程不为零。
4. **C**（速率恒定）。匀速圆周运动中 $\vec v$、$\vec a$ 方向时刻变化，仅速率 $v$ 不变。
5. **C**。$\vec u$ 为牵连速度，即动系相对静系的速度。
6. **A**。$\vec a'=\vec a-\dfrac{\mathrm d\vec u}{\mathrm dt}$，匀速平动时 $\dfrac{\mathrm d\vec u}{\mathrm dt}=0$。

</details>

---

## 三、计算题（10 题）

**1.（运动方程求速度加速度）** 质点运动方程 $\vec r = (2t^2-3t)\hat i + (t^3+2)\hat j$（SI）。求：
(1) $t=1\,\text{s}$ 时的速度与加速度；
(2) 第 1 秒内的位移。

<details>
<summary>解答</summary>

(1) $\vec v = \dfrac{\mathrm d\vec r}{\mathrm dt} = (4t-3)\hat i + 3t^2\hat j$；$\vec a = \dfrac{\mathrm d\vec v}{\mathrm dt} = 4\hat i + 6t\hat j$。

$t=1$：$\vec v = 1\hat i + 3\hat j$（m/s），$|\vec v|=\sqrt{10}\approx 3.16$ m/s；
$\vec a = 4\hat i + 6\hat j$（m/s²），$|\vec a|=\sqrt{52}\approx 7.21$ m/s²。

(2) $\vec r(0) = 0\hat i + 2\hat j$，$\vec r(1) = -1\hat i + 3\hat j$。
$\Delta\vec r = \vec r(1)-\vec r(0) = -1\hat i + 1\hat j$（m），$|\Delta\vec r|=\sqrt{2}\approx 1.41$ m。

**单位检验**：各分量量纲均为 m，速度 m/s，加速度 m/s²，自洽。

</details>

**2.（匀变速直线运动）** 汽车以 $v_0=20\,\text{m/s}$ 行驶，刹车后做匀减速直线运动，加速度大小 $a=5\,\text{m/s}^2$。求刹车距离与刹车时间。

<details>
<summary>解答</summary>

取初速方向为正，$a=-5$ m/s²。停止时 $v=0$。

由 $v=v_0+at$：$0=20-5t$，$t=4$ s。
由 $v^2-v_0^2=2a\Delta x$：$0-400=2\times(-5)\Delta x$，$\Delta x=40$ m。

或由 $x=v_0t+\tfrac12 at^2=20\times4-\tfrac12\times5\times16=80-40=40$ m。

**答**：刹车距离 $40\,\text{m}$，时间 $4\,\text{s}$。

</details>

**3.（自由落体与上抛）** 一石子从地面以 $v_0=19.6\,\text{m/s}$ 竖直上抛（$g=9.8\,\text{m/s}^2$，忽略空气阻力）。求：上升最大高度、落地时速度大小与总飞行时间。

<details>
<summary>解答</summary>

取向上为正，$a=-g=-9.8$ m/s²。

最高点 $v=0$：$v^2-v_0^2=2aH \Rightarrow 0-19.6^2=2\times(-9.8)H$，$H=\dfrac{19.6^2}{19.6}=19.6$ m。

落地时位移为零：$0=v_0t+\tfrac12(-g)t^2=t(v_0-\tfrac12 gt)$，$t=\dfrac{2v_0}{g}=\dfrac{39.2}{9.8}=4$ s。

落地速度：$v=v_0-gt=19.6-9.8\times4=-19.6$ m/s，大小 $19.6$ m/s（方向向下）。

**答**：最大高度 $19.6\,\text{m}$，落地速度大小 $19.6\,\text{m/s}$，飞行时间 $4\,\text{s}$。

</details>

**4.（斜抛运动）** 炮弹以 $v_0=400\,\text{m/s}$、$\theta=37°$ 发射（$g=10\,\text{m/s}^2$，$\sin 37°=0.6$，$\cos 37°=0.8$）。求射程、射高与飞行时间。

<details>
<summary>解答</summary>

飞行时间 $T=\dfrac{2v_0\sin\theta}{g}=\dfrac{2\times400\times0.6}{10}=48$ s。

射程 $R=\dfrac{v_0^2\sin 2\theta}{g}=\dfrac{400^2\times 2\times0.6\times0.8}{10}=\dfrac{160000\times0.96}{10}=15360$ m $\approx 15.36$ km。

射高 $H=\dfrac{v_0^2\sin^2\theta}{2g}=\dfrac{160000\times0.36}{20}=2880$ m。

**单位检验**：$R$ 与 $H$ 量纲为 $\dfrac{(\text{m/s})^2}{\text{m/s}^2}=\text{m}$，正确。

</details>

**5.（圆周运动角量与线量）** 质点做半径 $R=2\,\text{m}$ 的圆周运动，角位置 $\theta = t^3-3t$（rad，$t$ 单位 s）。求 $t=2\,\text{s}$ 时的角速度、角加速度、速率、切向加速度与向心加速度。

<details>
<summary>解答</summary>

$\omega=\dfrac{\mathrm d\theta}{\mathrm dt}=3t^2-3$；$t=2$：$\omega=12-3=9$ rad/s。
$\alpha=\dfrac{\mathrm d\omega}{\mathrm dt}=6t=12$ rad/s²。

$v=R\omega=2\times9=18$ m/s。
$a_t=R\alpha=2\times12=24$ m/s²。
$a_n=R\omega^2=2\times81=162$ m/s²。

总加速度 $a=\sqrt{24^2+162^2}=\sqrt{576+26244}=\sqrt{26820}\approx 163.8$ m/s²。

**单位检验**：$\omega$（rad/s）、$\alpha$（rad/s²）中 rad 无量纲；$v$（m/s）、$a_t$、$a_n$（m/s²）量纲正确。

</details>

**6.（圆周运动折返）** 飞轮半径 $R=0.5\,\text{m}$，从静止开始匀加速转动，角加速度 $\alpha=2\,\text{rad/s}^2$。求：(1) 轮缘一点在第 3 s 末的切向加速度、向心加速度；(2) 前 3 s 内轮缘一点走过的路程。

<details>
<summary>解答</summary>

(1) $\omega=\alpha t=2\times3=6$ rad/s。
$a_t=R\alpha=0.5\times2=1$ m/s²（常量）。
$a_n=R\omega^2=0.5\times36=18$ m/s²。

(2) 角位移 $\theta=\tfrac12\alpha t^2=\tfrac12\times2\times9=9$ rad。
路程 $s=R\theta=0.5\times9=4.5$ m。

**答**：$a_t=1\,\text{m/s}^2$，$a_n=18\,\text{m/s}^2$，路程 $4.5\,\text{m}$。

</details>

**7.（一般曲线运动法向切向分解）** 质点沿曲线 $y=x^2$（m）运动，沿 $x$ 方向 $x=2t$（m，$t$ 单位 s）。求 $t=1\,\text{s}$ 时的速度、加速度，以及该点曲率半径与法向加速度。

<details>
<summary>解答</summary>

$x=2t$，$y=x^2=4t^2$。$t=1$：$x=2$，$y=4$。

$v_x=\dfrac{\mathrm dx}{\mathrm dt}=2$ m/s；$v_y=\dfrac{\mathrm dy}{\mathrm dt}=8t=8$ m/s。
$\vec v=2\hat i+8\hat j$（m/s），$v=\sqrt{4+64}=\sqrt{68}\approx 8.25$ m/s。

$a_x=0$；$a_y=\dfrac{\mathrm dv_y}{\mathrm dt}=8$ m/s²。$\vec a=8\hat j$（m/s²），$a=8$ m/s²。

切向加速度 $a_t=\dfrac{\mathrm dv}{\mathrm dt}$，其中 $v=\sqrt{4+64t^2}$，$\dfrac{\mathrm dv}{\mathrm dt}=\dfrac{128t}{2\sqrt{4+64t^2}}=\dfrac{64t}{\sqrt{4+64t^2}}$。
$t=1$：$a_t=\dfrac{64}{\sqrt{68}}=\dfrac{64}{2\sqrt{17}}=\dfrac{32}{\sqrt{17}}\approx 7.76$ m/s²。

法向加速度 $a_n=\sqrt{a^2-a_t^2}=\sqrt{64-60.21}\approx \sqrt{3.79}\approx 1.95$ m/s²。

曲率半径 $\rho=\dfrac{v^2}{a_n}=\dfrac{68}{1.95}\approx 34.9$ m。

**说明**：此题法向分量较小，因 $t=1$ 时速度方向接近竖直（$v_y\gg v_x$），加速度几乎沿切向。

</details>

**8.（船过河）** 河宽 $d=100\,\text{m}$，水速 $\vec u=3\hat i$（m/s），船静水速度 $v'=5\,\text{m/s}$。(1) 船头垂直河岸，求渡河时间与到达点；(2) 船头偏上游某角使到达正对岸，求船头方向与渡河时间。

<details>
<summary>解答</summary>

$\hat i$ 沿河岸下游，$\hat j$ 垂直河岸指向对岸。

(1) $\vec v'=5\hat j$，$\vec v=3\hat i+5\hat j$。
$t=\dfrac{100}{5}=20$ s；下漂 $x=3\times20=60$ m。

(2) 设船头与 $\hat j$（河岸法线）成 $\alpha$ 偏向上游。$v'_x=-5\sin\alpha$，$v'_y=5\cos\alpha$。
到达正对岸：$v_x=0 \Rightarrow -5\sin\alpha+3=0 \Rightarrow \sin\alpha=0.6$，$\alpha\approx 36.9°$。
$\cos\alpha=0.8$，$v_y=5\times0.8=4$ m/s。$t=\dfrac{100}{4}=25$ s。

**答**：(1) $20\,\text{s}$，下游 $60\,\text{m}$；(2) 船头偏上游 $36.9°$，$25\,\text{s}$。

</details>

**9.（雨滴相对运动）** 雨滴竖直下落，对地速度 $v_y=10\,\text{m/s}$。一人骑自行车以 $v_车=15\,\text{m/s}$ 水平行驶。求雨滴相对人的速度大小与方向（相对竖直方向的偏角）。

<details>
<summary>解答</summary>

以地为静系，人为动系，牵连速度 $\vec u=15\hat i$（m/s）。雨对地 $\vec v=-10\hat j$（m/s）。

雨对人速度 $\vec v'=\vec v-\vec u=-15\hat i-10\hat j$（m/s）。
大小 $|\vec v'|=\sqrt{225+100}=\sqrt{325}\approx 18.03$ m/s。

方向：相对竖直方向（$\hat j$）的偏角
$$\tan\varphi=\frac{|v'_x|}{|v'_y|}=\frac{15}{10}=1.5,\quad \varphi\approx 56.3°$$

即雨相对人**向前下方斜 $56.3°$** 打来（人感觉雨从前方迎面而来）。

</details>

**10.（动系加速平动加速度变换）** 升降机以 $a_0=3\,\text{m/s}^2$ 向上加速。升降机内一物体从天花板自由下落（相对升降机初速为零），相对升降机加速度大小 $a'=9.8+3=12.8\,\text{m/s}^2$（向下）。验证此结果并求物体相对地面的加速度。

<details>
<summary>解答</summary>

以地为静系，升降机为动系。牵连加速度 $\vec a_{\text{牵}}=3\hat j$（m/s²，向上）。
物体相对地面的加速度即重力加速度 $\vec a=-9.8\hat j$（m/s²，自由落体仅受重力）。

由 $\vec a=\vec a'+\vec a_{\text{牵}}$：
$$\vec a'=\vec a-\vec a_{\text{牵}}=-9.8\hat j-3\hat j=-12.8\hat j\ \text{(m/s}^2\text{)}$$

即物体相对升降机以 $12.8\,\text{m/s}^2$ 向下加速——与题设一致。

物体相对地面的加速度仍为重力加速度 $\vec a=-9.8\hat j$（m/s²），因为物体离手后只受重力（运动学上不依赖参考系选取的力源，但相对加速度因动系加速而变化）。

**关键**：动系加速平动时 $\vec a'\neq\vec a$，须用 $\vec a'=\vec a-\vec a_{\text{牵}}$。

</details>

---

## 四、证明题与讨论题（2 题）

**1.（证明：匀速圆周运动加速度指向圆心）** 设质点做半径 $R$、角速度 $\omega$（常量）的匀速圆周运动，运动方程 $\vec r = R\cos\omega t\,\hat i + R\sin\omega t\,\hat j$。试用求导法证明加速度大小为 $R\omega^2$、方向指向圆心。

<details>
<summary>证明</summary>

求一阶导（速度）：
$$\vec v=\frac{\mathrm d\vec r}{\mathrm dt}=-R\omega\sin\omega t\,\hat i+R\omega\cos\omega t\,\hat j$$

求二阶导（加速度）：
$$\vec a=\frac{\mathrm d\vec v}{\mathrm dt}=-R\omega^2\cos\omega t\,\hat i-R\omega^2\sin\omega t\,\hat j=-\omega^2(R\cos\omega t\,\hat i+R\sin\omega t\,\hat j)=-\omega^2\vec r$$

即 $\vec a=-\omega^2\vec r$。

- 大小：$|\vec a|=\omega^2|\vec r|=\omega^2 R$；
- 方向：$\vec a$ 与 $\vec r$ 反向，$\vec r$ 由圆心指向质点，故 $\vec a$ 由质点指向圆心。

证毕。$\blacksquare$

</details>

**2.（讨论：伽利略变换的加速度不变性）** 设动系 $S'$ 相对静系 $S$ 以常矢量 $\vec u$ 平动。试由伽利略位置变换 $\vec r'=\vec r-\vec u\,t$ 出发，论证：(1) 两系加速度相等 $\vec a'=\vec a$；(2) 讨论若 $\vec u$ 随时间变化（动系加速平动）时结论如何变化；(3) 说明该不变性在力学中的意义。

<details>
<summary>讨论</summary>

(1) 由 $\vec r'=\vec r-\vec u\,t$（$\vec u$ 常矢量）对 $t$ 求导：
$$\vec v'=\frac{\mathrm d\vec r'}{\mathrm dt}=\frac{\mathrm d\vec r}{\mathrm dt}-\vec u=\vec v-\vec u$$
再求导：
$$\vec a'=\frac{\mathrm d\vec v'}{\mathrm dt}=\frac{\mathrm d\vec v}{\mathrm dt}-\frac{\mathrm d\vec u}{\mathrm dt}=\vec a-0=\vec a$$

即两惯性系间加速度不变。

(2) 若 $\vec u=\vec u(t)$ 随时间变化，则 $\dfrac{\mathrm d\vec u}{\mathrm dt}=\vec a_{\text{牵}}\neq 0$，此时
$$\vec a'=\vec a-\vec a_{\text{牵}}$$

加速度不再不变。动系为非惯性系，须引入惯性力（见 [[MOC - 第2章|第2章]]）。

(3) 力学意义：加速度不变性是牛顿第一、第二定律在一切惯性系中形式相同的运动学根源。只要 $\vec F=m\vec a$ 在 $S$ 中成立，则 $\vec F=m\vec a'$ 在 $S'$（匀速平动）中也成立——力学相对性原理得以保证。这是经典力学的基石之一；高速情形下被狭义相对论修正（见 [[MOC - 第11章|第11章]]）。

</details>

---

## 考点统计表

| 知识点 | 涉及题号 | 题数 | 难度分布 |
| :--- | :--- | :---: | :--- |
| [[1.1 参考系、坐标系、位置矢量\|参考系与质点模型]] | 选择1 | 1 | 易 |
| [[1.2 位移、速度、加速度\|运动方程求速度加速度]] | 填空1、计算1、计算2、计算7 | 4 | 易-中 |
| [[1.2 位移、速度、加速度\|位移与路程]] | 填空2、选择3 | 2 | 易 |
| [[1.3 直线运动、曲线运动\|匀变速直线运动]] | 填空6、计算2、计算3 | 3 | 易-中 |
| [[1.3 直线运动、曲线运动\|抛体运动]] | 填空4、计算4 | 2 | 中 |
| [[1.3 直线运动、曲线运动\|圆周运动角量线量]] | 填空3、选择2、选择4、计算5、计算6、证明1 | 6 | 中-难 |
| [[1.4 相对运动\|伽利略速度变换]] | 填空5、选择5、计算8、计算9 | 4 | 中 |
| [[1.4 相对运动\|加速度变换与动系平动]] | 选择6、计算10、讨论2 | 3 | 难 |
| 合计 | — | 24 | — |

> [!tip] 复习建议
> - **基础题**（填空、选择）确保概念清晰、公式熟练；
> - **圆周运动**题量最大、分值最高，重点掌握角量-线量互推与 $a_n=v^2/R$；
> - **相对运动**注意"绝对=相对+牵连"的矢量分解，动系加速时勿忘 $\vec a_{\text{牵}}$。

## 章节导航

> [!nav] 导航
> [[MOC - 第1章|第1章 知识点目录]] · [[MOC - 大学物理B|课程总览]] · 下一章习题：[[MOC - 第2章习题|第2章 牛顿运动定律习题]]
