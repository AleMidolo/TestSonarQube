def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Fixes for the following issues on windows
    - https://bugs.python.org/issue8557
    - windows does not parse shebangs

    This function also makes deep-path shebangs work just fine
    """
    import os
    import sys

    if sys.platform == "win32":
        # Normalize the command for Windows
        normalized_cmd = []
        for part in cmd:
            # Convert to a path that Windows can understand
            normalized_part = part.replace('/', '\\')
            normalized_cmd.append(normalized_part)
        
        # Handle shebangs
        if normalized_cmd[0].startswith('#!'):
            shebang = normalized_cmd[0][2:]
            if os.path.exists(shebang):
                normalized_cmd[0] = shebang
        
        return tuple(normalized_cmd)
    
    return cmd