def validate_key(key):
    """
    Validate the given key against the corresponding regular expression.

    Args:
        key: the string to validate

    Raises:
        ValidationError: if the given key is not conform to the regular expression.
    """
    import re
    
    # Regular expression pattern for valid keys
    # Allows alphanumeric characters, underscores, hyphens
    pattern = r'^[a-zA-Z0-9_-]+$'
    
    if not isinstance(key, str):
        raise ValidationError("Key must be a string")
        
    if not key:
        raise ValidationError("Key cannot be empty")
        
    if not re.match(pattern, key):
        raise ValidationError("Key contains invalid characters. Only alphanumeric characters, underscores and hyphens are allowed.")

class ValidationError(Exception):
    pass