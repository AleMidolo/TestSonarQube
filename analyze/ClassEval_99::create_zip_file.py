def create_zip_file(self, files, output_file_name):
    """
        निर्दिष्ट फ़ाइल सूची को एक ज़िप फ़ाइल में संकुचित करें और इसे निर्दिष्ट पथ में रखें
        :param files: स्ट्रिंग की सूची, संकुचित करने के लिए फ़ाइलों की सूची
        :param output_file_name: स्ट्रिंग, निर्दिष्ट आउटपुट पथ
        :return: True या False, यह दर्शाता है कि संकुचन संचालन सफल था या नहीं
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