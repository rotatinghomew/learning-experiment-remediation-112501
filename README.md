# 普法唱词理解实验的分层推断与补训兑现

这是一个保存合成业务资料的 Python 项目。资料字段和状态含义来自 普法唱词理解实验的分层推断与补训兑现 的业务场景，读取层只负责加载原始记录并检查基本契约，业务判断、分析、状态联动和结果展示由后续开发完成。

资料位于 data/，source_info.json 标记资料性质，events.json 描述事件，entities.json 描述业务对象，observations.json 保存可以缺失的观察值。缺失值、部分质量和待处理状态都是资料含义的一部分。

运行基线测试：python3 -m unittest discover -s tests

检查 Python 文件可编译：python3 -m compileall src tests
