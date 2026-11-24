# 资料字典

source_info.json 记录资料包版本和合成资料标记。events.json 中的 event_id、period、group 与 status 用于标识事件。entities.json 保存对象的稳定标识和当前可用状态。observations.json 以事件和对象关联观察值，value 可以为空，quality 区分完整、部分和缺失。

资料只用于本地可复现运行，后续功能应保留原始记录并让使用者能够查回采用的事实。
