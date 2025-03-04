def _get_resource_name_regex():
    """
    Build or return the regular expressions that are used to validate
    the name of the Krake resources.

    Returns:
        (re.Pattern): the compiled regular expressions, to validate
        the resource name.
    """
    import re
    
    # Regex pattern that matches:
    # - Must start with lowercase letter or number
    # - Can contain lowercase letters, numbers, hyphens
    # - Must end with lowercase letter or number
    # - Length between 1-63 characters
    pattern = r'^[a-z0-9][a-z0-9-]*[a-z0-9]$'
    
    return re.compile(pattern)