import re

class ValidationError(Exception):
    pass

def validate_value(value):
    """
    दिए गए मान को संबंधित नियमित अभिव्यक्ति (Regular Expression) के अनुसार सत्यापित करें।

    आर्ग्युमेंट्स (Args):
        value: सत्यापन के लिए स्ट्रिंग

    त्रुटि (Raises):
        ValidationError: यदि दिया गया मान नियमित अभिव्यक्ति के अनुरूप नहीं है।
    """
    pattern = r'^[a-zA-Z0-9]+$'  # उदाहरण के लिए, केवल अल्फ़ान्यूमेरिक मानों की अनुमति
    if not re.match(pattern, value):
        raise ValidationError(f"Invalid value: {value}")