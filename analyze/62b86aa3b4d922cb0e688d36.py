import re
from typing import Dict, Any, List

class ValidationError(Exception):
    def __init__(self, messages: List[Dict[str, str]]):
        self.messages = messages
        super().__init__(str(messages))

def _validate_labels(labels: Dict[str, Any]):
    """
    Check that keys and values in the given labels match against their corresponding
    regular expressions.

    Args:
        labels (dict): the different labels to validate.

    Raises:
        ValidationError: if any of the keys and labels does not match their respective
            regular expression. The error contains as message the list of all errors
            which occurred in the labels. Each element of the list is a dictionary with
            one key-value pair:
            - key: the label key or label value for which an error occurred as string.
            - value: the error message.
    """
    errors = []
    key_regex = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    value_regex = re.compile(r'^[a-zA-Z0-9_\-\.]*$')

    for key, value in labels.items():
        # Validate key
        if not isinstance(key, str):
            errors.append({str(key): 'expected string or bytes-like object'})
        elif not key_regex.match(key):
            errors.append({key: f"Label key '{key}' does not match the regex {key_regex.pattern}"})

        # Validate value
        if isinstance(value, (list, dict, bool)):
            errors.append({str(value): 'expected string or bytes-like object'})
        elif not isinstance(value, str):
            errors.append({str(value): 'expected string or bytes-like object'})
        elif not value_regex.match(value):
            errors.append({value: f"Label value '{value}' does not match the regex {value_regex.pattern}"})

    if errors:
        raise ValidationError(errors)