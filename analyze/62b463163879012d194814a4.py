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
        for file_info in zip_ref.infolist():
            if not file_info.is_dir():
                file_name = os.path.basename(file_info.filename)
                if file_name.endswith('.xml'):
                    basename = os.path.splitext(file_name)[0]
                    data[basename].append(file_info.filename)
    
    return dict(data)