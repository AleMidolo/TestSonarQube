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

    # Split varargs into chunks based on target_concurrency
    chunk_size = (len(varargs) + target_concurrency - 1) // target_concurrency
    chunks = [varargs[i:i + chunk_size] for i in range(0, len(varargs), chunk_size)]

    exit_code = 0
    output = b""

    for chunk in chunks:
        full_cmd = list(cmd) + list(chunk)
        try:
            process = subprocess.Popen(full_cmd, **kwargs)
            stdout, stderr = process.communicate()
            output += stdout if stdout else b""
            output += stderr if stderr else b""
            if process.returncode != 0:
                exit_code = process.returncode
        except Exception as e:
            output += str(e).encode()
            exit_code = 1

    if color and sys.platform != "win32":
        os.close(master)
        os.close(slave)

    return exit_code, output

def _get_platform_max_length() -> int:
    """Get the maximum command length allowed by the platform."""
    if sys.platform == "win32":
        return 8191  # Windows command line length limit
    else:
        return 131072  # Common limit on Unix-like systems