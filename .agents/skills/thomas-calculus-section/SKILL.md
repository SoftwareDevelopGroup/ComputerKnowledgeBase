---
name: thomas-calculus-section
description: "Extract a single section of Thomas' Calculus (15e) from the per-chapter split source PDFs and transcribe it faithfully into the Obsidian vault's knowledge-note style. Use when the user asks to 整理 / 转写 / knowledge-base a specific Thomas Calculus section (e.g. '整理 2.1 节', '整理 3.4'). Covers PyMuPDF section extraction, faithful (not aggressive) transcription, figure placeholders, the Markdown-table absolute-value pitfall, and a pre-write validation checklist."
agent_created: true
---

# 整理托马斯微积分单节（PDF → Obsidian 笔记）

把《Thomas' Calculus, 15th Edition》某一节，从该库拆分好的**按章 PDF** 中提取出来，
**忠实转写**为 Obsidian 知识笔记（不擅自总结/加 mermaid/加易错点 callout）。

## 源 PDF 位置

`D:\Code\Translate\source\Thomas Calculus, 15th Edition拆分\Chapter N <章节名>.pdf`

- 按章拆分：Chapter 1 Functions.pdf、Chapter 2 Limits and Continuity.pdf、…、Chapter 19 …。
- 一节通常在数页内。先定位起止页，再 dump 全文。

## 工作流程

### 0. 优先复用本地英文 OCR md（差异化比对）

进入目标 vault 目录后，先检查是否已存在一份用户自己的英文 OCR md（文件名与最终笔记同名，如 `8.3 Trigonometric Integrals.md`，内容为英文教材原文 + LaTeX）。若存在且用户确认「结构大致正确」：

1. **直接 Read 该英文 md 作为底稿**，用它快速确认本节有哪些小节、例题、定理/公式框、Figure。
2. **只对易错点做差异校验**（不必全文重抽 PDF 并逐页读图）：
   - 用 `fitz` 定位本节页码范围。
   - 仅把**公式密集的例题页、多列布局页、涉及 `\tan`/`\sec`/`\sin A\theta`/`\cos 2x` 等高危结构**的页渲染成 PNG。
   - 用多模态 `Read` 逐页核对关键公式（`\frac` 上下、系数、变量替换、编号式 (1)(2)），标记底稿与 PDF 不一致处。
3. **直接在英文底稿上翻译、套 callout、加 frontmatter、改分数为 `\frac`**，而不是从零重写。底稿公式正确时尽量保留其 LaTeX。
4. 若底稿明显缺小节/例题或公式大面积错误，再降级为「从 PDF 全文重抽」流程。

### 1. 定位并提取一节

若不存在可用的本地英文 md，或底稿质量不足以复用，再用 PyMuPDF（`fitz`）从头提取：

```python
import fitz
doc = fitz.open(r"D:\Code\Translate\source\Thomas Calculus, 15th Edition拆分\Chapter 2 Limits and Continuity.pdf")
# 找起点：正文含 "2.1" 且含节标题关键字（如 "Rates of Change"）
# 找终点：下一节号 "2.2" + 其标题，或 "Questions to Guide Your Review"
for i in range(doc.page_count):
    t = doc[i].get_text()
    if start is None and ("2.1" in t and "Rates of Change" in t): start = i
    if start is not None and ("2.2" in t and "Limit of a Function" in t): end = i; break
for i in range(start, end):
    print(doc[i].get_text())
```

- **上标/函数式含糊时务必渲染页面为 PNG 并目视核对**：`pix = doc[pno].get_pixmap(matrix=fitz.Matrix(2.2,2.2)); pix.save("page.png")`，再 Read 该 PNG。
  （PDF 纯文本提取会丢失上标：`x^3` 可能变 `x3`，`x^{1/3}` 可能错位。）
