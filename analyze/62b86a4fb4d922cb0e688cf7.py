import re

class ValidationError(Exception):
    pass

def validate_key(key):
    """
    根据对应的正则表达式验证给定的键。

    参数:
        key: 要验证的字符串

    异常:
        ValidationError: 如果给定的键不符合正则表达式，则抛出此异常。
    """
    pattern = r'^[a-zA-Z0-9_]+$'  # 示例正则表达式，允许字母、数字和下划线
    if not re.match(pattern, key):
        raise ValidationError(f"Invalid key: {key}")