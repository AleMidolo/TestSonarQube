def read_zip_file(self):
    """
    Get open file object
    :return:If successful, returns the open file object; otherwise, returns None
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> file = zfp.read_zip_file()
    """
    import zipfile
    import os
    
    try:
        if hasattr(self, 'zip_file_path') and self.zip_file_path:
            if os.path.exists(self.zip_file_path):
                return zipfile.ZipFile(self.zip_file_path, 'r')
        return None
    except Exception:
        return None