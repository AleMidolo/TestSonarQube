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
    pattern = r'^[a-zA-Z0-9_-]{1,20}$'  # Example regex pattern
    if not re.match(pattern, key):
        raise ValidationError(f"Invalid key: {key}")