import os

def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Correcciones para los siguientes problemas en Windows:  
    - https://bugs.python.org/issue8557  
    - Windows no interpreta correctamente los 'shebangs'  

    Esta función también permite que los 'shebangs' con rutas profundas funcionen correctamente.
    """
    if not cmd:
        return cmd

    # Handle shebang lines
    if cmd[0].startswith('#!'):
        # Extract the interpreter path from the shebang
        interpreter_path = cmd[0][2:].strip()
        # Normalize the path for Windows
        interpreter_path = os.path.normpath(interpreter_path)
        # Replace the shebang with the normalized interpreter path
        cmd = (interpreter_path,) + cmd[1:]

    # Normalize all paths in the command tuple
    normalized_cmd = tuple(os.path.normpath(arg) if os.path.isabs(arg) else arg for arg in cmd)

    return normalized_cmd