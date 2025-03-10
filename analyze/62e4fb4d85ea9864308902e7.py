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

    first_arg = cmd[0]

    # Check if the first argument is a shebang
    if first_arg.startswith('#!'):
        # Extract the path from the shebang
        shebang_path = first_arg[2:].strip()
        # Normalize the path to handle deep paths correctly
        normalized_path = os.path.normpath(shebang_path)
        # Replace the shebang with the normalized path
        return (normalized_path,) + cmd[1:]

    return cmd