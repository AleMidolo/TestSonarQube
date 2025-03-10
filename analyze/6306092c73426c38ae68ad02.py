def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    验证并打印已弃用的参数。


    :param cli_args: 来自命令行的参数字典
    :param answer_file_args: 来自文件的参数字典
    """
    deprecated_args = {
        'old_arg1': 'new_arg1',
        'old_arg2': 'new_arg2',
        # Add more deprecated arguments and their replacements here
    }

    for arg in cli_args:
        if arg in deprecated_args:
            print(f"Warning: The argument '{arg}' is deprecated. Use '{deprecated_args[arg]}' instead.")

    for arg in answer_file_args:
        if arg in deprecated_args:
            print(f"Warning: The argument '{arg}' is deprecated. Use '{deprecated_args[arg]}' instead.")