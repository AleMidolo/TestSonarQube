def extract_all(self, output_path):
    """
    提取所有 zip 文件并将其放置在指定路径中
    :param output_path: 字符串，提取文件的位置
    :return: True 或 False，表示提取操作是否成功
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_all("result/aaa")
    """
    try:
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            zip_file.extractall(output_path)
        return True
    except:
        return False