import os

def _group_files_by_xml_filename(source, xmls, files):
    """
    Group files by their XML basename

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    source : str
        The source directory or zipfile path
    xmls : list
        List of XML filenames
    files : list
        List of files in the folder or zipfile

    Returns
    -------
    dict
        key: name of the XML files
        value: list of files associated with the XML file
    """
    grouped_files = {}
    
    for xml in xmls:
        xml_basename = os.path.splitext(xml)[0]
        associated_files = [file for file in files if file.startswith(xml_basename)]
        grouped_files[xml] = associated_files
    
    return grouped_files