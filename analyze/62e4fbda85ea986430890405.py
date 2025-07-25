def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs: Any,
) -> tuple[int, bytes]:
    
    # Handle empty varargs case
    if not varargs:
        proc = subprocess.Popen(cmd, **kwargs)
        stdout, _ = proc.communicate()
        return proc.returncode, stdout or b''

    # Split varargs into partitions based on max length
    partitions = []
    current_partition = []
    current_length = 0
    
    for arg in varargs:
        arg_length = len(arg) + 1  # +1 for space
        if current_length + arg_length > _max_length:
            if current_partition:
                partitions.append(current_partition)
            current_partition = [arg]
            current_length = arg_length
        else:
            current_partition.append(arg)
            current_length += arg_length
            
    if current_partition:
        partitions.append(current_partition)

    # Run commands in parallel based on target_concurrency
    processes = []
    outputs = []
    return_codes = []
    
    for i in range(0, len(partitions), target_concurrency):
        batch = partitions[i:i + target_concurrency]
        processes = []
        
        for partition in batch:
            # Create PTY if color is enabled
            if color and sys.platform != 'win32':
                import pty
                master, slave = pty.openpty()
                proc = subprocess.Popen(
                    (*cmd, *partition),
                    stdout=slave,
                    **kwargs
                )
                os.close(slave)
                processes.append((proc, master))
            else:
                proc = subprocess.Popen(
                    (*cmd, *partition),
                    stdout=subprocess.PIPE,
                    **kwargs
                )
                processes.append((proc, None))

        # Wait for processes and collect output
        for proc, master in processes:
            if master is not None:
                output = b''
                while True:
                    try:
                        chunk = os.read(master, 1024)
                        if not chunk:
                            break
                        output += chunk
                    except OSError:
                        break
                os.close(master)
            else:
                output = proc.communicate()[0]
                
            proc.wait()
            return_codes.append(proc.returncode)
            outputs.append(output or b'')

    # Return max return code and concatenated output
    final_output = b''.join(outputs)
    return max(return_codes), final_output