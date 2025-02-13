import subprocess
import os
import shlex
from typing import Sequence, Any, Tuple

def _get_platform_max_length() -> int:
    return os.pathconf('.', 'PC_PATH_MAX')

def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs: Any,
) -> Tuple[int, bytes]:
    if color:
        pty = subprocess.Popen(['script', '-q', '/dev/null'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        cmd = ('/bin/bash', '-c', ' '.join(cmd))
    else:
        pty = None

    args = []
    for arg in varargs:
        args.append(arg)
        if len(' '.join(args)) >= _max_length:
            subprocess.run(cmd + tuple(args), **kwargs)
            args = []

    if args:
        subprocess.run(cmd + tuple(args), **kwargs)

    if pty:
        pty.terminate()

    return 0, b''