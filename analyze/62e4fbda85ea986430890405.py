import subprocess
import sys
import os
import shlex
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
    if not cmd:
        return (1, b"No command provided")

    # Split varargs into chunks based on target_concurrency
    chunk_size = max(1, len(varargs) // target_concurrency
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

    # Aggregate results
    final_return_code = max(rc for rc, _ in results)
    final_output = b"\n".join(output for _, output in results)
    return (final_return_code, final_output)

def _get_platform_max_length() -> int:
    """Get the maximum command length for the current platform."""
    if sys.platform == "win32":
        return 8191  # Windows command line length limit
    else:
        return 131072  # Common Unix limit