def append_text_to_file(file_name, text_buffer, encoding, overwrite=False):
    """
    दिए गए बाइनरी बफ़र को निर्दिष्ट फ़ाइल नाम में लिखें।  
    आवश्यक होने पर फ़ाइल बनाएँ।  
    :param file_name: फ़ाइल का नाम।  
    :type file_name: str  
    :param text_buffer: लिखने के लिए टेक्स्ट बफ़र।  
    :type text_buffer: str  
    :param encoding: उपयोग करने के लिए एन्कोडिंग।  
    :type encoding: str  
    :param overwrite: यदि सत्य है, तो फ़ाइल को ओवरराइट किया जाएगा।  
    :type overwrite: bool  
    :return: लिखे गए बाइट्स की संख्या या त्रुटि होने पर 0 से कम।  
    :rtype int  
    """
    try:
        mode = 'w' if overwrite else 'a'
        with open(file_name, mode, encoding=encoding) as file:
            bytes_written = file.write(text_buffer)
        return bytes_written
    except Exception as e:
        print(f"Error: {e}")
        return -1