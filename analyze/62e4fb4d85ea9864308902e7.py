def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    import os
    import sys

    if sys.platform == "win32":
        normalized_cmd = []
        for part in cmd:
            if part.startswith("#!") and len(part) > 2:
                shebang = part[2:]
                if os.path.isfile(shebang):
                    normalized_cmd.append(shebang)
                else:
                    normalized_cmd.append(part)
            else:
                normalized_cmd.append(part)
        return tuple(normalized_cmd)
    return cmd