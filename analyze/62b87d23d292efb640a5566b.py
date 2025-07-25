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
    
    # 如果verbose为True,打印执行的命令
    if verbose:
        print(f"Running command: {' '.join(cmd)}")
    
    try:
        # 执行命令
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=stderr,
            cwd=cwd,
            env=env,
            universal_newlines=True
        )
        
        # 获取输出
        output, error = process.communicate()
        
        # 检查返回码
        if process.returncode != 0:
            if error and not hide_stderr:
                print(f"Error: {error}", file=sys.stderr)
            raise subprocess.CalledProcessError(process.returncode, cmd)
            
        return output.strip()
        
    except (OSError, subprocess.CalledProcessError) as e:
        print(f"Command failed: {e}", file=sys.stderr)
        raise