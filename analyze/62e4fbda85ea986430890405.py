import subprocess
import sys
import os
import shlex
from typing import Sequence, Any

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
        return (1, b"No command provided")

    # Split the varargs into chunks based on target_concurrency
    chunk_size = (len(varargs) + target_concurrency - 1) // target_concurrency
    chunks = [varargs[i:i + chunk_size] for i in range(0, len(varargs), chunk_size)]

    results = []
    for chunk in chunks:
        full_cmd = list(cmd) + list(chunk)
        try:
            if color and sys.platform != "win32":
                import pty
                master, slave = pty.openpty()
                process = subprocess.Popen(
                    full_cmd,
                    stdout=slave,
                    stderr=slave,
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
            else:
                process = subprocess.Popen(
                    full_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    **kwargs
                )
                output, _ = process.communicate()
                return_code = process.returncode
            results.append((return_code, output))
        except Exception as e:
            results.append((1, str(e).encode()))

    # Return the result of the last command executed
    return results[-1] if results else (1, b"No commands executed")

def _get_platform_max_length() -> int:
    """Get the maximum command length allowed by the platform."""
    if sys.platform == "win32":
        return 8191
    else:
        return 131072  # Typical limit on Unix-like systems