import zipfile

def files_list_from_zipfile(zip_path):
    """Return the files in `zip_path`"""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        return zip_ref.namelist()