import argparse

def parse_arguments(*arguments):
    """
    根据调用此脚本时提供的命令行参数，解析这些参数并将其作为一个 `ArgumentParser` 实例返回。
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # 添加一些示例参数
    parser.add_argument('-f', '--file', type=str, help="Path to the input file.")
    parser.add_argument('-o', '--output', type=str, help="Path to the output file.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Increase output verbosity.")
    
    # 解析参数
    args = parser.parse_args(arguments)
    
    return args