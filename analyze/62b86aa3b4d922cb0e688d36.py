def _validate_labels(labels):
    import re

    class ValidationError(Exception):
        def __init__(self, messages):
            self.messages = messages

    errors = []
    key_regex = re.compile(r'^[a-zA-Z0-9_]+$')  # Example regex for keys
    value_regex = re.compile(r'^[a-zA-Z0-9_ ]+$')  # Example regex for values

    for key, value in labels.items():
        if not isinstance(key, str) or not key_regex.match(key):
            errors.append({str(key): f"Label key '{key}' does not match the regex [...]"})
        if not isinstance(value, str) or not value_regex.match(value):
            errors.append({str(value): 'expected string or bytes-like object'})

    if errors:
        raise ValidationError(errors)