import subprocess
import sys
import os
from typing import Sequence, Any, Tuple

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
    A simplified implementation of xargs.

    color: Make a pty if on a platform that supports it
    target_concurrency: Target number of partitions to run concurrently
    """
    if color and sys.platform != "win32":
        import pty
        master, slave = pty.openpty()
        kwargs['stdout'] = slave
        kwargs['stderr'] = slave
        kwargs['stdin'] = subprocess.PIPE

    processes = []
    for i in range(0, len(varargs), target_concurrency):
        chunk = varargs[i:i + target_concurrency]
        full_cmd = list(cmd) + list(chunk)
        process = subprocess.Popen(full_cmd, **kwargs)
        processes.append(process)

    for process in processes:
        process.wait()

    if color and sys.platform != "win32":
        os.close(slave)
        output = os.read(master, _max_length)
        os.close(master)
    else:
        output = b""

    return (0, output)

def _get_platform_max_length() -> int:
    if sys.platform == "win32":
        return 8192
    else:
        return 65536