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
    
    # Get the formatted traceback
    tb_list = traceback.format_exception(type(e), e, e.__traceback__)
    
    # Limit the traceback levels
    if len(tb_list) > max_level:
        tb_list = tb_list[:max_level]
    
    # Join the traceback into a single string
    traceback_str = "".join(tb_list)
    
    # Limit the path levels in the traceback
    if max_path_level > 0:
        lines = traceback_str.splitlines()
        for i in range(len(lines)):
            if "File" in lines[i]:
                path_parts = lines[i].split(",")
                if len(path_parts) > max_path_level:
                    lines[i] = ",".join(path_parts[:max_path_level]) + "..."
        traceback_str = "\n".join(lines)
    
    # Combine the exception message and traceback
    result = f"{exception_message}\n{traceback_str}"
    
    return result