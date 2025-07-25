import re

def _get_resource_name_regex():
    """
    返回用于验证 Krake 资源名称的正则表达式  
    构建或返回用于验证 Krake 资源名称的正则表达式。

    返回值：  
        (re.Pattern)：编译后的正则表达式，用于验证资源名称。
    """
    # 假设资源名称只能包含字母、数字、下划线和连字符，且长度在1到63个字符之间
    pattern = r'^[a-zA-Z0-9_-]{1,63}$'
    return re.compile(pattern)