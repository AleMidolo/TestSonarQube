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

    # 将 vars_dict 转换为 JSON 字符串，以便传递给 Ansible
    extra_vars = json.dumps(vars_dict)

    # 构建 Ansible 命令
    ansible_command = ["ansible-playbook"] + cli_args + ["-e", extra_vars]

    # 运行 Ansible 命令
    result = subprocess.run(ansible_command, capture_output=True, text=True)

    # 返回 Ansible 的结果
    return result