def register_vcs_handler(vcs, method):  # decorator
    """Create decorator to mark a method as the handler of a VCS."""
    
    def decorate(f):
        f.vcs_handler = True
        f.vcs_type = vcs
        f.method = method
        return f
    
    return decorate