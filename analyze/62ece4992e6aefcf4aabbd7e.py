def _resolve_string(matcher):
    """
    给定一个包含一个名称和一个可选的默认值（位于其分组字典中）的匹配器，从环境中获取值。
    如果环境中未定义该变量且未提供默认值，则会引发错误。

    给定一个包含一个名称和一个可选的默认值的匹配器，从环境中获取值。
    如果环境中未定义该变量且未提供默认值，则会引发错误。
    """
    name = matcher.group('name')
    default = matcher.group('default')
    
    # 尝试从环境变量中获取值
    value = os.environ.get(name)
    
    # 如果环境变量中没有该值
    if value is None:
        # 如果提供了默认值，则使用默认值
        if default is not None:
            return default
        # 如果没有提供默认值，则抛出错误
        else:
            raise KeyError(f"Environment variable '{name}' not found and no default value provided")
            
    return value