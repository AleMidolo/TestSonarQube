import subprocess

def addignored(ignored):
    """
    Usa el comando de git para obtener los nombres de los archivos, conviértelos en una lista, ordena la lista para incluir solo los archivos ignorados, y devuelve esos archivos como una única cadena con cada nombre de archivo separado por una coma.
    """
    # Obtener la lista de archivos ignorados usando git
    result = subprocess.run(['git', 'ls-files', '--others', '--ignored', '--exclude-standard'], stdout=subprocess.PIPE)
    ignored_files = result.stdout.decode('utf-8').splitlines()
    
    # Filtrar los archivos ignorados
    ignored_files = [file for file in ignored_files if file in ignored]
    
    # Ordenar la lista de archivos ignorados
    ignored_files.sort()
    
    # Devolver los archivos ignorados como una cadena separada por comas
    return ', '.join(ignored_files)