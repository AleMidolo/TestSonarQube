def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Correcciones para los siguientes problemas en Windows:  
    - https://bugs.python.org/issue8557  
    - Windows no interpreta correctamente los 'shebangs'  

    Esta función también permite que los 'shebangs' con rutas profundas funcionen correctamente.
    """
    if not cmd:
        return cmd

    normalized_cmd = []
    for part in cmd:
        if part.startswith('#!'):
            # Normalize shebang line
            shebang_parts = part.split()
            if len(shebang_parts) > 1:
                shebang_parts[1] = shebang_parts[1].replace('/', '\\')
            normalized_cmd.append(' '.join(shebang_parts))
        else:
            normalized_cmd.append(part.replace('/', '\\'))

    return tuple(normalized_cmd)