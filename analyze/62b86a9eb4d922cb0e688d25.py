import re

def _get_resource_name_regex():
    """
    क्रैके संसाधनों के नाम को मान्य करने के लिए उपयोग किए जाने वाले नियमित अभिव्यक्तियों का निर्माण करें या उन्हें लौटाएँ।

    रिटर्न करता है:
    - (re.Pattern): संकलित नियमित अभिव्यक्तियां, जो संसाधन नाम को मान्य करने के लिए उपयोग की जाती हैं।
    """
    pattern = r'^[a-zA-Z0-9-_]+$'  # Example pattern for resource names
    return re.compile(pattern)