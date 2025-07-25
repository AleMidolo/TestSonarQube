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
    import subprocess
    import json

    # Prepare the command
    command = ['ansible-playbook'] + cli_args
    if vars_dict:
        extra_vars = json.dumps(vars_dict)
        command += ['--extra-vars', extra_vars]

    # Set the working directory to the Infrared workspace
    workspace_path = ir_workspace.path
    result = subprocess.run(command, cwd=workspace_path, capture_output=True, text=True)

    # Check for errors
    if result.returncode != 0:
        raise RuntimeError(f"Ansible playbook failed: {result.stderr}")

    # Parse the results
    return json.loads(result.stdout)