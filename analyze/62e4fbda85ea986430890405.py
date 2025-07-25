import os
import pty
import subprocess
import sys
from typing import Any, Sequence

def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs: Any,
) -> tuple[int, bytes]:
    
    if not varargs:
        return 0, b''
        
    # Split varargs into chunks that fit within max command length
    chunks = []
    current_chunk = []
    current_length = sum(len(arg) + 1 for arg in cmd)
    
    for arg in varargs:
        arg_length = len(arg) + 1  # +1 for space
        if current_length + arg_length > _max_length:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = [arg]
            current_length = sum(len(arg) + 1 for arg in cmd) + arg_length
        else:
            current_chunk.append(arg)
            current_length += arg_length
            
    if current_chunk:
        chunks.append(current_chunk)

    # Run commands in parallel up to target_concurrency
    processes = []
    output = b''
    max_retcode = 0
    
    for i in range(0, len(chunks), target_concurrency):
        batch = chunks[i:i + target_concurrency]
        
        for chunk in batch:
            cmd_with_args = list(cmd) + chunk
            
            if color and sys.platform != 'win32' and hasattr(pty, 'openpty'):
                # Use PTY for color output
                master, slave = pty.openpty()
                p = subprocess.Popen(
                    cmd_with_args,
                    stdout=slave,
                    stderr=slave,
                    **kwargs
                )
                os.close(slave)
                processes.append((p, master))
            else:
                p = subprocess.Popen(
                    cmd_with_args,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    **kwargs
                )
                processes.append((p, None))
                
        # Wait for batch to complete
        for p, master in processes:
            if master is not None:
                # Read from PTY
                out = b''
                while True:
                    try:
                        chunk = os.read(master, 1024)
                        if not chunk:
                            break
                        out += chunk
                    except OSError:
                        break
                os.close(master)
            else:
                # Read from pipes
                out, _ = p.communicate()
                
            retcode = p.wait()
            max_retcode = max(max_retcode, retcode)
            output += out
            
        processes = []

    return max_retcode, output