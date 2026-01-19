def _validate_sex(self, sex: str) -> str:
    """
        Validate the sex and return it. If sex is not male, female, or UGM, set to None.
        :param sex: str, the sex to validate
        :return: str, the validated sex or None if invalid
        """
    if sex not in ['male', 'female', 'UGM']:
        return None
    return sex