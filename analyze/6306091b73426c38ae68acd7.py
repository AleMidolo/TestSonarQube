def ansible_config_manager(cls):  
    """
    Obtiene el administrador de configuración de Ansible.
    """
    from ansible.config.manager import ConfigManager
    return ConfigManager(cls)