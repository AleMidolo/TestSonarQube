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
        basename = xml.split('.')[0]  # Get the basename of the XML file
        grouped_files[basename] = []

        for file in files:
            if file.startswith(basename):  # Check if the file starts with the XML basename
                grouped_files[basename].append(file)

    return grouped_files