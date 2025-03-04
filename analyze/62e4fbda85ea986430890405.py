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
        return _run_command(cmd, color=color, **kwargs)
        
    partitions = _partition_varargs(varargs, _max_length, target_concurrency)
    
    futures = []
    with ThreadPoolExecutor(max_workers=target_concurrency) as executor:
        for partition in partitions:
            full_cmd = cmd + tuple(partition)
            future = executor.submit(_run_command, full_cmd, color=color, **kwargs)
            futures.append(future)
            
    output = b''
    retcode = 0
    for future in futures:
        try:
            partition_retcode, partition_output = future.result()
            output += partition_output
            if partition_retcode != 0:
                retcode = partition_retcode
        except Exception as e:
            retcode = 1
            output += str(e).encode()
            
    return retcode, output

def _partition_varargs(varargs: Sequence[str], max_length: int, target_parts: int) -> list[list[str]]:
    total_length = sum(len(arg) for arg in varargs) + len(varargs)
    min_parts = (total_length + max_length - 1) // max_length
    num_parts = max(min_parts, target_parts)
    
    partitions = [[] for _ in range(num_parts)]
    current_lengths = [0] * num_parts
    
    for i, arg in enumerate(varargs):
        part_idx = i % num_parts
        partitions[part_idx].append(arg)
        current_lengths[part_idx] += len(arg) + 1
        
    return partitions

def _run_command(cmd: tuple[str, ...], *, color: bool = False, **kwargs: Any) -> tuple[int, bytes]:
    if color and hasattr(os, 'openpty'):
        master, slave = os.openpty()
        kwargs.update(stdin=slave, stdout=slave, stderr=slave)
    
    process = subprocess.Popen(cmd, **kwargs)
    output, _ = process.communicate()
    
    if color and hasattr(os, 'openpty'):
        os.close(master)
        os.close(slave)
        
    return process.returncode, output if output else b''