def create_zip_file(self, files, output_file_name):
    """
    Compress the specified file list into a zip file and place it in the specified path
    :param files:list of string, List of files to compress
    :param output_file_name: string, Specified output path
    :return:True or False, representing whether the compression operation was successful
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.create_zip_file(["bbb.txt", "ccc,txt", "ddd.txt"], "output/bcd")
    """
    import zipfile
    import os
    
    try:
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_file_name)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Add .zip extension if not present
        if not output_file_name.endswith('.zip'):
            output_file_name += '.zip'
        
        # Create the zip file
        with zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                if os.path.exists(file):
                    # Add file to zip, using just the filename as the archive name
                    zipf.write(file, os.path.basename(file))
                else:
                    # If any file doesn't exist, return False
                    return False
        
        return True
    except Exception as e:
        return False