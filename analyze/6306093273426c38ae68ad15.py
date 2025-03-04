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
    # Configurar argumentos de Ansible
    ansible_args = []
    
    # Agregar playbook path
    playbook_path = os.path.join(ir_plugin.path, 'main.yml')
    ansible_args.append(playbook_path)

    # Agregar inventory si existe en workspace
    if ir_workspace.inventory:
        ansible_args.extend(['-i', ir_workspace.inventory])

    # Agregar variables extra como JSON
    if vars_dict:
        extra_vars = json.dumps(vars_dict)
        ansible_args.extend(['--extra-vars', extra_vars])

    # Agregar argumentos CLI adicionales
    if cli_args:
        ansible_args.extend(cli_args)

    try:
        # Configurar entorno
        os.environ['ANSIBLE_CONFIG'] = os.path.join(ir_plugin.path, 'ansible.cfg')
        
        # Ejecutar ansible-playbook
        ansible = ansible_playbook.AnsiblePlaybook(
            playbook=playbook_path,
            inventory=ir_workspace.inventory,
            extra_vars=vars_dict,
            verbosity=1
        )
        
        # Ejecutar y obtener resultados
        results = ansible.run()
        
        return results

    except Exception as e:
        raise Exception(f"Error ejecutando playbook: {str(e)}")
    
    finally:
        # Limpiar entorno
        if 'ANSIBLE_CONFIG' in os.environ:
            del os.environ['ANSIBLE_CONFIG']