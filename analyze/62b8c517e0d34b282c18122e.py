def extostr(cls, e, max_level=30, max_path_level=5):
    """
    Format an exception.
    :param e: Any exception instance.
    :type e: Exception 
    :param max_level: Maximum call stack level (default 30)
    :type max_level: int
    :param max_path_level: Maximum path level (default 5)
    :type max_path_level: int
    :return The exception readable string
    :rtype str
    """
    import traceback
    import os

    # Get the full traceback
    tb_list = traceback.extract_tb(e.__traceback__)
    
    # Format the exception message
    exception_str = f"{type(e).__name__}: {str(e)}\n\n"
    
    # Add stack trace info
    for i, tb in enumerate(tb_list[:max_level]):
        filename = tb.filename
        
        # Shorten path if needed
        if max_path_level > 0:
            path_parts = filename.split(os.sep)
            if len(path_parts) > max_path_level:
                filename = os.sep.join(['...'] + path_parts[-max_path_level:])
        
        # Add formatted stack trace line
        exception_str += f"  File \"{filename}\", line {tb.lineno}, in {tb.name}\n"
        if tb.line:
            exception_str += f"    {tb.line}\n"
            
    return exception_str