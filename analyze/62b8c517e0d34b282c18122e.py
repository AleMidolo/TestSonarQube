def extostr(cls, e, max_level=30, max_path_level=5):
    import traceback

    def format_exception(exc, level, path_level):
        if level > max_level or path_level > max_path_level:
            return f"{exc.__class__.__name__}: {str(exc)}"
        tb = traceback.extract_tb(exc.__traceback__)
        formatted_tb = []
        for frame in tb:
            formatted_tb.append(f"File \"{frame.filename}\", line {frame.lineno}, in {frame.name}")
        return "\n".join(formatted_tb) + f"\n{exc.__class__.__name__}: {str(exc)}"

    return format_exception(e, 0, 0)