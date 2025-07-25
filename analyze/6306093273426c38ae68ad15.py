def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    Runs ansible cli with vars dict

    :param vars_dict: dict, Will be passed as Ansible extra-vars
    :param cli_args: the list  of command line arguments
    :param ir_workspace: An Infrared Workspace object represents the active
     workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :return: ansible results
    """
    # Convert vars_dict to extra vars format
    extra_vars = ['{}={}'.format(key, value) for key, value in vars_dict.items()]
    
    # Build ansible command
    ansible_cmd = ['ansible-playbook']
    
    # Add workspace inventory if exists
    if ir_workspace.inventory:
        ansible_cmd.extend(['-i', ir_workspace.inventory])
    
    # Add plugin playbook path
    ansible_cmd.append(ir_plugin.playbook_path)
    
    # Add extra vars
    if extra_vars:
        ansible_cmd.extend(['--extra-vars', ' '.join(extra_vars)])
    
    # Add any additional CLI arguments
    if cli_args:
        ansible_cmd.extend(cli_args)
    
    try:
        # Execute ansible command
        import subprocess
        process = subprocess.Popen(
            ansible_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        
        # Get output
        stdout, stderr = process.communicate()
        
        # Check return code
        if process.returncode != 0:
            raise Exception(f"Ansible playbook execution failed: {stderr}")
            
        # Parse and return results
        return {
            'status': 'SUCCESS',
            'return_code': process.returncode,
            'stdout': stdout,
            'stderr': stderr
        }
        
    except Exception as e:
        return {
            'status': 'FAILED',
            'error': str(e),
            'return_code': process.returncode if 'process' in locals() else None
        }