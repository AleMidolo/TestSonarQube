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
    Una implementación simplificada de xargs.

    - color: Crea un pty si está en una plataforma que lo soporte.
    - target_concurrency: Número objetivo de particiones para ejecutar de forma concurrente.
    """
    def _get_platform_max_length() -> int:
        if sys.platform == "win32":
            return 8191
        else:
            return 131072

    def _partition_args(args: Sequence[str], max_length: int) -> list[list[str]]:
        partitions = []
        current_partition = []
        current_length = 0

        for arg in args:
            arg_length = len(arg) + 1  # +1 for the space
            if current_length + arg_length > max_length:
                partitions.append(current_partition)
                current_partition = []
                current_length = 0
            current_partition.append(arg)
            current_length += arg_length

        if current_partition:
            partitions.append(current_partition)

        return partitions

    partitions = _partition_args(varargs, _max_length)

    results = []
    for partition in partitions:
        full_cmd = list(cmd) + partition
        if color and sys.platform != "win32":
            # Use a pseudo-terminal for color support
            import pty
            master, slave = pty.openpty()
            process = subprocess.Popen(full_cmd, stdout=slave, stderr=slave, **kwargs)
            os.close(slave)
            output = os.read(master, 1024)
            os.close(master)
            return_code = process.wait()
        else:
            process = subprocess.Popen(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
            output, _ = process.communicate()
            return_code = process.returncode

        results.append((return_code, output))

    # Combine results
    final_return_code = max(rc for rc, _ in results)
    final_output = b''.join(output for _, output in results)

    return final_return_code, final_output