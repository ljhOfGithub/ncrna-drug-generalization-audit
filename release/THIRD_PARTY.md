# 第三方材料与许可边界

## 保守发布规则

本证据包不携带第三方原始数据、模型权重、缓存仓库或论文 PDF。公开 release 只应包含我们新增且权利清晰的代码、测试、聚合 summary、表格、图和获取说明；第三方材料由使用者从官方入口自行取得并核对哈希。

## 已核实边界

- 上游 `Biology-Lab/ncRD-LG` 当前 checkout 与文件树中未发现 `LICENSE`、`COPYING` 或等价许可证文件。因此不能把“GitHub 可见”解释为允许复制、修改或再许可。
- RAHGL-MDR、HMVCC、MGCNA、PLMF-MDA 的仓库只作为固定身份和方法核验来源；除非逐仓库确认许可证，否则不纳入本包。PLMF-MDA 固定提交为 `effabcb59f361a07ff5c1bc92158a3e8f7582f52`，仓库与 GitHub 元数据均未给出许可证；随仓库提供的 `DeepChem/ChemBERTa-77M-MLM` checkpoint 也不进入 release。
- RNA-FM 源码固定提交 `348951516e0963d22bbb33b3c9fc18c89081d38e`，上游仓库含 MIT 许可证。作者 README 指向 Hugging Face `cuhkaih/rnafm`；本地使用的权重必须固定仓库 revision 并核对 SHA-256，但 1.19 GB checkpoint 和任何生成缓存均不进入 release。源码许可、模型仓库标注的权重许可和下游数据许可分别记录，不能互相替代。
- 本地的 PLMF-MDA 严格协议适配器复用了论文/公开实现中特定的 69 维原子词表、四分支结构与单 token attention 设计；在取得权利人许可或完成明确的独立实现发布审查前，只限本地研究使用，不纳入公开 release manifest，也不称为 rights-clear。release 只纳入本研究生成的 `summary.json` 聚合数值，以支持主表复算；不纳入适配器源码、特征生成器、权重、冻结特征、逐药物预测或第三方仓库内容。
- sChemNET 官方仓库固定提交 `66c0c880c3477270a77dad412a05a8415a89d3a7` 只用于方法与数据格式核验；仓库未见许可证，`third_party/sChemNET` 不运行、不复制到 release，也不把本研究的独立无序列重实现表述为上游授权派生物。
- SM2miR、CTD、ncRNADrug、NoncoRNA、DrugBank、miRBase 与 PRISM 的内容和条款各自独立；本包不替它们授予任何权利。
- GEO `GSE70138` 与 `GSE92742` 的 LINCS 元数据只用于本地覆盖门；压缩文件和任何未来表达矩阵都不进入 release。
- 出版商 HTML/PDF 仅用于阅读和事实核验，不进入代码/数据 release。

## 发布前必须完成

1. 由权利人确认 ncRD-LG 派生代码的可发布范围，或把全部新增实现迁移到不复制上游代码的独立仓库。
2. 由作者为本研究新增代码选择明确许可证；本文件不擅自替作者选择。
3. 对每个下载脚本保留官方 URL、访问日期、版本/提交和 SHA-256；遇到登录、CAPTCHA 或付费墙不得绕过。
4. 在公开仓库中排除 `.cache/`、checkpoint、数据库原始文件和临时 clone。
