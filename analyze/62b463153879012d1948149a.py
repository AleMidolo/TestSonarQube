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
    from collections import defaultdict
    import os

    grouped_files = defaultdict(list)

    for xml in xmls:
        xml_basename = os.path.splitext(os.path.basename(xml))[0]
        for file in files:
            if xml_basename in file:
                grouped_files[xml_basename].append(file)

    return dict(grouped_files)