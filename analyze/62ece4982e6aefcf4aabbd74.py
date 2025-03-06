import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional, Union
import tarfile
import zipfile

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    """
    Given an existing archive_path, uncompress it.
    Returns a file repo url which can be used as origin url.

    This does not deal with the case where the archive passed along does not exist.
    """
    # Convert tmp_path to Path object if it's a string
    if isinstance(tmp_path, str):
        tmp_path = Path(tmp_path)
    
    # Create a temporary directory within tmp_path
    temp_dir = tempfile.mkdtemp(dir=tmp_path)
    
    # Determine the archive type based on the file extension
    if archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
        with tarfile.open(archive_path, 'r:gz') as tar:
            tar.extractall(path=temp_dir)
    elif archive_path.endswith('.tar'):
        with tarfile.open(archive_path, 'r:') as tar:
            tar.extractall(path=temp_dir)
    elif archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    else:
        raise ValueError("Unsupported archive format")
    
    # If filename is provided, return the path to the specific file
    if filename:
        return str(Path(temp_dir) / filename)
    
    # Otherwise, return the path to the extracted directory
    return temp_dir