def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Fixes for the following issues on windows
    - https://bugs.python.org/issue8557
    - windows does not parse shebangs

    This function also makes deep-path shebangs work just fine
    """
    if not cmd:
        return cmd

    # Normalize the command by handling shebangs and paths
    normalized_cmd = list(cmd)

    # Check if the first element is a shebang
    if normalized_cmd[0].startswith('#!'):
        # Remove the shebang for processing
        shebang = normalized_cmd.pop(0)
        # Normalize the path if necessary
        normalized_cmd[0] = normalized_cmd[0].replace('\\', '/')

    # Re-add the shebang if needed
    if shebang:
        normalized_cmd.insert(0, shebang)

    return tuple(normalized_cmd)