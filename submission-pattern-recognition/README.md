# Pattern Recognition 投稿目录

## 文件

- `main.tex`：单栏、双倍行距英文主稿；内置编译器已于 2026-10-20 编译通过。
- `references.bib`：7 篇已核验核心引用的投稿副本；权威来源是 `../paper/references_verified.bib`。
- `highlights.txt`：5 条 Highlights，每条 54–74 个字符，均不超过 85 字符。
- `cover_letter.tex`：按期刊要求回答 SOTA/五篇代表作、公共数据集和验证指标。
- `figures/`：两张冻结图的投稿副本。

## 上传前仍需人工核对

1. 作者姓名、独立研究者单位、深圳地点、通讯作者、CRediT、伦理、基金和利益冲突措辞均已确认；ORCID 未公开核实，因此不填猜测编号。
2. 公共仓库、`v0.1.2` release 和双许可证已确定；永久归档 DOI 尚未分配，不能把 GitHub tag 表述为 DOI。
3. 当前 10 篇直接相关引用已经核验，相关工作覆盖仍偏窄；未核实到期刊存在“35–55 篇”的硬性数量要求，不为凑数加入未读文献。
4. 上传前需按投稿系统要求选择匿名稿或实名稿，并由作者通读最终 PDF。
5. 上游 ncRD-LG 未发现许可证，不能把其代码、原始数据、权重或缓存并入本 release。

## 编译

本目录已使用 Codex 内置 LaTeX 编辑器编译 `main.tex` 成功。投稿时提交 `.tex`、`.bib`、图文件、Highlights 和 Cover Letter；PDF 只用于审阅，不作为可编辑源文件。
