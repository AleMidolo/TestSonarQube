def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs: Any,
) -> tuple[int, bytes]:
    """
    A simplified implementation of xargs.

    color: Make a pty if on a platform that supports it
    target_concurrency: Target number of partitions to run concurrently
    """
    import subprocess
    from multiprocessing import Pool

    def run_command(args):
        return subprocess.run(cmd + args, capture_output=True)

    # Split varargs into chunks based on target_concurrency
    chunk_size = max(1, len(varargs) // target_concurrency)
    chunks = [varargs[i:i + chunk_size] for i in range(0, len(varargs), chunk_size)]

    with Pool(processes=target_concurrency) as pool:
        results = pool.map(run_command, chunks)

    # Combine results
    return_code = sum(result.returncode for result in results)
    combined_output = b''.join(result.stdout for result in results)

    return return_code, combined_output