def workspace_manager(cls):
    """
    Gets the workspace manager.
    """
    return cls.workspace_manager if hasattr(cls, 'workspace_manager') else None