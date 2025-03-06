import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional, Union
from zipfile import ZipFile
from tarfile import TarFile

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    """
    Uncompress the existing `archive_path`.
    Returns a file repository URL that can be used as the origin URL.

    This does not handle the case where the given archive does not exist.
    """
    # Convert tmp_path to Path object if it's a string
    if isinstance(tmp_path, str):
        tmp_path = Path(tmp_path)
    
    # Create a temporary directory in the specified tmp_path
    temp_dir = tempfile.mkdtemp(dir=tmp_path)
    
    # Determine the archive type based on the file extension
    if archive_path.endswith('.zip'):
        with ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    elif archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
        with TarFile.open(archive_path, 'r:gz') as tar_ref:
            tar_ref.extractall(temp_dir)
    elif archive_path.endswith('.tar.bz2') or archive_path.endswith('.tbz2'):
        with TarFile.open(archive_path, 'r:bz2') as tar_ref:
            tar_ref.extractall(temp_dir)
    elif archive_path.endswith('.tar'):
        with TarFile.open(archive_path, 'r:') as tar_ref:
            tar_ref.extractall(temp_dir)
    else:
        raise ValueError("Unsupported archive format")
    
    # If a specific filename is provided, return the path to that file
    if filename:
        return str(Path(temp_dir) / filename)
    
    # Otherwise, return the path to the extracted directory
    return temp_dir