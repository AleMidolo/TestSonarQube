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
    import zipfile
    from collections import defaultdict
    
    # 创建一个默认字典来存储分组
    grouped_files = defaultdict(list)
    
    # 打开zip文件
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # 获取所有文件名列表
        file_list = zip_ref.namelist()
        
        # 遍历所有文件
        for file_name in file_list:
            # 获取文件的基本名称（不包含扩展名）
            base_name = file_name.rsplit('.', 1)[0]
            
            # 如果文件名以.xml结尾，将其作为键
            if file_name.endswith('.xml'):
                xml_key = base_name
                grouped_files[xml_key].append(file_name)
            else:
                # 查找对应的XML文件名
                for xml_key in grouped_files.keys():
                    if base_name.startswith(xml_key):
                        grouped_files[xml_key].append(file_name)
                        break
    
    # 将defaultdict转换为普通字典并返回
    return dict(grouped_files)