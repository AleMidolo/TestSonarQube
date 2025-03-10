import os
import sys

def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Corrections for the following issues on Windows:
    - https://bugs.python.org/issue8557
    - Windows does not correctly interpret shebangs

    This function also allows proper functioning of shebangs with deep paths.
    """
    if not cmd:
        return cmd

    # Extract the first part of the command (the executable)
    executable = cmd[0]

    # If the executable is a shebang, we need to handle it differently
    if executable.startswith('#!'):
        # Split the shebang line into parts
        shebang_parts = executable.split()
        if len(shebang_parts) < 2:
            return cmd  # Not a valid shebang, return the original command

        # The interpreter is the second part of the shebang
        interpreter = shebang_parts[1]

        # If the interpreter is a path, we need to normalize it
        if os.path.isabs(interpreter):
            interpreter = os.path.normpath(interpreter)

        # Construct the new command with the interpreter and the rest of the arguments
        new_cmd = (interpreter,) + cmd[1:]
        return new_cmd

    # If the executable is not a shebang, just return the original command
    return cmd