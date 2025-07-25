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
            arg_len = len(arg) + 1  # +1 for space
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
        full_cmd = (*cmd, *chunk)
        
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

    chunks = _chunk_args(varargs, _max_length)
    
    if target_concurrency == 1:
        for chunk in chunks:
            retcode, output = _run_chunk(chunk)
            if retcode != 0:
                return retcode, output
        return 0, b''
    
    with ThreadPoolExecutor(max_workers=target_concurrency) as executor:
        futures = [executor.submit(_run_chunk, chunk) for chunk in chunks]
        for future in futures:
            retcode, output = future.result()
            if retcode != 0:
                return retcode, output
    
    return 0, b''