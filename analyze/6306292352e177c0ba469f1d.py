import re
from typing import Set, Tuple, Callable

def find_tags(text: str, replacer: Callable = None) -> Tuple[Set, str]:
    """
    टेक्स्ट में टैग्स खोजें।

    कोड ब्लॉक्स के अंदर मौजूद टैग्स को अनदेखा करने की कोशिश करता है।

    वैकल्पिक रूप से, यदि "replacer" पास किया गया है, तो यह टैग शब्द को 
    replacer फ़ंक्शन द्वारा लौटाए गए परिणाम से बदल देगा, जिसे टैग शब्द के साथ कॉल किया गया है।

    एक सेट के रूप में टैग्स और मूल या बदला हुआ टेक्स्ट लौटाता है।
    """
    # Regex to match tags (words starting with '#')
    tag_pattern = re.compile(r'#\w+')
    
    # Regex to match code blocks (