import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    创建 in-style 参数的正则表达式。

    返回 in-style 参数的正则表达式 (:class:`re.Pattern`).
    """
    # 假设 in-style 参数的格式为 "value1,value2,value3"
    # 我们将创建一个正则表达式来匹配这些值
    values = r'([^,]+)'  # 匹配非逗号的字符
    regex_pattern = rf'^{values}(,{values})*$'  # 完整的 in-style 正则表达式
    return re.compile(regex_pattern)