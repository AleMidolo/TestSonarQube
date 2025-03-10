import subprocess
import sys
import os
import importlib

def subprocess_run_helper(func, *args, timeout, extra_env=None):
    """
    在子进程中运行一个函数

    参数：
      `func`: function，需要运行的函数。该函数必须位于可导入的模块中。
      `*args`: str。任何额外的命令行参数，这些参数将作为 subprocess.run 的第一个参数传递。
      `extra_env`: dict[str, str]。为子进程设置的额外环境变量。
    返回值：
      `CompletedProcess` 实例。

    在子进程中运行一个函数。

    参数
    ----------
     `func`: function，需要运行的函数。该函数必须位于可导入的模块中。
      `*args`: str。任何额外的命令行参数，这些参数将作为 subprocess.run 的第一个参数传递。
      `extra_env`: dict[str, str]。为子进程设置的额外环境变量。
    """
    # 获取函数的模块名和函数名
    module_name = func.__module__
    func_name = func.__name__

    # 构建命令行参数
    command = [sys.executable, '-c', f'from {module_name} import {func_name}; {func_name}()']
    command.extend(args)

    # 合并环境变量
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # 运行子进程
    result = subprocess.run(command, env=env, timeout=timeout, capture_output=True, text=True)

    return result