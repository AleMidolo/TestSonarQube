import requests
import tarfile
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
    # Scarica l'archivio
    response = requests.get(url)
    response.raise_for_status()  # Verifica che la richiesta sia andata a buon fine

    # Crea la directory di destinazione se non esiste
    destination_path.mkdir(parents=True, exist_ok=True)

    # Percorso del file temporaneo
    temp_file_path = destination_path / "archive.tar.gz"

    # Scrivi il contenuto scaricato in un file temporaneo
    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(response.content)

    # Estrai l'archivio
    with tarfile.open(temp_file_path, 'r:gz') as tar:
        tar.extractall(path=destination_path)

    # Rimuovi il file temporaneo
    temp_file_path.unlink()

    return destination_path