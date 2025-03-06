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
    import sys

    # Get the exception type and message
    exc_type = type(e).__name__
    exc_msg = str(e)

    # Get the traceback
    tb = e.__traceback__
    tb_list = traceback.extract_tb(tb)

    # Limit the traceback to max_level
    if len(tb_list) > max_level:
        tb_list = tb_list[-max_level:]

    # Format the traceback
    formatted_tb = []
    for frame in tb_list:
        filename = frame.filename
        lineno = frame.lineno
        funcname = frame.name
        line = frame.line

        # Limit the path level
        if max_path_level > 0:
            parts = filename.split('/')
            if len(parts) > max_path_level:
                filename = '/'.join(parts[-max_path_level:])

        formatted_tb.append(f"File \"{filename}\", line {lineno}, in {funcname}\n  {line}")

    # Combine the exception type, message, and traceback
    formatted_exception = f"{exc_type}: {exc_msg}\n"
    formatted_exception += "\n".join(formatted_tb)

    return formatted_exception