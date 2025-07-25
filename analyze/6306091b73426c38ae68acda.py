def plugins_manager(cls):
    """
    通过 `cls._get_service()` 中的 `ServiceName.PLUGINS_MANAGER` 获取插件管理器。
    获取插件管理器。
    """
    return cls._get_service(ServiceName.PLUGINS_MANAGER)