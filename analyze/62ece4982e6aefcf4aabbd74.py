import os
import shutil
import tarfile
import tempfile
from pathlib import Path
from typing import Optional, Union
from zipfile import ZipFile

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
    
    # Create a temporary directory to extract the archive
    extract_dir = tempfile.mkdtemp(dir=tmp_path)
    
    # Determine the archive type and extract it
    if archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
        with tarfile.open(archive_path, 'r:gz') as tar:
            tar.extractall(path=extract_dir)
    elif archive_path.endswith('.tar'):
        with tarfile.open(archive_path, 'r:') as tar:
            tar.extractall(path=extract_dir)
    elif archive_path.endswith('.zip'):
        with ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
    else:
        raise ValueError(f"Unsupported archive format: {archive_path}")
    
    # If a specific filename is provided, ensure it exists in the extracted directory
    if filename:
        extracted_path = os.path.join(extract_dir, filename)
        if not os.path.exists(extracted_path):
            raise FileNotFoundError(f"File {filename} not found in the archive.")
        return extracted_path
    
    # Return the path to the extracted directory
    return extract_dir