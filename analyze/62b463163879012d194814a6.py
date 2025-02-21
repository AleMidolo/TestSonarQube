import zipfile

def files_list_from_zipfile(zip_path):
    """Restituisce i file presenti in `zip_path`."""
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        return zip_file.namelist()