import requests
import tarfile
from pathlib import Path
import shutil

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

    # Download the archive
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # Save the archive to a temporary file
    temp_archive_path = destination_path / "temp_archive.tar.gz"
    with open(temp_archive_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    # Extract the archive
    with tarfile.open(temp_archive_path, 'r:gz') as tar:
        tar.extractall(path=destination_path)

    # Remove the temporary archive file
    temp_archive_path.unlink()

    # Return the path where the archive was extracted
    return destination_path