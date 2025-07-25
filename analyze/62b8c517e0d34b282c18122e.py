def extostr(cls, e, max_level=30, max_path_level=5):
    import traceback

    # Get the exception type and message
    exc_type = type(e).__name__
    exc_message = str(e)

    # Get the traceback information
    tb = traceback.extract_tb(e.__traceback__)
    tb_info = []

    # Limit the traceback to max_level
    for frame in tb[:max_level]:
        filename, lineno, funcname, code = frame
        tb_info.append(f'File "{filename}", line {lineno}, in {funcname}\n    {code}')

    # Join the traceback information
    tb_str = "\n".join(tb_info)

    # Format the final output
    result = f"{exc_type}: {exc_message}\nTraceback (most recent call last):\n{tb_str}"

    # Limit the output to max_path_level if necessary
    if len(tb_info) > max_path_level:
        result += f"\n... (truncated to {max_path_level} frames)"

    return result