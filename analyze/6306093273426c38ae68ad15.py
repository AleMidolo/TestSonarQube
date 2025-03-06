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
    import shlex

    # 将 vars_dict 转换为 Ansible 的 extra-vars 格式
    extra_vars = " ".join([f"{key}={value}" for key, value in vars_dict.items()])

    # 构建完整的 Ansible 命令
    ansible_command = f"ansible-playbook {extra_vars} {' '.join(cli_args)}"

    # 使用 subprocess 运行 Ansible 命令
    process = subprocess.Popen(shlex.split(ansible_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # 返回 Ansible 的结果
    return {
        "stdout": stdout.decode("utf-8"),
        "stderr": stderr.decode("utf-8"),
        "returncode": process.returncode
    }