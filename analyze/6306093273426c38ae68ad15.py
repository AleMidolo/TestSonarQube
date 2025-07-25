def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    使用 `vars` 字典运行 Ansible CLI。

    :param vars_dict: dict, 将作为 Ansible 的 extra-vars 传递
    :param cli_args: list, 命令行参数列表 
    :param ir_workspace: 一个表示当前活动的工作区的Infrared Workspace 对象
    :param ir_plugin: 一个表示当前插件的InfraredPlugin 对象
    :return: ansible 的结果
    """
    import os
    import json
    import subprocess
    from tempfile import NamedTemporaryFile

    # 创建临时文件存储extra vars
    with NamedTemporaryFile(mode='w', suffix='.json', delete=False) as vars_file:
        json.dump(vars_dict, vars_file)
        vars_file_path = vars_file.name

    try:
        # 构建ansible-playbook命令
        cmd = ['ansible-playbook']
        
        # 添加命令行参数
        cmd.extend(cli_args)
        
        # 添加extra vars文件
        cmd.extend(['-e', '@' + vars_file_path])
        
        # 如果workspace有inventory文件,添加inventory参数
        if hasattr(ir_workspace, 'inventory') and ir_workspace.inventory:
            cmd.extend(['-i', ir_workspace.inventory])
            
        # 如果plugin有playbook路径,添加playbook参数    
        if hasattr(ir_plugin, 'playbook_path') and ir_plugin.playbook_path:
            cmd.append(ir_plugin.playbook_path)

        # 执行ansible-playbook命令
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            check=True
        )
        
        return result

    except subprocess.CalledProcessError as e:
        # 处理ansible执行错误
        raise Exception(f"Ansible playbook execution failed: {e.stderr}")
        
    finally:
        # 清理临时文件
        if os.path.exists(vars_file_path):
            os.unlink(vars_file_path)