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
    parser.add_argument('--config', '-c', type=str, help='配置文件路径')
    
    # 创建子解析器
    subparsers = parser.add_subparsers(dest='command')
    
    # 添加 "init" 子命令
    init_parser = subparsers.add_parser('init', help='初始化配置')
    init_parser.add_argument('--force', '-f', action='store_true', help='强制初始化')
    
    # 添加 "run" 子命令
    run_parser = subparsers.add_parser('run', help='运行任务')
    run_parser.add_argument('--name', '-n', type=str, required=True, help='任务名称')
    run_parser.add_argument('--timeout', '-t', type=int, default=60, help='超时时间(秒)')
    
    # 解析参数
    args = parser.parse_args(unparsed_arguments if unparsed_arguments else None)
    
    # 创建返回字典
    result = {'global': args}
    
    # 如果指定了子命令，将其添加到结果字典中
    if args.command:
        result[args.command] = args
        
    return result