def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    import subprocess
    import json

    # Prepare the command
    command = ['ansible-playbook'] + cli_args
    if vars_dict:
        extra_vars = ' '.join(f"{key}={value}" for key, value in vars_dict.items())
        command += ['--extra-vars', extra_vars]

    # Set the working directory to the Infrared workspace
    workspace_path = ir_workspace.path
    result = subprocess.run(command, cwd=workspace_path, capture_output=True, text=True)

    # Parse the results
    if result.returncode != 0:
        raise RuntimeError(f"Ansible playbook failed: {result.stderr}")

    return json.loads(result.stdout)