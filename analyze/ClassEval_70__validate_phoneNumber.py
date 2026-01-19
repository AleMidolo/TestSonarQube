def _validate_phoneNumber(self, phoneNumber: str) -> str:
    """
    फोन नंबर को मान्य करें और इसे लौटाएं। यदि phoneNumber खाली है या 11 अंकों की संख्या नहीं है, तो इसे None पर सेट करें।
    :param phoneNumber: str, मान्य करने के लिए फोन नंबर
    :return: str, मान्य फोन नंबर या यदि अमान्य है तो None
    """
    if not phoneNumber or len(phoneNumber.strip()) == 0:
        return None
    
    # Remove any non-digit characters for validation
    digits_only = ''.join(filter(str.isdigit, phoneNumber))
    
    # Check if it has exactly 11 digits
    if len(digits_only) == 11:
        return phoneNumber
    else:
        return None