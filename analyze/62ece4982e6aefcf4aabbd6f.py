import requests
import tarfile
from pathlib import Path
import shutil

def get_repo_archive(url: str, destination_path: Path) -> Path:
    # Create the destination directory if it doesn't exist
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # Download the .tar.gz archive
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Failed to download the archive from {url}")
    
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
    
    # Return the path where the archive was extracted
    return destination_path