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
    current_part = 0
    
    for arg in varargs:
        arg_len = len(arg) + 1
        if current_lengths[current_part] + arg_len > max_length:
            current_part = (current_part + 1) % num_parts
            
        partitions[current_part].append(arg)
        current_lengths[current_part] += arg_len
        
    return [p for p in partitions if p]

def _run_command(cmd: tuple[str, ...], *, color: bool = False, **kwargs: Any) -> tuple[int, bytes]:
    if color and sys.platform != 'win32':
        import pty
        master_fd, slave_fd = pty.openpty()
        kwargs['stdout'] = slave_fd
        kwargs['stderr'] = slave_fd
        
    proc = subprocess.Popen(cmd, **kwargs)
    output, _ = proc.communicate()
    
    if color and sys.platform != 'win32':
        os.close(slave_fd)
        output = os.read(master_fd, 1024*1024)
        os.close(master_fd)
        
    return proc.returncode, output