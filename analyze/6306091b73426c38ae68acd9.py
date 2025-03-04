def workspace_manager(cls):
    """
    Ottiene il gestore dello spazio di lavoro.
    """
    if not hasattr(cls, '_workspace_manager'):
        from workspace.manager import WorkspaceManager
        cls._workspace_manager = WorkspaceManager()
    return cls._workspace_manager