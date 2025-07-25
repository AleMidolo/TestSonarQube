def _group_files_by_xml_filename(source, xmls, files):
    """
    将文件按 XML 文件名分组并以字典格式返回数据。

    按 XML 文件的文件名分组文件

    将文件按其 XML 文件的文件名分组，并以字典格式返回数据。

    参数
    ----------
    xml_filename: str  
        XML 文件名  
    files: list  
        文件夹或压缩文件中的文件列表  

    返回值
    -------
    dict
        键：XML 文件的名称  
        值：Package  
    """
    result = {}
    
    # 遍历所有XML文件
    for xml in xmls:
        # 获取XML文件名(不含扩展名)
        xml_name = xml.rsplit('.', 1)[0]
        
        # 找到与该XML文件名相关的所有文件
        related_files = []
        for file in files:
            # 如果文件名以XML文件名开头
            if file.startswith(xml_name):
                related_files.append(file)
                
        # 如果找到相关文件，添加到结果字典
        if related_files:
            result[xml_name] = {
                'source': source,
                'xml': xml,
                'files': related_files
            }
            
    return result