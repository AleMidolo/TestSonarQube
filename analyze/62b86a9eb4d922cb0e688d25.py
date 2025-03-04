def _get_resource_name_regex():
    """
    返回用于验证 Krake 资源名称的正则表达式  
    构建或返回用于验证 Krake 资源名称的正则表达式。

    返回值：  
        (re.Pattern)：编译后的正则表达式，用于验证资源名称。
    """
    import re
    
    # 资源名称规则:
    # - 必须以字母或数字开头和结尾
    # - 可以包含字母、数字、连字符(-)和点(.)
    # - 长度在1-253个字符之间
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9\-\.]{0,251}[a-zA-Z0-9]$'
    
    return re.compile(pattern)