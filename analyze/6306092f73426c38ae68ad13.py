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
    cmd = ['ansible-playbook', playbook_path]
    
    # Agregar nivel de verbosidad si está especificado
    if verbose:
        if isinstance(verbose, bool):
            cmd.append('-v')
        elif isinstance(verbose, int):
            cmd.append('-' + 'v' * verbose)
            
    # Agregar variables extra si existen
    if extra_vars:
        for key, value in extra_vars.items():
            cmd.extend(['--extra-vars', f'{key}={value}'])
            
    # Agregar inventario del workspace
    if hasattr(ir_workspace, 'inventory'):
        cmd.extend(['-i', ir_workspace.inventory])
        
    # Agregar argumentos adicionales de ansible si existen
    if ansible_args:
        for arg, value in ansible_args.items():
            if value is True:
                cmd.append(f'--{arg}')
            elif value is not False:
                cmd.extend([f'--{arg}', str(value)])
                
    # Ejecutar el comando
    import subprocess
    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error ejecutando ansible-playbook: {e.stderr}")