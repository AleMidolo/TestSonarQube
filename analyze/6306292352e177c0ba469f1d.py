def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    """
    टेक्स्ट में टैग्स खोजें।

    कोड ब्लॉक्स के अंदर मौजूद टैग्स को अनदेखा करने की कोशिश करता है।

    वैकल्पिक रूप से, यदि "replacer" पास किया गया है, तो यह टैग शब्द को 
    replacer फ़ंक्शन द्वारा लौटाए गए परिणाम से बदल देगा, जिसे टैग शब्द के साथ कॉल किया गया है।

    एक सेट के रूप में टैग्स और मूल या बदला हुआ टेक्स्ट लौटाता है।
    """
    tags = set()
    result = text
    in_code_block = False
    
    # Split text into lines
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Check for code block markers
        if line.strip().startswith('