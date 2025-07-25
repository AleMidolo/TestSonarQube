def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    验证并打印已弃用的参数。

    :param cli_args: 来自命令行的参数字典 
    :param answer_file_args: 来自文件的参数字典
    """
    # 合并两个参数字典
    all_args = {**cli_args, **answer_file_args}
    
    # 已弃用参数列表
    deprecated_args = [
        ('old_param', 'new_param'),
        ('legacy_flag', 'modern_flag'),
        # 可以添加更多已弃用的参数对
    ]
    
    # 检查每个已弃用的参数
    for old_arg, new_arg in deprecated_args:
        if old_arg in all_args:
            print(f"Warning: Parameter '{old_arg}' is deprecated. "
                  f"Please use '{new_arg}' instead.")
            
            # 如果新参数未设置,则将旧参数的值复制给新参数
            if new_arg not in all_args:
                all_args[new_arg] = all_args[old_arg]
                
            # 从参数字典中删除旧参数
            if old_arg in cli_args:
                del cli_args[old_arg]
            if old_arg in answer_file_args:
                del answer_file_args[old_arg]