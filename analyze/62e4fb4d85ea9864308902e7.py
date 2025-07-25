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
                shebang_path = part[2:].strip()
                if os.path.isabs(shebang_path):
                    normalized_cmd.append(part)
                else:
                    # Convert to absolute path if necessary
                    normalized_cmd.append('#!' + os.path.abspath(shebang_path))
            else:
                normalized_cmd.append(part)
        return tuple(normalized_cmd)
    else:
        return cmd