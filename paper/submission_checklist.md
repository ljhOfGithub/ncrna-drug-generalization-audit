# 投稿打包检查表

## 已完成并冻结

- [x] 条件性主线：固定普通 drug-cold 有增益，本次严格 scaffold-disjoint 未确认稳健增益。
- [x] 13 行主结果表及逐行来源路径。
- [x] 结论翻转主图、评估阶梯图和 captions。
- [x] 58/58 pilot 设计的运行/停止索引。
- [x] 简体中文完整事实稿、Highlights 源稿和 Cover Letter 源稿。
- [x] 可移植证据包、SHA-256 manifest 和 clean-room 核心重建。
- [x] 从 93 文件 manifest-only 干净目录重建 13 行主表/主图；14 项重建测试、22 项包内测试与全部哈希通过；主稿编译通过。
- [x] 第三方数据/代码不重新分发的边界。
- [x] 英文事实稿、英文 Highlights、英文 Cover Letter 和可编译单栏 LaTeX 投稿工程。
- [x] 10 篇直接相关引用逐条存在性/语境审计；错配的 MGCNA、PLMF-MDA 和 HMVCC 年份已修正。
- [x] 许可证推荐方案与不可再许可边界。

## 作者必须补齐

- [x] 单作者顺序、独立研究者单位、通讯作者已确认；ORCID 未公开核实，不填猜测编号。
- [x] 单作者 CRediT 贡献已确认。
- [x] 无专项基金、无利益冲突和伦理措辞已确认。
- [x] 稿件原创、未一稿多投，作者同意投稿。
- [x] 公共仓库、`v0.1.2` 版本标签和新增代码/文稿双许可证已确定。
- [ ] 永久归档 DOI（GitHub release 不是 DOI；无 DOI 时不得声称已有）。
- [x] 目标期刊暂锁定 `Pattern Recognition`，英文正文和方括号顺序编号格式已落盘。

## 英文终稿与格式

- [x] 将 `manuscript_zh_cn.md` 转为英文，不改变冻结数字和主张强度。
- [x] 从正式出版页面/PubMed 补齐 10 篇直接相关参考文献的完整作者、题名、卷期和文章号。
- [x] 逐条核验正文引用与参考文献对应关系；状态为 `same-family/provisional`。
- [x] 英文摘要 218 词，不超过 250 词；Keywords 为 6 个。
- [x] Highlights 为 5 条，每条 54–74 个字符，不超过 85 个字符。
- [x] 生成期刊要求的主稿、图、Highlights 和 Cover Letter 独立文件，并通过内置 LaTeX 编译。
- [ ] 继续按论断需要扩充并核验相关工作；当前 10 篇直接相关引用覆盖仍偏窄，但未核实到期刊官方存在“35--55 篇”数量要求，不能为凑数引入未读引用。
- [ ] 确认最终正文是否达到 20–35 页；内置编译通过，但当前工具未导出可由 `pdfinfo` 复核的 PDF。
- [x] 已删除基金、利益冲突、原创性和未一稿多投占位符。
- [ ] 按投稿系统要求核对匿名审稿并通读最终 PDF。

## 发布与复现

- [x] 通过独立发布 worktree 形成不吸收既有 tracked 修改的提交。
- [x] 按项目 Git 规则先 pull/rebase 最新 `origin/main`，再显式 `--no-ff` 合并。
- [x] 从 committed clean checkout 运行核心重建、22 项包内测试和 93 项 manifest 核验。
- [ ] 合法取得第三方材料后，按需运行 `--with-third-party-diagnostics`；默认 clean-room
      只重建主表/主图并哈希核验冻结统计表。
- [x] 投稿版本通过 Git tag 和 SHA-256 manifest 冻结。
- [ ] 补充可独立重建完整环境的锁文件；现有 `requirements-audit.txt` 只记录已验证环境。

## 上传前人工动作

技术投稿包和公共 release 已完成。上传前仍需按投稿系统要求选择匿名或实名文件、填写系统字段，并由作者通读最终 PDF。永久归档 DOI 尚未分配，不能把 GitHub tag 表述为 DOI。
