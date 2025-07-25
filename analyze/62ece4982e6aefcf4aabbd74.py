import os
import zipfile
from pathlib import Path
from typing import Optional, Union

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[Path, str] = "/tmp",
) -> str:
    """
    Dado un `archive_path` existente, descomprímelo.  
    Devuelve una URL del repositorio de archivos que puede ser utilizada como URL de origen.

    Este método no maneja el caso en el que el archivo comprimido proporcionado no exista.
    """
    # Convert tmp_path to Path object
    tmp_path = Path(tmp_path)
    
    # Create temporary directory if it doesn't exist
    tmp_path.mkdir(parents=True, exist_ok=True)
    
    # Define the extraction path
    extraction_path = tmp_path / Path(archive_path).stem
    
    # Unzip the archive
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_path)
    
    # Return the URL of the repository
    return f"file://{extraction_path.resolve()}"