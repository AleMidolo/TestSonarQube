def _validate_name(self, name: str) -> str:
    """
        Validate the name and return it. If the name is empty or exceeds 33 characters, set to None.
        :param name: str, the name to validate
        :return: str, the validated name or None if invalid
        """
    if not name or len(name) > 33:
        return None
    return name