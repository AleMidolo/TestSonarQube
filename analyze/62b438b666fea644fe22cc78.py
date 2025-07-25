import argparse

def parse_arguments(*arguments):
    """
    根据调用此脚本时提供的命令行参数，解析这些参数并将其作为一个 `ArgumentParser` 实例返回。
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # 添加一个示例参数
    parser.add_argument('--example', type=str, help='An example argument')
    
    # 解析传入的参数
    args = parser.parse_args(arguments)
    
    return args