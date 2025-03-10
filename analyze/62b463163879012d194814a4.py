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
        根据XML文件名分组的文件数据
    """
    def _group_files_by_xml_filename(file_list):
        """
        根据文件的XML文件名对其进行分组。

        参数
        ----------
        file_list : `list`
            文件列表

        Returns
        -------
        dict
            根据XML文件名分组的文件数据
        """
        grouped_files = defaultdict(list)
        for file_name in file_list:
            if file_name.endswith('.xml'):
                base_name = file_name[:-4]  # 去掉.xml后缀
                grouped_files[base_name].append(file_name)
        return grouped_files

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        grouped_files = _group_files_by_xml_filename(file_list)
        return grouped_files