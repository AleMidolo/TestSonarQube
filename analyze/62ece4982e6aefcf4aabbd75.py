def addignored(ignored):
    """
    Usa el comando de git para obtener los nombres de los archivos, conviértelos en una lista, ordena la lista para incluir solo los archivos ignorados, y devuelve esos archivos como una única cadena con cada nombre de archivo separado por una coma.
    """
    import subprocess

    # Obtener la lista de archivos ignorados usando git
    result = subprocess.run(['git', 'check-ignore', '-n', '*'], stdout=subprocess.PIPE, text=True)
    
    # Dividir la salida en líneas y filtrar los nombres de archivo
    ignored_files = result.stdout.strip().split('\n')
    
    # Ordenar la lista de archivos ignorados
    ignored_files = sorted(set(file.split(':')[1].strip() for file in ignored_files if file))
    
    # Unir los nombres de archivo en una cadena separada por comas
    return ', '.join(ignored_files)