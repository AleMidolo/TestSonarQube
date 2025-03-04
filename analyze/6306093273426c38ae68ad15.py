def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    Esegue il comando Ansible CLI con un dizionario di variabili.

    :param vars_dict: dict, Sarà passato come extra-vars ad Ansible
    :param cli_args: la lista di argomenti della riga di comando
    :param ir_workspace: Un oggetto Infrared Workspace che rappresenta
                         lo spazio di lavoro attivo
    :param ir_plugin: Un oggetto InfraredPlugin del plugin corrente
    :return: risultati di Ansible
    """
    import os
    import json
    import tempfile
    from ansible.cli.playbook import PlaybookCLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Create temporary file for extra vars
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as vars_file:
        json.dump(vars_dict, vars_file)
        vars_file_path = vars_file.name

    try:
        # Construct Ansible CLI command
        ansible_args = ['ansible-playbook']
        ansible_args.extend(cli_args)
        ansible_args.extend(['--extra-vars', '@' + vars_file_path])

        # Set up Ansible environment
        loader = DataLoader()
        inventory = InventoryManager(loader=loader)
        variable_manager = VariableManager(loader=loader, inventory=inventory)

        # Initialize PlaybookCLI
        pbcli = PlaybookCLI(ansible_args)
        
        # Set workspace and plugin specific environment variables
        os.environ['IR_WORKSPACE'] = ir_workspace.path
        os.environ['IR_PLUGIN'] = ir_plugin.name

        # Run playbook
        results = pbcli.run()

        return results

    finally:
        # Clean up temporary vars file
        if os.path.exists(vars_file_path):
            os.unlink(vars_file_path)