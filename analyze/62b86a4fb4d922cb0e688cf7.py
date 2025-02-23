import re

class ValidationError(Exception):
    pass

def validate_key(key):
    """
    Validate the given key against the corresponding regular expression.

    Args:
        key: the string to validate

    Raises:
        ValidationError: if the given key is not conform to the regular expression.
    """
    pattern = r'^[A-Za-z0-9]{8,}$'  # Example pattern: at least 8 alphanumeric characters
    if not re.match(pattern, key):
        raise ValidationError(f"Invalid key: {key}")