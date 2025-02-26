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
    """
    data = defaultdict(list)

    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for file_info in zip_file.infolist():
            if file_info.filename.endswith('.xml'):
                basename = os.path.basename(file_info.filename)
                data[basename].append(zip_file.read(file_info.filename))

    return dict(data)