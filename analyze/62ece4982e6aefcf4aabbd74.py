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
    tmp_path = Path(tmp_path) if isinstance(tmp_path, str) else tmp_path
    
    # Ensure the tmp_path exists
    tmp_path.mkdir(parents=True, exist_ok=True)
    
    # Create a temporary directory within tmp_path
    with tempfile.TemporaryDirectory(dir=tmp_path) as temp_dir:
        # Extract the archive to the temporary directory
        shutil.unpack_archive(archive_path, temp_dir)
        
        # If filename is provided, use it as the repository name
        if filename:
            repo_name = filename
        else:
            # Use the archive's basename without extension as the repository name
            repo_name = Path(archive_path).stem
        
        # Create the final repository path
        repo_path = tmp_path / repo_name
        
        # Move the extracted contents to the final repository path
        shutil.move(temp_dir, repo_path)
        
        # Generate the URL for the repository
        repo_url = urljoin("file://", str(repo_path))
        
        return repo_url