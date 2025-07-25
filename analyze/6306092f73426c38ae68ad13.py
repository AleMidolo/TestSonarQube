import subprocess

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
    # Construir el comando base
    command = ['ansible-playbook', playbook_path]

    # Agregar verbosidad si se especifica
    if verbose:
        command.append(f'-{"v" * verbose}')

    # Agregar extra_vars si se especifica
    if extra_vars:
        extra_vars_str = ' '.join([f'{k}={v}' for k, v in extra_vars.items()])
        command.extend(['--extra-vars', extra_vars_str])

    # Agregar argumentos adicionales de Ansible si se especifica
    if ansible_args:
        for key, value in ansible_args.items():
            command.append(f'--{key}')
            if value is not None:
                command.append(str(value))

    # Ejecutar el comando
    result = subprocess.run(command, capture_output=True, text=True)

    # Devolver la salida y el código de retorno
    return result.stdout, result.stderr, result.returncode