import re

class ValidationError(Exception):
    pass

def validate_value(value):
    """
    根据对应的正则表达式验证给定的值。

    参数:
        value: 要验证的字符串

    异常:
        ValidationError: 如果给定的值不符合正则表达式，将抛出此异常。
    """
    pattern = r'^[a-zA-Z0-9_]+$'  # 示例正则表达式，允许字母、数字和下划线
    if not re.match(pattern, value):
        raise ValidationError(f"Value '{value}' does not match the required pattern.")