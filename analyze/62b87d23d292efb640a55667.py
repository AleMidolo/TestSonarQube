def register_vcs_handler(vcs, method):  # decorator
    """Create decorator to mark a method as the handler of a VCS."""

    def decorate(f):
        if not hasattr(register_vcs_handler, 'handlers'):
            register_vcs_handler.handlers = {}
        if vcs not in register_vcs_handler.handlers:
            register_vcs_handler.handlers[vcs] = {}
        register_vcs_handler.handlers[vcs][method] = f
        return f

    return decorate