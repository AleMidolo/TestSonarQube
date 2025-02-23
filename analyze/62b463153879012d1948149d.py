import os
import xml.etree.ElementTree as ET

def _explore_folder(folder):
    """
    Get packages' data from folder

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    folder : str
        Folder of the package
    Returns
    -------
    dict
    """
    package_data = {}
    
    for filename in os.listdir(folder):
        if filename.endswith('.xml'):
            basename = os.path.splitext(filename)[0]
            file_path = os.path.join(folder, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()
            package_data[basename] = {child.tag: child.text for child in root}
    
    return package_data