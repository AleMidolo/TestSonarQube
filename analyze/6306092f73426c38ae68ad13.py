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
    import subprocess
    import os

    # Build base command
    cmd = ['ansible-playbook', playbook_path]

    # Add verbosity if specified
    if verbose:
        verbosity = '-' + ('v' * verbose)
        cmd.append(verbosity)

    # Add extra vars if provided
    if extra_vars:
        extra_vars_arg = '--extra-vars'
        for key, value in extra_vars.items():
            cmd.extend([extra_vars_arg, f"{key}={value}"])

    # Add any additional ansible arguments
    if ansible_args:
        for arg, value in ansible_args.items():
            if value is True:
                cmd.append(f"--{arg}")
            elif value:
                cmd.extend([f"--{arg}", str(value)])

    # Set environment variables from workspace if available
    env = os.environ.copy()
    if hasattr(ir_workspace, 'ansible_config'):
        env['ANSIBLE_CONFIG'] = ir_workspace.ansible_config

    # Set inventory from workspace if available
    if hasattr(ir_workspace, 'inventory'):
        cmd.extend(['-i', ir_workspace.inventory])

    # Execute ansible-playbook command
    try:
        process = subprocess.Popen(
            cmd,
            env=env,
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