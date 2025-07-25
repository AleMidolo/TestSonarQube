def file_to_textbuffer(file_name, encoding):
    """
    एक फाइल को टेक्स्ट बफर (UTF-8) में लोड करें, पढ़ने के दौरान निर्दिष्ट एन्कोडिंग का उपयोग करें।
    सावधानी: यह पूरी फाइल को मेमोरी में पढ़ेगा।
    :param file_name: फाइल का नाम।
    :type file_name: str 
    :param encoding: उपयोग करने के लिए एन्कोडिंग।
    :type encoding: str
    :return: एक टेक्स्ट बफर या त्रुटि की स्थिति में None।
    :rtype: str
    """
    try:
        with open(file_name, 'r', encoding=encoding) as f:
            return f.read()
    except (IOError, UnicodeDecodeError):
        return None