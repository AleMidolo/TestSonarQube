def _get_resource_name_regex():
    """
    क्रैके संसाधनों के नाम को मान्य करने के लिए उपयोग किए जाने वाले नियमित अभिव्यक्तियों का निर्माण करें या उन्हें लौटाएँ।

    रिटर्न करता है:
    - (re.Pattern): संकलित नियमित अभिव्यक्तियां, जो संसाधन नाम को मान्य करने के लिए उपयोग की जाती हैं।
    """
    import re
    
    # Valid resource name pattern:
    # - Must start with a letter or underscore
    # - Can contain letters, numbers, underscores, hyphens
    # - Must be between 1-63 characters
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_-]{0,62}$'
    
    return re.compile(pattern)