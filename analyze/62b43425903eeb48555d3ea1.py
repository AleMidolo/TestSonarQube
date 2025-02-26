import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    创建 in-style 参数的正则表达式。

    返回 in-style 参数的正则表达式 (:class:`re.Pattern`).
    """
    # Example implementation: matches a list of values separated by commas
    return re.compile(r'^\s*(\w+)(\s*,\s*\w+)*\s*$')