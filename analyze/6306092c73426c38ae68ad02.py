def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    验证并打印已弃用的参数。

    :param cli_args: 来自命令行的参数字典 
    :param answer_file_args: 来自文件的参数字典
    """
    # 合并两个参数字典
    all_args = {**cli_args, **answer_file_args}
    
    # 已弃用参数列表
    deprecated_args = {
        'old_param1': 'new_param1',
        'old_param2': 'new_param2',
        'old_param3': None  # 完全弃用,无替代参数
    }
    
    # 检查弃用参数
    for old_arg, new_arg in deprecated_args.items():
        if old_arg in all_args:
            if new_arg:
                warning_msg = (f"Warning: Parameter '{old_arg}' is deprecated. "
                             f"Please use '{new_arg}' instead.")
            else:
                warning_msg = f"Warning: Parameter '{old_arg}' is deprecated and will be removed."
                
            print(warning_msg)