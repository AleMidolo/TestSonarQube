import re

class ValidationError(Exception):
    def __init__(self, messages):
        self.messages = messages
        super().__init__(f"Validation failed with errors: {messages}")

def validate_key(key):
    # Example regex for key validation
    key_regex = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if not isinstance(key, str):
        return False, 'expected string or bytes-like object'
    if not re.match(key_regex, key):
        return False, f"Label key '{key}' does not match the regex {key_regex}"
    return True, None

def validate_value(value):
    # Example regex for value validation
    value_regex = r'^[a-zA-Z0-9_]*$'
    if not isinstance(value, str):
        return False, 'expected string or bytes-like object'
    if not re.match(value_regex, value):
        return False, f"Label value '{value}' does not match the regex {value_regex}"
    return True, None

def _validate_labels(labels):
    errors = []
    for key, value in labels.items():
        key_valid, key_error = validate_key(key)
        if not key_valid:
            errors.append({str(key): key_error})
        
        value_valid, value_error = validate_value(value)
        if not value_valid:
            errors.append({str(value): value_error})
    
    if errors:
        raise ValidationError(errors)