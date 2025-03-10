import subprocess

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
    # Base command
    command = ['ansible-playbook', playbook_path]

    # Add verbosity if specified
    if verbose:
        command.extend(['-' + 'v' * verbose])

    # Add extra-vars if specified
    if extra_vars:
        extra_vars_str = ' '.join([f"{k}={v}" for k, v in extra_vars.items()])
        command.extend(['--extra-vars', extra_vars_str])

    # Add additional ansible arguments if specified
    if ansible_args:
        for arg, value in ansible_args.items():
            command.extend([f"--{arg}", str(value)])

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Return the result
    return result