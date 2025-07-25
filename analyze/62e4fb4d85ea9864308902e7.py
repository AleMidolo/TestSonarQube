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
        
    # Leer el primer archivo para buscar shebang
    try:
        with open(cmd[0], 'rb') as f:
            first_line = f.readline().decode('utf-8').strip()
            
        # Si tiene shebang, extraer el intérprete
        if first_line.startswith('#!'):
            interpreter = first_line[2:].strip().split()
            
            # Si el intérprete es python, usar sys.executable
            if 'python' in interpreter[-1].lower():
                import sys
                return (sys.executable,) + (cmd[0],) + cmd[1:]
                
            # Si no es python, usar el intérprete del shebang
            return tuple(interpreter + [cmd[0]] + list(cmd[1:]))
            
    except (IOError, UnicodeDecodeError):
        pass
        
    return cmd