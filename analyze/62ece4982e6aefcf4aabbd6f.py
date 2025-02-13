import requests
import tarfile
from pathlib import Path

def get_repo_archive(url: str, destination_path: Path) -> Path:
    response = requests.get(url)
    response.raise_for_status()
    
    tar_gz_path = destination_path / "archive.tar.gz"
    with open(tar_gz_path, 'wb') as f:
        f.write(response.content)
    
    with tarfile.open(tar_gz_path, 'r:gz') as tar:
        tar.extractall(path=destination_path)
    
    return destination_path