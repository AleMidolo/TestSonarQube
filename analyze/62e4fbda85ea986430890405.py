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
        # No arguments to process
        return 0, b''
    
    # Build command arguments in chunks that fit within max length
    chunks = []
    current_chunk = []
    current_length = sum(len(arg) + 1 for arg in cmd)  # +1 for spaces
    
    for arg in varargs:
        arg_length = len(arg) + 1  # +1 for space
        if current_length + arg_length > _max_length:
            if current_chunk:  # Only append non-empty chunks
                chunks.append(current_chunk)
            current_chunk = [arg]
            current_length = sum(len(arg) + 1 for arg in cmd) + arg_length
        else:
            current_chunk.append(arg)
            current_length += arg_length
            
    if current_chunk:
        chunks.append(current_chunk)

    # Process chunks with specified concurrency
    all_output = b''
    max_retcode = 0
    
    for i in range(0, len(chunks), target_concurrency):
        batch = chunks[i:i + target_concurrency]
        processes = []
        
        for chunk in batch:
            if color and sys.platform != 'win32' and hasattr(pty, 'openpty'):
                # Create a pseudo-terminal for colored output
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

        # Wait for all processes in batch and collect output
        for process, master in processes:
            if master is not None:
                # Read from pseudo-terminal
                output = b''
                try:
                    while True:
                        output += os.read(master, 1024)
                except OSError:
                    pass
                os.close(master)
            else:
                # Read from pipes
                stdout, stderr = process.communicate()
                output = stdout + stderr
                
            retcode = process.wait()
            max_retcode = max(max_retcode, retcode)
            all_output += output

    return max_retcode, all_output