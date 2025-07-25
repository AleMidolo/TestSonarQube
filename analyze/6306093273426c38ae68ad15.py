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
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
        json.dump(vars_dict, tmp)
        extra_vars_file = tmp.name

    try:
        # Construct Ansible CLI command
        ansible_args = ['ansible-playbook']
        ansible_args.extend(cli_args)
        
        # Add workspace inventory if exists
        if ir_workspace and hasattr(ir_workspace, 'inventory'):
            ansible_args.extend(['-i', ir_workspace.inventory])
        
        # Add extra vars file
        ansible_args.extend(['--extra-vars', f'@{extra_vars_file}'])

        # Initialize Ansible components
        loader = DataLoader()
        inventory = InventoryManager(loader=loader, sources=ir_workspace.inventory)
        variable_manager = VariableManager(loader=loader, inventory=inventory)

        # Create and run playbook CLI
        pbcli = PlaybookCLI(ansible_args)
        pbcli.parse()
        return pbcli.run()

    finally:
        # Cleanup temporary file
        if os.path.exists(extra_vars_file):
            os.unlink(extra_vars_file)