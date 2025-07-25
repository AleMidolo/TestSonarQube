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
    # Convert tmp_path to Path object if it's a string
    tmp_path = Path(tmp_path) if isinstance(tmp_path, str) else tmp_path
    
    # Ensure the temporary directory exists
    tmp_path.mkdir(parents=True, exist_ok=True)
    
    # Create a temporary directory to extract the archive
    extract_dir = tempfile.mkdtemp(dir=tmp_path)
    
    # Determine the archive type based on the file extension
    if archive_path.endswith('.zip'):
        with ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
    elif archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
        with TarFile.open(archive_path, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_dir)
    elif archive_path.endswith('.tar'):
        with TarFile.open(archive_path, 'r:') as tar_ref:
            tar_ref.extractall(extract_dir)
    else:
        raise ValueError("Unsupported archive format")
    
    # If a specific filename is provided, return the path to that file
    if filename:
        extracted_file_path = os.path.join(extract_dir, filename)
        if not os.path.exists(extracted_file_path):
            raise FileNotFoundError(f"The file {filename} was not found in the archive.")
        return extracted_file_path
    
    # Otherwise, return the path to the extracted directory
    return extract_dir