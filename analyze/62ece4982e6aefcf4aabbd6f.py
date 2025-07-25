def get_repo_archive(url: str, destination_path: Path) -> Path:
    import requests
    import tarfile
    import io

    # Download the archive
    response = requests.get(url)
    response.raise_for_status()

    # Create destination directory if it doesn't exist
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # Extract archive
    tar_bytes = io.BytesIO(response.content)
    with tarfile.open(fileobj=tar_bytes, mode='r:gz') as tar:
        tar.extractall(path=destination_path)

    return destination_path