- **含具体数学公式的例题，必须用多模态读图核对（必经一步）**：PyMuPDF 的纯文本提取在以下场景严重乱码，仅凭文本+OCR 重建极易写错关键表达式：
  - 多列布局（如 Example 1 左侧图右侧表，列顺序会被打乱）。
  - 小写希腊字母 + 函数粘连：`tan sec 2 / 3` 实际可能是 `\tan t\,\sec 2t / 3t`，OCR 看不出空格/参数。
  - 涉及 `\sec`、`\csc`、`\cot` 等次要三角函数时，PDF 提取常把它们与相邻 token 拼接错位。
  - 分子分母互换型表达式（如 `\sin A\theta / \sin B\theta` vs `\sin B\theta / \sin A\theta`），文本顺序与 LaTeX 视觉顺序都不可信。

  **核对步骤**：每节关键例题所在页全部 `Read page_XX.png`（多模态 Read）目视确认，对照待写入的公式逐字符核对（特别是 `\frac` 上下结构、`A/B` 系数、变量替换如 $\theta=2t$）。**用户曾因此三次失误**（2.4 节 Ex 5a/6/7 一律错，事后读图才发现），凡涉及 `\tan`/`\sec`/`\sin A\theta/\sin B\theta`/`\cos y-1` 这类结构务必先 Read 后写。
  - **多模态不可用时的降级核对法**：若当前会话模型不支持读图（Read PNG 返回 "model does not support images"），改用纯文本方案：用 `doc[i].get_text()` 逐页 dump 本节全文，与英文底稿**逐条比对**例题/定理/公式框的数值、系数、变量替换与不等式方向；用 `grep "FIGURE X.YY"` 确认图号与图注。此方案对文本结构可靠，但多列页的块顺序会乱（如小节标题被提取到页末），以底稿+代数推导为准即可。核对后记得删除临时渲染/脚本文件。

### 2. 忠实转写（关键：不是激进重构）

遵循  `Templates/知识点笔记模板.md`，但采用**忠实转写**模式：
- 顶部：`[!info] 📘 本节引言`（1–2 句说明本节解决什么问题）。
- **不**加顶部 `[[#...]]` 导航目录（TOC）——用户要求笔记不要有目录。
- 教材块的英文标签（`DEFINITION` / `DEFINITIONS` / `THEOREM` / `EXAMPLE` 等）**必须原样写进 callout 标题**，格式参照 `2.6`（先类型、再 `📐`/`✏️`、再标签、再 ` — `、再英文标题、最后中文括号）：
  - `> [!definition] 📐 DEFINITIONS — <英文标题>（<中文标题>）`
  - `> [!definition] 📐 DEFINITION — <英文标题>（<中文标题>）`
  - `> [!theorem] 📐 THEOREM 11 — <英文标题>（<中文标题>）`
  - `> [!example] ✏️ EXAMPLE 1 — <英文标题>（<中文标题>）`
  - 定义/定理类用 `📐`，例题用 `✏️`；`DEFINITIONS`（复数，含多条相关定义）与 `DEFINITION`（单条）要区分清楚，不要把教材的 `DEFINITIONS` 笼统写成中文或漏标。
- **不**另加 mermaid、`[!warning]`、`[!summary]`、"易错点"等个人发挥——只呈现教材内容。
- **正文必须译为中文（与同库 2.x 笔记对齐）**：本库已有的托马斯微积分分节笔记（如 `2.1 Rates of Change and Tangent Lines to Curves.md`）正文均为中文，英文只保留在分节标题、例题标题与术语括号中（如「平均速率（average speed）」、「差商（difference quotient）」）。新整理的分节须把定义、例题、小结等主体**全部译为中文**，不得整段保留英文教材原文；保留的英文仅限于分节/例题标题与术语括号。
- **绝不删减教材内容**：转写与编辑时，不得删除任何教材原文/例题/习题/推导，**除非用户明确指示**。改格式、修公式、挪位置都只能在保留全部内容的前提下进行。脚本批量替换前必须先备份原文并校验边界唯一，避免误删大段内容（曾因边界误匹配误删一节的习题 21–46 与附录）。
- 公式：`$...$` 行内、`$$...$$` 独立；教材编号式 (1)(2) 用 `\tag{1}`。
- **除法用正式分数形式**：转写时**尽量不用 `/` 斜杠表示除法**，一律写成分子在上、分母在下的横线分数（LaTeX 用 `\frac{分子}{分母}`）。例如 `$x^2+1/x-2$` 应写为 `$\frac{x^2+1}{x-2}$`；即使行内短式也优先 `\frac` 而非 `a/b`。教材原本用横线分数的，必须保持横线分数；仅当教材本身以 `÷` 或斜杠排布且改写会扭曲原意时才保留斜杠。
- 紧凑排版：短公式行内化，连续推导并入单个 `$$...$$`（`aligned`/`cases`）。

