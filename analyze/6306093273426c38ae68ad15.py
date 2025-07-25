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

    # Costruire il comando Ansible
    ansible_command = ['ansible-playbook'] + cli_args
    if vars_dict:
        extra_vars = json.dumps(vars_dict)
        ansible_command += ['--extra-vars', extra_vars]

    # Eseguire il comando
    try:
        result = subprocess.run(ansible_command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr