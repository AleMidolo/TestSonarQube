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

    # 获取命令的第一个元素
    command = cmd[0]
    
    # 检查命令是否是完整路径
    if os.path.isfile(command):
        return cmd

    # 尝试查找命令的完整路径
    if sys.platform == "win32":
        # 在 Windows 上，使用 PATHEXT 来查找可执行文件
        pathext = os.environ.get('PATHEXT', '').split(';')
        for ext in pathext:
            full_command = f"{command}{ext}"
            if os.path.isfile(full_command):
                return (full_command,) + cmd[1:]

    # 在其他平台上，使用 which 命令查找可执行文件
    else:
        from shutil import which
        full_command = which(command)
        if full_command:
            return (full_command,) + cmd[1:]

    return cmd