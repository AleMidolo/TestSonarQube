def ansible_config_manager(cls):  
    """
    Obtiene el administrador de configuración de Ansible.
    """
    from ansible import context
    from ansible.config.manager import ConfigManager

    # Initialize the Ansible context
    context.CLIARGS = dict()
    context.CLIARGS['inventory'] = None
    context.CLIARGS['module_path'] = None
    context.CLIARGS['forks'] = 5
    context.CLIARGS['timeout'] = 10
    context.CLIARGS['private_key_file'] = None
    context.CLIARGS['ssh_common_args'] = None
    context.CLIARGS['ssh_extra_args'] = None
    context.CLIARGS['ask_pass'] = False
    context.CLIARGS['ask_sudo_pass'] = False
    context.CLIARGS['ask_vault_pass'] = False
    context.CLIARGS['vault_password_files'] = None
    context.CLIARGS['become'] = False
    context.CLIARGS['become_method'] = None
    context.CLIARGS['become_user'] = None
    context.CLIARGS['verbosity'] = 0
    context.CLIARGS['check'] = False
    context.CLIARGS['diff'] = False

    # Create and return the Ansible ConfigManager
    return ConfigManager()