import subprocess
import sys
import os
import shlex
from typing import Sequence, Any

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
    def _get_platform_max_length() -> int:
        # 获取平台的最大命令行长度
        if sys.platform == "linux":
            return os.sysconf("SC_ARG_MAX")
        else:
            return 131072  # 默认值

    def _chunk_args(args: Sequence[str], max_length: int) -> list[list[str]]:
        # 将参数列表分块，确保每个块的长度不超过最大长度
        chunks = []
        current_chunk = []
        current_length = 0

        for arg in args:
            arg_length = len(arg) + 1  # 包括空格
            if current_length + arg_length > max_length:
                chunks.append(current_chunk)
                current_chunk = []
                current_length = 0
            current_chunk.append(arg)
            current_length += arg_length

        if current_chunk:
            chunks.append(current_chunk)

        return chunks

    def _run_command(cmd: tuple[str, ...], args: Sequence[str], color: bool) -> tuple[int, bytes]:
        # 运行命令并返回退出码和输出
        full_cmd = list(cmd) + list(args)
        if color:
            # 使用伪终端运行命令
            import pty
            master, slave = pty.openpty()
            process = subprocess.Popen(full_cmd, stdout=slave, stderr=slave, **kwargs)
            os.close(slave)
            output = b""
            while True:
                try:
                    data = os.read(master, 1024)
                    if not data:
                        break
                    output += data
                except OSError:
                    break
            os.close(master)
            return process.wait(), output
        else:
            # 直接运行命令
            process = subprocess.Popen(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
            stdout, _ = process.communicate()
            return process.returncode, stdout

    # 分块处理参数
    chunks = _chunk_args(varargs, _max_length - sum(len(arg) for arg in cmd) - 1)

    # 并发执行命令
    results = []
    for chunk in chunks:
        exit_code, output = _run_command(cmd, chunk, color)
        results.append((exit_code, output))

    # 返回最后一个命令的结果
    return results[-1]