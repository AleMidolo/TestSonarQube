def difference(d1, d2, level=-1):
    """
    यह फ़ंक्शन एक डिक्शनरी लौटाता है जिसमें *d1* के वे आइटम्स शामिल होते हैं जो *d2* में नहीं हैं।
  
    *level* पुनरावृत्ति की अधिकतम गहराई निर्धारित करता है। अनंत पुनरावृत्ति के लिए,
    इसे -1 पर सेट करें। स्तर 1 के लिए,
    यदि कोई कुंजी *d1* और *d2* दोनों में मौजूद है, लेकिन उसके मान अलग-अलग हैं,
    तो उसे अंतर में शामिल किया जाता है।
    अधिक जानकारी के लिए :func:`intersection` देखें।

    *d1* और *d2* अपरिवर्तित रहते हैं। हालाँकि, *d1* या इसके कुछ
    उपशब्दकोश सीधे लौटाए जा सकते हैं।
    जब उचित हो तो परिणाम की एक गहरी प्रतिलिपि बनाएँ।

    ..versionadded::0.5
    कीवर्ड तर्क *level* जोड़ें।
    """
    def _difference(d1, d2, current_level):
        if current_level == 0:
            return {}
        
        diff = {}
        for key, value in d1.items():
            if key not in d2:
                diff[key] = value
            elif isinstance(value, dict) and isinstance(d2[key], dict):
                if level == -1 or current_level > 1:
                    sub_diff = _difference(value, d2[key], current_level - 1)
                    if sub_diff:
                        diff[key] = sub_diff
            elif value != d2[key]:
                diff[key] = value
        return diff

    return _difference(d1, d2, level if level != -1 else float('inf'))