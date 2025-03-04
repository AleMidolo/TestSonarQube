def register_vcs_handler(vcs, method):  # decorator
    """Create decorator to mark a method as the handler of a VCS.

    Args:
        vcs: The version control system name
        method: The method name to handle

    Returns:
        A decorator function that registers the handler
    """
    def decorate(f):
        # Store the handler in the function's attributes
        if not hasattr(f, '_vcs_handlers'):
            f._vcs_handlers = {}
        f._vcs_handlers[(vcs, method)] = True
        return f
    return decorate