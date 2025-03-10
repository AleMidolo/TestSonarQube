def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    验证并打印已弃用的参数。


    :param cli_args: 来自命令行的参数字典
    :param answer_file_args: 来自文件的参数字典
    """
    deprecated_args = set(cli_args.keys()).intersection(answer_file_args.keys())
    for arg in deprecated_args:
        print(f"警告: 参数 '{arg}' 已被弃用，建议使用来自文件的参数。")