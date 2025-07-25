def get_repo_archive(url: str, destination_path: Path) -> Path:
    import requests
    import tarfile
    import tempfile
    from pathlib import Path

    # Create destination directory if it doesn't exist
    destination_path.mkdir(parents=True, exist_ok=True)

    # Download the archive
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # Create a temporary file to store the downloaded archive
    with tempfile.NamedTemporaryFile() as temp_file:
        # Write archive content to temporary file
        for chunk in response.iter_content(chunk_size=8192):
            temp_file.write(chunk)
        temp_file.flush()

        # Extract archive to destination path
        with tarfile.open(temp_file.name, 'r:gz') as tar:
            tar.extractall(path=destination_path)

    return destination_path