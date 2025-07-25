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
        # Normalize the interpreter path
        interpreter_path = os.path.normpath(interpreter_path)
        # Replace the shebang with the normalized interpreter path
        cmd = (interpreter_path,) + cmd[1:]

    # Ensure the first argument is an absolute path
    if not os.path.isabs(first_arg):
        # Search for the executable in the PATH
        for path in os.environ.get('PATH', '').split(os.pathsep):
            full_path = os.path.join(path, first_arg)
            if os.path.isfile(full_path):
                first_arg = full_path
                break

    return (first_arg,) + cmd[1:]