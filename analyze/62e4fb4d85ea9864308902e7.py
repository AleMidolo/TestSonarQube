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
            # Replace the shebang with the interpreter path
            cmd = (interpreter,) + cmd[1:]

    # Handle deep-path shebangs
    if os.name == 'nt':
        first_arg = cmd[0]
        if os.path.exists(first_arg):
            # If the first argument is a file, try to read the shebang
            with open(first_arg, 'r') as f:
                first_line = f.readline().strip()
                if first_line.startswith('#!'):
                    interpreter = first_line[2:].strip()
                    interpreter = os.path.normpath(interpreter)
                    cmd = (interpreter,) + cmd

    return cmd