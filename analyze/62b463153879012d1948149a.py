def _group_files_by_xml_filename(source, xmls, files):
    """
    将文件按 XML 文件名分组并以字典格式返回数据。

    按 XML 文件的文件名分组文件

    将文件按其 XML 文件的文件名分组，并以字典格式返回数据。

    参数
    ----------
    source: str
        源文件路径
    xmls: list
        XML 文件列表
    files: list
        文件夹或压缩文件中的文件列表

    返回值
    -------
    dict
        键：XML 文件的名称
        值：对应的文件列表
    """
    grouped_files = {}
    
    for xml in xmls:
        xml_filename = xml.split('/')[-1]  # 获取 XML 文件名
        grouped_files[xml_filename] = []
        
        for file in files:
            if xml_filename in file:
                grouped_files[xml_filename].append(file)
    
    return grouped_files