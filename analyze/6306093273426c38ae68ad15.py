import subprocess

def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    使用 `vars` 字典运行 Ansible CLI。

    :param vars_dict: dict, 将作为 Ansible 的 extra-vars 传递
    :param cli_args: list, 命令行参数列表
    :param ir_workspace: 一个表示当前活动的工作区的Infrared Workspace 对象
    :param ir_plugin: 一个表示当前插件的InfraredPlugin 对象
    :return: ansible 的结果
    """
    # 将 vars_dict 转换为 Ansible 的 extra-vars 格式
    extra_vars = " ".join([f"{key}={value}" for key, value in vars_dict.items()])
    
    # 构建完整的 Ansible 命令
    command = ["ansible-playbook"] + cli_args + ["-e", extra_vars]
    
    # 运行 Ansible 命令并捕获输出
    result = subprocess.run(command, capture_output=True, text=True)
    
    # 返回 Ansible 的结果
    return result