import os
import sys

def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Fixes for the following issues on windows
    - https://bugs.python.org/issue8557
    - windows does not parse shebangs

    This function also makes deep-path shebangs work just fine
    """
    if not cmd:
        return cmd

    # Handle shebang lines on Windows
    if os.name == 'nt':
        first_arg = cmd[0]
        if first_arg.startswith('#!'):
            # Extract the interpreter path from the shebang
            interpreter_path = first_arg[2:].strip()
            # Normalize the path to handle deep-path shebangs
            interpreter_path = os.path.normpath(interpreter_path)
            # Replace the shebang with the interpreter path
            cmd = (interpreter_path,) + cmd[1:]

    # Handle the issue where Windows does not parse shebangs
    if os.name == 'nt' and len(cmd) > 1:
        first_arg = cmd[0]
        if first_arg.endswith('.py') or first_arg.endswith('.pyw'):
            # Prepend the Python interpreter if the first argument is a Python script
            python_executable = sys.executable
            cmd = (python_executable,) + cmd

    return cmd