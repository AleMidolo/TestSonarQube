def extostr(cls, e, max_level=30, max_path_level=5):
    """
    अपवाद को स्वरूपित करें।  
    :param e: कोई भी अपवाद उदाहरण।  
    :type e: Exception  
    :param max_level: अधिकतम कॉल स्टैक स्तर (डिफ़ॉल्ट 30)।  
    :type max_level: int  
    :param max_path_level: अधिकतम पथ स्तर (डिफ़ॉल्ट 5)।  
    :type max_path_level: int  
    :return: अपवाद को पढ़ने योग्य स्ट्रिंग।  
    :rtype: str  
    """
    import traceback

    # Get the exception type and message
    exc_type = type(e).__name__
    exc_message = str(e)

    # Format the exception message
    formatted_message = f"{exc_type}: {exc_message}"

    # Get the traceback
    tb = traceback.extract_tb(e.__traceback__)
    
    # Limit the traceback to max_level
    tb = tb[:max_level]

    # Format the traceback
    formatted_tb = []
    for frame in tb:
        filename, lineno, funcname, code = frame
        # Limit the path to max_path_level
        path_parts = filename.split('/')
        limited_path = '/'.join(path_parts[-max_path_level:]) if len(path_parts) > max_path_level else filename
        formatted_tb.append(f"File \"{limited_path}\", line {lineno}, in {funcname}\n    {code}")

    # Combine the formatted message and traceback
    return formatted_message + "\n" + "\n".join(formatted_tb)