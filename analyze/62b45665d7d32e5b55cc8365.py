import argparse

def parse_arguments(*unparsed_arguments):
    """
    解析参数并将其作为字典映射返回

    给定调用该脚本时使用的命令行参数，解析这些参数并返回一个字典，该字典将子解析器名称（或 "global"）映射到相应的 argparse.Namespace 实例。
    """
    # 创建主解析器
    parser = argparse.ArgumentParser(description="主解析器")
    subparsers = parser.add_subparsers(dest="subparser_name", help="子解析器名称")

    # 添加全局参数
    parser.add_argument('--global-arg', type=str, help="全局参数")

    # 创建子解析器1
    parser_sub1 = subparsers.add_parser('sub1', help="子解析器1")
    parser_sub1.add_argument('--sub1-arg', type=str, help="子解析器1的参数")

    # 创建子解析器2
    parser_sub2 = subparsers.add_parser('sub2', help="子解析器2")
    parser_sub2.add_argument('--sub2-arg', type=int, help="子解析器2的参数")

    # 解析参数
    args = parser.parse_args(unparsed_arguments)

    # 根据子解析器名称返回相应的字典
    if args.subparser_name:
        return {args.subparser_name: args}
    else:
        return {'global': args}