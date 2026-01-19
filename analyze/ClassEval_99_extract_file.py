def extract_file(self, file_name, output_path):
    """
        从zip文件中提取指定名称的文件，并将其放置在指定路径中
        :param file_name:字符串, 要解压缩的文件名
        :param output_path:字符串, 解压后文件的位置
        :return: True或False，表示提取操作是否成功
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_file("bbb.txt", "result/aaa")
        """
    try:
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            zip_file.extract(file_name, output_path)
        return True
    except:
        return False