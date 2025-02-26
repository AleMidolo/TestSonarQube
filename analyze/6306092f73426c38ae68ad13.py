def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None, extra_vars=None, ansible_args=None):
    """
    封装 'ansible-playbook' 命令行接口。
    :param ir_workspace: 一个 Infrared Workspace 对象，表示当前活动的工作区
    :param ir_plugin: 当前插件的一个 InfraredPlugin 对象
    :param playbook_path: 要调用的 playbook 文件路径
    :param verbose: Ansible 的详细级别
    :param extra_vars: dict。作为额外变量 (extra-vars) 传递给 Ansible
    :param ansible_args: ansible-playbook 参数的字典，直接传递给 Ansible
    """
    import subprocess
    import json

    command = ['ansible-playbook', playbook_path]

    if verbose is not None:
        command.append(f'-v' * verbose)

    if extra_vars:
        extra_vars_str = json.dumps(extra_vars)
        command.append(f'--extra-vars={extra_vars_str}')

    if ansible_args:
        for key, value in ansible_args.items():
            command.append(f'--{key}={value}')

    result = subprocess.run(command, cwd=ir_workspace.path, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Ansible playbook failed: {result.stderr}")

    return result.stdout