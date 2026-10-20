# 硬件与运行时间记录

## 当前执行环境

- 机器：MacBook Pro（`MacBookPro18,2`）。
- 芯片：Apple M1 Max，10 核 CPU（8 个性能核、2 个能效核），32 核集成 GPU。
- 内存：64 GB unified memory。
- 深度学习设备：正式 LocalGL 与 RAHGL 训练使用 PyTorch MPS；测试与轻量审计使用 CPU。
- 隐私边界：不记录设备序列号、硬件 UUID、Provisioning UDID 或账户信息。

## 可复核 wall-clock

| 项目 | 范围 | 设备 | 实测 wall-clock | 状态与用途 |
|---|---|---|---:|---|
| 全量测试 | 179 个 pytest 测试 | CPU | `65.15 s` | 完成；7 条已知 warning |
| release 清单测试 | 3 个 manifest 测试 | CPU | `0.06 s` | 完成；只验证清单逻辑 |
| LocalGL recovery smoke | fold 0、2 epochs、最多 600 train pairs、每轮重采样 | CPU | `19.8 s` | 仅运行性检查，不进入论文结果 |
| LocalGL 首次正式单进程尝试 | fold 0 在内存中完成、fold 1 进入 epoch 2，但未落盘 | MPS | `4847.51 s` | 外部信号异常终止；不是结果，也不能当完整运行估时 |
| LocalGL 分折正式运行 | 5 个独立 40-epoch folds、每轮重采样 | MPS | `4716.75/3648.02/2675.91/2627.07/2541.18 s`；合计 `16208.93 s` | 五折全部完成并聚合；动态敏感性进入主结果 |
| PLMF-MDA 独立严格适配 | 3 seeds × 5 folds、最多 80 epochs、patience 15、pair batch 32 | CPU | `9099 s` | 15/15 完成；由输出目录创建至完整 summary 写入的文件系统时间差，不是脚本内置计时器 |
| RAHGL 三种子确认 | 3 seeds × 5 folds | MPS | 未记录 | 结果有效，但需在 clean reproduction 中补测时间 |

## 可报告边界

- 不用失败进程的 `4847.51 s` 外推五折总时间，因为它包含两个折的不同完成比例且没有输出 checkpoint。
- 不用 smoke 的小样本 CPU 时长推算正式 MPS 运行。
- 当前表已补齐 LocalGL 五折完整训练时间，并记录 PLMF 正式运行的可复核文件系统观测区间；RAHGL clean rerun 和端到端证据包复现时间仍是投稿前待补项。

CSV 同源表：`runtime_hardware.csv`。
