import os
import pty
import subprocess
from typing import Any, Sequence
from concurrent.futures import ThreadPoolExecutor

def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs: Any,
) -> tuple[int, bytes]:
    
    def _chunk_args(args: Sequence[str], max_len: int) -> list[list[str]]:
        chunks = []
        current_chunk = []
        current_len = 0
        
        for arg in args:
            arg_len = len(arg) + 1  # +1 for space
            if current_len + arg_len > max_len and current_chunk:
                chunks.append(current_chunk)
                current_chunk = []
                current_len = 0
            current_chunk.append(arg)
            current_len += arg_len
            
        if current_chunk:
            chunks.append(current_chunk)
            
        return chunks

    def _run_chunk(chunk: list[str]) -> tuple[int, bytes]:
        full_cmd = list(cmd) + chunk
        
        if color and hasattr(os, 'openpty'):
            master, slave = pty.openpty()
            process = subprocess.Popen(
                full_cmd,
                stdout=slave,
                stderr=slave,
                **kwargs
            )
            os.close(slave)
            output = b''
            while True:
                try:
                    data = os.read(master, 1024)
                    if not data:
                        break
                    output += data
                except OSError:
                    break
            os.close(master)
            return process.wait(), output
        else:
            process = subprocess.run(
                full_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                **kwargs
            )
            return process.returncode, process.stdout + process.stderr

    chunks = _chunk_args(varargs, _max_length)
    
    if target_concurrency <= 1:
        for chunk in chunks:
            retcode, output = _run_chunk(chunk)
            if retcode != 0:
                return retcode, output
        return 0, b''
    
    with ThreadPoolExecutor(max_workers=target_concurrency) as executor:
        results = list(executor.map(_run_chunk, chunks))
        
    for retcode, output in results:
        if retcode != 0:
            return retcode, output
            
    return 0, b''