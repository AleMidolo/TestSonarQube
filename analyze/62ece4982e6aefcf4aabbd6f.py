import tarfile
import requests
from pathlib import Path

def get_repo_archive(url: str, destination_path: Path) -> Path:
    """
    给定一个 URL 和目标路径，下载并提取包含每个软件包的 'desc' 文件的 .tar.gz 压缩包。
    每个 .tar.gz 压缩包对应一个 Arch Linux 仓库（如 'core'、'extra'、'community'）。

    参数：
      url：要下载的 .tar.gz 压缩包的 URL。
      destination_path：在磁盘上提取压缩包的目标路径。

    返回值：
      返回提取压缩包的目录路径。
    """
    # 确保目标路径存在
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # 下载压缩包
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    # 保存压缩包到临时文件
    temp_file = destination_path / "temp_archive.tar.gz"
    with open(temp_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # 提取压缩包
    with tarfile.open(temp_file, 'r:gz') as tar:
        tar.extractall(path=destination_path)
    
    # 删除临时文件
    temp_file.unlink()
    
    # 返回提取后的目录路径
    return destination_path