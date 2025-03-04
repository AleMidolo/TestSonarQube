def workspace_manager(cls):
    """
    वर्कस्पेस मैनेजर प्राप्त करता है।
    """
    if not hasattr(cls, '_workspace_manager'):
        from workspace_manager import WorkspaceManager
        cls._workspace_manager = WorkspaceManager()
    return cls._workspace_manager