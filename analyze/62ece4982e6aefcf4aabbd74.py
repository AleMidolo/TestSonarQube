def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    import os
    import shutil
    import tempfile
    from pathlib import Path
    
    # Create temporary directory
    temp_dir = tempfile.mkdtemp(dir=tmp_path)
    
    # If filename not provided, use basename of archive_path
    if not filename:
        filename = os.path.basename(archive_path)
    
    # Copy archive to temp directory
    temp_archive = os.path.join(temp_dir, filename)
    shutil.copy2(archive_path, temp_archive)
    
    # Extract archive
    shutil.unpack_archive(temp_archive, temp_dir)
    
    # Remove the archive file after extraction
    os.remove(temp_archive)
    
    # Convert temp_dir to file URL format
    repo_url = Path(temp_dir).as_uri()
    
    return repo_url