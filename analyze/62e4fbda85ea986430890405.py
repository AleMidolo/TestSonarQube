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
    if color and sys.platform != 'linux':
        raise NotImplementedError("Color mode is only supported on Linux.")

    if target_concurrency < 1:
        raise ValueError("target_concurrency must be at least 1.")

    # Split varargs into chunks based on target_concurrency
    chunk_size = (len(varargs) + target_concurrency - 1) // target_concurrency
    chunks = [varargs[i:i + chunk_size] for i in range(0, len(varargs), chunk_size)]

    results = []
    for chunk in chunks:
        full_cmd = list(cmd) + list(chunk)
        if color:
            # Use a pseudo-terminal for color output
            import pty
            master, slave = pty.openpty()
            process = subprocess.Popen(full_cmd, stdout=slave, stderr=slave, **kwargs)
            os.close(slave)
            output = b''
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
            # Regular subprocess call
            process = subprocess.Popen(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
            output, _ = process.communicate()
            return_code = process.returncode

        results.append((return_code, output))

    # Aggregate results
    final_return_code = max(rc for rc, _ in results)
    final_output = b''.join(output for _, output in results)

    return final_return_code, final_output

def _get_platform_max_length() -> int:
    """Get the maximum command length allowed by the platform."""
    if sys.platform == 'linux':
        return 131072  # Typical ARG_MAX on Linux
    elif sys.platform == 'darwin':
        return 262144  # Typical ARG_MAX on macOS
    else:
        return 32768  # Default for other platforms