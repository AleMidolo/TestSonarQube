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
    tmp_path = Path(tmp_path)
    tmp_path.mkdir(parents=True, exist_ok=True)

    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(tmp_path)
    elif archive_path.endswith(('.tar', '.tar.gz', '.tgz')):
        with tarfile.open(archive_path, 'r:*') as tar_ref:
            tar_ref.extractall(tmp_path)
    else:
        raise ValueError("Unsupported archive format")

    if filename:
        extracted_path = tmp_path / filename
    else:
        extracted_path = next(tmp_path.iterdir())

    return str(extracted_path.resolve())