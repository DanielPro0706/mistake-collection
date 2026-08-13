# Mistake Collection

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](https://github.com/openai/codex)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Mistake Collection** 是一个独立的 Codex Skill，用于把拍摄或扫描的中学错题整理成可编辑的中文 LaTeX 项目和两份经过核验的 A4 PDF。

它不会依赖其他题目总结类 Skill。

## 输出内容

默认生成：

- `纯题目版.pdf`：只含章节标题、原题题号、题干、选项或填空，以及作答所必需的原题图；
- `答案解析版.pdf`：保留相同的黑色题目，并加入红色答案、详细解析、规范步骤、步骤说明和必要的红色解释图；
- 可编辑的 LaTeX 源码；
- 经过去字迹、曝光或透视修正并核对过的题图资源。

纯题目版不会出现题前知识点、考点标签、公式提醒、方法提示、难度说明、易错提醒、答案或解析。

## 主要能力

- 逐张检查 HEIC、照片和扫描件，防止一张图中多道题被漏掉；
- 逐字保留题号、题干、空格、选项、符号、单位和图中标注；
- 简单图使用 LaTeX/TikZ 重绘；复杂或状态敏感的图基于原图清理；
- 严格保持电表指针、开关状态、接触点、线路连接、箭头和刻度等关键信息；
- 独立求解，不把照片中的手写答案当作正确答案；
- 为大题提供符合中学生书写习惯的步骤，并逐步解释依据和易错点；
- 使用同一份 LaTeX 主文件生成同步的纯题版和答案版；
- 编译后逐页渲染，检查遗漏、裁切、重叠、乱码和图片尺寸。

## 安装

### 方法一：克隆到 Codex Skills 目录

```bash
git clone https://github.com/DanielPro0706/mistake-collection.git \
  ~/.codex/skills/mistake-collection
```

重新启动 Codex 或开启新任务，使 Skill 列表刷新。

### 方法二：让 Codex 安装

把仓库链接发给 Codex，并要求：

```text
安装这个 Skill：https://github.com/DanielPro0706/mistake-collection
```

## 使用方法

上传题目照片并明确章节标题、输出文件夹及额外要求，例如：

```text
使用 $mistake-collection 整理这些题目。
标题为“第十三章 简单电路”，建立“错题整理”文件夹。
给我纯题目版和答案解析版；黑色题目、红色答案，解析要详细。
简单图用 LaTeX 重绘，复杂图基于原图去除字迹并保持状态完全一致。
```

后续可以继续补充：

```text
把这几道大题追加进去。按初中生标准格式写步骤，
并在每一步旁边解释为什么这样做。
```

## 工作流程

1. 建立题目清单，确定每道题的准确边界。
2. 转录题干并逐字核对。
3. 为每幅图选择 TikZ 重绘或基于原图清理。
4. 独立求解并检查单位、方向、量程、节点和图示状态。
5. 生成纯题目版与答案解析版。
6. 检查纯题版没有任何教学提示或答案内容。
7. 编译、逐页渲染并与原始照片对照。

完整执行规则见 [SKILL.md](SKILL.md)。图像还原与答案编写规范分别见 [source-reconstruction.md](references/source-reconstruction.md) 和 [solution-writing.md](references/solution-writing.md)。

## 项目结构

```text
mistake-collection/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── mistake-collection-template.tex
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
