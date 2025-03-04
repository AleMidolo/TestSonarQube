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
    
    # Iterate through XML files
    for xml in xmls:
        # Get base filename without extension
        xml_base = xml.rsplit('.', 1)[0]
        
        # Find all files that start with the XML base name
        matching_files = [f for f in files if f.startswith(xml_base)]
        
        # Add to dictionary with XML name as key and matching files as value
        grouped_files[xml] = matching_files
        
    return grouped_files