def register_vcs_handler(vcs, method):  # decorator
    """Create decorator to mark a method as the handler of a VCS.

    Args:
        vcs: The version control system to handle.
        method: The method to be marked as the handler.

    Returns:
        A decorator function that marks the method as the handler for the specified VCS.
    """
    def decorate(f):
        if not hasattr(f, '_vcs_handlers'):
            f._vcs_handlers = {}
        f._vcs_handlers[vcs] = method
        return f
    return decorate