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
    import json

    command = ['ansible-playbook', playbook_path]

    if verbose:
        command.append(f'-v' * verbose)

    if extra_vars:
        extra_vars_str = ' '.join(f'--extra-vars="{k}={v}"' for k, v in extra_vars.items())
        command.append(extra_vars_str)

    if ansible_args:
        for key, value in ansible_args.items():
            command.append(f'--{key}')
            if value is not None:
                command.append(str(value))

    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return {"error": str(e), "output": e.output}