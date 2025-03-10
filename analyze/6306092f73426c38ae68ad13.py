import subprocess

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
    command = ['ansible-playbook', playbook_path]

    if verbose:
        command.append(f'-{verbose}')

    if extra_vars:
        extra_vars_str = ' '.join([f'{k}={v}' for k, v in extra_vars.items()])
        command.extend(['--extra-vars', extra_vars_str])

    if ansible_args:
        for arg, value in ansible_args.items():
            if value is True:
                command.append(f'--{arg}')
            else:
                command.extend([f'--{arg}', str(value)])

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ansible playbook execution failed: {e.stderr}")
        raise