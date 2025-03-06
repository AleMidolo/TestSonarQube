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
    if level == 0:
        return {k: v for k, v in d1.items() if k not in d2 or d1[k] != d2[k]}
    
    diff = {}
    for k, v in d1.items():
        if k not in d2:
            diff[k] = v
        elif isinstance(v, dict) and isinstance(d2[k], dict) and (level == -1 or level > 0):
            sub_diff = difference(v, d2[k], level - 1 if level != -1 else -1)
            if sub_diff:
                diff[k] = sub_diff
        elif v != d2[k]:
            diff[k] = v
    return diff