### 3. Frontmatter（与同库 1.x 笔记同 schema）

```yaml
---
domain: 数学基础
subject: 托马斯微积分
type: knowledge
chapter: Chapter 2 Limits and Continuity
section: 2.1 Rates of Change and Tangent Lines to Curves（变化率与曲线切线）
tags: [微积分, 极限与连续, 变化率, 切线, 割线, 托马斯微积分]
prerequisites:
  - "[[1.1 Functions and Their Graphs]]"
aliases: [变化率与曲线切线, Rates of Change and Tangent Lines to Curves, 2.1 变化率与曲线切线]
---
```

- **标签只写进 frontmatter 的 `tags` 字段，绝不在笔记正文末尾追加 `#标签` 块**（如 `#微积分`、`#定积分` 等行内标签行）。顶部 H1 标题（`# 5.x ...`）是正规标题，不受影响。2026-08-17 因在 5.3 末尾加了 `#微积分 #积分 #定积分 #黎曼和 #中点法则 #可积性` 被用户纠正，写死此规则。

### 4. 图片：留占位（用户自行粘贴）【硬规则，绝不替用户嵌入】

每处 Figure 留一个占位块，用户把教材图粘贴到 Obsidian 后会生成 `![[Pasted image 时间戳.png]]`。

```
> [!abstract] 🖼️ 插图占位 · Figure 2.1
> 教材原图：曲线 y=f(x) 的割线 PQ，斜率即 Δy/Δx（平均变化率）。
> 操作：在 Obsidian 中将教材图粘贴到此处，生成 `![[Pasted image 时间戳.png]]` 后删除本占位块。
```

**重写时原样保留用户已粘贴的插图**：若笔记中已存在用户手动粘贴的 `![[Pasted image <时间戳>.png]]` 嵌入，**必须原样保留每条嵌入及其尺寸参数，不得删除、不得移动**（重写/编辑/改格式/挪位置都必须保留全部已粘贴嵌入）。

**⚠️ 绝不替用户嵌入图片（写死）**：无论 `Attachments/` 里是否已有对应图片（如 `idx*_full.png`、`Figure X.NN.png`、`Pasted image *.png`），整理/重写笔记时**都不得**用 `![[...]]` 把这些图塞进笔记。用户明确说过"图我自己来放，你不要帮我放"。凡遇到 Figure 处，只留上面的占位块；即便知道 Attachments 里哪张图对应哪个 Figure，也**绝不要**替用户嵌进去（2026-08-14 因替用户嵌入 `idx5_full.png` / `Figure 3.4_cand.png` 被用户纠正）。占位块的"教材原图"描述要写清该图内容，方便用户对照粘贴。

- **核对 Figure 编号**：不要盲信现有占位符或原文中的“图 X.YY”。应从源 PDF 中 grep `FIGURE X.YY` 或渲染相关页目视确认，确保占位块的编号与真实教材编号一致（例如 3.3 节只有 Figure 3.10/3.11/3.12，页边插图“Picturing the Product Rule”并非 Figure 3.13；图 3.13 实际在 3.4 节）。发现错标占位块时，按真实编号修正或改为描述性说明。

### 5. 习题不并入本节笔记

