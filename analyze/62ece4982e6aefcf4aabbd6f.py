import tarfile
import requests
from pathlib import Path

def get_repo_archive(url: str, destination_path: Path) -> Path:
    """
    Dato un URL e un percorso di destinazione, recupera e decomprimi un archivio .tar.gz che contiene il file 'desc' per ogni pacchetto.  
    Ogni archivio .tar.gz corrisponde a un repository di Arch Linux ('core', 'extra', 'community').
    Args:
        url: URL dell'archivio .tar.gz da scaricare
        destination_path: il percorso sul disco dove estrarre l'archivio

    Returns:
        un oggetto Path che rappresenta la directory dove l'archivio è stato estratto.
    """
    # Ensure the destination directory exists
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # Download the archive
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    # Save the archive to a temporary file
    temp_archive_path = destination_path / "temp_archive.tar.gz"
    with open(temp_archive_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # Extract the archive
    with tarfile.open(temp_archive_path, 'r:gz') as tar:
        tar.extractall(path=destination_path)
    
    # Remove the temporary archive file
    temp_archive_path.unlink()
    
    return destination_path