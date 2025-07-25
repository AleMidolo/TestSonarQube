import subprocess

def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None, extra_vars=None, ansible_args=None):
    """
    Wraps the 'ansible-playbook' CLI.

    :param ir_workspace: An Infrared Workspace object represents the active workspace
    :param ir_plugin: An InfraredPlugin object of the current plugin
    :param playbook_path: the playbook to invoke
    :param verbose: Ansible verbosity level
    :param extra_vars: dict. Passed to Ansible as extra-vars
    :param ansible_args: dict of ansible-playbook arguments to plumb down directly to Ansible.
    """
    command = ["ansible-playbook", playbook_path]

    if verbose:
        command.append(f"-{verbose}")

    if extra_vars:
        extra_vars_str = " ".join([f"{k}={v}" for k, v in extra_vars.items()])
        command.extend(["--extra-vars", extra_vars_str])

    if ansible_args:
        for arg, value in ansible_args.items():
            if value is True:
                command.append(f"--{arg}")
            elif value is False:
                continue
            else:
                command.extend([f"--{arg}", str(value)])

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ansible playbook execution failed with error: {e}")
        raise