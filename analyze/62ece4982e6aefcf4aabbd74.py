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
        
        # Determine the repository path
        if filename:
            repo_path = temp_dir_path / filename
        else:
            # If no filename is provided, assume the archive contains a single directory
            contents = list(temp_dir_path.iterdir())
            if len(contents) == 1 and contents[0].is_dir():
                repo_path = contents[0]
            else:
                repo_path = temp_dir_path
        
        # Generate a URL for the repository
        repo_url = urljoin('file://', str(repo_path.absolute()))
        
        return repo_url