def extostr(cls, e, max_level=30, max_path_level=5):
    import traceback

    # Get the exception type and message
    exc_type = type(e).__name__
    exc_message = str(e)

    # Format the exception header
    result = f"{exc_type}: {exc_message}\n"

    # Get the traceback
    tb = traceback.extract_tb(e.__traceback__)
    
    # Limit the traceback to max_level
    tb = tb[:max_level]

    # Format the traceback
    for frame in tb:
        filename, lineno, funcname, text = frame
        result += f"  File \"{filename}\", line {lineno}, in {funcname}\n"
        result += f"    {text}\n"

    # If the traceback is longer than max_path_level, truncate it
    if len(tb) > max_path_level:
        result += f"  ... (truncated to {max_path_level} frames)\n"

    return result