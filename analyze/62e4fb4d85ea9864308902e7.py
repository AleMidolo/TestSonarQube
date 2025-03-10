def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Normalizes the command tuple to handle issues with shebangs and paths on Windows.

    Args:
        cmd: A tuple of strings representing the command and its arguments.

    Returns:
        A normalized tuple of strings that can be used to execute the command correctly on Windows.
    """
    if not cmd:
        return cmd

    # Handle shebang lines by extracting the interpreter path
    if cmd[0].startswith('#!'):
        # Split the shebang line into parts
        shebang_parts = cmd[0].split()
        if len(shebang_parts) > 1:
            # The first part is the interpreter path
            interpreter = shebang_parts[1]
            # The rest of the command is the script and its arguments
            script_and_args = cmd[1:]
            # Combine the interpreter with the script and arguments
            return (interpreter,) + script_and_args

    # Handle paths with spaces by quoting them
    normalized_cmd = []
    for part in cmd:
        if ' ' in part and not part.startswith('"') and not part.startswith("'"):
            normalized_cmd.append(f'"{part}"')
        else:
            normalized_cmd.append(part)

    return tuple(normalized_cmd)