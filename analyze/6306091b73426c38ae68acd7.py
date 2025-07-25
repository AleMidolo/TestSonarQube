def ansible_config_manager(cls):
    """
    ansible कॉन्फ़िगरेशन मैनेजर प्राप्त करता है।
    """
    from ansible.config.manager import ConfigManager
    return ConfigManager()