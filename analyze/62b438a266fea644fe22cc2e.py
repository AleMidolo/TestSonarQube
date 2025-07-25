def parse_arguments(*unparsed_arguments):
    """
    给定调用此脚本时提供的命令行参数，解析这些参数并返回一个字典。
    该字典将子解析器名称（或 "global"）映射到一个 argparse.Namespace 实例。
    """
    import argparse

    # 创建主解析器
    parser = argparse.ArgumentParser(description='命令行参数解析器')
    
    # 添加全局参数
    parser.add_argument('--verbose', '-v', action='store_true', help='启用详细输出')
    parser.add_argument('--config', '-c', type=str, help='配置文件路径')
    
    # 创建子解析器
    subparsers = parser.add_subparsers(dest='command')
    
    # 添加 "init" 子命令
    init_parser = subparsers.add_parser('init', help='初始化配置')
    init_parser.add_argument('--force', '-f', action='store_true', help='强制初始化')
    
    # 添加 "run" 子命令
    run_parser = subparsers.add_parser('run', help='运行程序')
    run_parser.add_argument('--input', '-i', required=True, help='输入文件')
    run_parser.add_argument('--output', '-o', required=True, help='输出文件')
    
    # 解析参数
    if len(unparsed_arguments) == 0:
        args = parser.parse_args()
    else:
        args = parser.parse_args(unparsed_arguments)
    
    # 创建返回字典
    result = {'global': args}
    
    # 如果指定了子命令，将其参数添加到字典中
    if args.command:
        # 创建一个新的 Namespace 对象，只包含子命令的参数
        sub_args = argparse.Namespace()
        for key, value in vars(args).items():
            if key != 'command':
                setattr(sub_args, key, value)
        result[args.command] = sub_args
    
    return result