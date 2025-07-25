def ansible_config_manager(cls):
    """
    Ottiene il gestore di configurazione Ansible.
    """
    from ansible.config.manager import ConfigManager
    return ConfigManager()