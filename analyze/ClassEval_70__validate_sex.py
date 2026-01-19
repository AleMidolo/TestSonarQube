def _validate_sex(self, sex: str) -> str:
    """
    लिंग को मान्य करें और इसे लौटाएं। यदि लिंग पुरुष, महिला, या UGM नहीं है, तो इसे None पर सेट करें।
    :param sex: str, मान्य करने के लिए लिंग
    :return: str, मान्य लिंग या यदि अमान्य है तो None
    """
    valid_sexes = ['पुरुष', 'महिला', 'UGM']
    
    if sex in valid_sexes:
        return sex
    else:
        return None