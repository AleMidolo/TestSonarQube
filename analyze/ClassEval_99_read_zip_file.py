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
        # Check if the file exists
        if not hasattr(self, 'zip_file_path') or not os.path.exists(self.zip_file_path):
            return None
        
        # Open and return the ZipFile object
        zip_file = zipfile.ZipFile(self.zip_file_path, 'r')
        return zip_file
    except (zipfile.BadZipFile, IOError, OSError):
        return None