def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    提供了一组命令。使用子进程运行给定的命令及其参数。返回运行结果（标准输出和返回码）。
    
    调用给定的命令。
    """
    import subprocess
    import sys
    
    # 构建完整的命令列表
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
        stdout, stderr = process.communicate()
        return_code = process.returncode
        
        # 如果verbose为True,打印输出
        if verbose:
            if stdout:
                print(f"stdout:\n{stdout}")
            if stderr and not hide_stderr:
                print(f"stderr:\n{stderr}", file=sys.stderr)
            print(f"Return code: {return_code}")
            
        return stdout, return_code
        
    except Exception as e:
        if verbose:
            print(f"Error executing command: {e}", file=sys.stderr)
        return None, -1