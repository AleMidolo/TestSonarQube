import requests
import tarfile
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
    
    # Download the .tar.gz file
    response = requests.get(url)
    tar_file_path = destination_path / 'archive.tar.gz'
    
    with open(tar_file_path, 'wb') as f:
        f.write(response.content)
    
    # Extract the .tar.gz file
    with tarfile.open(tar_file_path, 'r:gz') as tar:
        tar.extractall(path=destination_path)
    
    # Return the path where the archive has been extracted
    return destination_path