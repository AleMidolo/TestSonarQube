def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Fixes for the following issues on windows
    - https://bugs.python.org/issue8557 
    - windows does not parse shebangs

    This function also makes deep-path shebangs work just fine
    """
    import sys
    import os

    if sys.platform != 'win32' or not cmd:
        return cmd

    # Get first argument (the executable)
    exe = cmd[0]
    
    # Return as-is if it's not a script file
    if not os.path.isfile(exe) or exe.lower().endswith(('.exe', '.bat', '.com')):
        return cmd

    # Read first line to check for shebang
    try:
        with open(exe, 'rb') as f:
            first_line = f.readline().decode('utf-8').strip()
    except (IOError, UnicodeDecodeError):
        return cmd

    # Check if first line is a shebang
    if not first_line.startswith('#!'):
        return cmd

    # Parse shebang line
    shebang = first_line[2:].strip().split()
    if not shebang:
        return cmd

    interpreter = shebang[0]
    args = shebang[1:]

    # Handle special cases like /usr/bin/env
    if os.path.basename(interpreter) == 'env':
        if args:
            interpreter = args[0]
            args = args[1:]
        else:
            return cmd

    # Convert unix paths to windows paths if needed
    if '/' in interpreter:
        interpreter = interpreter.replace('/', '\\')

    # Construct new command
    new_cmd = (interpreter,)
    if args:
        new_cmd += tuple(args)
    new_cmd += (exe,)
    if len(cmd) > 1:
        new_cmd += cmd[1:]

    return new_cmd