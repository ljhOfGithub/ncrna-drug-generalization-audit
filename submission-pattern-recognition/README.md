# Pattern Recognition 投稿目录

## 文件

- `main.tex`：单栏、双倍行距英文主稿；内置编译器已于 2026-10-20 编译通过。
- `references.bib`：7 篇已核验核心引用的投稿副本；权威来源是 `../paper/references_verified.bib`。
- `highlights.txt`：5 条 Highlights，每条 54–74 个字符，均不超过 85 字符。
- `cover_letter.tex`：按期刊要求回答 SOTA/五篇代表作、公共数据集和验证指标。
- `figures/`：两张冻结图的投稿副本。

## 尚不能上传的原因

1. 作者姓名、独立研究者单位、深圳地点、通讯作者、CRediT 和伦理措辞已记录；ORCID 未公开核实，基金和利益冲突仍待作者确认。
2. 公共仓库、`v0.1.1` release 和双许可证已确定；永久归档 DOI 尚未分配。
3. 当前正文仅引用 7 篇核心文献，低于 Guide for Authors 建议的 35–55 篇；不得为凑数加入未核验文献。
4. 当前工作树尚未形成不吸收既有 tracked 修改的干净提交，也未从 committed clean checkout 复现。
5. 上游 ncRD-LG 未发现许可证，不能把其代码或派生部分重新许可。

## 编译

本目录已使用 Codex 内置 LaTeX 编辑器编译 `main.tex` 成功。投稿时提交 `.tex`、`.bib`、图文件、Highlights 和 Cover Letter；PDF 只用于审阅，不作为可编辑源文件。
