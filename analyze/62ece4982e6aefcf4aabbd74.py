import os
import shutil
import tarfile
import zipfile
from pathlib import Path
from typing import Optional, Union

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[Path, str] = "/tmp",
) -> str:
    """
    Dato un `archive_path` esistente, decomprimilo.  
    Restituisce un URL del repository del file che può essere utilizzato come URL di origine.

    Questo metodo non gestisce il caso in cui l'archivio passato non esista.
    """
    # Convert tmp_path to Path object
    tmp_path = Path(tmp_path)
    
    # Create temporary directory
    tmp_path.mkdir(parents=True, exist_ok=True)
    
    # Determine the file extension
    file_extension = os.path.splitext(archive_path)[1].lower()
    
    # Extract the archive
    if file_extension == '.zip':
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(tmp_path)
    elif file_extension in ['.tar', '.tar.gz', '.tgz']:
        with tarfile.open(archive_path, 'r:*') as tar_ref:
            tar_ref.extractall(tmp_path)
    else:
        raise ValueError("Unsupported archive format")
    
    # Construct the URL for the extracted repository
    if filename:
        extracted_file_path = tmp_path / filename
    else:
        extracted_file_path = next(tmp_path.glob('*'))  # Get the first extracted directory or file
    
    return f'file://{extracted_file_path.resolve()}'