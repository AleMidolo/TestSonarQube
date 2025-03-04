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

    # Distribute chunks into target_concurrency partitions
    partitions = [[] for _ in range(target_concurrency)]
    for i, chunk in enumerate(chunks):
        partitions[i % target_concurrency].append(chunk)

    # Run commands in parallel
    output = b''
    max_returncode = 0
    
    def run_partition(partition):
        nonlocal output, max_returncode
        for chunk in partition:
            full_cmd = list(cmd) + chunk
            if color:
                import pty
                pid, fd = pty.fork()
                if pid == 0:  # Child process
                    os.execvp(full_cmd[0], full_cmd)
                    os._exit(1)
                else:  # Parent process
                    chunk_output = b''
                    while True:
                        try:
                            chunk_output += os.read(fd, 1024)
                        except OSError:
                            break
                    _, status = os.waitpid(pid, 0)
                    max_returncode = max(max_returncode, status >> 8)
                    output += chunk_output
            else:
                import subprocess
                process = subprocess.run(
                    full_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    **kwargs
                )
                max_returncode = max(max_returncode, process.returncode)
                output += process.stdout

    # Create and start threads for each partition
    import threading
    threads = []
    for partition in partitions:
        if partition:  # Only create threads for non-empty partitions
            thread = threading.Thread(target=run_partition, args=(partition,))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return max_returncode, output