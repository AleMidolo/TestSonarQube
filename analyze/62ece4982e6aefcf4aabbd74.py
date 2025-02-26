import os
import zipfile
from pathlib import Path
from typing import Optional, Union

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[Path, str] = "/tmp",
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
    # Ensure tmp_path is a Path object
    tmp_path = Path(tmp_path)
    tmp_path.mkdir(parents=True, exist_ok=True)

    # Extract the archive
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(tmp_path)

    # If a filename is provided, construct the repository URL
    if filename:
        file_path = tmp_path / filename
        if file_path.exists():
            return f"file://{file_path.resolve()}"
        else:
            raise FileNotFoundError(f"{filename} not found in the archive.")
    
    # If no filename is provided, return the URL of the tmp_path
    return f"file://{tmp_path.resolve()}"