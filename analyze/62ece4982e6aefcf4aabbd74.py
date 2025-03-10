import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional, Union
import zipfile
import tarfile

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    """
    Uncompress the existing `archive_path`.
    Returns a file repository URL that can be used as the origin URL.

    This does not handle the case where the given archive does not exist.
    """
    # Convert tmp_path to Path object if it's a string
    tmp_path = Path(tmp_path) if isinstance(tmp_path, str) else tmp_path
    
    # Create a temporary directory within tmp_path
    with tempfile.TemporaryDirectory(dir=tmp_path) as temp_dir:
        temp_dir_path = Path(temp_dir)
        
        # Determine the archive type based on the file extension
        if archive_path.endswith('.zip'):
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir_path)
        elif archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
            with tarfile.open(archive_path, 'r:gz') as tar_ref:
                tar_ref.extractall(temp_dir_path)
        elif archive_path.endswith('.tar.bz2') or archive_path.endswith('.tbz2'):
            with tarfile.open(archive_path, 'r:bz2') as tar_ref:
                tar_ref.extractall(temp_dir_path)
        elif archive_path.endswith('.tar'):
            with tarfile.open(archive_path, 'r:') as tar_ref:
                tar_ref.extractall(temp_dir_path)
        else:
            raise ValueError("Unsupported archive format")
        
        # If filename is provided, move the extracted content to a new directory with that name
        if filename:
            final_dir = temp_dir_path / filename
            os.makedirs(final_dir, exist_ok=True)
            for item in temp_dir_path.iterdir():
                if item.name != filename:
                    shutil.move(str(item), str(final_dir))
            return str(final_dir)
        else:
            return str(temp_dir_path)