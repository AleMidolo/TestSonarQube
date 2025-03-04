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
    
    # Get filename from archive path if not provided
    if filename is None:
        filename = os.path.basename(archive_path)
    
    # Extract archive to temp directory
    if archive_path.endswith('.zip'):
        shutil.unpack_archive(archive_path, temp_dir, 'zip')
    elif archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
        shutil.unpack_archive(archive_path, temp_dir, 'gztar')
    elif archive_path.endswith('.tar'):
        shutil.unpack_archive(archive_path, temp_dir, 'tar')
    else:
        raise ValueError(f"Unsupported archive format: {archive_path}")

    # Convert temp directory path to file URL format
    repo_url = Path(temp_dir).as_uri()
    
    return repo_url