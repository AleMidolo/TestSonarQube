import tarfile
import requests
from pathlib import Path

def get_repo_archive(url: str, destination_path: Path) -> Path:
    """
    Given an url and a destination path, retrieve and extract .tar.gz archive
    which contains 'desc' file for each package.
    Each .tar.gz archive corresponds to an Arch Linux repo ('core', 'extra', 'community').

    Args:
        url: url of the .tar.gz archive to download
        destination_path: the path on disk where to extract archive

    Returns:
        a directory Path where the archive has been extracted to.
    """
    # Ensure the destination path exists
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # Download the archive
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    # Save the archive to a temporary file
    archive_path = destination_path / "archive.tar.gz"
    with open(archive_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # Extract the archive
    with tarfile.open(archive_path, 'r:gz') as tar:
        tar.extractall(path=destination_path)
    
    # Remove the temporary archive file
    archive_path.unlink()
    
    return destination_path