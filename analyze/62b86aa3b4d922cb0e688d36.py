import re

class ValidationError(Exception):
    def __init__(self, messages):
        self.messages = messages

def _validate_labels(labels):
    key_regex = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    value_regex = r'^[a-zA-Z0-9_]+$'
    errors = []

    for key, value in labels.items():
        if not isinstance(key, str) or not re.match(key_regex, key):
            errors.append({key: f"Label key '{key}' does not match the regex [{key_regex}]"})
        
        if not isinstance(value, str):
            errors.append({str(value): 'expected string or bytes-like object'})
        elif not re.match(value_regex, value):
            errors.append({value: f"Label value '{value}' does not match the regex [{value_regex}]"})

    if errors:
        raise ValidationError(errors)