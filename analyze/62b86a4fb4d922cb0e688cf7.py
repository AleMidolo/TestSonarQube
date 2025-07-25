def validate_key(key):
    """
    根据对应的正则表达式验证给定的键。

    参数:
        key: 要验证的字符串

    异常:
        ValidationError: 如果给定的键不符合正则表达式，则抛出此异常。
    """
    import re
    
    class ValidationError(Exception):
        pass
        
    # 键的正则表达式模式:
    # - 只能包含字母、数字、下划线
    # - 必须以字母开头
    # - 长度在1-64个字符之间
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{0,63}$'
    
    if not isinstance(key, str):
        raise ValidationError("Key must be a string")
        
    if not re.match(pattern, key):
        raise ValidationError("Invalid key format. Key must start with a letter and contain only letters, numbers and underscores")
        
    return True