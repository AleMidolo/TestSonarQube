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
    
    # 运行命令
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
        returncode = process.returncode
        
        # 如果verbose为True,打印输出
        if verbose:
            if stdout:
                print(stdout)
            if stderr and not hide_stderr:
                print(stderr, file=sys.stderr)
                
        return stdout, returncode
        
    except Exception as e:
        if verbose:
            print(f"Error executing command: {e}", file=sys.stderr)
        return None, -1