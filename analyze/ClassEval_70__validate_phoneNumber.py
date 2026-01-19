def _validate_phoneNumber(self, phoneNumber: str) -> str:
    """
    验证电话号码并返回。如果 phoneNumber 为空或不是 11 位数字，则设置为 None。
    :param phoneNumber: str，要验证的电话号码
    :return: str，验证后的电话号码，如果无效则返回 None
    """
    if not phoneNumber or not isinstance(phoneNumber, str):
        return None
    
    # 去除空格
    phoneNumber = phoneNumber.strip()
    
    # 检查是否为11位数字
    if len(phoneNumber) == 11 and phoneNumber.isdigit():
        return phoneNumber
    
    return None