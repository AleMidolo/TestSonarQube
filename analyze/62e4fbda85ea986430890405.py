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
    Un'implementazione semplificata di xargs.

    - **color**: Crea un pty se si è su una piattaforma che lo supporta.
    - **target_concurrency**: Numero target di partizioni da eseguire in parallelo.
    """
    if color and sys.platform != "win32":
        import pty
        master, slave = pty.openpty()
        kwargs['stdout'] = slave
        kwargs['stderr'] = slave

    processes = []
    for i in range(0, len(varargs), target_concurrency):
        chunk = varargs[i:i + target_concurrency]
        if color and sys.platform != "win32":
            process = subprocess.Popen(cmd + tuple(chunk), **kwargs)
        else:
            process = subprocess.Popen(cmd + tuple(chunk), **kwargs)
        processes.append(process)

    exit_codes = []
    outputs = []
    for process in processes:
        stdout, stderr = process.communicate()
        exit_codes.append(process.returncode)
        outputs.append(stdout)

    if color and sys.platform != "win32":
        os.close(master)
        os.close(slave)

    return max(exit_codes), b''.join(outputs)

def _get_platform_max_length() -> int:
    if sys.platform == "win32":
        return 8191
    else:
        return 131072