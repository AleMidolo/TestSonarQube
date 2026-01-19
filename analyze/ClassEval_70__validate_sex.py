def _validate_sex(self, sex: str) -> str:
    """
    验证性别并返回。如果性别不是男、女或UGM，则设置为None。
    :param sex: str，要验证的性别
    :return: str，验证后的性别，如果无效则返回None
    """
    valid_sexes = ["男", "女", "UGM"]
    if sex in valid_sexes:
        return sex
    else:
        return None