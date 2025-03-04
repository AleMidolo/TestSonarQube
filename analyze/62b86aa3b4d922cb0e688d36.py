def _validate_labels(labels):
    import re
    from typing import Dict, Any, List

    # Regular expressions for validation
    KEY_REGEX = r'^[a-zA-Z][a-zA-Z0-9_-]*$'
    VALUE_REGEX = r'^[a-zA-Z0-9_-]+$'

    errors: List[Dict[str, str]] = []

    # Validate each key-value pair
    for key, value in labels.items():
        # Validate key type
        if not isinstance(key, str):
            errors.append({
                str(key): 'expected string or bytes-like object'
            })
            continue

        # Validate key format
        if not re.match(KEY_REGEX, key):
            errors.append({
                key: f"Label key '{key}' does not match the regex {KEY_REGEX}"
            })

        # Validate value type
        if not isinstance(value, str):
            errors.append({
                str(value): 'expected string or bytes-like object'
            })
            continue

        # Validate value format
        if not re.match(VALUE_REGEX, value):
            errors.append({
                value: f"Label value '{value}' does not match the regex {VALUE_REGEX}"
            })

    # Raise ValidationError if any errors found
    if errors:
        raise ValidationError(errors)

class ValidationError(Exception):
    def __init__(self, messages):
        self.messages = messages
        super().__init__(str(messages))