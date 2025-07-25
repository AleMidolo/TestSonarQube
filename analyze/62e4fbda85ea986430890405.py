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
    def _get_platform_max_length() -> int:
        if sys.platform == "win32":
            return 8191
        else:
            return 131072

    if _max_length is None:
        _max_length = _get_platform_max_length()

    if color and sys.platform != "win32":
        import pty
        master, slave = pty.openpty()
        kwargs['stdout'] = slave
        kwargs['stderr'] = slave

    results = []
    for i in range(0, len(varargs), target_concurrency):
        chunk = varargs[i:i + target_concurrency]
        full_cmd = cmd + tuple(chunk)
        try:
            process = subprocess.Popen(full_cmd, **kwargs)
            stdout, stderr = process.communicate()
            results.append((process.returncode, stdout))
        except subprocess.CalledProcessError as e:
            results.append((e.returncode, e.output))

    if color and sys.platform != "win32":
        os.close(master)
        os.close(slave)

    return results[0] if results else (0, b'')