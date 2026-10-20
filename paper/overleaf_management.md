# Overleaf 统一管理记录

## 当前项目

- Overleaf 项目：<https://www.overleaf.com/project/6ad7141f64fe08d0dafd2f16>
- 项目标题：`Drug-Cold Gains Do Not Persist under Scaffold Separation in ncRNA–Drug Prediction`
- 建立日期：2026-10-20
- 上传来源：`submission-pattern-recognition/`
- 主文档：`main.tex`
- 云端状态：Overleaf 自动选中 `main.tex`，编译成功，PDF 预览为 25 页。
- 当前页数边界：25 页位于期刊普通论文建议的 20–35 页范围内；正文实际引用 35 篇，达到作者指南请求的 35–55 篇下限。

## 唯一权威副本规则

从本记录建立后，**Overleaf 是协作写作期间的权威投稿副本**。本地
`submission-pattern-recognition/` 是审计、测试和重建镜像，不应与 Overleaf 同时编辑。

每轮操作只能选择一个方向：

1. **Overleaf → 本地：**暂停网页编辑，下载 Overleaf source ZIP；先比较差异，再把通过审查的文件同步到本地。数字、结论或引用变化分别重新运行 claim/citation audit。
2. **本地 → Overleaf：**先确认 Overleaf 自上次下载后没有新修改；本地编译和测试通过后，只上传经过审查的变更文件。不得通过新建第二个项目掩盖分叉。

## 当前同步能力

Overleaf 页面显示当前账户为 Free plan。官方 Git bridge 属于 Premium 能力，因此本轮采用官方
`New project → Existing project (.zip)` 上传路径建立项目，尚不是自动双向 Git 同步。

若未来启用 Premium，应按 `overleaf-sync` Skill 建立独立 `paper-overleaf/` clone：认证令牌只能由用户在自己的交互式终端输入并存入 macOS Keychain，不得进入聊天、环境变量、Git remote URL 或仓库文件。每次 push 前必须先 pull、检查差异并确认没有远端漂移。

## 本轮浏览器成功路径

- 浏览器：系统 Chrome，默认用户目录，普通标签页。
- 登录状态：已登录既有 Overleaf 账户；未新建账户、未输入或提交密码/令牌。
- 路径：`Your projects → New project → Existing project (.zip) → 选择本地 ZIP`。
- 上传结果：根目录包含 `main.tex`、`references.bib`、`cover_letter.tex`、`highlights.txt`、`README.md` 和 `figures/`；云端显示 16 页 PDF。
- 成功截图：`paper/overleaf_project_20261020.jpg`。
- 未使用：Codex 内置浏览器、Edge、调试端口 Chrome、新 profile、CAPTCHA 绕过或 Git token。

## 作者元数据浏览器核验（2026-10-20）

- 浏览器：系统 Chrome，默认用户目录，普通标签页；Google 只用于一次精确定位，最终证据回到 PolyU 与 arXiv 官方页面。
- PolyU IHERD `Research & Project Staff` 页面列出 `Mr Jackie LI`、职务 `Project Associate`、邮箱 `jihao.li@polyu.edu.hk` 和办公室 `BC621`。
- arXiv:2608.12857v1 官方 HTML 列出作者 `Jihao Li`、单位 `Institute for Higher Education Research and Development`、机构 `The Hong Kong Polytechnic University, Hong Kong, China`，并给出同一邮箱。
- PolyU 官方联系页面与多个 PolyU 单位联系页支持机构地址写作 `The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong`；稿件同时保留经人员页核实的办公室 `BC621`。
- 精确检索出现多个同名 ORCID，无法唯一归属于本作者；稿件不填猜测编号。
- 作者随后明确指定本稿署名为 `Independent Researcher, Shenzhen, Guangdong, China`；PolyU/IHERD 页面仅保留为姓名与邮箱核验来源，不作为本稿单位。
- 未提交表单、账号凭据或个人文件；未使用内置浏览器、Edge、调试端口或新 profile。

## 投稿文件回传与云端编译（2026-10-20）

- 浏览器：系统 Chrome，默认用户目录，普通标签页；复用既有 Overleaf 项目 `6ad7141f64fe08d0dafd2f16`，未新建第二个项目。
- 在文件树使用 `Upload` → `Select files`，一次选择本地 `main.tex`、`references.bib`、`cover_letter.tex`，在 Overleaf 明确列出同名文件后选择 `Overwrite`。
- 上传完成后重新编译并刷新同一项目页。云端源码与 PDF 均显示 `Jihao Li`、`Independent Researcher, Shenzhen, Guangdong, China`；旧的作者/单位占位符已消失。
- 首次同步后云端主稿为 16 页；补齐 3 条数据资源引用并发布一致性补丁后，再次覆盖 `main.tex` 和 `cover_letter.tex`，云端 PDF 成功更新为 17 页。云端源码/PDF 保持 `Jihao Li` 与 `Independent Researcher, Shenzhen, Guangdong, China`，旧作者占位符为零。公开代码地址已写入本地主稿，当前 GitHub release 为 `v0.1.2`；未把 GitHub tag 表述为归档 DOI。
- 未提交密码或其他表单；未使用内置浏览器、Edge、调试端口或新 profile。

## 作者声明终稿同步（2026-10-20）

- 浏览器：系统 Chrome 默认用户目录、既有普通标签页；复用 Overleaf 项目 `6ad7141f64fe08d0dafd2f16`，未新建项目。
- 在 `Upload` 面板一次选择公共 release 中的 `main.tex` 与 `cover_letter.tex`，核对同名文件后执行 `Overwrite`；上传结束后确认 `Document Updated Externally` 提示并重新编译。
- 云端源码搜索确认：`v0.1.2` 为 `2/2` 命中；主稿包含 `The author declares no competing interests.` 与无专项基金声明；Cover Letter 包含原创、未在其他期刊审理、单作者同意投稿的确认。
- 新编译生成了新的 PDF build，预览仍为 17 页；首页显示 `Jihao Li` 与 `Independent Researcher, Shenzhen, Guangdong, China`。
- 本轮只同步作者声明、投稿状态和版本链接；没有新增实验、训练、下载、调参或冻结数字变更。

## v0.1.3 投稿终稿同步（2026-10-20）

- 浏览器：系统 Chrome 默认用户目录、既有普通标签页；复用同一 Overleaf 项目，未新建项目、profile 或调试端口。
- 依次覆盖上传 `main.tex`、`references.bib`、`cover_letter.tex` 与 `README.md`；没有提交密码、令牌或其他表单。
- 云端重新编译成功，PDF 为 25 页；编译日志为 0 errors、0 warnings，另有 1 条不阻断排版信息：第 108--119 行段落存在 `Overfull \\hbox`。
- 云端源码与 PDF 保留实名作者 `Jihao Li`、单位 `Independent Researcher, Shenzhen, Guangdong, China`，符合当前单盲投稿流程；版本链接为 `v0.1.3`。
- 本轮只扩充相关工作、方法协议说明和已核验引用，没有新增实验、训练、下载、调参或改变冻结结果。
- 成功截图：`/Users/jackie/.codex/visualizations/2026/10/19/01a1523e-45ec-7e03-b2b8-c21afd885560/overleaf-v013-25-pages.png`。
