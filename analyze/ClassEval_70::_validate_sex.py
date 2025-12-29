def _validate_sex(self, sex: str) -> str:
    """
        Validate the sex and return it. If the sex is not Male, Female, or UGM, set to None.
        :param sex: str, the sex to validate
        :return: str, the validated sex or None if invalid
        """
    if sex not in ['Male', 'Female', 'UGM']:
        return None
    return sex