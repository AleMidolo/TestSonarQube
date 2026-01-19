def extract_all(self, output_path):
    """
    提取所有 zip 文件并将其放置在指定路径中
    :param output_path: 字符串，提取文件的位置
    :return: True 或 False，表示提取操作是否成功
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_all("result/aaa")
    """
    import zipfile
    import os
    
    try:
        # 确保输出目录存在
        os.makedirs(output_path, exist_ok=True)
        
        # 打开并提取 zip 文件
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_path)
        
        return True
    except Exception as e:
        return False