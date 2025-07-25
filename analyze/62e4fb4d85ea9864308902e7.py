def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Fixes for the following issues on windows
    - https://bugs.python.org/issue8557 
    - windows does not parse shebangs

    This function also makes deep-path shebangs work just fine
    """
    import os
    import sys

    if not cmd:
        return cmd
        
    # Only apply fixes on Windows
    if os.name != 'nt':
        return cmd

    # Get first argument (the executable)
    exe = cmd[0]
    
    # If it's a Python file, prepend the Python interpreter
    if exe.endswith('.py'):
        return (sys.executable, exe) + cmd[1:]
        
    # Check for shebang in first line
    try:
        with open(exe, 'rb') as f:
            first_line = f.readline().decode('utf-8').strip()
            
        if first_line.startswith('#!'):
            interpreter = first_line[2:].strip().split()[0]
            if interpreter.endswith('python'):
                return (sys.executable, exe) + cmd[1:]
            return (interpreter, exe) + cmd[1:]
    except (IOError, UnicodeDecodeError):
        pass

    return cmd