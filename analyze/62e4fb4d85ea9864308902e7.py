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

    # 获取第一个命令（通常是可执行文件）
    executable = cmd[0]

    # 如果可执行文件已经是一个完整路径，直接返回
    if os.path.isabs(executable):
        return cmd

    # 尝试在 PATH 中查找可执行文件
    path = os.environ.get('PATH', '')
    for dir in path.split(os.pathsep):
        full_path = os.path.join(dir, executable)
        if os.path.isfile(full_path):
            # 找到可执行文件，返回完整路径的命令
            return (full_path,) + cmd[1:]

    # 如果未找到，返回原始命令
    return cmd