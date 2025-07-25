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
        return {}
    
    diff = {}
    for key in d1:
        if key not in d2:
            diff[key] = d1[key]
        elif isinstance(d1[key], dict) and isinstance(d2[key], dict) and level != 1:
            sub_diff = difference(d1[key], d2[key], level - 1 if level != -1 else -1)
            if sub_diff:
                diff[key] = sub_diff
        elif d1[key] != d2[key]:
            diff[key] = d1[key]
    
    return diff