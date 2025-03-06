import re
from typing import Dict, List, Union

class ValidationError(Exception):
    def __init__(self, messages: List[Dict[str, str]]):
        self.messages = messages
        super().__init__(f"Validation failed with errors: {messages}")

def validate_key(key: str) -> bool:
    # Example regex for key validation
    key_regex = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return bool(re.match(key_regex, key))

def validate_value(value: Union[str, bytes]) -> bool:
    # Example regex for value validation
    value_regex = r"^[a-zA-Z0-9_]+$"
    return bool(re.match(value_regex, value))

def _validate_labels(labels: Dict[str, Union[str, bytes, List, bool]]) -> None:
    errors = []
    
    for key, value in labels.items():
        # Validate key
        if not isinstance(key, str):
            errors.append({str(key): "expected string or bytes-like object"})
        elif not validate_key(key):
            errors.append({key: f"Label key '{key}' does not match the regex"})
        
        # Validate value
        if isinstance(value, (str, bytes)):
            if not validate_value(value):
                errors.append({str(value): "Value does not match the regex"})
        elif isinstance(value, list):
            for item in value:
                if not isinstance(item, (str, bytes)):
                    errors.append({str(item): "expected string or bytes-like object"})
                elif not validate_value(item):
                    errors.append({str(item): "Value does not match the regex"})
        else:
            errors.append({str(value): "expected string or bytes-like object"})
    
    if errors:
        raise ValidationError(errors)