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
            if part.startswith("#!"):
                # Handle shebangs
                shebang = part[2:]
                if os.path.isfile(shebang):
                    normalized_cmd.append(shebang)
                else:
                    # If the shebang is not a valid file, keep it as is
                    normalized_cmd.append(part)
            else:
                # Normalize paths for Windows
                normalized_cmd.append(part.replace('/', '\\'))
        return tuple(normalized_cmd)
    return cmd