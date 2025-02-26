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
        # Remove the shebang for Windows compatibility
        normalized_cmd[0] = normalized_cmd[0][2:]

    # Normalize paths for Windows
    normalized_cmd = [path.replace('/', '\\') for path in normalized_cmd]

    return tuple(normalized_cmd)