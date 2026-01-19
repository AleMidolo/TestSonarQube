def validate_phone_number(self, phone_number):
    """
    验证电话号码是否有效
    :param phone_number: 待验证的电话号码
    :return: True 或 False，表示电话号码是否有效
    >>> ru = RegexUtils()
    >>> ru.validate_phone_number("123-456-7890")
    True
    """
    import re
    
    # 定义多种常见的电话号码格式
    patterns = [
        r'^\d{3}-\d{3}-\d{4}$',  # 123-456-7890
        r'^\(\d{3}\)\s?\d{3}-\d{4}$',  # (123) 456-7890 or (123)456-7890
        r'^\d{3}\.\d{3}\.\d{4}$',  # 123.456.7890
        r'^\d{10}$',  # 1234567890
        r'^\+?1?\s?\d{3}[\s.-]?\d{3}[\s.-]?\d{4}$',  # +1 123-456-7890, 1 123 456 7890, etc.
    ]
    
    for pattern in patterns:
        if re.match(pattern, phone_number):
            return True
    
    return False