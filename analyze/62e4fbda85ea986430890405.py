import subprocess
import sys
import os
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
    A simplified implementation of xargs.

    color: Make a pty if on a platform that supports it
    target_concurrency: Target number of partitions to run concurrently
    """
    if color and sys.platform != "win32":
        import pty
        master, slave = pty.openpty()
        kwargs['stdout'] = slave
        kwargs['stderr'] = slave

    # Split varargs into chunks based on target_concurrency
    chunk_size = (len(varargs) + target_concurrency - 1) // target_concurrency
    chunks = [varargs[i:i + chunk_size] for i in range(0, len(varargs), chunk_size)]

    results = []
    for chunk in chunks:
        full_cmd = list(cmd) + list(chunk)
        try:
            if color and sys.platform != "win32":
                process = subprocess.Popen(full_cmd, **kwargs)
                os.close(slave)
                output, _ = process.communicate()
                return_code = process.returncode
            else:
                process = subprocess.Popen(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
                output, _ = process.communicate()
                return_code = process.returncode
            results.append((return_code, output))
        except subprocess.CalledProcessError as e:
            results.append((e.returncode, e.output))

    # Aggregate results
    final_return_code = max(rc for rc, _ in results)
    final_output = b''.join(output for _, output in results)

    return (final_return_code, final_output)