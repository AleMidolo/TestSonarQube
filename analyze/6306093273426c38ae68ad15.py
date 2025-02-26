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
    import subprocess
    import json

    # Convert vars_dict to JSON string for Ansible
    extra_vars = json.dumps(vars_dict)

    # Prepare the command to run Ansible
    command = ['ansible-playbook'] + cli_args + ['--extra-vars', extra_vars]

    # Run the command in the context of the Infrared workspace
    result = subprocess.run(command, cwd=ir_workspace.path, capture_output=True, text=True)

    # Check for errors
    if result.returncode != 0:
        raise RuntimeError(f"Ansible playbook failed: {result.stderr}")

    # Return the results
    return result.stdout