按 vault 习惯，Exercises 单独成"习题"笔记（用户后续可能要求整理）。

## Callout 约定（DEFINITION / THEOREM / EXAMPLE / PROOF / SOLUTION）

教材里的"过程性"内容（证明、解法）**必须放进对应的父 callout 内部**，绝不能开成独立的 `[!proof]` / `[!success]` callout 块（2026-08-17 用户明确纠正：单独开 proof/success callout 太难看）。

- **PROOF（证明）**：写在所属 `[!theorem]` callout **内部**，以加粗 `**Proof.**` 作为段首标记（theorem 正文空一行后接 `**Proof.**` + 证明正文）。证明内部的图、公式同属该 theorem callout。**不要**另开 `[!proof]` 独立 callout。
  > 例：
  > ```
  > > [!theorem] 📐 THEOREM 3 — ...
  > > 若 $f$ 在 $[a,b]$ 上连续……
  > >
  > > **Proof.** 若把最大-最小不等式……
  > > ![[Pasted image ...]]   # 证明中的图也在 theorem callout 内
  > ```
- **SOLUTION（解法）**：写在所属 `[!example]` callout **内部**，以加粗 `**Solution.**`（中文笔记可用 `**解答.**`）作为段首标记（题目空一行后接 `**Solution.**` + 解法正文）。**不要**另开 `[!success]` 独立 callout，也不要写成与 example 同级的普通 `>` 引用块（如 `> **Solution** …` 单独成块）。
  > 例：
  > ```
  > > [!example] ✏️ EXAMPLE 1 — ...
  > > 题目……
  > >
  > > **Solution.** 由题意……
  > > ![[Pasted image ...]]   # 解法中的图也在 example callout 内
  > ```
- 历史传记/页边提示等其它块沿用既有 `[!info]`、`[!abstract]`、`[!quote]`、`[!example]`、`[!definition]`、`[!theorem]` 等类型；**不要自创 proof / success callout 类型**。
- 若某定理在源教材中其证明被例题隔开（如先讲定理、再举例、最后才给证明），仍把证明收进该 theorem 的 `[!theorem]` callout：可把证明移到定理陈述之后（例题之前），或保持原文顺序但用 `**Proof.**` 段首标记接在 theorem 结尾——总之证明正文须与定理处于同一个 callout 内。

## ⚠️ 关键坑（已踩过，务必遵守）

1. **Markdown 表格 + 行内公式的坑**：表格单元格 `$...$` 里的绝对值竖线 `|`（如 `$|x|$`）
   会被当成列分隔符，把公式劈成多列、表格错位。绝对值一律写成 `\lvert \rvert`
   （如 `$\lvert x\rvert$`）。**写完务必校验**：每张表的每行 `|` 数量一致，且单元格内 `$...$` 不含字面 `|`。
2. **脚本批量改表的坑**：用 Python 替换表格时，若按"第一个 `| 题号` 表头"定位 `start`，
   可能误匹配到前面另一个同名表头，从而把中间大段内容（多节习题）一并删除。
   定位块边界要唯一（匹配带特定列的**完整表头**，或先 grep 确认只有一个目标），
   写完务必校验总行数与各节是否齐全。
3. **回车符**：Windows 下脚本写文件可能混入 `\r`；统一用 `open(path,"w",encoding="utf-8")`
   写出，写完 `grep`/`count("\r")` 确认 0 个。
