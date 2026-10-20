# 公开发布与许可证决策稿

## 建议方案

- **本研究独立新写的重建脚本和测试：**作者确认权利后采用 MIT License。
- **本研究原创稿件、表格、图和说明文档：**作者确认后采用 CC BY 4.0。
- **第三方数据、代码、权重、缓存、论文 PDF 和出版商补充材料：**不进入公开仓库，不由本项目再许可。
- **从无许可证上游 ncRD-LG 复制或改写的代码：**默认不公开、不再许可，除非权利人书面授权或完成可证明的独立重实现审查。

## 授权状态

作者已在本对话中要求执行既定的 MIT（独立代码）与 CC BY 4.0（原创稿件、图表和说明文档）方案。`release/LICENSE-CODE` 与 `release/LICENSE-DOCUMENTATION` 因此作为发布源文件建立。该授权只覆盖 Jihao Li 有权许可的独立原创材料，不改变任何第三方材料的许可证，也不覆盖从无许可证上游复制或改写的代码。

## 发布执行清单

1. 列出每个拟发布文件及权利来源；把 rights-clear 文件写入 release manifest。
2. 在独立公共仓库根目录放置 `LICENSE-CODE`、`LICENSE-DOCUMENTATION` 和 `THIRD_PARTY.md`。
3. 从 committed clean checkout 重建并核验 SHA-256 manifest。
4. 建立带版本号的 release；永久 DOI 仍需 Zenodo 等归档服务完成绑定。

## 当前结论

双许可方案已获作者执行授权。公开仓库、tag 和 clean-checkout 复现完成后方可填入稿件；GitHub URL/tag 不冒充 DOI。
