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
    # Convert tmp_path to Path object if it's a string
    if isinstance(tmp_path, str):
        tmp_path = Path(tmp_path)
    
    # Ensure the tmp_path exists
    tmp_path.mkdir(parents=True, exist_ok=True)
    
    # Create a temporary directory within tmp_path
    with tempfile.TemporaryDirectory(dir=tmp_path) as temp_dir:
        temp_dir_path = Path(temp_dir)
        
        # Extract the archive to the temporary directory
        shutil.unpack_archive(archive_path, temp_dir_path)
        
        # If filename is provided, use it as the repository name
        if filename:
            repo_dir = temp_dir_path / filename
        else:
            # Otherwise, use the first directory found in the extracted archive
            extracted_items = list(temp_dir_path.iterdir())
            if not extracted_items:
                raise ValueError("No files or directories found in the archive.")
            repo_dir = extracted_items[0]
        
        # Move the repository to a new directory with a unique name
        final_repo_dir = tmp_path / f"repo_{os.urandom(8).hex()}"
        shutil.move(repo_dir, final_repo_dir)
        
        # Return the URL of the repository
        return urljoin("file://", str(final_repo_dir))