def extostr(cls, e, max_level=30, max_path_level=5):
    import traceback

    def format_exception(exc, level, path_level):
        if level > max_level:
            return f"{exc.__class__.__name__}: {exc}\n"
        
        tb_lines = traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        formatted = ''.join(tb_lines)

        if path_level > max_path_level:
            return formatted
        
        cause = getattr(exc, '__cause__', None)
        if cause:
            formatted += format_exception(cause, level + 1, path_level + 1)
        
        return formatted

    return format_exception(e, 0, 0)