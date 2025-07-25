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
    
    # Split args into chunks that fit within max length
    chunks = []
    current_chunk = []
    current_length = 0
    
    for arg in varargs:
        arg_length = len(arg) + 1  # +1 for space
        if current_length + arg_length > _max_length:
            chunks.append(current_chunk)
            current_chunk = [arg]
            current_length = arg_length
        else:
            current_chunk.append(arg)
            current_length += arg_length
            
    if current_chunk:
        chunks.append(current_chunk)
        
    # Determine number of concurrent processes
    n_chunks = len(chunks)
    concurrency = min(target_concurrency, n_chunks)
    
    # Run commands in parallel
    if concurrency > 1:
        with ThreadPoolExecutor(max_workers=concurrency) as executor:
            futures = []
            for chunk in chunks:
                full_cmd = cmd + tuple(chunk)
                futures.append(executor.submit(_run_command, full_cmd, color=color, **kwargs))
                
            # Get results
            exit_code = 0
            output = b''
            for future in futures:
                chunk_code, chunk_output = future.result()
                if chunk_code != 0:
                    exit_code = chunk_code
                output += chunk_output
                
            return exit_code, output
            
    # Run sequentially
    else:
        exit_code = 0
        output = b''
        for chunk in chunks:
            full_cmd = cmd + tuple(chunk)
            chunk_code, chunk_output = _run_command(full_cmd, color=color, **kwargs)
            if chunk_code != 0:
                exit_code = chunk_code
            output += chunk_output
            
        return exit_code, output