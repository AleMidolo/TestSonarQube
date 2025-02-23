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

    # Salva l'archivio .tar.gz temporaneamente
    archive_path = destination_path / "archive.tar.gz"
    with open(archive_path, 'wb') as f:
        f.write(response.content)

    # Decomprime l'archivio
    with tarfile.open(archive_path, 'r:gz') as tar:
        tar.extractall(path=destination_path)

    # Rimuove l'archivio scaricato
    archive_path.unlink()

    return destination_path