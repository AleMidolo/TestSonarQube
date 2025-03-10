import zipfile
import os
from collections import defaultdict

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
        A dictionary where keys are XML basenames and values are lists of file paths.
    """
    data = defaultdict(list)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            basename = os.path.basename(file_name)
            if basename.endswith('.xml'):
                xml_basename = basename[:-4]  # Remove '.xml' extension
                data[xml_basename].append(file_name)
    
    return dict(data)