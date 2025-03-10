import os
import shutil
import tarfile
import zipfile
from pathlib import Path
from typing import Optional, Union
from tempfile import mkdtemp

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    # Ensure tmp_path is a Path object
    tmp_path = Path(tmp_path)
    tmp_path.mkdir(parents=True, exist_ok=True)
    
    # Create a temporary directory to extract the archive
    extract_dir = Path(mkdtemp(dir=tmp_path))
    
    # Determine the archive type and extract it
    if archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
        with tarfile.open(archive_path, 'r:gz') as tar:
            tar.extractall(path=extract_dir)
    elif archive_path.endswith('.tar'):
        with tarfile.open(archive_path, 'r:') as tar:
            tar.extractall(path=extract_dir)
    elif archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(path=extract_dir)
    else:
        raise ValueError("Unsupported archive format")
    
    # If filename is provided, ensure it exists in the extracted directory
    if filename:
        extracted_file = extract_dir / filename
        if not extracted_file.exists():
            raise FileNotFoundError(f"File {filename} not found in the archive")
    
    # Return the path to the extracted directory as a string
    return str(extract_dir)