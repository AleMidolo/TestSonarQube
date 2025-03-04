def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    # Handle empty command
    if not cmd:
        return cmd
        
    # Get first argument (command/script path)
    first = cmd[0]
    
    # Skip processing if not a Python script
    if not first.endswith('.py'):
        return cmd
        
    # Read first line to check for shebang
    try:
        with open(first, 'rb') as f:
            first_line = f.readline().decode('utf-8').strip()
    except (IOError, UnicodeDecodeError):
        return cmd
        
    # Check if first line is a shebang
    if not first_line.startswith('#!'):
        return cmd
        
    # Extract interpreter path from shebang
    interp = first_line[2:].strip().split()[0]
    
    # Handle deep paths with spaces
    if ' ' in interp:
        interp = f'"{interp}"'
        
    # Return normalized command with interpreter
    return (interp,) + cmd