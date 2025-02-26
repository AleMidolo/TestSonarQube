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
    
    # Extract the archive based on its type
    if file_extension == '.zip':
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(tmp_path)
    elif file_extension in ['.tar', '.tar.gz', '.tgz']:
        with tarfile.open(archive_path, 'r:*') as tar_ref:
            tar_ref.extractall(tmp_path)
    else:
        raise ValueError("Unsupported archive format: {}".format(file_extension))
    
    # If a filename is provided, construct the repository URL
    if filename:
        repo_path = tmp_path / filename
    else:
        # If no filename is provided, use the archive name without extension
        repo_name = os.path.basename(archive_path).rsplit('.', 1)[0]
        repo_path = tmp_path / repo_name
    
    # Return the URL of the repository
    return str(repo_path.resolve())