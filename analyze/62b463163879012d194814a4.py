import zipfile
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
        以XML文件名为键，文件内容为值的字典
    """
    def _group_files_by_xml_filename(zip_file):
        grouped_files = defaultdict(list)
        for file_info in zip_file.infolist():
            if file_info.filename.endswith('.xml'):
                with zip_file.open(file_info) as file:
                    content = file.read()
                    grouped_files[file_info.filename].append(content)
        return grouped_files

    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        return _group_files_by_xml_filename(zip_file)