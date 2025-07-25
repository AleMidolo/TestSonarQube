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
    मौजूदा `archive_path` को अनकंप्रेस करें।  
    यह एक फ़ाइल रिपॉजिटरी URL लौटाता है जिसे ओरिजिन URL के रूप में उपयोग किया जा सकता है।  

    यह उस स्थिति को संभालने का काम नहीं करता है जहां दिया गया आर्काइव मौजूद नहीं है।
    """
    # Convert tmp_path to Path object
    tmp_path = Path(tmp_path)
    
    # Create temporary directory
    tmp_path.mkdir(parents=True, exist_ok=True)
    
    # Determine the archive type and extract
    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(tmp_path)
    elif archive_path.endswith(('.tar', '.tar.gz', '.tgz')):
        with tarfile.open(archive_path, 'r:*') as tar_ref:
            tar_ref.extractall(tmp_path)
    else:
        raise ValueError("Unsupported archive format")
    
    # If a filename is provided, return the path to that file
    if filename:
        return str(tmp_path / filename)
    
    # Otherwise, return the path to the extracted directory
    return str(tmp_path)