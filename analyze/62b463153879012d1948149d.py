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
    file_groups = defaultdict(list)
    
    for filename in os.listdir(folder):
        if filename.endswith('.xml'):
            xml_filename = filename
            # Assuming the XML filename is used to group related files
            base_name = os.path.splitext(xml_filename)[0]
            file_groups[base_name].append(os.path.join(folder, filename))
        else:
            # Group other files based on their related XML file
            base_name = os.path.splitext(filename)[0]
            file_groups[base_name].append(os.path.join(folder, filename))
    
    return dict(file_groups)