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

    if sys.platform != 'win32':
        return cmd

    first_arg = cmd[0]
    if not first_arg.endswith('.exe'):
        first_arg += '.exe'

    # Check if the first argument is a shebang
    if first_arg.startswith('#!'):
        # Extract the interpreter path from the shebang
        interpreter_path = first_arg[2:].strip()
        if os.path.exists(interpreter_path):
            # Replace the shebang with the interpreter path
            return (interpreter_path,) + cmd[1:]
        else:
            # If the interpreter path doesn't exist, return the original command
            return cmd

    # If the first argument is not a shebang, ensure it has the .exe extension
    return (first_arg,) + cmd[1:]