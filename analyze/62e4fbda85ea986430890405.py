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
    在 Linux 中简化实现 Xargs
    一个简化版的 xargs 实现。

    color: 如果运行在支持的操作系统平台上，创建一个伪终端（pty）。
    target_concurrency: 目标并发分区的数量。
    """
    import os
    import subprocess
    from multiprocessing import Pool

    def run_command(args):
        return subprocess.run(cmd + args, capture_output=True)

    if color:
        # Create a pseudo terminal if color is enabled
        import pty
        master_fd, slave_fd = pty.openpty()
        os.close(slave_fd)
        os.dup2(master_fd, 1)  # Redirect stdout to the master fd

    # Split varargs into chunks based on target_concurrency
    chunk_size = (len(varargs) + target_concurrency - 1) // target_concurrency
    chunks = [varargs[i:i + chunk_size] for i in range(0, len(varargs), chunk_size)]

    with Pool(processes=target_concurrency) as pool:
        results = pool.map(run_command, chunks)

    # Combine results
    return_code = sum(result.returncode for result in results)
    combined_output = b''.join(result.stdout for result in results)

    return return_code, combined_output