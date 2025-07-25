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
            if current_chunk:  # Only add non-empty chunks
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
            if color and sys.platform != 'win32' and hasattr(os, 'openpty'):
                master, slave = pty.openpty()
                kwargs['stdin'] = slave
                kwargs['stdout'] = slave
                kwargs['stderr'] = slave
            
            process = subprocess.Popen(
                [*cmd, *chunk],
                stdout=subprocess.PIPE if not color else None,
                stderr=subprocess.STDOUT if not color else None,
                **kwargs
            )
            processes.append((process, master if color else None))
            
        # Wait for all processes in batch to complete
        for process, master_fd in processes:
            if color and master_fd is not None:
                output = b''
                while True:
                    try:
                        output += os.read(master_fd, 1024)
                    except OSError:
                        break
                os.close(master_fd)
            else:
                output, _ = process.communicate()
                
            retcode = process.wait()
            max_retcode = max(max_retcode, retcode)
            all_output += output or b''
            
    return max_retcode, all_output