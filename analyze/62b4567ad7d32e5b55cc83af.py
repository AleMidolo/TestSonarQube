import argparse

def parse_arguments(*arguments):
    """
    根据调用此脚本时提供的命令行参数，解析这些参数并将其作为一个 `ArgumentParser` 实例返回。
    """
    parser = argparse.ArgumentParser()
    
    # 这里可以添加需要解析的参数
    # 例如：parser.add_argument('--example', help='这是一个示例参数')
    
    # 解析传入的参数
    parsed_args = parser.parse_args(arguments)
    
    return parsed_args