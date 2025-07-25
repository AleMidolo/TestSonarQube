def _validate_labels(labels):
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
    import re
    
    # Regular expressions for label keys and values
    key_regex = r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'
    value_regex = r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'
    
    errors = []
    
    for key, value in labels.items():
        # Validate key type
        if not isinstance(key, (str, bytes)):
            errors.append({str(key): 'expected string or bytes-like object'})
            continue
            
        # Validate key format
        if not re.match(key_regex, key):
            errors.append({key: f"Label key '{key}' does not match the regex {key_regex}"})
            
        # Validate value type
        if not isinstance(value, (str, bytes)):
            errors.append({str(value): 'expected string or bytes-like object'})
            continue
            
        # Validate value format
        if not re.match(value_regex, value):
            errors.append({value: f"Label value '{value}' does not match the regex {value_regex}"})
    
    if errors:
        raise ValidationError(messages=errors)