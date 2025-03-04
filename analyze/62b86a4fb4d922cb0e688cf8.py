def validate_value(value):
    """
    Validate the given value against the corresponding regular expression.

    Args:
        value: the string to validate

    Raises:
        ValidationError: if the given value is not conform to the regular expression.
    """
    import re

    # Regular expression pattern for validation
    pattern = r'^[A-Za-z0-9\s\-_]+$'

    # Check if value is a string
    if not isinstance(value, str):
        raise ValidationError("Value must be a string")

    # Check if value matches pattern
    if not re.match(pattern, value):
        raise ValidationError("Value contains invalid characters. Only alphanumeric characters, spaces, hyphens and underscores are allowed.")

class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass