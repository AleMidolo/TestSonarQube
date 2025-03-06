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

    # Handle shebang lines
    if cmd[0].startswith('#!'):
        # Extract the interpreter path from the shebang
        interpreter = cmd[0][2:].strip()
        # Split the interpreter path into parts
        interpreter_parts = interpreter.split()
        # The first part is the interpreter path
        interpreter_path = interpreter_parts[0]
        # The rest are arguments to the interpreter
        interpreter_args = interpreter_parts[1:]
        # Normalize the interpreter path
        interpreter_path = os.path.normpath(interpreter_path)
        # Reconstruct the command
        cmd = (interpreter_path,) + tuple(interpreter_args) + cmd[1:]

    # Normalize paths in the command
    normalized_cmd = []
    for part in cmd:
        if os.path.exists(part):
            normalized_cmd.append(os.path.normpath(part))
        else:
            normalized_cmd.append(part)

    return tuple(normalized_cmd)