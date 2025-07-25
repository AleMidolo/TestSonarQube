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
    from ansible.cli.playbook import PlaybookCLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    
    # Crea un file temporaneo per le extra vars
    extra_vars_file = os.path.join(ir_workspace.path, 'extra_vars.json')
    with open(extra_vars_file, 'w') as f:
        json.dump(vars_dict, f)

    # Costruisci gli argomenti per Ansible
    ansible_args = ['ansible-playbook']
    ansible_args.extend(cli_args)
    ansible_args.extend(['--extra-vars', '@' + extra_vars_file])
    
    # Aggiungi l'inventory se specificato nel workspace
    if ir_workspace.inventory:
        ansible_args.extend(['-i', ir_workspace.inventory])
    
    # Configura Ansible
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    
    # Esegui il playbook
    playbook = PlaybookCLI(ansible_args)
    playbook.parse()
    
    try:
        result = playbook.run()
        
        # Pulisci il file temporaneo
        if os.path.exists(extra_vars_file):
            os.remove(extra_vars_file)
            
        return result
        
    except Exception as e:
        # Pulisci il file temporaneo anche in caso di errore
        if os.path.exists(extra_vars_file):
            os.remove(extra_vars_file)
        raise Exception(f"Errore durante l'esecuzione del playbook: {str(e)}")