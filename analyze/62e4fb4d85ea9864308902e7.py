def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    import os
    import sys

    if sys.platform == "win32":
        # Normalize the command for Windows
        normalized_cmd = []
        for part in cmd:
            if part.startswith("#!") and len(part) > 2:
                # Handle shebangs
                shebang = part[2:].strip()
                if os.path.isfile(shebang):
                    normalized_cmd.append(shebang)
                else:
                    normalized_cmd.append(part)
            else:
                normalized_cmd.append(part)
        return tuple(normalized_cmd)
    return cmd