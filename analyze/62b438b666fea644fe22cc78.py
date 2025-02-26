import argparse

def parse_arguments(*arguments):
    """
    根据调用此脚本时提供的命令行参数，解析这些参数并将其作为一个 `ArgumentParser` 实例返回。
    """
    parser = argparse.ArgumentParser()
    
    # 添加一些常见的参数示例
    parser.add_argument('--input', type=str, help='输入文件路径')
    parser.add_argument('--output', type=str, help='输出文件路径')
    parser.add_argument('--verbose', action='store_true', help='启用详细输出')
    
    # 解析传入的参数
    parsed_args = parser.parse_args(arguments)
    
    return parsed_args