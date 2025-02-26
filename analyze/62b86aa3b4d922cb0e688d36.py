import re

class ValidationError(Exception):
    def __init__(self, messages):
        self.messages = messages

def _validate_labels(labels):
    regex_key = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    regex_value = r'^[a-zA-Z0-9_]+$'
    errors = []

    for key, value in labels.items():
        if not isinstance(key, str) or not re.match(regex_key, key):
            errors.append({key: f"Label key '{key}' does not match the regex [{regex_key}]"})
        
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, str) or not re.match(regex_value, item):
                    errors.append({str(value): 'expected string or bytes-like object'})
        elif not isinstance(value, str) or not re.match(regex_value, value):
            errors.append({str(value): 'expected string or bytes-like object'})

    if errors:
        raise ValidationError(errors)