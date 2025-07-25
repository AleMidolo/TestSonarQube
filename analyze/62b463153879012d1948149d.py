import os
from collections import defaultdict

def _explore_folder(folder):
    """
    通过使用 _group_files_by_xml_filename 将给定组中的文件进行分组。

    从文件夹中获取包的数据

    根据 XML 文件的文件名对文件进行分组，并以字典格式返回数据。

    参数
    ----------
    folder: `str`  
        包所在的文件夹

    返回值
    -------
    dict
    """
    def _group_files_by_xml_filename(files):
        """
        根据 XML 文件的文件名对文件进行分组。

        参数
        ----------
        files: `list`  
            文件列表

        返回值
        -------
        dict
        """
        grouped_files = defaultdict(list)
        for file in files:
            if file.endswith('.xml'):
                base_name = os.path.splitext(file)[0]
                grouped_files[base_name].append(file)
            else:
                base_name = os.path.splitext(file)[0]
                grouped_files[base_name].append(file)
        return grouped_files

    if not os.path.isdir(folder):
        raise ValueError(f"The folder {folder} does not exist.")

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    return _group_files_by_xml_filename(files)