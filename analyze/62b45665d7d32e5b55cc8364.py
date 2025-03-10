def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    给定一个参数序列和一个从子解析器名称到 argparse.ArgumentParser 实例的字典，让每个请求的操作的子解析器尝试解析所有参数。这允许共享常见参数（例如 --repository）给多个子解析器。

    将结果作为一个元组返回，其中包含一个将子解析器名称映射到其解析后的 argparse.Namespace 实例的字典和一个包含未被任何子解析器认领的剩余参数的列表。
    """
    parsed_results = {}
    remaining_args = list(unparsed_arguments)
    
    for subparser_name, parser in subparsers.items():
        try:
            # Try to parse the arguments with the current subparser
            parsed_args, remaining = parser.parse_known_args(unparsed_arguments)
            parsed_results[subparser_name] = parsed_args
            # Update the remaining_args to be the intersection of remaining_args and remaining
            remaining_args = list(set(remaining_args).intersection(remaining))
        except SystemExit:
            # If parsing fails, continue to the next subparser
            continue
    
    return parsed_results, remaining_args