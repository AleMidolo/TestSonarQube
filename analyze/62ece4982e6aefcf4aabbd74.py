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
    मौजूदा `archive_path` को अनकंप्रेस करें।  
    यह एक फ़ाइल रिपॉजिटरी URL लौटाता है जिसे ओरिजिन URL के रूप में उपयोग किया जा सकता है।  

    यह उस स्थिति को संभालने का काम नहीं करता है जहां दिया गया आर्काइव मौजूद नहीं है।
    """
    # Convert tmp_path to Path object if it's a string
    if isinstance(tmp_path, str):
        tmp_path = Path(tmp_path)
    
    # Create a temporary directory within the specified tmp_path
    temp_dir = tempfile.mkdtemp(dir=tmp_path)
    
    # Determine the archive filename
    if filename is None:
        filename = os.path.basename(archive_path)
    
    # Extract the archive based on its type
    if filename.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    elif filename.endswith('.tar.gz') or filename.endswith('.tgz'):
        with tarfile.open(archive_path, 'r:gz') as tar_ref:
            tar_ref.extractall(temp_dir)
    elif filename.endswith('.tar.bz2') or filename.endswith('.tbz'):
        with tarfile.open(archive_path, 'r:bz2') as tar_ref:
            tar_ref.extractall(temp_dir)
    elif filename.endswith('.tar'):
        with tarfile.open(archive_path, 'r:') as tar_ref:
            tar_ref.extractall(temp_dir)
    else:
        raise ValueError("Unsupported archive format")
    
    # Return the path to the extracted repository
    return temp_dir