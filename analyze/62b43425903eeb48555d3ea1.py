import re

def _create_in_regex(self) -> Pattern:
    """
    创建 in-style 参数的正则表达式。

    返回 in-style 参数的正则表达式 (:class:`re.Pattern`)。
    """
    # 假设 in-style 参数的形式为 "in:value1,value2,value3"
    pattern = r"in:([^,]+(?:,[^,]+)*)"
    return re.compile(pattern)