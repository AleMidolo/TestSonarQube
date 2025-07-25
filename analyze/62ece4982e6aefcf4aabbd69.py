def _replace_register(flow_params, register_number, register_value):
    """
    将 `flow_params[register_number]` 的值替换为 `flow_params[register_value]`，并删除 `flow_params[register_value]`。
    
    将流中的值替换为指定的寄存器编号。

    在字典中，用 register_number 指定的寄存器号替换 register_value 键的值。

    :flow_params: 包含已定义流的字典
    :register_number: 用于存储值的寄存器编号
    :register_value: 将被寄存器编号替换的键
    """
    if register_value in flow_params:
        flow_params[register_number] = flow_params[register_value]
        del flow_params[register_value]