def _dump_string(obj, dumper=None):
    """
    给定一个 Python 对象并将其序列化为 YAML 流

    参数：
        obj：Python 对象

    返回值：
        YAML 流

    将对象转储为 Python 2 的 Unicode 字符串或 Python 3 的字符串。
    """
    import yaml

    if dumper is None:
        dumper = yaml.Dumper

    return yaml.dump(obj, Dumper=dumper, allow_unicode=True)