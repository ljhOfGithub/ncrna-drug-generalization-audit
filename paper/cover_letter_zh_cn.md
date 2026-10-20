# Pattern Recognition Cover Letter 简体中文源稿

> 状态：事实和结构源稿；作者、单位、公开 URL 已记录，稿件编号与编辑姓名待投稿系统生成/指定，英文措辞仍需作者终审。

尊敬的编辑：

我们拟向 *Pattern Recognition* 提交 Original Article，工作标题为：
*When Gains under Drug-Cold Evaluation Do Not Persist under Scaffold Separation: A Conditional Study of ncRNA–Drug Association Prediction*。

本研究关注 ncRNA–药物关联预测中两个经常被混用的评估条件：固定普通 drug-cold
新药排序，以及训练与测试 Bemis–Murcko scaffold 完全隔离的新骨架评估。
在 RAHGL-MDR 公开数据的固定 drug-cold 折上，按药物均衡的 prior-residual 排序器在三个
训练种子中相对训练集 RNA 频率先验提高 `+0.013580` drug-macro AP，95% 区间为
`[+0.005139,+0.024170]`，五折均不下降。使用严格 scaffold-disjoint 五折后，增量缩小为
`+0.000296`，scaffold-cluster 95% 区间为 `[-0.007782,+0.008476]`，只有 `2/5` 折不下降。

稿件的贡献是条件性结论和评估边界，而不是普适新算法或跨协议 SOTA。普通 drug-cold 的
性能主张不能直接推广到新骨架，但本文也不声称证明所有新骨架条件下算法均无效。我们进一步在 Mi
严格 scaffold-cold 终点上比较 LocalGL、sChemNET 无序列消融和 PLMF-MDA 独立适配，
并审计 ncRNADrug 的跨库实体/正 pair 重叠、非 Mi 时间新药和不同 PMID 再支持标签。
结果一致表明，完整候选、强频率先验、scaffold 隔离和来源独立性会实质改变可支持的主张。

该工作与 *Pattern Recognition* 的关联在于：它研究表示与排序方法在分布变化下的可泛化
边界，提供共同终点、公开方法严格适配、不确定性估计和可复核证据包。稿件不会把未知关联
称为真实阴性，也不会把独立适配写成作者原模型复现。

作者确认：本稿为原创、未在其他期刊审理，且作者同意投稿。作者声明不存在利益冲突；本研究未获得公共、商业或非营利资助机构的专项基金资助。数据与代码的公开 URL：`https://github.com/ljhOfGithub/ncrna-drug-generalization-audit`；冻结版本：`v0.1.2`。独立代码采用 MIT，原创文稿/图采用 CC BY 4.0；尚未分配永久归档 DOI。

感谢审阅。

此致  
通讯作者：Jihao Li
单位：Independent Researcher, Shenzhen, Guangdong, China
电子邮箱：jihao.li@polyu.edu.hk
