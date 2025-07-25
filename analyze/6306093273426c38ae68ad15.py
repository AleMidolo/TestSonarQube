def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    使用 `vars` 字典运行 Ansible CLI。

    :param vars_dict: dict, 将作为 Ansible 的 extra-vars 传递
    :param cli_args: list, 命令行参数列表
    :param ir_workspace: 一个表示当前活动的工作区的Infrared Workspace 对象
    :param ir_plugin: 一个表示当前插件的InfraredPlugin 对象
    :return: ansible 的结果
    """
    import subprocess
    import json

    # Prepare the command
    command = ['ansible-playbook'] + cli_args
    if vars_dict:
        command += ['--extra-vars', json.dumps(vars_dict)]

    # Run the command in the context of the Infrared workspace and plugin
    result = subprocess.run(command, capture_output=True, text=True, cwd=ir_workspace.path)

    # Check for errors
    if result.returncode != 0:
        raise RuntimeError(f"Ansible playbook failed: {result.stderr}")

    return result.stdout