def read_zip_file(self):
        """
        खुला फ़ाइल ऑब्जेक्ट प्राप्त करें
        :return: यदि सफल, तो खुला फ़ाइल ऑब्जेक्ट लौटाता है; अन्यथा, None लौटाता है
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> file = zfp.read_zip_file()
        """
        try:
            zip_file = zipfile.ZipFile(self.file_name, 'r')
            return zip_file
        except:
            return None