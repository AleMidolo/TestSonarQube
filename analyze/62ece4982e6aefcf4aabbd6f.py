def get_repo_archive(url: str, destination_path: Path) -> Path:
    import requests
    import tarfile
    import tempfile
    from pathlib import Path

    # Create temporary file to store downloaded archive
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    
    try:
        # Download the archive
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Write archive to temporary file
        for chunk in response.iter_content(chunk_size=8192):
            temp_file.write(chunk)
        temp_file.close()
        
        # Create destination directory if it doesn't exist
        destination_path.mkdir(parents=True, exist_ok=True)
        
        # Extract archive
        with tarfile.open(temp_file.name, 'r:gz') as tar:
            tar.extractall(path=destination_path)
            
        return destination_path
        
    finally:
        # Clean up temporary file
        Path(temp_file.name).unlink(missing_ok=True)