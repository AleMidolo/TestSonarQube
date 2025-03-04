def parse_arguments(*arguments):
    """
    根据调用此脚本时提供的命令行参数，解析这些参数并将其作为一个 `ArgumentParser` 实例返回。
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Command line argument parser')
    
    # Add arguments
    parser.add_argument('--input', '-i', type=str, help='Input file path')
    parser.add_argument('--output', '-o', type=str, help='Output file path')
    parser.add_argument('--verbose', '-v', action='store_true', help='Increase output verbosity')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    
    # Parse arguments
    if arguments:
        args = parser.parse_args(arguments)
    else:
        args = parser.parse_args()
        
    return args