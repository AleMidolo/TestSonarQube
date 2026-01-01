def read_zip_file(self):
    """
        Obtener objeto de archivo abierto
        :return: Si tiene éxito, devuelve el objeto de archivo abierto; de lo contrario, devuelve None
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> file = zfp.read_zip_file()
        """
    try:
        zip_file = zipfile.ZipFile(self.file_name, 'r')
        return zip_file
    except:
        return None