def _validate_sex(self, sex: str) -> str:
    """
        Validate the sex and return it. If sex is not Man, Woman, or UGM, set to None.
        :param sex: str, the sex to validate
        :return: str, the validated sex or None if invalid
        """
    valid_sexes = {'Man', 'Woman', 'UGM'}
    if sex not in valid_sexes:
        return None
    return sex