4. **公式框 ≠ DEFINITION 块**：源教材里 "Shift Formulas"、"Scaling and Reflecting Formulas" 这类变换规则是**带标题的框（boxed rule）**，源正文**并未标 DEFINITION**。转写时保留 `[!definition]` 即可，但 callout 标题**不要**强加 `DEFINITION —` 前缀，只写英文标题：`> [!definition] 📐 Shift Formulas（平移公式）`。只有源正文确以 `DEFINITION/DEFINITIONS/THEOREM` 开头的块才加对应前缀。
5. **源正文可能有笔误，以图/代数结果为准**：例如 1.2 EXAMPLE 5 正文解题写 "substituting −x/2 for x"，但图 1.35 子图标签 (c)=`16x⁴+32x³+10`、(b)=`−½x⁴+2x³−5`，且代数推导（水平压缩取 `2x`、再关于 y 轴反射取 `−x` → 替换 `−2x`）只得到 `16x⁴+32x³+10`。凡正文与图/代数结果冲突，以图与正确代数推导为准，不要照抄笔误。
6. **源 `DEFINITION` 块可能藏在散文里，容易被漏标**：有些 `DEFINITION`/`DEFINITIONS` 不是独立成框，而是（a）出现在**一节最开头、节号之前**（如 1.1 开头 "DEFINITION A function f from a set D to a set Y is a rule…"），或（b）**内嵌在某段散文讨论中**（如 1.1 常见函数段里 "DEFINITION Two variables y and x are proportional…"）。忠实转写时容易把这类写成普通段落而漏掉 `[!definition]` 包裹。核对清单：写完后**逐节 grep 源 PDF 的 `^\s*(DEFINITION|DEFINITIONS|THEOREM)` 行**，与笔记里的 `[!definition]`/`[!theorem]` 数量与位置逐一比对；任何源里有、笔记里却是散文的定义，都补成 `📐 DEFINITION — …（…）` callout。
7. **教材侧边栏/辅助框不要漏掉**：像 "Applying the Power Rule"、"Denoting Functions by u and v"、"Picturing the Product Rule"、"How to Read the Symbols for Derivatives" 这类页边提示框虽不是 Figure/例题/定义，但属于教材正文内容，整理时也应保留。通常用 `[!info]` callout 简短呈现（如 `> [!info] 🔢 Applying the Power Rule`），并在页边插图处写清教材原图描述，不替用户嵌入图片。
8. **LaTeX 反斜杠 / `\tag` 编号的坑（曾致 11.6 节公式编号几乎全失）**：用 `re.sub` 去平移/替换含 `$$` 或 `\tag` 的模式，极易把 `$$` 双美元符破坏成单 `$`（整块公式失效），甚至把 `\tag{2}`…`\tag{11}` **静默删除**（最终只留 `\tag{1}`）。教训与正确做法：
   - **改写含大量公式的笔记时，直接整篇用 Write 工具重写**，正文里写**单**反斜杠（如 `\tag{2}`、`\begin{aligned}`），不要用 `re.sub` / `str.replace` 反复打补丁。
   - 写完后用 Python 校验：`re.findall(r"\\tag\{(\d+)\}", text)` 应返回**完整**编号集合（如 `['1'..'11']`）；且每个 `\tag` 前**恰好 1 个反斜杠**——`re.findall(r"\\\\tag\{\d+\}", text)` 必须为空（ nonempty 即有双反斜杠 `\tag` 会破坏 MathJax）。
   - 同时校验 `text.count("$$") % 2 == 0`、`"\r" not in text`、`\begin{aligned}` 与 `\end{aligned}` 均以单反斜杠存在。
   - 若发现 `$$` 被 `re.sub` 改坏，**最干净的恢复是整篇重写**，而非再跑一次 `re.sub`（会越改越乱）。同样别用 `s.replace("\\\\","\\")` 这类"全局去双反斜杠"操作——它会把 `aligned` 里的行分隔 `\\` 也一并破坏。
   - **Obsidian MathJax 渲染坑（`\tag` 与 `aligned`）**：Obsidian 内置 MathJax **不支持把 `\tag{N}` 放在 `aligned` 环境内部**——整块会渲染失败（显示为原始 LaTeX 或不渲染）。编号公式若需在多行推导末尾打标签，应把 `\tag{N}` 移到 `aligned` 之外的独立 `$$ ... \tag{N} $$` 显示方程中。此外，`aligned` 块**务必写成多行**（每行 `\\` 单独成行），单行 `aligned` 在 Obsidian 中较脆弱；所有独立编号方程 `(1)(2)...` 一律用顶层 `$$ ... \tag{N} $$`，绝不包在 `aligned` 内。

