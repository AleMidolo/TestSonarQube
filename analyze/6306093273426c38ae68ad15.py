def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    Ejecuta el CLI de Ansible con un diccionario de variables.

    :param vars_dict: dict, Será pasado como extra-vars de Ansible.
    :param cli_args: la lista de argumentos de línea de comandos.
    :param ir_workspace: Un objeto Infrared Workspace que representa el 
    espacio de trabajo activo.
    :param ir_plugin: Un objeto InfraredPlugin del plugin actual.
    :return: resultados de Ansible.
    """
    import subprocess
    import json

    # Convertir el diccionario de variables a formato JSON
    extra_vars = json.dumps(vars_dict)

    # Construir el comando de Ansible
    command = ['ansible-playbook'] + cli_args + ['--extra-vars', extra_vars]

    # Ejecutar el comando y capturar la salida
    result = subprocess.run(command, capture_output=True, text=True)

    # Procesar la salida
    if result.returncode != 0:
        raise RuntimeError(f"Ansible playbook failed: {result.stderr}")

    return result.stdout