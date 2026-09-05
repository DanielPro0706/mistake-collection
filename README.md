# Mistake Collection

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](https://github.com/openai/codex)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Mistake Collection** 是一个独立的 Codex Skill，用于把拍摄或扫描的中学错题整理成可编辑的中文 LaTeX 项目和两份经过核验的 A4 PDF。

它不会依赖其他题目总结类 Skill。

## 输出内容

默认生成：

- `纯题目版.pdf`：只含章节标题、原题题号、题干、选项或填空，以及作答所必需的原题图；
- `答案解析版.pdf`：保留相同的黑色题目，并加入红色答案、左栏标准步骤、右栏逐步解释和必要的红色解释图；
- 可编辑的 LaTeX 源码；
- 经过去字迹、曝光或透视修正并核对过的题图资源。

两份 PDF 的每一页都带黑色页码，并在页脚以清晰可读的灰色统一标注“由 Codex 生成，内容可能存在错误，请自行核对。”。

纯题目版不会出现题前知识点、考点标签、公式提醒、方法提示、难度说明、易错提醒、答案或解析。

## 主要能力

- 人工逐张检查 HEIC、照片和扫描件，不把 OCR 当作唯一识别依据；
- 记录原题题号并逐字保留题干、空格、选项、符号、单位和图中标注，成册时统一连续编号；
- 先锁定原照片题干，再以原图裁片为参考用 ImageGen 重绘高清黑白教材题图，文字和数值优先由 LaTeX 精确叠加；
- ImageGen 图要求打印尺寸下线条清晰、长边至少 1200 px、背景为纯白，不使用二值化截图充当成品；
- 用审计清单记录 `TEXT_EXACT`、`FIGURE_EXACT`、`ANSWER_CROSSCHECKED`，阻止参考答案反向改写原题；
- 严格保持电表指针、开关状态、接触点、线路连接、箭头和刻度等关键信息；
- 独立求解，不把照片中的手写答案当作正确答案；
- 主标题默认左对齐，整份错题按 `1—N` 连续编号，小问编号保持不变；
- 大题如有经核对的同题标准答案，正式步骤按其顺序、写法和得分点呈现；每一步在左栏单独成行，公式尽量使用行内形式；
- 作图和交点定义使用完整文字，不写成 `O=AC∩BD`；基础推理可用“∵ / ∴”，但禁止用箭头替代证明理由；
- 教学批注由 Codex 独立撰写，默认在右栏与对应步骤水平对齐；若某一步过宽，则仅将该步批注移到其下一行，不能省略详细解释；
- 同一批材料包含多个学科时，默认按学科分别建立独立项目；
- 题面或图形信息模糊时，必须指出具体位置并索要清晰原图，不得猜测或从其他来源补全；
- 每幅题图另建线段连通性清单：题干或原图点名的每条线段都必须有实际连续路径，只有端点标签不算完成；
- 对 `B-C-E` 一类延长线逐段检查共线和无断口，并按长度条件确定点位，不能为了排版把本应倾斜的线画成水平线；
- 新项目使用审计清单 schema 2，逐图记录线段清单和共线、中点、平行、垂直、等长、角平分线等几何约束；验证脚本仍兼容旧 schema 1；
- 使用同一份 LaTeX 主文件生成同步的纯题版和答案版；
- 编译后逐页渲染，检查遗漏、裁切、重叠、乱码和图片尺寸。

## 安装

### 方法一：克隆到 Codex Skills 目录

```bash
git clone https://github.com/DanielPro0706/mistake-collection.git \
  ~/.codex/skills/mistake-collection
```

重新启动 Codex 或开启新任务，使 Skill 列表刷新。

使用 Skill 时，它会至多每 24 小时自动检查一次仓库中的 `VERSION`。发现新版本后只会提示本地与远端版本，不会静默覆盖本地文件；是否更新仍由用户明确确认。断网或 GitHub 暂时不可用不会阻塞错题整理。

### 方法二：让 Codex 安装

把仓库链接发给 Codex，并要求：

```text
安装这个 Skill：https://github.com/DanielPro0706/mistake-collection
```

## 使用方法

在当前工作区上传题目照片，只需发送：

```text
使用 $mistake-collection 整理这些题目。
```

Skill 默认会把结果保存到当前工作区的 `错题整理` 文件夹，并根据全部题目自动归纳合适的章节标题。双版本 PDF、黑色题目、红色答案、详细解析、题图处理和逐页核验等要求已经写入 Skill，无需重复说明。

只有想覆盖自动标题时才需要明确指定，例如：

```text
使用 $mistake-collection 整理这些题目，标题用“第十三章 简单电路”。
```

后续追加题目也只需发送：

```text
把新上传的题目追加到现有错题整理。
```

## 工作流程

1. 建立题目清单，确定每道题的准确边界。
2. 转录题干并逐字核对。
3. 优先用 ImageGen 参考原图重绘可忠实还原的题图；用户明确指定 ImageGen 时，不静默改用 TikZ、截图或二值化图片。
4. 独立求解并检查单位、方向、量程、节点和图示状态。
5. 生成纯题目版与答案解析版。
6. 检查纯题版没有任何教学提示或答案内容。
7. 编译、逐页渲染并与原始照片对照。

完整执行规则见 [SKILL.md](SKILL.md)。图像还原与答案编写规范分别见 [source-reconstruction.md](references/source-reconstruction.md) 和 [solution-writing.md](references/solution-writing.md)。

## 项目结构

```text
mistake-collection/
├── SKILL.md
├── VERSION
├── agents/
│   └── openai.yaml
├── assets/
│   ├── audit-manifest-template.json
│   └── mistake-collection-template.tex
├── scripts/
│   ├── check_for_updates.py
│   └── validate_audit_manifest.py
├── references/
│   ├── solution-writing.md
│   └── source-reconstruction.md
├── LICENSE
└── README.md
```

## 环境建议

- Codex with Skills support
- XeLaTeX 与中文字体支持；模板默认使用 Fandol 字体
- PDF 页面渲染工具，例如 Poppler 或 Ghostscript
- 对复杂题图进行清理时可用 ImageGen 图像编辑能力

## 准确性边界

- 无法辨认或被裁切的内容不会凭空补写；应先向用户确认。
- 图像更清晰不等于图像正确；任何改变指针角度、刻度、连接或实验状态的结果都必须弃用。
- 编译成功只代表文件能够构建，不代表题目、图像和答案已核对正确。
- 原始照片可能包含个人信息，公开分享输出前请自行检查并脱敏。

## English

Mistake Collection is a self-contained Codex Skill that reconstructs photographed school problems into an editable Chinese LaTeX project and two synchronized PDFs:

- a strict question-only edition with no knowledge-point notes, hints, answers, or explanations;
- a detailed edition with black questions and red solutions, step-level reasoning, and optional answer-side diagrams.

It prioritizes source fidelity, independent solution checking, state-preserving figure restoration, and rendered-page QA. See [SKILL.md](SKILL.md) for the full workflow.

## License

Released under the [MIT License](LICENSE).
