def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    import os
    import sys

    if sys.platform == "win32":
        # Normalize the command for Windows
        normalized_cmd = []
        for part in cmd:
            if part.startswith("#!"):
                # Handle shebangs
                shebang = part.splitlines()[0]
                normalized_cmd.append(shebang)
                normalized_cmd.append(part[len(shebang):].lstrip())
            else:
                normalized_cmd.append(part)

        # Convert to a tuple and return
        return tuple(normalized_cmd)
    else:
        # On non-Windows platforms, return the command as is
        return cmd