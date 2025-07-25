def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None,
                     extra_vars=None, ansible_args=None):
    """
    Avvolge il comando 'ansible-playbook' della CLI.

    :param ir_workspace: Un oggetto Infrared Workspace che rappresenta lo spazio di lavoro attivo
    :param ir_plugin: Un oggetto InfraredPlugin del plugin corrente 
    :param playbook_path: il percorso del playbook da eseguire
    :param verbose: Livello di verbosità di Ansible
    :param extra_vars: dict. Passato ad Ansible come extra-vars
    :param ansible_args: dizionario di argomenti per ansible-playbook da inoltrare
        direttamente ad Ansible.
    """
    
    # Inizializza la lista dei comandi base
    cmd = ['ansible-playbook', playbook_path]
    
    # Aggiungi il livello di verbosità se specificato
    if verbose:
        verbosity = '-' + ('v' * verbose)
        cmd.append(verbosity)
        
    # Aggiungi l'inventory file dallo workspace
    if ir_workspace and ir_workspace.inventory:
        cmd.extend(['-i', ir_workspace.inventory])
        
    # Gestisci le extra vars
    if extra_vars:
        for key, value in extra_vars.items():
            cmd.extend(['--extra-vars', f'{key}={value}'])
            
    # Aggiungi gli argomenti ansible aggiuntivi
    if ansible_args:
        for arg, value in ansible_args.items():
            if value is True:
                cmd.append(f'--{arg}')
            elif value is not False:
                cmd.extend([f'--{arg}', str(value)])
                
    # Esegui il comando ansible-playbook
    import subprocess
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            raise Exception(f"Ansible playbook execution failed: {stderr}")
            
        return stdout
        
    except Exception as e:
        raise Exception(f"Failed to execute ansible-playbook: {str(e)}")