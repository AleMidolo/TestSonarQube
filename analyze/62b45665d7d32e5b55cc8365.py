def parse_arguments(*unparsed_arguments):
    """
    解析参数并将其作为字典映射返回

    给定调用该脚本时使用的命令行参数，解析这些参数并返回一个字典，该字典将子解析器名称（或 "global"）映射到相应的 argparse.Namespace 实例。
    """
    import argparse

    # 创建主解析器
    parser = argparse.ArgumentParser(description='命令行参数解析器')
    
    # 添加全局参数
    parser.add_argument('--verbose', '-v', action='store_true', help='启用详细输出')
    
    # 创建子解析器
    subparsers = parser.add_subparsers(dest='command')
    
    # 添加 "add" 子命令
    add_parser = subparsers.add_parser('add', help='添加操作')
    add_parser.add_argument('numbers', nargs='+', type=float, help='要相加的数字')
    
    # 添加 "multiply" 子命令
    multiply_parser = subparsers.add_parser('multiply', help='乘法操作')
    multiply_parser.add_argument('numbers', nargs='+', type=float, help='要相乘的数字')
    
    # 解析参数
    if unparsed_arguments:
        args = parser.parse_args(unparsed_arguments)
    else:
        args = parser.parse_args()
        
    # 创建返回字典
    result = {'global': args}
    
    # 如果指定了子命令，将其添加到结果字典中
    if hasattr(args, 'command') and args.command:
        result[args.command] = args
        
    return result