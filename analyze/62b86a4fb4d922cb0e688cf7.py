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
    # Allows alphanumeric characters and underscores, must start with a letter
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]*$'
    
    if not isinstance(key, str):
        raise ValidationError("Key must be a string")
        
    if not re.match(pattern, key):
        raise ValidationError(f"Invalid key format: {key}. Key must start with a letter and contain only alphanumeric characters and underscores.")
        
class ValidationError(Exception):
    """Custom exception for key validation errors"""
    pass