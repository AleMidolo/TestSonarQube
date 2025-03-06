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
    
    # Get the exception message
    exception_message = str(e)
    
    # Get the traceback as a list of strings
    tb_list = traceback.format_tb(e.__traceback__)
    
    # Limit the traceback to max_level
    if len(tb_list) > max_level:
        tb_list = tb_list[:max_level]
    
    # Format the traceback
    formatted_traceback = []
    for i, tb_line in enumerate(tb_list):
        if i < max_path_level:
            formatted_traceback.append(tb_line.strip())
        else:
            # Truncate the path if it exceeds max_path_level
            parts = tb_line.strip().split('\n')
            if len(parts) > max_path_level:
                parts = parts[:max_path_level] + ['...']
            formatted_traceback.append('\n'.join(parts))
    
    # Combine the exception message and formatted traceback
    result = f"Exception: {exception_message}\n"
    result += "Traceback (most recent call last):\n"
    result += '\n'.join(formatted_traceback)
    
    return result