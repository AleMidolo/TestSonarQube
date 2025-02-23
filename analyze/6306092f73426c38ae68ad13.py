def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None, extra_vars=None, ansible_args=None):
    """
    Envuelve la interfaz de línea de comandos (CLI) de 'ansible-playbook'.

    :param ir_workspace: Un objeto Infrared Workspace que representa el espacio de trabajo activo.
    :param ir_plugin: Un objeto InfraredPlugin del plugin actual.
    :param playbook_path: La ruta del playbook que se va a ejecutar.
    :param verbose: Nivel de verbosidad de Ansible.
    :param extra_vars: dict. Se pasa a Ansible como extra-vars.
    :param ansible_args: dict de argumentos de ansible-playbook que se pasan directamente a Ansible.
    """
    import subprocess
    import json

    command = ['ansible-playbook', playbook_path]

    if verbose is not None:
        command.append(f'-v' * verbose)

    if extra_vars:
        extra_vars_str = ' '.join([f'{key}={value}' for key, value in extra_vars.items()])
        command.append(f'--extra-vars={extra_vars_str}')

    if ansible_args:
        for key, value in ansible_args.items():
            command.append(f'--{key}')
            if value is not None:
                command.append(str(value))

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing playbook: {e.stderr}"