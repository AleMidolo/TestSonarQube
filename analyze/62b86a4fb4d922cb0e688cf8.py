import re

class ValidationError(Exception):
    pass

def validate_value(value):
    """
    Validate the given value against the corresponding regular expression.

    Args:
        value: the string to validate

    Raises:
        ValidationError: if the given value is not conform to the regular expression.
    """
    pattern = r'^[a-zA-Z0-9_]+$'  # Example regex pattern, adjust as needed
    if not re.match(pattern, value):
        raise ValidationError(f"Value '{value}' does not conform to the required format.")