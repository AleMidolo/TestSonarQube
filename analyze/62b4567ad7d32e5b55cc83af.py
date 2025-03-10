import argparse

def parse_arguments(*arguments):
    """
    根据调用此脚本时提供的命令行参数，解析这些参数并将其作为一个 `ArgumentParser` 实例返回。
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # 假设我们解析一个简单的参数，例如 --input 和 --output
    parser.add_argument('--input', type=str, help='Input file path')
    parser.add_argument('--output', type=str, help='Output file path')
    
    # 将传入的参数列表转换为 argparse 可以解析的格式
    args = parser.parse_args(list(arguments))
    
    return args