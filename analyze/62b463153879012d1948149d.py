import os
from collections import defaultdict

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
        A dictionary where keys are XML basenames and values are lists of file paths.
    """
    if not os.path.exists(folder):
        raise FileNotFoundError(f"The folder {folder} does not exist.")

    file_groups = defaultdict(list)

    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.xml'):
                basename = os.path.splitext(file)[0]
                file_groups[basename].append(os.path.join(root, file))

    return dict(file_groups)