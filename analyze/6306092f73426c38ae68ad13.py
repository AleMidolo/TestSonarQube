def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None,
                     extra_vars=None, ansible_args=None):
    import subprocess
    import json

    command = ['ansible-playbook', playbook_path]

    if verbose:
        command.append(f'-v{"v" * (verbose - 1)}')

    if extra_vars:
        command.append('--extra-vars')
        command.append(json.dumps(extra_vars))

    if ansible_args:
        for key, value in ansible_args.items():
            command.append(f'--{key}')
            command.append(str(value))

    result = subprocess.run(command, cwd=ir_workspace.path, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Ansible playbook failed: {result.stderr}")

    return result.stdout