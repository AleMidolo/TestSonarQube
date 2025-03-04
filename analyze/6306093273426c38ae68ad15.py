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
        ansible_args.extend(['--extra-vars', f'@{extra_vars_file}'])

        if ir_workspace:
            # Add inventory file if workspace has one
            inventory_file = os.path.join(ir_workspace.path, 'hosts')
            if os.path.exists(inventory_file):
                ansible_args.extend(['-i', inventory_file])

        if ir_plugin:
            # Add plugin specific playbook directory
            playbook_dir = os.path.join(ir_plugin.path, 'playbooks')
            if os.path.exists(playbook_dir):
                ansible_args.append(playbook_dir)

        # Initialize Ansible components
        loader = DataLoader()
        inventory = InventoryManager(loader=loader)
        variable_manager = VariableManager(loader=loader, inventory=inventory)

        # Run playbook
        playbook = PlaybookCLI(ansible_args)
        playbook.parse()
        return playbook.run()

    finally:
        # Cleanup temporary file
        if os.path.exists(extra_vars_file):
            os.unlink(extra_vars_file)