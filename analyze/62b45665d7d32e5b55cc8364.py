def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    给定一个参数序列和一个从子解析器名称到 argparse.ArgumentParser 实例的字典，让每个请求的操作的子解析器尝试解析所有参数。这允许共享常见参数（例如 --repository）给多个子解析器。

    将结果作为一个元组返回，其中包含一个将子解析器名称映射到其解析后的 argparse.Namespace 实例的字典和一个包含未被任何子解析器认领的剩余参数的列表。
    """
    parsed_args = {}
    remaining_args = list(unparsed_arguments)
    
    # 遍历每个子解析器
    for name, subparser in subparsers.items():
        try:
            # 尝试用当前子解析器解析所有参数
            # parse_known_args() 返回一个包含已知参数的命名空间和未知参数列表的元组
            namespace, unknown = subparser.parse_known_args(remaining_args)
            parsed_args[name] = namespace
            remaining_args = unknown
        except:
            # 如果解析失败，继续尝试下一个子解析器
            continue
            
    return parsed_args, remaining_args