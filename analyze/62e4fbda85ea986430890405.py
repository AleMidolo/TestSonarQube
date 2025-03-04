import os
import pty
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
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
    
    def _run_chunk(chunk: list[str]) -> tuple[int, bytes]:
        full_cmd = list(cmd) + chunk
        
        if color and sys.platform != 'win32':
            master, slave = pty.openpty()
            proc = subprocess.Popen(
                full_cmd,
                stdout=slave,
                stderr=slave,
                **kwargs
            )
            os.close(slave)
            
            output = b''
            while True:
                try:
                    chunk = os.read(master, 1024)
                    if not chunk:
                        break
                    output += chunk
                except OSError:
                    break
                    
            os.close(master)
            returncode = proc.wait()
            
        else:
            proc = subprocess.run(
                full_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                **kwargs
            )
            output = proc.stdout
            returncode = proc.returncode
            
        return returncode, output

    # Split varargs into chunks that fit within max length
    chunks: list[list[str]] = [[]]
    current_length = 0
    
    for arg in varargs:
        arg_length = len(arg) + 1  # +1 for space
        if current_length + arg_length > _max_length:
            chunks.append([])
            current_length = 0
        chunks[-1].append(arg)
        current_length += arg_length

    # Run chunks concurrently
    with ThreadPoolExecutor(max_workers=target_concurrency) as executor:
        results = list(executor.map(_run_chunk, chunks))

    # Combine results
    final_returncode = 0
    final_output = b''
    
    for returncode, output in results:
        if returncode != 0:
            final_returncode = returncode
        final_output += output

    return final_returncode, final_output