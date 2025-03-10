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
    # Ensure tmp_path is a Path object
    tmp_path = Path(tmp_path)
    
    # Create a temporary directory in the specified tmp_path
    with tempfile.TemporaryDirectory(dir=tmp_path) as temp_dir:
        temp_dir_path = Path(temp_dir)
        
        # Determine the archive type based on the file extension
        if archive_path.endswith('.zip'):
            with ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir_path)
        elif archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
            with TarFile.open(archive_path, 'r:gz') as tar_ref:
                tar_ref.extractall(temp_dir_path)
        elif archive_path.endswith('.tar.bz2') or archive_path.endswith('.tbz'):
            with TarFile.open(archive_path, 'r:bz2') as tar_ref:
                tar_ref.extractall(temp_dir_path)
        else:
            raise ValueError("Unsupported archive format")
        
        # If filename is provided, ensure it exists in the extracted files
        if filename:
            extracted_file_path = temp_dir_path / filename
            if not extracted_file_path.exists():
                raise FileNotFoundError(f"File {filename} not found in the archive")
        
        # Return the path to the extracted repository
        return str(temp_dir_path)