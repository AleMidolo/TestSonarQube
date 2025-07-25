def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Correcciones para los siguientes problemas en Windows:  
    - https://bugs.python.org/issue8557  
    - Windows no interpreta correctamente los 'shebangs'  

    Esta función también permite que los 'shebangs' con rutas profundas funcionen correctamente.
    """
    if not cmd:
        return cmd

    # Normalize the command by replacing backslashes with forward slashes
    normalized_cmd = tuple(part.replace('\\', '/') for part in cmd)

    # Handle shebangs
    if normalized_cmd[0].startswith('#!'):
        shebang_parts = normalized_cmd[0].split()
        if len(shebang_parts) > 1:
            shebang_parts[1] = shebang_parts[1].replace('\\', '/')
            normalized_cmd = (shebang_parts[0] + ' ' + shebang_parts[1],) + normalized_cmd[1:]

    return normalized_cmd