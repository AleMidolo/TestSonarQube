import requests
import tarfile
from pathlib import Path
import shutil

def get_repo_archive(url: str, destination_path: Path) -> Path:
    # Create the destination directory if it doesn't exist
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # Download the .tar.gz file
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Failed to download the archive from {url}")
    
    # Save the downloaded file temporarily
    temp_file = destination_path / "temp_archive.tar.gz"
    with open(temp_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # Extract the .tar.gz file
    with tarfile.open(temp_file, 'r:gz') as tar:
        tar.extractall(path=destination_path)
    
    # Remove the temporary .tar.gz file
    temp_file.unlink()
    
    # Return the path where the archive was extracted
    return destination_path