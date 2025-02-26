def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    import os
    import sys

    if sys.platform == "win32":
        # Normalize the command for Windows
        normalized_cmd = []
        for part in cmd:
            # Handle shebangs
            if part.startswith("#!"):
                # Normalize shebang path
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