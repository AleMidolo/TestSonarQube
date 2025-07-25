def workspace_manager(cls):
    """
    Gets the workspace manager.
    """
    if not hasattr(cls, '_workspace_manager'):
        cls._workspace_manager = WorkspaceManager()
    return cls._workspace_manager