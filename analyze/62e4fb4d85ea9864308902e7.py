def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    import os
    import sys
    import shutil
    
    if not cmd:
        return cmd
        
    # Get first argument (executable)
    exe = cmd[0]
    
    # Handle shebang on Windows
    if sys.platform == 'win32' and os.path.exists(exe):
        with open(exe, 'rb') as f:
            # Check if file starts with shebang
            if f.read(2) == b'#!':
                shebang = f.readline().decode().strip()
                interpreter = shebang.split()[0]
                
                # Get full path of interpreter
                interpreter_path = shutil.which(os.path.basename(interpreter))
                if interpreter_path:
                    return (interpreter_path, exe) + cmd[1:]
    
    # Get full path of executable
    exe_path = shutil.which(exe)
    if exe_path:
        return (exe_path,) + cmd[1:]
        
    return cmd