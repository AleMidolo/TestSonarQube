def read_zip_file(self):
    """
        Ottieni l'oggetto del file aperto
        :return: Se ha successo, restituisce l'oggetto file aperto; altrimenti, restituisce None
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> file = zfp.read_zip_file()
        """
    try:
        zip_file = zipfile.ZipFile(self.file_name, 'r')
        return zip_file
    except:
        return None