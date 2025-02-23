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
    import json

    command = ['ansible-playbook', playbook_path]

    if verbose:
        command.append(f'-v' * verbose)

    if extra_vars:
        extra_vars_str = ' '.join(f'--extra-vars="{key}={value}"' for key, value in extra_vars.items())
        command.append(extra_vars_str)

    if ansible_args:
        for key, value in ansible_args.items():
            command.append(f'--{key}')
            if value is not None:
                command.append(str(value))

    result = subprocess.run(command, capture_output=True, text=True, cwd=ir_workspace.path)

    if result.returncode != 0:
        raise RuntimeError(f"Ansible playbook failed: {result.stderr}")

    return json.loads(result.stdout)