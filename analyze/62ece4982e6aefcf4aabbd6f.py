def get_repo_archive(url: str, destination_path: Path) -> Path:
    import requests
    import tarfile
    import io

    # Create destination directory if it doesn't exist
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # Download the tar.gz file
    response = requests.get(url)
    response.raise_for_status()
    
    # Extract the tar.gz file
    tar_bytes = io.BytesIO(response.content)
    with tarfile.open(fileobj=tar_bytes, mode='r:gz') as tar:
        # Extract only 'desc' files
        for member in tar.getmembers():
            if member.name.endswith('/desc'):
                tar.extract(member, path=destination_path)
    
    return destination_path