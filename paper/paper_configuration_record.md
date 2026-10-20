# 论文配置记录

状态：`scope_frozen_submission_draft_compiled`  
更新日期：2026-10-20

## 建议配置

| 项目 | 建议值 | 状态/依据 |
|---|---|---|
| 稿件类型 | Original Article；条件性方法贡献＋评估协议论文 | 已冻结，不包装成普适新算法 |
| 目标期刊 | Pattern Recognition | 工作目标；官方 scope 与格式见 `venue_fit_pattern_recognition.md` |
| 当前事实稿语言 | 简体中文 + 英文 | 中文保留为权威事实源；英文投稿稿已转换并需作者终审 |
| 投稿语言 | 英文 | 已落盘并通过内置 LaTeX 编译 |
| 引用格式 | 方括号顺序编号，按出现顺序排列 | 已按期刊格式落盘 |
| 篇幅 | 20–35 页，单栏双倍行距初稿 | 期刊官方要求 |
| 摘要 | ≤250 词 | 期刊官方要求 |
| Keywords | 1–7 个英文关键词 | 期刊官方要求 |
| Highlights | 3–5 条，每条 ≤85 字符 | 期刊官方要求，单独文件 |
| 工作标题 | *Drug-Cold Gains Do Not Persist under Scaffold Separation in ncRNA–Drug Prediction* | 11 词短标题；与冻结的条件性贡献一致；尚未做标题碰撞终查 |
| 核心贡献 | 固定普通 drug-cold 有增益，但本次严格 scaffold 评估未确认稳健增益；统一审计框架；可复核证据包 | 已冻结 |
| 非贡献 | 新模型 SOTA；跨数据库普适；完整 sChemNET 胜负；因果生物机制 | 现有证据不支持 |
| 作者/单位/通讯作者 | TBD | 不推测 |
| 基金/利益冲突/数据与代码最终 URL | TBD | 提交前必须由作者确认 |

## 当前写作边界

目标期刊、英文正文和顺序编号格式已按 `Pattern Recognition` 落盘。当前只保留真实阻断：

1. 作者、单位、CRediT、基金、利益冲突和伦理措辞；
2. 公开仓库、版本标签、永久归档和许可证授权；
3. 35–55 篇建议参考文献覆盖及逐条核验；
4. 20–35 页最终页数与匿名/实名文件要求；
5. committed clean checkout 的复现和 release 哈希。

这些阻断不影响继续审阅英文稿，但未解决前不得称“可直接上传”。
