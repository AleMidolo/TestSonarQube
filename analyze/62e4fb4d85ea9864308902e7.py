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
            if part.startswith("#!"):
                # Handle shebangs
                shebang_path = part[2:].strip()
                normalized_cmd.append(os.path.normpath(shebang_path))
            else:
                normalized_cmd.append(os.path.normpath(part))
        return tuple(normalized_cmd)
    else:
        # On non-Windows systems, return the command as is
        return cmd