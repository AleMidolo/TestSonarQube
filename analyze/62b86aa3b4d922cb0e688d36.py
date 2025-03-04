def _validate_labels(labels):
    import re
    
    # Regular expressions for label keys and values
    KEY_REGEX = r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'
    VALUE_REGEX = r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'
    
    errors = []
    
    # Validate each label key-value pair
    for key, value in labels.items():
        # Validate key type
        if not isinstance(key, (str, bytes)):
            errors.append({
                str(key): 'expected string or bytes-like object'
            })
            continue
            
        # Validate key format
        if not re.match(KEY_REGEX, str(key)):
            errors.append({
                str(key): f"Label key '{key}' does not match the regex {KEY_REGEX}"
            })
            
        # Validate value type
        if not isinstance(value, (str, bytes)):
            errors.append({
                str(value): 'expected string or bytes-like object'
            })
            continue
            
        # Validate value format
        if not re.match(VALUE_REGEX, str(value)):
            errors.append({
                str(value): f"Label value '{value}' does not match the regex {VALUE_REGEX}"
            })
    
    # Raise ValidationError if any errors occurred
    if errors:
        raise ValidationError(messages=errors)