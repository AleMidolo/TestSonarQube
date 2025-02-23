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
    if os.name == 'nt':
        # Windows 系统
        path_env = os.environ.get('PATH', '').split(os.pathsep)
        for path in path_env:
            full_path = os.path.join(path, command + '.exe')
            if os.path.isfile(full_path):
                return (full_path,) + cmd[1:]
    else:
        # 非 Windows 系统
        full_path = os.path.join(os.getcwd(), command)
        if os.path.isfile(full_path):
            return (full_path,) + cmd[1:]

    return cmd