import subprocess
import sys
import os
import shlex
from typing import Sequence, Any

def _get_platform_max_length() -> int:
    # 获取平台的最大命令行长度
    if sys.platform == "win32":
        return 8191
    else:
        return 131072  # 128 KB

def xargs(
    cmd: tuple[str, ...],
    varargs: Sequence[str],
    *,
    color: bool = False,
    target_concurrency: int = 1,
    _max_length: int = _get_platform_max_length(),
    **kwargs: Any,
) -> tuple[int, bytes]:
    """
    在 Linux 中简化实现 Xargs
    一个简化版的 xargs 实现。

    color: 如果运行在支持的操作系统平台上，创建一个伪终端（pty）。
    target_concurrency: 目标并发分区的数量。
    """
    if not cmd:
        raise ValueError("cmd must not be empty")
    
    if not varargs:
        return (0, b"")

    # 将命令和参数拼接成字符串
    cmd_str = " ".join(shlex.quote(arg) for arg in cmd)
    varargs_str = " ".join(shlex.quote(arg) for arg in varargs)

    # 检查总长度是否超过最大长度
    total_length = len(cmd_str) + len(varargs_str) + 1  # +1 for space
    if total_length > _max_length:
        raise ValueError(f"Command length exceeds platform limit of {_max_length} characters")

    # 构建完整的命令
    full_cmd = f"{cmd_str} {varargs_str}"

    # 如果 color 为 True，尝试使用伪终端
    if color and sys.platform != "win32":
        import pty
        master, slave = pty.openpty()
        process = subprocess.Popen(
            full_cmd,
            shell=True,
            stdout=slave,
            stderr=slave,
            close_fds=True,
            **kwargs
        )
        os.close(slave)
        output = b""
        while True:
            try:
                data = os.read(master, 1024)
                if not data:
                    break
                output += data
            except OSError:
                break
        os.close(master)
        return_code = process.wait()
        return (return_code, output)
    else:
        # 不使用伪终端
        process = subprocess.Popen(
            full_cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            **kwargs
        )
        stdout, stderr = process.communicate()
        return (process.returncode, stdout)