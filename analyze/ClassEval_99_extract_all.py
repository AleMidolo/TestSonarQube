def extract_all(self, output_path):
    """
    Extract all zip files and place them in the specified path
    :param output_path: string, The location of the extracted file
    :return: True or False, representing whether the extraction operation was successful
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_all("result/aaa")
    """
    import zipfile
    import os
    
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Open and extract the zip file
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_path)
        
        return True
    except Exception as e:
        return False