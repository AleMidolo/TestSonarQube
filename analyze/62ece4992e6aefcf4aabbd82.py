import re

def get_pattern(pattern, strip=True):
    """
    यह मेथड दी गई स्ट्रिंग को रेगुलर एक्सप्रेशन (Regex) पैटर्न में बदलता है।
    
    :param pattern: स्ट्रिंग जिसे रेगुलर एक्सप्रेशन पैटर्न में बदलना है।
    :param strip: यदि True है, तो स्ट्रिंग के शुरुआत और अंत के सफेद स्थान (whitespace) हटा दिए जाएंगे।
    :return: रेगुलर एक्सप्रेशन पैटर्न।
    """
    if strip:
        pattern = pattern.strip()
    return re.compile(pattern)