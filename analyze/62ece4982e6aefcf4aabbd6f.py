import requests
import tarfile
from pathlib import Path

def get_repo_archive(url: str, destination_path: Path) -> Path:
    """
    Dado un URL y una ruta de destino, recuperar y extraer un archivo .tar.gz que contiene el archivo 'desc' para cada paquete.  
    Cada archivo .tar.gz corresponde a un repositorio de Arch Linux ('core', 'extra', 'community').

    Argumentos:
        url: URL del archivo .tar.gz a descargar.
        destination_path: la ruta en el disco donde se extraerá el archivo.

    Retorno:
        un objeto Path que representa el directorio donde se ha extraído el archivo.
    """
    # Crear el directorio de destino si no existe
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # Descargar el archivo .tar.gz
    response = requests.get(url)
    tar_gz_path = destination_path / 'repo_archive.tar.gz'
    
    with open(tar_gz_path, 'wb') as f:
        f.write(response.content)
    
    # Extraer el archivo .tar.gz
    with tarfile.open(tar_gz_path, 'r:gz') as tar:
        tar.extractall(path=destination_path)
    
    # Eliminar el archivo .tar.gz después de la extracción
    tar_gz_path.unlink()
    
    return destination_path