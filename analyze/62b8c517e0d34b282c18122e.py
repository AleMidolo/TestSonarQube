def extostr(cls, e, max_level=30, max_path_level=5):
    import traceback

    def format_exception(exc, level, path_level):
        if level > max_level:
            return f"{exc.__class__.__name__}: {str(exc)}\n"

        tb_lines = traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        formatted_tb = ''.join(tb_lines)

        if path_level > max_path_level:
            return f"{exc.__class__.__name__}: {str(exc)}\n"

        return formatted_tb

    return format_exception(e, 0, 0)