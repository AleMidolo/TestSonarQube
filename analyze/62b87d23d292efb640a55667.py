def register_vcs_handler(vcs, method):  # decorator
    """Create decorator to mark a method as the handler of a VCS.

    Args:
        vcs: The version control system name
        method: The method name to handle

    Returns:
        A decorator function that registers the handler
    """
    def decorate(f):
        # Store the handler function in the registry
        if not hasattr(decorate, '_registry'):
            decorate._registry = {}
            
        if vcs not in decorate._registry:
            decorate._registry[vcs] = {}
            
        decorate._registry[vcs][method] = f
        return f
        
    return decorate