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
    import subprocess

    # Costruisci il comando base
    command = ['ansible-playbook', playbook_path]

    # Aggiungi il livello di verbosità se specificato
    if verbose:
        command.extend(['-' + 'v' * verbose])

    # Aggiungi extra_vars se specificato
    if extra_vars:
        extra_vars_str = ' '.join([f"{k}={v}" for k, v in extra_vars.items()])
        command.extend(['--extra-vars', extra_vars_str])

    # Aggiungi ansible_args se specificato
    if ansible_args:
        for key, value in ansible_args.items():
            command.extend([f"--{key}", str(value)])

    # Esegui il comando
    result = subprocess.run(command, capture_output=True, text=True)

    # Gestisci l'output
    if result.returncode != 0:
        print(f"Errore durante l'esecuzione del playbook: {result.stderr}")
    else:
        print(f"Playbook eseguito con successo: {result.stdout}")