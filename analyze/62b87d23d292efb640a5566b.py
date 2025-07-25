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
        output, error = process.communicate()
        
        # 打印详细信息
        if verbose:
            if output:
                print(output)
            if error and not hide_stderr:
                print(error, file=sys.stderr)
                
        # 检查返回码
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, cmd)
            
        return output.strip() if output else ""
        
    except (OSError, subprocess.CalledProcessError) as e:
        if verbose:
            print(f"Command execution failed: {e}", file=sys.stderr)
        raise