def validate_key(key):
    import re
    from django.core.exceptions import ValidationError

    # Regular expression pattern for key validation
    # Allows alphanumeric characters and underscores, minimum 1 character
    pattern = r'^[a-zA-Z0-9_]+$'

    if not isinstance(key, str):
        raise ValidationError("Key must be a string")

    if not key:
        raise ValidationError("Key cannot be empty")

    if not re.match(pattern, key):
        raise ValidationError("Key can only contain letters, numbers and underscores")

    return True