9. **临时辅助文件必须清理（每节交付前删除）**：整理过程中会在 vault 根目录（如 `数学基础/托马斯微积分/`）生成一批辅助脚本与渲染图——`locate_*.py`、`dump_*.py`、`render_*.py`、`verify_*.py`、`build_*.py`、`fix_*.py`、`diag_*.py`、`figcheck_*.py`、`section*_raw.txt`、`page_*.png` 等。它们**只用于当节定位 / 核对，绝不能留在知识库里**（会污染库、被 git 跟踪、干扰下次整理）。每节交付前用 `rm` 全部删除，并 `ls` 确认无 `locate_/dump_/render_/verify_/build_/fix_/diag_/figcheck_/page_/section*_raw` 残留。
   - **最终笔记一律用 Write 工具直接写出，不要用含 LaTeX 的 Python 脚本 `f.write` 落盘**：`build_12_2.py` 正是用普通字符串写出含 LaTeX 的内容，导致 `\b` 被 Python 当成退格转义，6 处 `begin{aligned}` 全部变成 `<BS>egin{aligned}` 而失效（与第 8 条同源）。Write 工具写出的反斜杠是安全的；若要批量校验，脚本只做**只读检查**，不要让它负责写出笔记正文。

## 交付前校验（必做）

- `$$` 数量必须为偶数（每对一开一闭）。
- `\tag{N}` 公式编号：每个 `\tag` 前**恰好 1 个反斜杠**（`re.findall(r"\\\\tag\{\d+\}", text)` 应为空），且编号集合与源教材一致（如 `1..11`，未编号的推导式不标 `\tag`）。用 Python 校验后，再人工核对正文里"方程 (N)"的引用是否也都对得上。
- 每张 Markdown 表：各行列数一致；单元格内 `$...$` 无字面 `|`。
- **除法均用 `\frac` 横线分数**：通读公式，确认无 `/` 斜杠除法的式子（如 `a/b`、`(x+1)/(x-2)`），改成 `\frac{...}{...}`（例外：指数 $x^{2/3}$、Leibniz 导数记号 $dy/dx$ 等教材本身使用斜杠的标准写法可保留）。
- 全文 0 个 `\r`、0 个残留 LaTeX 专用命令（`\textbf`、`\textcolor`、`\includegraphics`、`\R`、`longtable`、`\titleformat` 等）。
- Figure 占位块的数量、编号**与源 PDF 中 `FIGURE X.YY` 标题一致**；不要硬凑固定数量，每节实际图数不同。
- 与源 PDF 核对：**教材原文/例题/习题无遗漏、无删减**（内容完整性优先于格式）。
- 笔记**不含**顶部 `[[#...]]` TOC 目录（用户要求不要目录）。
- 笔记**不含**正文末尾的 `#标签` 块（如 `#微积分` 等行内标签行）——标签只写在 frontmatter 的 `tags` 字段；顶部 H1 标题除外。
- **Proof / Solution 均位于父 callout 内部**：**无**独立的 `[!proof]` / `[!success]` callout 块（2026-08-17 用户纠正：单独开 proof/success callout 太难看）。证明以加粗 `**Proof.**` 作为段首标记、写在所属 `[!theorem]` callout 内；解法以加粗 `**Solution.**`（中文笔记可用 `**解答.**`）作为段首标记、写在所属 `[!example]` callout 内。不要写成与 example/theorem 同级的普通 `>` 引用块。
- **清理本节临时文件**：删除 vault 根目录下本节产生的所有辅助脚本与渲染图（`locate_*.py` / `dump_*.py` / `render_*.py` / `verify_*.py` / `build_*.py` / `fix_*.py` / `diag_*.py` / `figcheck_*.py` / `section*_raw.txt` / `page_*.png`），并 `ls` 确认无残留（详见第 9 条）。笔记正文用 Write 工具落盘，不要用生成脚本代写。
