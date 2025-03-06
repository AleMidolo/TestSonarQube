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
    file_groups = defaultdict(list)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith('.xml'):
                xml_filename = file_name.split('/')[-1]
                with zip_ref.open(file_name) as file:
                    content = file.read()
                    file_groups[xml_filename].append(content)
    
    return dict(file_groups)