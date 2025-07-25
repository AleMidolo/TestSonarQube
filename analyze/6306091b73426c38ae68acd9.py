def workspace_manager(cls):
    """
    通过 `cls._get_service(ServiceName.WORKSPACE_MANAGER)` 获取工作区管理器
    获取工作区管理器。
    """
    return cls._get_service(ServiceName.WORKSPACE_MANAGER)