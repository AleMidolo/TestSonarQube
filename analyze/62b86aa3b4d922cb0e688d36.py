def _validate_labels(labels):
    import re

    class ValidationError(Exception):
        def __init__(self, messages):
            self.messages = messages

    key_regex = r'^[a-zA-Z0-9_]+$'  # Example regex for keys
    value_regex = r'^[a-zA-Z0-9_ ]+$'  # Example regex for values
    errors = []

    for key, value in labels.items():
        if not isinstance(key, str) or not re.match(key_regex, key):
            errors.append({str(key): f"Label key '{key}' does not match the regex [{key_regex}]"})
        
        if not isinstance(value, str) or not re.match(value_regex, value):
            errors.append({str(value): 'expected string or bytes-like object'})

    if errors:
        raise ValidationError(errors)