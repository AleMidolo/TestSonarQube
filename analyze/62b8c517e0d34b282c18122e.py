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
    import os

    # Get the exception traceback as a list of strings
    tb_list = traceback.format_exception(type(e), e, e.__traceback__)
    
    # Format the path to be relative and shortened
    formatted_tb = []
    for line in tb_list:
        if "File" in line:
            parts = line.split('"')
            if len(parts) > 1:
                path = parts[1]
                # Shorten path to max_path_level directories
                path_parts = path.split(os.sep)
                if len(path_parts) > max_path_level:
                    path = os.sep.join(['...'] + path_parts[-max_path_level:])
                line = line.replace(parts[1], path)
        formatted_tb.append(line)
    
    # Limit the traceback to max_level frames
    if len(formatted_tb) > max_level:
        formatted_tb = formatted_tb[:max_level]
        formatted_tb.append(f"... (traceback truncated to {max_level} levels)\n")
        
    # Join all lines and return
    return ''.join(formatted_tb)