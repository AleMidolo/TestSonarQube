def create_zip_file(self, files, output_file_name):
    """
        将指定的文件列表压缩成一个zip文件，并放置在指定路径中
        :param files: 字符串列表, 要压缩的文件列表
        :param output_file_name: 字符串, 指定的输出路径
        :return: True或False，表示压缩操作是否成功
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.create_zip_file(["bbb.txt", "ccc,txt", "ddd.txt"], "output/bcd")
        """
    try:
        output_dir = os.path.dirname(output_file_name)
        if output_dir and (not os.path.exists(output_dir)):
            os.makedirs(output_dir)
        with zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in files:
                if os.path.exists(file_path):
                    zipf.write(file_path, os.path.basename(file_path))
                else:
                    continue
        return True
    except Exception as e:
        print(f'Error creating zip file: {e}')
        return False