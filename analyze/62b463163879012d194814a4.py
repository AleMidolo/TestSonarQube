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
        A dictionary where keys are XML basenames and values are lists of file data.
    """
    data_dict = defaultdict(list)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            base_name = os.path.splitext(file_name)[0]
            if base_name.endswith('.xml'):
                with zip_ref.open(file_name) as file:
                    file_data = file.read()
                    data_dict[base_name].append(file_data)
    
    return dict(data_dict)