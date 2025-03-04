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
        
    # Split varargs into chunks that fit within max length
    chunks = []
    current_chunk = []
    current_length = 0
    
    for arg in varargs:
        arg_length = len(arg) + 1  # +1 for space
        if current_length + arg_length > _max_length:
            chunks.append(current_chunk)
            current_chunk = [arg]
            current_length = arg_length
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
            if color and sys.platform != 'win32' and hasattr(os, 'openpty'):
                master, slave = pty.openpty()
                process = subprocess.Popen(
                    (*cmd, *chunk),
                    stdout=slave,
                    stderr=slave,
                    **kwargs
                )
                os.close(slave)
                processes.append((process, master))
            else:
                process = subprocess.Popen(
                    (*cmd, *chunk),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    **kwargs
                )
                processes.append((process, None))

        # Wait for all processes in batch to complete
        for process, master in processes:
            if master is not None:
                # Read from PTY
                while True:
                    try:
                        chunk_output = os.read(master, 1024)
                        if not chunk_output:
                            break
                        output += chunk_output
                    except OSError:
                        break
                os.close(master)
            else:
                # Read from pipes
                stdout, stderr = process.communicate()
                output += stdout + stderr
                
            retcode = process.wait()
            if retcode > max_retcode:
                max_retcode = retcode
                
        processes = []

    return max_retcode, output