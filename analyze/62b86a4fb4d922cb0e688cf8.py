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
        'date': r'^\d{4}-\d{2}-\d{2}$',
        'time': r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
    }

    # 检查值是否为字符串
    if not isinstance(value, str):
        raise ValidationError("输入值必须是字符串类型")

    # 尝试匹配所有模式
    valid = False
    for pattern in patterns.values():
        if re.match(pattern, value):
            valid = True
            break
    
    if not valid:
        raise ValidationError(f"输入值 '{value}' 不符合任何有效格式")

    return True