def workspace_manager(cls):
    """
    Obtiene el gestor de espacios de trabajo.
    """
    if not hasattr(cls, '_workspace_manager'):
        from workspace.manager import WorkspaceManager
        cls._workspace_manager = WorkspaceManager()
    return cls._workspace_manager