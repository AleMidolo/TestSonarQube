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
        
        if isinstance(value, str):
            if not re.match(value_regex, value):
                errors.append({value: 'expected string or bytes-like object'})
        elif isinstance(value, list):
            for item in value:
                if not isinstance(item, str) or not re.match(value_regex, item):
                    errors.append({str(item): 'expected string or bytes-like object'})
        else:
            errors.append({str(value): 'expected string or bytes-like object'})

    if errors:
        raise ValidationError(errors)