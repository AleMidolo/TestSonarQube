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

    # Handle shebang on Windows
    if os.name == 'nt':
        first_arg = cmd[0]
        if first_arg.startswith('#!'):
            # Extract the interpreter path from the shebang
            interpreter = first_arg[2:].strip()
            # Normalize the interpreter path
            interpreter = os.path.normpath(interpreter)
            # Replace the shebang with the interpreter
            cmd = (interpreter,) + cmd[1:]

    # Normalize paths in the command
    normalized_cmd = tuple(os.path.normpath(arg) if os.path.isabs(arg) else arg for arg in cmd)

    return normalized_cmd