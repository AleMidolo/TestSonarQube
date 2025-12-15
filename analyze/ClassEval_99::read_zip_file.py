def read_zip_file(self):
        """
        获取打开的文件对象
        :return: 如果成功，返回打开的文件对象；否则，返回 None
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> file = zfp.read_zip_file()
        """
        try:
            zip_file = zipfile.ZipFile(self.file_name, 'r')
            return zip_file
        except:
            return None