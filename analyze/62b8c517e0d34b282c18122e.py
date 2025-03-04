def extostr(cls, e, max_level=30, max_path_level=5):
    import traceback

    # Get the exception type and message
    exception_type = type(e).__name__
    exception_message = str(e)

    # Get the traceback information
    tb = traceback.extract_tb(e.__traceback__)
    tb_info = []

    # Limit the traceback to max_level
    for frame in tb[:max_level]:
        filename, lineno, funcname, text = frame
        tb_info.append(f'File "{filename}", line {lineno}, in {funcname}\n    {text}')

    # Join the traceback information
    tb_str = "\n".join(tb_info)

    # Format the final output
    formatted_exception = f"{exception_type}: {exception_message}\nTraceback (most recent call last):\n{tb_str}"

    # Limit the output to max_path_level if necessary
    if len(tb_info) > max_path_level:
        formatted_exception += f"\n... (truncated to {max_path_level} frames)"

    return formatted_exception