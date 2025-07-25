def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    import os
    import sys

    if sys.platform == "win32":
        # Normalize the command for Windows
        normalized_cmd = []
        for part in cmd:
            # Replace backslashes with forward slashes
            part = part.replace('\\', '/')
            # Handle shebangs
            if part.startswith('#!'):
                # Ensure the shebang is correctly formatted
                shebang = part.splitlines()[0]
                normalized_cmd.append(shebang)
                normalized_cmd.append(part[len(shebang):].lstrip())
            else:
                normalized_cmd.append(part)
        return tuple(normalized_cmd)
    return cmd