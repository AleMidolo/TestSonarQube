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
    
    # 创建子解析器
    subparsers = parser.add_subparsers(dest='command', help='可用的子命令')
    
    # 添加 "init" 子命令
    init_parser = subparsers.add_parser('init', help='初始化配置')
    init_parser.add_argument('--config', type=str, help='配置文件路径')
    
    # 添加 "run" 子命令
    run_parser = subparsers.add_parser('run', help='运行任务')
    run_parser.add_argument('--input', type=str, required=True, help='输入文件路径')
    run_parser.add_argument('--output', type=str, help='输出文件路径')
    
    # 解析参数
    if len(unparsed_arguments) == 0:
        args = parser.parse_args()
    else:
        args = parser.parse_args(unparsed_arguments)
    
    # 创建返回字典
    parsed_args = {}
    
    # 添加全局参数
    parsed_args['global'] = argparse.Namespace(verbose=args.verbose)
    
    # 根据子命令添加特定参数
    if args.command == 'init':
        parsed_args['init'] = argparse.Namespace(config=args.config)
    elif args.command == 'run':
        parsed_args['run'] = argparse.Namespace(input=args.input, output=args.output)
        
    return parsed_args