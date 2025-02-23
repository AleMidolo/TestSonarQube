import requests
import tarfile
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
    # 创建目标路径目录
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # 下载 .tar.gz 文件
    response = requests.get(url)
    tar_file_path = destination_path / 'repo_archive.tar.gz'
    
    with open(tar_file_path, 'wb') as f:
        f.write(response.content)
    
    # 解压 .tar.gz 文件
    with tarfile.open(tar_file_path, 'r:gz') as tar:
        tar.extractall(path=destination_path)
    
    # 返回提取的目录路径
    return destination_path