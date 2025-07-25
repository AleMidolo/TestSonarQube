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
        # Extract the archive to the temporary directory
        shutil.unpack_archive(archive_path, temp_dir)
        
        # Determine the repository path
        if filename:
            repo_path = Path(temp_dir) / filename
        else:
            # If no filename is provided, assume the archive contains a single directory
            extracted_items = list(Path(temp_dir).iterdir())
            if len(extracted_items) == 1 and extracted_items[0].is_dir():
                repo_path = extracted_items[0]
            else:
                repo_path = Path(temp_dir)
        
        # Move the repository to a permanent location
        repo_name = repo_path.name
        final_repo_path = tmp_path / repo_name
        if final_repo_path.exists():
            shutil.rmtree(final_repo_path)
        shutil.move(str(repo_path), str(final_repo_path))
    
    # Return the URL of the repository
    return urljoin("file://", str(final_repo_path))