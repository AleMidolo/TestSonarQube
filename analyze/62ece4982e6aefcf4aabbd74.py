import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional, Union
from urllib.parse import urljoin

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    """
    Dado un `archive_path` existente, descomprímelo.  
    Devuelve una URL del repositorio de archivos que puede ser utilizada como URL de origen.

    Este método no maneja el caso en el que el archivo comprimido proporcionado no exista.
    """
    # Convert tmp_path to Path object if it's a string
    if isinstance(tmp_path, str):
        tmp_path = Path(tmp_path)
    
    # Create a temporary directory within tmp_path
    temp_dir = tempfile.mkdtemp(dir=tmp_path)
    
    # Determine the filename if not provided
    if filename is None:
        filename = os.path.basename(archive_path)
    
    # Extract the archive to the temporary directory
    shutil.unpack_archive(archive_path, temp_dir)
    
    # Construct the repository URL
    repo_url = urljoin('file://', temp_dir)
    
    return repo_url