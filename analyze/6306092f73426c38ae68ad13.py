import subprocess

def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None, extra_vars=None, ansible_args=None):
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
    # Base command
    command = ['ansible-playbook', playbook_path]

    # Add verbose level if specified
    if verbose:
        command.extend(['-' + 'v' * verbose])

    # Add extra-vars if specified
    if extra_vars:
        extra_vars_str = ' '.join([f"{k}={v}" for k, v in extra_vars.items()])
        command.extend(['--extra-vars', extra_vars_str])

    # Add additional ansible arguments if specified
    if ansible_args:
        for key, value in ansible_args.items():
            if value is True:
                command.append(f"--{key}")
            else:
                command.extend([f"--{key}", str(value)])

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Return the result
    return result