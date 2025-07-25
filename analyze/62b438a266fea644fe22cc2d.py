def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    给定一个参数序列和一个从子解析器名称到 argparse.ArgumentParser 实例的字典，让每个请求的操作的子解析器尝试解析所有参数。这允许共享常见参数（例如 --repository）给多个子解析器。

    将结果作为一个元组返回，其中包含一个将子解析器名称映射到其解析后的 argparse.Namespace 实例的字典和一个包含未被任何子解析器认领的剩余参数的列表。
    """
    import argparse

    results = {}
    remaining_args = unparsed_arguments

    for name, parser in subparsers.items():
        try:
            # Try to parse the arguments for the current subparser
            parsed_args, remaining_args = parser.parse_known_args(remaining_args)
            results[name] = parsed_args
        except SystemExit:
            # Handle the case where parsing fails
            continue

    return results, remaining_args