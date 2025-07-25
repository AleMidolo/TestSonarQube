def workspace_manager(cls):
    """
    Obtiene el gestor de espacios de trabajo.
    """
    # Assuming cls has a method or attribute to get the workspace manager
    return cls.get_workspace_manager() if hasattr(cls, 'get_workspace_manager') else None