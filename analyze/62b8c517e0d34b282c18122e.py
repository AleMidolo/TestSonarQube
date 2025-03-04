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
    def format_path(path):
        try:
            rel_path = os.path.relpath(path)
            parts = rel_path.split(os.sep)
            if len(parts) > max_path_level:
                return os.sep.join(['...'] + parts[-max_path_level:])
            return rel_path
        except ValueError:
            return path

    # Process each line of the traceback
    formatted_lines = []
    level = 0
    
    for line in tb_list:
        if 'File "' in line:
            # Format file paths in traceback
            path_start = line.find('File "') + 6
            path_end = line.find('"', path_start)
            original_path = line[path_start:path_end]
            formatted_path = format_path(original_path)
            line = line[:path_start] + formatted_path + line[path_end:]
            
            level += 1
            if level > max_level:
                formatted_lines.append("  [... additional stack frames truncated ...]\n")
                break
                
        formatted_lines.append(line)
    
    # Join all lines and remove any extra whitespace
    return ''.join(formatted_lines).strip()