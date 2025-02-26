def match(filename):
    """
    तर्क (Args):
    - `filename`: वह फ़ाइल नाम जिसे मिलाना है।

    रिटर्न (Returns):
    - यदि फ़ाइल प्रकार समर्थित नहीं है, तो `False` लौटाएगा। यदि समर्थित है, तो `True` लौटाएगा।
    """
    supported_extensions = ['.txt', '.csv', '.json', '.xml']
    file_extension = filename.split('.')[-1] if '.' in filename else ''
    
    return f'.{file_extension}' in supported_extensions