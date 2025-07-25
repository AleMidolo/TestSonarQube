import zipfile
import os
from collections import defaultdict

def _explore_zipfile(zip_path):
    """
    通过 `_group_files_by_xml_filename` 对给定的 zip 路径进行分组。

    从`zip_path`获取包数据。

    根据文件的XML文件名对其进行分组，并用字典格式返回数据。

    参数
    ----------
    zip_path : `str`
        zip文件路径
    Returns
    -------
    dict
    """
    grouped_files = defaultdict(list)

    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for file_info in zip_file.infolist():
            if file_info.filename.endswith('.xml'):
                xml_filename = os.path.basename(file_info.filename)
                grouped_files[xml_filename].append(file_info.filename)

    return dict(grouped_files)