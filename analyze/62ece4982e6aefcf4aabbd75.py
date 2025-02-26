def addignored(ignored):
    """
    Usa el comando de git para obtener los nombres de los archivos, conviértelos en una lista, ordena la lista para incluir solo los archivos ignorados, y devuelve esos archivos como una única cadena con cada nombre de archivo separado por una coma.
    """
    import subprocess

    # Obtener la lista de archivos ignorados usando git
    result = subprocess.run(['git', 'check-ignore', '-n', '*'], stdout=subprocess.PIPE, text=True)
    
    # Convertir la salida en una lista de archivos
    ignored_files = result.stdout.strip().split('\n')
    
    # Filtrar y ordenar la lista de archivos ignorados
    ignored_files = sorted(set(ignored_files))
    
    # Devolver los archivos como una cadena separada por comas
    return ', '.join(ignored_files)