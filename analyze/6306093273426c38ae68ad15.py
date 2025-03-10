import subprocess

def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    Runs ansible cli with vars dict

    :param vars_dict: dict, Will be passed as Ansible extra-vars
    :param cli_args: the list of command line arguments
    :param ir_workspace: An Infrared Workspace object represents the active workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :return: ansible results
    """
    # Convert vars_dict to a string format suitable for ansible extra-vars
    extra_vars = " ".join([f"{key}={value}" for key, value in vars_dict.items()])
    
    # Construct the full command
    command = ["ansible-playbook"] + cli_args + ["--extra-vars", extra_vars]
    
    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Return the result
    return result