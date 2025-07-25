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

    def format_exception(exc, level, path_level):
        if level > max_level:
            return f"{type(exc).__name__}: {exc}\n[...]\n"
        
        tb = traceback.extract_tb(exc.__traceback__)
        formatted_tb = []
        for frame in tb:
            if path_level > max_path_level:
                break
            formatted_tb.append(f"File \"{frame.filename}\", line {frame.lineno}, in {frame.name}")
            path_level += 1
        
        return ''.join(formatted_tb)

    exception_message = f"{type(e).__name__}: {e}\n"
    formatted_traceback = format_exception(e, 0, 0)
    
    return exception_message + formatted_traceback