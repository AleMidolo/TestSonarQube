import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional, Union
import zipfile
import tarfile

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
    
    # Determine the filename if not provided
    if filename is None:
        filename = os.path.basename(archive_path)
    
    # Extract the archive based on its type
    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    elif archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
        with tarfile.open(archive_path, 'r:gz') as tar_ref:
            tar_ref.extractall(temp_dir)
    elif archive_path.endswith('.tar.bz2') or archive_path.endswith('.tbz'):
        with tarfile.open(archive_path, 'r:bz2') as tar_ref:
            tar_ref.extractall(temp_dir)
    elif archive_path.endswith('.tar'):
        with tarfile.open(archive_path, 'r:') as tar_ref:
            tar_ref.extractall(temp_dir)
    else:
        raise ValueError(f"Unsupported archive format: {archive_path}")
    
    # Return the path to the extracted repository
    return temp_dir