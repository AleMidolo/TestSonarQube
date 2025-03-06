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

    # Convert the vars_dict to a string format suitable for extra-vars
    extra_vars = " ".join([f"{key}={value}" for key, value in vars_dict.items()])

    # Construct the full command
    command = ["ansible-playbook"] + cli_args + ["--extra-vars", extra_vars]

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Return the result
    return result