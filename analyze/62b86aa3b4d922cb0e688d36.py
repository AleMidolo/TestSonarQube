import re

class ValidationError(Exception):
    def __init__(self, messages):
        self.messages = messages

def validate_key(key):
    # Example regex for key validation
    return isinstance(key, str) and re.match(r'^[a-zA-Z0-9_]+$', key)

def validate_value(value):
    # Example regex for value validation
    return isinstance(value, str) and re.match(r'^[a-zA-Z0-9_ ]+$', value)

def _validate_labels(labels):
    errors = []
    
    for key, value in labels.items():
        if not validate_key(key):
            errors.append({str(key): f"Label key '{key}' does not match the regex [...]"})
        
        if not validate_value(value):
            errors.append({str(value): 'expected string or bytes-like object'})
    
    if errors:
        raise ValidationError(errors)