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
    executable = cmd[0]

    # 检查是否是完整路径
    if os.path.isfile(executable):
        return cmd

    # 尝试查找可执行文件
    if sys.platform == "win32":
        # 在 Windows 上，使用 PATHEXT 环境变量来查找可执行文件
        pathext = os.environ.get('PATHEXT', '').split(';')
        for ext in pathext:
            full_path = f"{executable}{ext}"
            if os.path.isfile(full_path):
                return (full_path,) + cmd[1:]

        # 如果没有找到，尝试在 PATH 中查找
        for path in os.environ.get('PATH', '').split(os.pathsep):
            full_path = os.path.join(path, executable)
            if os.path.isfile(full_path):
                return (full_path,) + cmd[1:]

    else:
        # 在非 Windows 系统上，直接查找
        full_path = os.path.join(os.getcwd(), executable)
        if os.path.isfile(full_path):
            return (full_path,) + cmd[1:]

    return cmd