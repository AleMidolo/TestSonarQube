import argparse

def parse_arguments(*arguments):
    """
    根据调用此脚本时提供的命令行参数，解析这些参数并将其作为一个 `ArgumentParser` 实例返回。
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # 假设我们解析一个简单的参数 --input
    parser.add_argument('--input', type=str, help='Input file path')
    
    # 假设我们解析一个简单的参数 --output
    parser.add_argument('--output', type=str, help='Output file path')
    
    # 假设我们解析一个简单的参数 --verbose
    parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')
    
    # 解析传入的参数
    args = parser.parse_args(arguments)
    
    return args