import os
import shutil
import zipfile
from pathlib import Path
from typing import Optional, Union

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[Path, str] = "/tmp",
) -> str:
    tmp_path = Path(tmp_path)
    tmp_path.mkdir(parents=True, exist_ok=True)
    
    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(tmp_path)
    else:
        raise ValueError("Unsupported archive format")
    
    if filename is None:
        filename = os.path.basename(archive_path).replace('.zip', '')
    
    repo_path = tmp_path / filename
    return f'file://{repo_path.resolve()}'