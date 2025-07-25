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

    # Get the exception traceback
    tb = sys.exc_info()[2]
    if tb is None:
        tb = e.__traceback__

    # Limit the traceback to max_level
    if tb is not None:
        tb_list = traceback.format_tb(tb)
        if len(tb_list) > max_level:
            tb_list = tb_list[:max_level]

    # Format the exception message
    exception_type = type(e).__name__
    exception_message = str(e)
    formatted_exception = f"{exception_type}: {exception_message}\n"

    # Add the traceback if available
    if tb is not None:
        formatted_exception += "Traceback (most recent call last):\n"
        formatted_exception += "".join(tb_list)

    # Limit the path levels in the traceback
    if max_path_level > 0:
        lines = formatted_exception.splitlines()
        for i in range(len(lines)):
            if "File" in lines[i] and "line" in lines[i]:
                path = lines[i].split(",")[0].split("File ")[1].strip()
                path_parts = path.split("/")
                if len(path_parts) > max_path_level:
                    path_parts = path_parts[-max_path_level:]
                    lines[i] = lines[i].replace(path, ".../" + "/".join(path_parts))
        formatted_exception = "\n".join(lines)

    return formatted_exception