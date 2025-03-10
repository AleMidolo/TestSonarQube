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
    
    # Get the exception traceback
    tb = traceback.format_exception(type(e), e, e.__traceback__)
    
    # Limit the traceback to max_level
    if len(tb) > max_level:
        tb = tb[:max_level]
        tb.append(f"... (truncated to {max_level} levels)")
    
    # Limit the path levels in each traceback line
    for i in range(len(tb)):
        parts = tb[i].split('\n')
        if len(parts) > 1:
            path_parts = parts[0].split('/')
            if len(path_parts) > max_path_level:
                parts[0] = '/'.join(path_parts[-max_path_level:])
            tb[i] = '\n'.join(parts)
    
    # Join the traceback into a single string
    formatted_traceback = ''.join(tb)
    
    return formatted_traceback