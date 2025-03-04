def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    """
    Correcciones para los siguientes problemas en Windows:  
    - https://bugs.python.org/issue8557  
    - Windows no interpreta correctamente los 'shebangs'  
    
    Esta función también permite que los 'shebangs' con rutas profundas funcionen correctamente.
    """
    if not cmd:
        return cmd
        
    # Si el primer elemento es un archivo Python, no necesita normalización
    if cmd[0].endswith('.py'):
        return cmd
        
    # Leer la primera línea del archivo para buscar shebang
    try:
        with open(cmd[0], 'r') as f:
            first_line = f.readline().strip()
    except (IOError, UnicodeDecodeError):
        return cmd
        
    # Verificar si hay shebang
    if not first_line.startswith('#!'):
        return cmd
        
    # Extraer el intérprete del shebang
    interpreter = first_line[2:].strip().split()
    
    # Si el intérprete es python, usar sys.executable
    if any('python' in part.lower() for part in interpreter):
        import sys
        return (sys.executable,) + (cmd[0],) + cmd[1:]
        
    # Para otros intérpretes, usar el path del shebang
    return tuple(interpreter + [cmd[0]] + list(cmd[1:]))