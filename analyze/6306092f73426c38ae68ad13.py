def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None,
                     extra_vars=None, ansible_args=None):
    """
    Wraps the 'ansible-playbook' CLI.

    :param ir_workspace: An Infrared Workspace object represents the active
    workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :param playbook_path: the playbook to invoke
    :param verbose: Ansible verbosity level
    :param extra_vars: dict. Passed to Ansible as extra-vars
    :param ansible_args: dict of ansible-playbook arguments to plumb down
        directly to Ansible.
    """
    # Initialize command list with base ansible-playbook command
    cmd = ['ansible-playbook']

    # Add playbook path
    cmd.append(playbook_path)

    # Add verbosity if specified
    if verbose:
        verbosity = '-' + ('v' * verbose)
        cmd.append(verbosity)

    # Add extra vars if provided
    if extra_vars:
        cmd.append('--extra-vars')
        extra_vars_str = ' '.join([f"{k}={v}" for k, v in extra_vars.items()])
        cmd.append(f"'{extra_vars_str}'")

    # Add inventory file from workspace
    if hasattr(ir_workspace, 'inventory'):
        cmd.extend(['-i', ir_workspace.inventory])

    # Add any additional ansible arguments
    if ansible_args:
        for arg, value in ansible_args.items():
            if value is True:
                cmd.append(f"--{arg}")
            elif value:
                cmd.extend([f"--{arg}", str(value)])

    # Convert command list to string
    cmd_str = ' '.join(cmd)

    # Execute ansible-playbook command
    import subprocess
    try:
        process = subprocess.Popen(
            cmd_str,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            raise Exception(f"Ansible playbook execution failed: {stderr}")
            
        return stdout
        
    except Exception as e:
        raise Exception(f"Failed to execute ansible-playbook: {str(e)}")