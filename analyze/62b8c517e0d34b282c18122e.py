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
    exception_type = type(e).__name__
    exception_message = str(e)
    
    # Get the traceback information
    tb_list = traceback.format_tb(e.__traceback__)
    
    # Limit the traceback levels
    if len(tb_list) > max_level:
        tb_list = tb_list[:max_level]
    
    # Format the traceback paths
    formatted_tb = []
    for tb in tb_list:
        lines = tb.splitlines()
        if len(lines) > max_path_level:
            lines = lines[:max_path_level]
        formatted_tb.append("\n".join(lines))
    
    # Combine the formatted traceback
    formatted_traceback = "\n".join(formatted_tb)
    
    # Construct the final formatted exception string
    formatted_exception = f"{exception_type}: {exception_message}\n{formatted_traceback}"
    
    return formatted_exception