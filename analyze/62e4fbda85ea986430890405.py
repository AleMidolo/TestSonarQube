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
    
    def _chunk_args(args: Sequence[str], max_len: int) -> list[tuple[str, ...]]:
        chunks = []
        current_chunk = []
        current_len = 0
        
        for arg in args:
            arg_len = len(arg) + 1  # Add 1 for space
            if current_len + arg_len > max_len and current_chunk:
                chunks.append(tuple(current_chunk))
                current_chunk = []
                current_len = 0
            current_chunk.append(arg)
            current_len += arg_len
            
        if current_chunk:
            chunks.append(tuple(current_chunk))
            
        return chunks

    def _run_chunk(chunk: tuple[str, ...]) -> tuple[int, bytes]:
        full_cmd = cmd + chunk
        
        if color and sys.platform != 'win32':
            master, slave = pty.openpty()
            try:
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
                return proc.wait(), output
            finally:
                os.close(master)
        else:
            proc = subprocess.Popen(
                full_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                **kwargs
            )
            stdout, stderr = proc.communicate()
            return proc.returncode, stdout + stderr

    # Split arguments into chunks based on max length
    chunks = _chunk_args(varargs, _max_length)
    
    # Run chunks in parallel using ThreadPoolExecutor
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