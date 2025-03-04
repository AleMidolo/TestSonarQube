def _validate_labels(labels):
    import re
    
    # Regex patterns for validation
    key_pattern = r'^[a-zA-Z][a-zA-Z0-9_-]*$'
    value_pattern = r'^[a-zA-Z0-9_-]+$'
    
    errors = []
    
    # Validate each label key-value pair
    for key, value in labels.items():
        
        # Validate key type
        if not isinstance(key, str):
            errors.append({
                str(key): 'expected string or bytes-like object'
            })
            continue
            
        # Validate key format
        if not re.match(key_pattern, key):
            errors.append({
                key: f"Label key '{key}' does not match the regex {key_pattern}"
            })
            
        # Validate value type
        if not isinstance(value, str):
            errors.append({
                str(value): 'expected string or bytes-like object'
            })
            continue
            
        # Validate value format
        if not re.match(value_pattern, value):
            errors.append({
                value: f"Label value '{value}' does not match the regex {value_pattern}"
            })
            
    # Raise ValidationError if any errors found
    if errors:
        raise ValidationError(errors)