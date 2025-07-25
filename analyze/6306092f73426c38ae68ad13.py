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
        extra_vars_arg = '--extra-vars'
        if isinstance(extra_vars, dict):
            # Convert dict to JSON string
            import json
            extra_vars = json.dumps(extra_vars)
        cmd.extend([extra_vars_arg, extra_vars])

    # Add any additional ansible arguments
    if ansible_args:
        for key, value in ansible_args.items():
            if value is True:
                # For flag arguments
                cmd.append(f"--{key}")
            elif value:
                # For arguments with values
                cmd.append(f"--{key}={value}")

    # Execute ansible-playbook command
    import subprocess
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            raise Exception(f"Ansible playbook execution failed:\n{stderr}")
            
        return stdout
        
    except Exception as e:
        raise Exception(f"Failed to execute ansible-playbook: {str(e)}")