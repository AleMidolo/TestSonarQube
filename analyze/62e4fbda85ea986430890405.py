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
        
    partitions = _partition_varargs(varargs, _max_length)
    num_partitions = len(partitions)
    
    if target_concurrency == 1 or num_partitions == 1:
        # Run sequentially
        output = b''
        retcode = 0
        for partition in partitions:
            curr_retcode, curr_output = _run_command(
                (*cmd, *partition),
                color=color,
                **kwargs
            )
            output += curr_output
            if curr_retcode != 0:
                retcode = curr_retcode
        return retcode, output
        
    else:
        # Run in parallel
        with ThreadPoolExecutor(max_workers=min(target_concurrency, num_partitions)) as executor:
            futures = []
            for partition in partitions:
                future = executor.submit(
                    _run_command,
                    (*cmd, *partition),
                    color=color,
                    **kwargs
                )
                futures.append(future)
                
            output = b''
            retcode = 0
            for future in futures:
                curr_retcode, curr_output = future.result()
                output += curr_output
                if curr_retcode != 0:
                    retcode = curr_retcode
                    
            return retcode, output

def _partition_varargs(varargs: Sequence[str], max_length: int) -> list[tuple[str, ...]]:
    """Split varargs into partitions that don't exceed max command line length"""
    partitions = []
    current_partition = []
    current_length = 0
    
    for arg in varargs:
        arg_length = len(arg)
        if current_length + arg_length + 1 > max_length:
            if current_partition:
                partitions.append(tuple(current_partition))
            current_partition = [arg]
            current_length = arg_length
        else:
            current_partition.append(arg)
            current_length += arg_length + 1
            
    if current_partition:
        partitions.append(tuple(current_partition))
        
    return partitions

def _run_command(cmd: tuple[str, ...], color: bool = False, **kwargs: Any) -> tuple[int, bytes]:
    """Run a single command and return (return_code, output)"""
    if color and sys.platform != 'win32':
        import pty
        master_fd, slave_fd = pty.openpty()
        kwargs.update({'stdout': slave_fd, 'stderr': slave_fd})
        
    proc = subprocess.Popen(cmd, **kwargs)
    output, _ = proc.communicate()
    return proc.returncode, output