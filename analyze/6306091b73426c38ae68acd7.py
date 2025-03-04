def ansible_config_manager(cls):
    """
    Gets the ansible config manager.
    """
    from ansible.config.manager import ConfigManager
    return ConfigManager()