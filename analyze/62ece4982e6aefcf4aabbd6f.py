import requests
import tarfile
from pathlib import Path

def get_repo_archive(url: str, destination_path: Path) -> Path:
    """
    दिए गए URL और गंतव्य पथ के आधार पर, `.tar.gz` संग्रह को प्राप्त करें और निकालें,
    जिसमें प्रत्येक पैकेज के लिए 'desc' फ़ाइल होती है।
    प्रत्येक `.tar.gz` संग्रह एक Arch Linux रिपॉजिटरी ('core', 'extra', 'community') से संबंधित होता है।

    तर्क (Args):
        url: `.tar.gz` संग्रह को डाउनलोड करने का URL।
        destination_path: वह पथ (डिस्क पर) जहाँ संग्रह को निकाला जाएगा।

    वापसी मान (Returns):
        वह डायरेक्टरी पथ (Path) जहाँ संग्रह को निकाला गया है।
    """
    # Ensure the destination directory exists
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # Download the .tar.gz archive
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    # Save the archive to a temporary file
    archive_path = destination_path / "archive.tar.gz"
    with open(archive_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # Extract the archive
    with tarfile.open(archive_path, 'r:gz') as tar:
        tar.extractall(path=destination_path)
    
    # Remove the temporary archive file
    archive_path.unlink()
    
    return destination_path