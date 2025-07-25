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

    # Create temporary directory to extract archive
    temp_dir = tempfile.mkdtemp(dir=tmp_path)
    
    # Get filename from archive_path if not provided
    if filename is None:
        filename = os.path.basename(archive_path)
    
    # Handle different archive types
    if archive_path.endswith(('.tar.gz', '.tgz')):
        with tarfile.open(archive_path, 'r:gz') as tar:
            tar.extractall(temp_dir)
    elif archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    elif archive_path.endswith('.tar'):
        with tarfile.open(archive_path, 'r:') as tar:
            tar.extractall(temp_dir)
    else:
        raise ValueError(f"Unsupported archive format: {archive_path}")

    # Convert temp directory path to file:// URL format
    repo_url = f"file://{temp_dir}"
    
    return repo_url