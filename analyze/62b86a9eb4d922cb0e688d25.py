import re

def _get_resource_name_regex():
    """
    返回用于验证 Krake 资源名称的正则表达式  
    构建或返回用于验证 Krake 资源名称的正则表达式。

    返回值：  
        (re.Pattern)：编译后的正则表达式，用于验证资源名称。
    """
    # 假设资源名称由小写字母、数字和连字符组成，且长度在1到63个字符之间
    pattern = r'^[a-z0-9-]{1,63}$'
    return re.compile(pattern)