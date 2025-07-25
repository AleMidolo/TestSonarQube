import re

def validate_key(key):
    """
    दिए गए कुंजी (key) को संबंधित नियमित अभिव्यक्ति (regular expression) के खिलाफ सत्यापित करें।

    आर्ग्युमेंट्स (Args):
        key: सत्यापन के लिए स्ट्रिंग (string)

    त्रुटि (Raises):
        ValidationError: यदि दी गई कुंजी नियमित अभिव्यक्ति के अनुरूप नहीं है।
    """
    # Define the regular expression pattern for the key
    pattern = r'^[A-Za-z0-9_]{8,20}$'
    
    # Compile the pattern
    regex = re.compile(pattern)
    
    # Check if the key matches the pattern
    if not regex.match(key):
        raise ValidationError("Invalid key format. Key must be 8-20 characters long and can only contain letters, numbers, and underscores.")
    
    return True

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass