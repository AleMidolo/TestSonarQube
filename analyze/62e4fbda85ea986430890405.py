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
    
    results = []
    with ThreadPoolExecutor(max_workers=target_concurrency) as executor:
        futures = []
        for partition in partitions:
            full_cmd = cmd + tuple(partition)
            future = executor.submit(_run_command, full_cmd, color=color, **kwargs)
            futures.append(future)
            
        for future in futures:
            try:
                retcode, output = future.result()
                if retcode != 0:
                    return retcode, output
                results.append(output)
                
    return 0, b''.join(results)

def _partition_varargs(varargs: Sequence[str], max_length: int, target_parts: int) -> list[list[str]]:
    if not varargs:
        return [[]]
        
    total_length = sum(len(arg) for arg in varargs) + len(varargs)
    partition_size = max(1, total_length // target_parts)
    
    partitions = []
    current_partition = []
    current_length = 0
    
    for arg in varargs:
        arg_length = len(arg) + 1
        if current_length + arg_length > max_length:
            if current_partition:
                partitions.append(current_partition)
            current_partition = [arg]
            current_length = arg_length
        else:
            current_partition.append(arg) 
            current_length += arg_length
            
    if current_partition:
        partitions.append(current_partition)
        
    return partitions

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
        os.close(master_fd)
        
    return proc.returncode, output if output else b''