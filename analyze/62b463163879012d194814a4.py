import zipfile
import os
from collections import defaultdict
import xml.etree.ElementTree as ET

def _explore_zipfile(zip_path):
    """
    Get packages' data from zip_path

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    zip_path : str
        zip file path
    Returns
    -------
    dict
    """
    data_dict = defaultdict(list)

    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for file_info in zip_file.infolist():
            if file_info.filename.endswith('.xml'):
                basename = os.path.basename(file_info.filename)
                with zip_file.open(file_info.filename) as file:
                    xml_content = file.read()
                    data_dict[basename].append(xml_content)

    return dict(data_dict)