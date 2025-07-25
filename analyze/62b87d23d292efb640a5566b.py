def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    执行指定的命令。
    """
    import subprocess
    import sys
    
    # 构建完整命令
    if isinstance(commands, str):
        commands = [commands]
    cmd = commands + args if args else commands
    
    # 设置stderr重定向
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
    
    # 执行命令
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=stderr,
            cwd=cwd,
            env=env,
            universal_newlines=True
        )
        
        # 获取输出
        stdout, stderr = process.communicate()
        
        # 打印详细信息
        if verbose:
            if stdout:
                print(stdout)
            if stderr and not hide_stderr:
                print(stderr, file=sys.stderr)
                
        # 检查返回码
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, cmd)
            
        return stdout.strip() if stdout else ""
        
    except (OSError, subprocess.CalledProcessError) as e:
        if verbose:
            print(f"Command failed: {e}", file=sys.stderr)
        raise