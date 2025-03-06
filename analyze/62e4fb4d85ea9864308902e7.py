import os

def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Corrections for the following issues on Windows:
    - https://bugs.python.org/issue8557
    - Windows does not correctly interpret shebangs

    This function also allows proper functioning of shebangs with deep paths.
    """
    if not cmd:
        return cmd

    first_arg = cmd[0]
    if os.name == 'nt' and first_arg.startswith('#!'):
        # On Windows, replace the shebang with the Python interpreter
        python_executable = sys.executable
        return (python_executable,) + cmd[1:]
    
    return cmd