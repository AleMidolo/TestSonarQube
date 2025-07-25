def register_vcs_handler(vcs, method):  # decorator
    """Create decorator to mark a method as the handler of a VCS.

    Args:
        vcs: The version control system to handle.
        method: The method to be used as the handler.

    Returns:
        A decorator function that marks the method as the handler for the specified VCS.
    """
    def decorate(f):
        f.vcs = vcs
        f.method = method
        return f
    return decorate