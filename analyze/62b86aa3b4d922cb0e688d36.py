def _validate_labels(labels):
    """
    检查给定标签中的键和值是否通过 `validate_key()` 和 `validate_value()` 验证。
    检查给定标签中的键和值是否符合其对应的正则表达式。

    参数:
        labels (dict): 需要验证的不同标签。

    异常:
        ValidationError: 如果任何键或值不符合其对应的正则表达式，将抛出此异常。
    """
    errors = []
    
    if not isinstance(labels, dict):
        raise ValidationError("Labels must be a dictionary")
        
    for key, value in labels.items():
        # Validate key
        try:
            if not isinstance(key, (str, bytes)):
                errors.append({str(key): 'expected string or bytes-like object'})
                continue
                
            if not validate_key(key):
                errors.append({key: f"Label key '{key}' does not match the regex [...]"})
        except Exception as e:
            errors.append({str(key): str(e)})
            
        # Validate value  
        try:
            if not isinstance(value, (str, bytes)):
                errors.append({str(value): 'expected string or bytes-like object'})
                continue
                
            if not validate_value(value):
                errors.append({value: f"Label value '{value}' does not match the regex [...]"})
        except Exception as e:
            errors.append({str(value): str(e)})
            
    if errors:
        raise ValidationError(messages=errors)