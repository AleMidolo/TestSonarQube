def match(filename):
    """
    तर्क (Args):
    - `filename`: वह फ़ाइल नाम जिसे मिलाना है।

    रिटर्न (Returns):
    - यदि फ़ाइल प्रकार समर्थित नहीं है, तो `False` लौटाएगा। यदि समर्थित है, तो `True` लौटाएगा।
    """
    # List of supported file extensions
    supported_extensions = ['.txt', '.pdf', '.doc', '.docx', '.csv', '.xls', '.xlsx']
    
    # Get the file extension from filename
    file_extension = filename[filename.rfind('.'):].lower() if '.' in filename else ''
    
    # Check if extension is in supported list
    return file_extension in supported_extensions