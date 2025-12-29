def create_zip_file(self, files, output_file_name):
    """
    将指定的文件列表压缩成一个zip文件，并放置在指定路径中
    :param files: 字符串列表, 要压缩的文件列表
    :param output_file_name: 字符串, 指定的输出路径
    :return: True或False，表示压缩操作是否成功
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.create_zip_file(["bbb.txt", "ccc.txt", "ddd.txt"], "output/bcd")
    """
    try:
        with zipfile.ZipFile(output_file_name, 'w') as zip_file:
            for file in files:
                zip_file.write(file)
        return True
    except:
        return False