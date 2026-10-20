# 论文证据工件包

本目录定义的是可公开审查的**论文证据工件包**，不是完整训练数据或所有探索实验的镜像。目标是让审稿人从冻结的小型 summary/config 输入重建论文主结果表、数据/协议统计、案例表和结论反转图，同时保留每一行结果的来源路径。

## 包含范围

- 17 个确认性实验的冻结 summary/config；
- 主表、数据/协议统计、规则选取的案例表；
- 结论反转森林图和评估阶梯图；
- 五篇全文近邻的协议比较；
- 七个公开方法族的证据等级、严格协议适配状态与不可比原因；
- 覆盖 58/58 个 pilot 设计的运行/停止决策索引，其中 target-to-regulator 在模型前由用户冻结；完整性测试依赖未公开的探索设计与完整日志，仅在内部全库运行，不纳入 clean-room 包；
- 隐私安全的硬件信息、可复核 wall-clock 与明确的未测时长边界；
- 重建脚本、专项测试、环境版本、主张审计和 SHA-256 清单。
- 数据卡、第三方许可边界与版本/纠错/退役维护策略。
- 结果冻结记录与简体中文论文事实稿。
- 中英文事实稿、Highlights、Cover Letter、核心引用审计、许可证决策稿和可编译 LaTeX 投稿工程。

## 不包含范围

- ncRD-LG 上游仓库的原始数据、预训练权重和代码副本；
- ncRNADrug、NoncoRNA、SM2miR、CTD、DrugBank、miRBase、PRISM 等第三方原始文件；
- Hugging Face 模型缓存、临时 Git clone、完整失败实验输出和模型 checkpoint；
- 前瞻性实验或生物学验证。

## 本地重建

使用项目共享环境时：

```bash
/Users/jackie/Documents/Git/.venv/bin/python reproduce_paper_artifacts.py
/Users/jackie/Documents/Git/.venv/bin/python release_manifest.py
```

第一条命令在不包含第三方原始数据的干净证据包中重建 13 行主结果表和结论翻转图，运行可移植专项测试，并检查资源统计/案例表等冻结输出存在；第二条命令核验所有声明文件与 `manifest.json` 的 SHA-256 是否一致。具体文件数以清单的 `file_count` 为准。

资源统计和 RAHGL 案例表依赖未随包分发的 `Dataset/`、RAHGL 缓存及逐药物文件。合法取得 `THIRD_PARTY.md` 所列材料后，才运行：

```bash
/Users/jackie/Documents/Git/.venv/bin/python reproduce_paper_artifacts.py --with-third-party-diagnostics
```

这会额外重建 7 行资源统计和 3 个规则选取案例并运行其测试。默认 clean-room 成功不等于第三方数据或完整训练已从零复现。

## 当前状态

`v0.1.0` 包只包含权利边界清晰的独立工件。发布前的 manifest-only 干净目录完成了 13 行主表、主图、14 项重建测试、22 项包内测试和全部 93 个受管理文件哈希核验；投稿主稿也由桌面编辑器编译通过。独立代码采用 MIT，原创文稿、图和说明采用 CC BY 4.0。原作者仓库未发现许可证文件，因此其代码、原始数据、权重与缓存均不进入本 release。公共仓库为 `https://github.com/ljhOfGithub/ncrna-drug-generalization-audit`；GitHub 标签不是永久归档 DOI。

## 冻结边界

本包冻结的论文主线是：方法在原始普通 drug-cold 数据分布中有效，但该优势未在严格
scaffold-disjoint 协议中保持。包内不得加入冻结日期后的新候选、新训练结果或事后调参结果；
允许的更新仅限纠错、引用、文稿、图表、测试、哈希和复现记录。
