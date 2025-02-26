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
    formatted_message = f"{exc_type}: {exc_message}\n"

    # Get the traceback
    tb = traceback.extract_tb(e.__traceback__)
    
    # Limit the traceback to max_level
    tb = tb[:max_level]

    # Format the traceback
    for frame in tb:
        filename, lineno, funcname, code = frame
        formatted_message += f"  File \"{filename}\", line {lineno}, in {funcname}\n"
        formatted_message += f"    {code}\n"

    # Limit the number of paths shown
    if len(tb) > max_path_level:
        formatted_message += f"  ... (truncated to {max_path_level} frames)\n"

    return formatted_message