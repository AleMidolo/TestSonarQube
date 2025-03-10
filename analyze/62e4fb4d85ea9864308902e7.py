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

    # Extract the first part of the command (the executable)
    executable = cmd[0]

    # If the executable is a shebang, we need to handle it
    if executable.startswith('#!'):
        # Split the shebang line into parts
        shebang_parts = executable.split()
        if len(shebang_parts) < 2:
            return cmd  # Invalid shebang, return as-is

        # The interpreter is the second part of the shebang
        interpreter = shebang_parts[1]

        # If the interpreter is a path, we need to resolve it
        if os.path.exists(interpreter):
            interpreter = os.path.abspath(interpreter)

        # Replace the shebang with the interpreter and the rest of the command
        return (interpreter,) + cmd[1:]

    # If the executable is a path, we need to resolve it
    if os.path.exists(executable):
        executable = os.path.abspath(executable)

    # Return the normalized command
    return (executable,) + cmd[1:]