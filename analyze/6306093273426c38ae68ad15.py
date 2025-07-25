import subprocess

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
    # Convertir el diccionario de variables a una cadena de extra-vars
    extra_vars = " ".join([f"{key}={value}" for key, value in vars_dict.items()])
    
    # Construir el comando de Ansible
    command = ["ansible-playbook"] + cli_args + ["--extra-vars", extra_vars]
    
    # Ejecutar el comando
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Retornar los resultados
    return result