import subprocess
import os
import sys
import pickle

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
    # Serialize the function and arguments
    func_name = func.__module__ + '.' + func.__qualname__
    args = pickle.dumps(args)

    # Prepare the command to run
    command = [sys.executable, '-c', f'import pickle; import {func.__module__}; '
                                       f'func = {func_name}; '
                                       f'args = pickle.loads({args}); '
                                       f'func(*args)']

    # Set up the environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Run the subprocess
    result = subprocess.run(command, env=env, timeout=timeout, capture_output=True)

    return result