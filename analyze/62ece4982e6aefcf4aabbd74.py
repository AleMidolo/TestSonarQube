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
    Dato un `archive_path` esistente, decomprimilo.  
    Restituisce un URL del repository del file che può essere utilizzato come URL di origine.

    Questo metodo non gestisce il caso in cui l'archivio passato non esista.
    """
    # Convert tmp_path to Path object if it's a string
    tmp_path = Path(tmp_path) if isinstance(tmp_path, str) else tmp_path
    
    # Create a temporary directory in the specified tmp_path
    with tempfile.TemporaryDirectory(dir=tmp_path) as temp_dir:
        temp_dir_path = Path(temp_dir)
        
        # Determine the archive type and extract it
        if archive_path.endswith('.zip'):
            with ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir_path)
        elif archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
            with TarFile.open(archive_path, 'r:gz') as tar_ref:
                tar_ref.extractall(temp_dir_path)
        elif archive_path.endswith('.tar'):
            with TarFile.open(archive_path, 'r:') as tar_ref:
                tar_ref.extractall(temp_dir_path)
        else:
            raise ValueError("Unsupported archive format")
        
        # If filename is provided, move it to the root of the temp directory
        if filename:
            file_path = temp_dir_path / filename
            if not file_path.exists():
                raise FileNotFoundError(f"File {filename} not found in the archive")
            shutil.move(str(file_path), str(temp_dir_path))
        
        # Return the path to the extracted repository
        return str(temp_dir_path)