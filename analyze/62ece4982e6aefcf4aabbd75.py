def addignored(ignored):
    # Importar subprocess para ejecutar comandos git
    import subprocess
    
    # Ejecutar comando git ls-files para obtener todos los archivos
    all_files = subprocess.check_output(['git', 'ls-files', '--others', '--ignored', '--exclude-standard']).decode('utf-8')
    
    # Convertir la salida en una lista, eliminando espacios en blanco
    ignored_files = all_files.strip().split('\n')
    
    # Filtrar archivos vacíos
    ignored_files = [f for f in ignored_files if f]
    
    # Ordenar la lista alfabéticamente
    ignored_files.sort()
    
    # Unir los archivos con comas
    result = ','.join(ignored_files)
    
    return result