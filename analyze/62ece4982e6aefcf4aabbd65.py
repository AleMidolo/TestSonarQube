def parser_flags(parser):
    """
    给定一个 `argparse.ArgumentParser` 实例，返回其参数标志（argument flags）组成的以空格分隔的字符串。

    参数：
      script：`argparse.ArgumentParser` 实例

    返回值：
      参数标志组成的以空格分隔的字符串
    """
    flags = []
    for action in parser._actions:
        if action.option_strings:
            flags.extend(action.option_strings)
    return ' '.join(flags)