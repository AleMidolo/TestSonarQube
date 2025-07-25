import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional, Union
from zipfile import ZipFile
from tarfile import TarFile

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    """
    给定一个已存在的 `archive_path`，解压该文件。
    返回一个可以用作源 URL 的文件仓库 URL。

    此函数不处理传入的归档文件不存在的情况。

    @param archive_path : 归档文件路径  
    @param filename: 文件名  
    @param tmp_path: 临时文件路径  
    @return 仓库 URL
    """
    # Convert tmp_path to Path object if it's a string
    tmp_path = Path(tmp_path) if isinstance(tmp_path, str) else tmp_path
    
    # Create a temporary directory within tmp_path
    with tempfile.TemporaryDirectory(dir=tmp_path) as temp_dir:
        temp_dir_path = Path(temp_dir)
        
        # Determine the archive type and extract it
        if archive_path.endswith('.zip'):
            with ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir_path)
        elif archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz'):
            with TarFile.open(archive_path, 'r:gz') as tar_ref:
                tar_ref.extractall(temp_dir_path)
        elif archive_path.endswith('.tar.bz2') or archive_path.endswith('.tbz2'):
            with TarFile.open(archive_path, 'r:bz2') as tar_ref:
                tar_ref.extractall(temp_dir_path)
        elif archive_path.endswith('.tar'):
            with TarFile.open(archive_path, 'r:') as tar_ref:
                tar_ref.extractall(temp_dir_path)
        else:
            raise ValueError(f"Unsupported archive format: {archive_path}")
        
        # If filename is provided, move it to the root of the temp directory
        if filename:
            file_path = temp_dir_path / filename
            if not file_path.exists():
                raise FileNotFoundError(f"File {filename} not found in the archive.")
            shutil.move(str(file_path), str(temp_dir_path))
        
        # Return the path to the extracted directory as a string
        return str(temp_dir_path)