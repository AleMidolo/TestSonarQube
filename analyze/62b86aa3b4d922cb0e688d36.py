import re
from typing import Dict, List, Union

class ValidationError(Exception):
    def __init__(self, messages: List[Dict[str, str]]):
        self.messages = messages
        super().__init__("Validation failed for labels.")

def _validate_labels(labels: Dict[Union[str, bool], Union[str, List, bool]]) -> None:
    """
    Validate the keys and values in the given labels against their respective regular expressions.

    Args:
        labels (dict): A dictionary of labels to validate.

    Raises:
        ValidationError: If any key or value does not match its respective regular expression.
                        The error contains a list of all errors that occurred in the labels.
                        Each element in the list is a dictionary with a key-value pair:
                        - key: The label key or value that caused the error, as a string.
                        - value: The error message.
    """
    errors = []
    
    # Define regex patterns for keys and values
    key_pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    value_pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    
    for key, value in labels.items():
        # Validate key
        if not isinstance(key, str):
            errors.append({str(key): 'expected string or bytes-like object'})
        elif not key_pattern.match(key):
            errors.append({key: f"Label key '{key}' does not match the regex {key_pattern.pattern}"})
        
        # Validate value
        if not isinstance(value, str):
            errors.append({str(value): 'expected string or bytes-like object'})
        elif not value_pattern.match(value):
            errors.append({value: f"Label value '{value}' does not match the regex {value_pattern.pattern}"})
    
    if errors:
        raise ValidationError(errors)