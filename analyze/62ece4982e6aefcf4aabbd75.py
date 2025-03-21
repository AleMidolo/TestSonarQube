import subprocess

def addignored(ignored):
    """
    Usa el comando de git para obtener los nombres de los archivos, conviértelos en una lista, ordena la lista para incluir solo los archivos ignorados, y devuelve esos archivos como una única cadena con cada nombre de archivo separado por una coma.
    """
    # Obtener la lista de archivos ignorados usando git ls-files --ignored --exclude-standard
    result = subprocess.run(['git', 'ls-files', '--ignored', '--exclude-standard'], stdout=subprocess.PIPE, text=True)
    ignored_files = result.stdout.splitlines()
    
    # Filtrar los archivos ignorados que coincidan con la lista proporcionada
    filtered_files = [file for file in ignored_files if file in ignored]
    
    # Ordenar la lista de archivos ignorados
    filtered_files.sort()
    
    # Convertir la lista en una cadena separada por comas
    return ', '.join(filtered_files)