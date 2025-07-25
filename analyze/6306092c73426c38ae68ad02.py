def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    验证并打印已弃用的参数。

    :param cli_args: 来自命令行的参数字典
    :param answer_file_args: 来自文件的参数字典
    """
    deprecated_args = set(cli_args.keys()).intersection(set(answer_file_args.keys()))
    
    if deprecated_args:
        print("已弃用的参数:")
        for arg in deprecated_args:
            print(f"- {arg}")
    else:
        print("没有已弃用的参数。")