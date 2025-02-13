import os
import sys

def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    if sys.platform == "win32":
        normalized_cmd = []
        for arg in cmd:
            if arg.endswith('.py'):
                # Check for shebang
                with open(arg, 'r') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith('#!'):
                        # Normalize the path to the executable
                        exe_path = os.path.normpath(arg)
                        normalized_cmd.append(exe_path)
                    else:
                        normalized_cmd.append(os.path.normpath(arg))
            else:
                normalized_cmd.append(os.path.normpath(arg))
        return tuple(normalized_cmd)
    return cmd