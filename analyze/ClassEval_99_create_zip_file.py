def create_zip_file(self, files, output_file_name):
    """
        Compress the specified file list into a zip file and place it in the specified path
        :param files:list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return:True or False, representing whether the compression operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.create_zip_file(["bbb.txt", "ccc,txt", "ddd.txt"], "output/bcd")
        """
    try:
        output_dir = os.path.dirname(output_file_name)
        if output_dir and (not os.path.exists(output_dir)):
            os.makedirs(output_dir)
        with zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                if os.path.exists(file):
                    zipf.write(file, os.path.basename(file))
                else:
                    continue
        return True
    except Exception as e:
        return False