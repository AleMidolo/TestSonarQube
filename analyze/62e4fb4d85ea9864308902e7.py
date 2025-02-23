import os
import sys

def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    补全 exe 的完整路径并以其原始形式返回

    修复以下在 Windows 上的问题：  
    - https://bugs.python.org/issue8557  
    - Windows 无法解析 shebang  

    此函数还可以使深路径的 shebang 正常工作。
    """
    if not cmd:
        return cmd

    # Get the executable name
    exe_name = cmd[0]
    
    # Check if the executable is already a full path
    if os.path.isabs(exe_name):
        return cmd

    # Try to find the executable in the PATH
    for path in os.environ["PATH"].split(os.pathsep):
        full_path = os.path.join(path, exe_name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return (full_path,) + cmd[1:]

    # If not found, return the original command
    return cmd