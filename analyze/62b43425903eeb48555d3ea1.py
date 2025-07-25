import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    创建 in-style 参数的正则表达式。

    返回 in-style 参数的正则表达式 (:class:`re.Pattern`).
    """
    # 假设 in-style 参数的格式为 "value1,value2,value3"
    # 我们将创建一个正则表达式来匹配这些值
    return re.compile(r'^(?P<value>[^,]+)(,(?P<value>[^,]+))*$')