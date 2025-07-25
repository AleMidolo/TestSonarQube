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
    
    # Get filename if not provided
    if not filename:
        filename = os.path.basename(archive_path)
    
    # Extract archive based on file extension
    if filename.endswith('.zip'):
        shutil.unpack_archive(archive_path, temp_dir, 'zip')
    elif filename.endswith(('.tar.gz', '.tgz')):
        shutil.unpack_archive(archive_path, temp_dir, 'gztar') 
    elif filename.endswith('.tar'):
        shutil.unpack_archive(archive_path, temp_dir, 'tar')
    else:
        # For other formats, just copy the file
        shutil.copy2(archive_path, temp_dir)

    # Convert temp directory path to file URL
    repo_url = Path(temp_dir).as_uri()
    
    return repo_url