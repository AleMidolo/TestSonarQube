import re

class ValidationError(Exception):
    pass

def validate_value(value):
    pattern = r'^[a-zA-Z0-9_]+$'  # Example regex pattern
    if not re.match(pattern, value):
        raise ValidationError(f"Value '{value}' does not conform to the regular expression.")