def _group_files_by_xml_filename(source, xmls, files):
    """
    Group files by their XML basename

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    xml_filename : str
        XML filenames
    files : list
        list of files in the folder or zipfile

    Returns
    -------
    dict
        key: name of the XML files
        value: Package
    """
    grouped_files = {}
    
    for xml in xmls:
        xml_basename = xml.split('.')[0]  # Get the basename of the XML file
        grouped_files[xml_basename] = []

        for file in files:
            if file.startswith(xml_basename):
                grouped_files[xml_basename].append(file)

    return grouped_files