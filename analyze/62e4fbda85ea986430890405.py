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
        return 0, b''

    # Calculate chunks based on max command line length
    chunks = []
    current_chunk = []
    current_length = sum(len(arg) + 1 for arg in cmd)  # +1 for spaces

    for arg in varargs:
        arg_length = len(arg) + 1  # +1 for space
        if current_length + arg_length > _max_length:
            if current_chunk:  # Only append non-empty chunks
                chunks.append(current_chunk)
            current_chunk = [arg]
            current_length = sum(len(arg) + 1 for arg in cmd) + arg_length
        else:
            current_chunk.append(arg)
            current_length += arg_length

    if current_chunk:
        chunks.append(current_chunk)

    # Split chunks into target_concurrency partitions
    if target_concurrency > 1:
        partitions = [[] for _ in range(target_concurrency)]
        for i, chunk in enumerate(chunks):
            partitions[i % target_concurrency].append(chunk)
    else:
        partitions = [chunks]

    # Execute commands
    output = b''
    max_return_code = 0
    
    for partition in partitions:
        processes = []
        for chunk in partition:
            full_cmd = list(cmd) + chunk
            
            if color:
                import pty
                master_fd, slave_fd = pty.openpty()
                process = subprocess.Popen(
                    full_cmd,
                    stdout=slave_fd,
                    stderr=slave_fd,
                    **kwargs
                )
                os.close(slave_fd)
            else:
                process = subprocess.Popen(
                    full_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    **kwargs
                )
            
            processes.append((process, master_fd if color else None))

        # Wait for all processes in partition to complete
        for process, fd in processes:
            if color:
                while True:
                    try:
                        chunk = os.read(fd, 1024)
                        if not chunk:
                            break
                        output += chunk
                    except OSError:
                        break
                os.close(fd)
            else:
                stdout, stderr = process.communicate()
                output += stdout + stderr
            
            return_code = process.wait()
            max_return_code = max(max_return_code, return_code)

    return max_return_code, output