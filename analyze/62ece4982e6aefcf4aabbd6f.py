import requests
import tarfile
from pathlib import Path
import shutil

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
    if response.status_code != 200:
        raise Exception(f"Failed to download archive from {url}")
    
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