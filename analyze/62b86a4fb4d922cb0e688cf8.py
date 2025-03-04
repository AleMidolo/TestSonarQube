def validate_value(value):
    import re
    from django.core.exceptions import ValidationError

    # Check if value is empty or None
    if not value:
        raise ValidationError("मान खाली नहीं हो सकता")

    # Regular expression pattern for validation
    # Allows alphanumeric characters and some special characters
    pattern = r'^[\u0900-\u097F\w\s\-\_\.\,\@\#\&\+\=\(\)]{1,100}$'

    # Check if value matches pattern
    if not re.match(pattern, str(value)):
        raise ValidationError(
            "अमान्य मान। कृपया केवल वर्णमाला अक्षर, अंक और मान्य विशेष वर्णों का प्रयोग करें।"
        )

    return value