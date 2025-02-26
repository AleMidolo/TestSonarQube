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
    from multiprocessing import Pool

    def run_command(args):
        return subprocess.run(cmd + args, capture_output=True)

    # Chunk the varargs into smaller lists based on target_concurrency
    chunks = [varargs[i:i + target_concurrency] for i in range(0, len(varargs), target_concurrency)]

    with Pool(processes=target_concurrency) as pool:
        results = pool.map(run_command, chunks)

    # Combine the return codes and output
    return_code = sum(result.returncode for result in results)
    combined_output = b''.join(result.stdout for result in results)

    return return_code, combined_output