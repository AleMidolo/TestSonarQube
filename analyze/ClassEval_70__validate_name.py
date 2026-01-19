def _validate_name(self, name: str) -> str:
    """
    验证名称并返回。如果名称为空或超过33个字符,则设置为None。
    :param name: str,要验证的名称
    :return: str,验证后的名称,如果无效则返回None
    """
    if not name or len(name) > 33:
        return None
    return name