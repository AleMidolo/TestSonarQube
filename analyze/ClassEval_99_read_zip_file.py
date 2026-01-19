def read_zip_file(self):
    """
        Get open file object
        :return: If successful, returns the open file object; otherwise, returns None
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> file = zfp.read_zip_file()
        """
    try:
        zip_file = zipfile.ZipFile(self.file_name, 'r')
        return zip_file
    except:
        return None