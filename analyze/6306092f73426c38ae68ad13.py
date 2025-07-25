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
    import os
    import subprocess
    
    # 构建基本命令
    cmd = ['ansible-playbook', playbook_path]
    
    # 添加详细级别
    if verbose:
        if isinstance(verbose, bool):
            cmd.append('-v')
        elif isinstance(verbose, int):
            cmd.append('-' + 'v' * verbose)
            
    # 添加inventory文件
    if ir_workspace and hasattr(ir_workspace, 'inventory'):
        cmd.extend(['-i', ir_workspace.inventory])
        
    # 添加额外变量
    if extra_vars:
        for key, value in extra_vars.items():
            cmd.extend(['--extra-vars', f'{key}={value}'])
            
    # 添加其他ansible参数
    if ansible_args:
        for key, value in ansible_args.items():
            if value is True:
                cmd.append(f'--{key}')
            elif value is not None:
                cmd.extend([f'--{key}', str(value)])
                
    # 设置环境变量
    env = os.environ.copy()
    if ir_plugin and hasattr(ir_plugin, 'vars'):
        env.update(ir_plugin.vars)
        
    # 执行命令
    try:
        result = subprocess.run(
            cmd,
            env=env,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        return result
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ansible playbook execution failed: {e.stderr}")