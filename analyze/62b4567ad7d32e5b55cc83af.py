import argparse

def parse_arguments(*arguments):
    """
    根据调用此脚本时提供的命令行参数，解析这些参数并将其作为一个 `ArgumentParser` 实例返回。
    """
    parser = argparse.ArgumentParser()
    
    # 这里可以根据需要添加参数
    parser.add_argument('--example', type=str, help='示例参数')
    
    # 解析传入的参数
    parsed_args = parser.parse_args(arguments)
    
    return parsed_args