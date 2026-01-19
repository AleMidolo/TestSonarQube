def _validate_phoneNumber(self, phoneNumber: str) -> str:
    """
    फोन नंबर को मान्य करें और इसे लौटाएं। यदि phoneNumber खाली है या 11 अंकों की संख्या नहीं है, तो इसे None पर सेट करें।
    :param phoneNumber: str, मान्य करने के लिए फोन नंबर
    :return: str, मान्य फोन नंबर या यदि अमान्य है तो None
    """
    if not phoneNumber or not phoneNumber.strip():
        return None
    
    # Remove any whitespace
    cleaned_number = phoneNumber.strip()
    
    # Check if it contains only digits and is exactly 11 digits long
    if cleaned_number.isdigit() and len(cleaned_number) == 11:
        return cleaned_number
    
    return None