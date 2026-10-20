# ncRNA--药物泛化审计

本仓库是论文 *Drug-Cold Gains Do Not Persist under Scaffold Separation in ncRNA--Drug Prediction* 的冻结证据包。核心结论是条件性的：候选模型在固定普通 drug-cold 协议下有效，但该收益未在严格 scaffold-disjoint 条件下保持。

## 快速核验

```bash
python reproduce_paper_artifacts.py
python release_manifest.py
```

第一条命令从冻结 summary/config 重建 13 行主结果表、结论反转图并运行 14 项重建测试；第二条命令核验 93 个证据工件的 SHA-256。发布前的 clean-room 包另通过了 22 项包内测试。

- 完整范围与排除项：[`release/README.md`](release/README.md)
- 第三方边界：[`release/THIRD_PARTY.md`](release/THIRD_PARTY.md)
- 数据卡：[`release/DATA_CARD.md`](release/DATA_CARD.md)
- 英文投稿源码：[`submission-pattern-recognition/main.tex`](submission-pattern-recognition/main.tex)
- 结果冻结记录：[`paper/result_freeze_record.md`](paper/result_freeze_record.md)

仓库级 `README.md` 与 `.gitignore` 是托管元文件，不计入 `release/manifest.json` 的 93 个证据工件。

## 许可证

- 独立代码：MIT，见 [`release/LICENSE-CODE`](release/LICENSE-CODE)。
- 原创文稿、图和说明：CC BY 4.0，见 [`release/LICENSE-DOCUMENTATION`](release/LICENSE-DOCUMENTATION)。
- 第三方数据、代码、权重、缓存和论文不随本仓库再许可或重新分发。
