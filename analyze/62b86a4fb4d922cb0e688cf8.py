def validate_value(value):
    """
    根据对应的正则表达式验证给定的值。

    参数:
        value: 要验证的字符串

    异常:
        ValidationError: 如果给定的值不符合正则表达式，将抛出此异常。
    """
    import re

    class ValidationError(Exception):
        pass

    # 定义正则表达式模式
    patterns = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'phone': r'^\+?1?\d{9,15}$',
        'url': r'^(http|https):\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}(\/\S*)?$',
        'date': r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$',
        'ipv4': r'^(\d{1,3}\.){3}\d{1,3}$'
    }

    # 检查值是否为字符串
    if not isinstance(value, str):
        raise ValidationError("输入值必须是字符串类型")

    # 检查值是否为空
    if not value.strip():
        raise ValidationError("输入值不能为空")

    # 尝试匹配所有模式
    valid = False
    for pattern_name, pattern in patterns.items():
        if re.match(pattern, value):
            valid = True
            break

    if not valid:
        raise ValidationError(f"输入值 '{value}' 不符合任何有效格式")

    return True