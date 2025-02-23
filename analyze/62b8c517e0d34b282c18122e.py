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

    # Get the traceback
    tb = traceback.extract_tb(e.__traceback__)
    tb_lines = []

    # Limit the traceback to max_level
    for frame in tb[:max_level]:
        filename, lineno, funcname, text = frame
        # Limit the path to max_path_level
        if len(tb_lines) < max_path_level:
            tb_lines.append(f'File "{filename}", line {lineno}, in {funcname}\n    {text}')

    # Join the traceback lines
    tb_output = "\n".join(tb_lines)

    # Format the final output
    return f"{exc_type}: {exc_message}\nTraceback (most recent call last):\n{tb_output}"