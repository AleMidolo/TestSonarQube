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
    
    # 添加 "init" 子命令
    init_parser = subparsers.add_parser('init', help='初始化配置')
    init_parser.add_argument('--config', type=str, help='配置文件路径')
    
    # 添加 "run" 子命令
    run_parser = subparsers.add_parser('run', help='运行任务')
    run_parser.add_argument('--input', type=str, required=True, help='输入文件路径')
    run_parser.add_argument('--output', type=str, help='输出文件路径')
    
    # 解析参数
    args = parser.parse_args(unparsed_arguments if unparsed_arguments else None)
    
    # 创建返回字典
    result = {}
    
    # 添加全局参数
    result['global'] = args
    
    # 如果指定了子命令，添加子命令特定的参数
    if args.command:
        # 创建一个新的 Namespace 对象，只包含相关的参数
        command_args = argparse.Namespace()
        for key, value in vars(args).items():
            if key != 'command':
                setattr(command_args, key, value)
        result[args.command] = command_args
    
    return result