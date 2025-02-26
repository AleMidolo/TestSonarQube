def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    import os
    import sys

    if sys.platform == "win32":
        normalized_cmd = []
        for part in cmd:
            if part.startswith("#!") and len(part) > 2:
                # Handle shebangs
                shebang_path = part[2:].strip()
                if os.path.isabs(shebang_path):
                    normalized_cmd.append(part)
                else:
                    # Convert to absolute path
                    normalized_cmd.append("#!" + os.path.abspath(shebang_path))
            else:
                normalized_cmd.append(part)
        return tuple(normalized_cmd)
    return cmd