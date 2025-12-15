def extract_file(self, file_name, output_path):
    """
    Extract a specified file from the zip file and place it in the specified path
    :param file_name: string, The name of the file to extract
    :param output_path: string, The location where the extracted file will be placed
    :return: True or False, representing whether the extraction operation was successful
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_file("bbb.txt", "result/aaa")
    """
    
    try:
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            zip_file.extract(file_name, output_path)
        return True
    except:
        return False