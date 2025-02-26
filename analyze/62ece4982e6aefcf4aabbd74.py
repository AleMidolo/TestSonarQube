from pathlib import Path
import zipfile
import os
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
    
    # Create temporary directory if it doesn't exist
    tmp_path.mkdir(parents=True, exist_ok=True)
    
    # Unzip the archive
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(tmp_path)
    
    # Determine the repository URL
    if filename is None:
        # If no filename is provided, use the first file in the archive
        extracted_files = list(tmp_path.glob('*'))
        if extracted_files:
            filename = extracted_files[0].name
        else:
            raise ValueError("No files extracted from the archive.")
    
    # Return the repository URL
    return str(tmp_path / filename)