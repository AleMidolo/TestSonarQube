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
        _max_length: int = os.get_terminal_size().columns if sys.platform != "win32" else 80,
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
        args = list(cmd) + list(varargs[i:i + target_concurrency])
        process = subprocess.Popen(args, **kwargs)
        processes.append(process)

    output = b""
    for process in processes:
        process.wait()
        if color and sys.platform != "win32":
            os.close(slave)
            output += os.read(master, _max_length)
            os.close(master)
        else:
            output += process.communicate()[0]

    return (process.returncode, output)