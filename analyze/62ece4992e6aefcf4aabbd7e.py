def _resolve_string(matcher):
    """
    给定一个包含一个名称和一个可选的默认值（位于其分组字典中）的匹配器，从环境中获取值。
    如果环境中未定义该变量且未提供默认值，则会引发错误。

    给定一个包含一个名称和一个可选的默认值的匹配器，从环境中获取值。
    如果环境中未定义该变量且未提供默认值，则会引发错误。
    """
    import os

    name = matcher.group('name')
    default_value = matcher.group('default', None)

    value = os.getenv(name, default_value)

    if value is None:
        raise ValueError(f"Environment variable '{name}' is not defined and no default value provided.")

    return value