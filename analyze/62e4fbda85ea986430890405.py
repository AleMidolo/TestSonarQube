def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs: Any,
) -> tuple[int, bytes]:
    import subprocess
    import os
    from multiprocessing import Pool

    def run_command(args):
        return subprocess.run(cmd + args, capture_output=True)

    if color:
        # Create a pseudo-terminal if supported
        import pty
        master_fd, slave_fd = pty.openpty()
        os.setsid()
        os.close(slave_fd)

    # Split varargs into chunks for concurrency
    chunk_size = (len(varargs) + target_concurrency - 1) // target_concurrency
    chunks = [varargs[i:i + chunk_size] for i in range(0, len(varargs), chunk_size)]

    with Pool(processes=target_concurrency) as pool:
        results = pool.map(run_command, chunks)

    # Combine results
    return_code = sum(result.returncode for result in results)
    combined_output = b''.join(result.stdout for result in results)

    return return_code, combined_output