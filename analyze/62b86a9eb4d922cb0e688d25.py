import re

def _get_resource_name_regex():
    """
    返回用于验证 Krake 资源名称的正则表达式  
    构建或返回用于验证 Krake 资源名称的正则表达式。

    返回值：  
      (re.Pattern)：编译后的正则表达式，用于验证资源名称。
    """
    # 定义资源名称的正则表达式
    pattern = r'^[a-zA-Z0-9-_]{1,64}$'
    return re.compile(pattern)