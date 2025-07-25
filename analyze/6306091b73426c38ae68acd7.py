def ansible_config_manager(cls):
    """
    通过 `cls._get_service()` 中的 `ServiceName.ANSIBLE_CONFIG_MANAGER` 获取 Ansible 配置管理器。
    获取 Ansible 配置管理器。
    """
    return cls._get_service(ServiceName.ANSIBLE_CONFIG_MANAGER)