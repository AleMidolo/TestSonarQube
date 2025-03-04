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
    import os
    import json
    import subprocess
    from tempfile import NamedTemporaryFile

    # Crear archivo temporal para las variables extra
    with NamedTemporaryFile(mode='w', suffix='.json', delete=False) as vars_file:
        json.dump(vars_dict, vars_file)
        vars_file_path = vars_file.name

    try:
        # Construir comando base de ansible-playbook
        cmd = ['ansible-playbook']
        
        # Agregar argumentos de CLI
        cmd.extend(cli_args)
        
        # Agregar archivo de variables extra
        cmd.extend(['--extra-vars', f'@{vars_file_path}'])
        
        # Agregar inventario del workspace si existe
        if hasattr(ir_workspace, 'inventory'):
            cmd.extend(['-i', ir_workspace.inventory])
            
        # Agregar playbook principal del plugin
        if hasattr(ir_plugin, 'playbook'):
            cmd.append(ir_plugin.playbook)
            
        # Ejecutar ansible-playbook
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        
        # Capturar salida
        stdout, stderr = process.communicate()
        
        # Verificar código de salida
        if process.returncode != 0:
            raise Exception(f"Error ejecutando Ansible: {stderr}")
            
        return {
            'rc': process.returncode,
            'stdout': stdout,
            'stderr': stderr
        }
        
    finally:
        # Limpiar archivo temporal
        if os.path.exists(vars_file_path):
            os.unlink(vars_file_path)