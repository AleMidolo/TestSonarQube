def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    import os
    import tempfile
    import tarfile
    import zipfile
    from pathlib import Path

    # Create temporary directory
    temp_dir = tempfile.mkdtemp(dir=tmp_path)
    
    # Get filename if not provided
    if filename is None:
        filename = os.path.basename(archive_path)
    
    # Handle different archive types
    if tarfile.is_tarfile(archive_path):
        with tarfile.open(archive_path) as tar:
            tar.extractall(path=temp_dir)
    elif zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path) as zip_file:
            zip_file.extractall(path=temp_dir)
            
    # Convert temp directory path to file URL format
    repo_url = Path(temp_dir).as_uri()
    
    return repo_url