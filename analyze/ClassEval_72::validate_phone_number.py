def validate_phone_number(self, phone_number):
    """
    验证电话号码是否有效
    :param phone_number: 待验证的电话号码
    :return: True 或 False，表示电话号码是否有效
    >>> ru = RegexUtils()
    >>> ru.validate_phone_number("123-456-7890")
    True
    """
    pattern = self.generate_phone_number_pattern()
    return self.match(pattern, phone_number)