def read_zip_file(self):
    """
    Ottieni l'oggetto del file aperto
    :return: Se ha successo, restituisce l'oggetto file aperto; altrimenti, restituisce None
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> file = zfp.read_zip_file()
    """
    import zipfile
    import os
    
    try:
        # Check if the zip file path exists and is accessible
        if hasattr(self, 'zip_file_path') and os.path.exists(self.zip_file_path):
            # Open and return the ZipFile object
            return zipfile.ZipFile(self.zip_file_path, 'r')
        else:
            return None
    except Exception:
        return None