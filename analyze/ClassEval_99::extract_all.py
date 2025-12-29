def extract_all(self, output_path):
    """
    सभी ज़िप फ़ाइलों को निकालें और उन्हें निर्दिष्ट पथ में रखें
    :param output_path: स्ट्रिंग, निकाली गई फ़ाइल का स्थान
    :return: True या False, यह दर्शाता है कि निकासी प्रक्रिया सफल रही या नहीं
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_all("result/aaa")
    """
    try:
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            zip_file.extractall(output_path)
        return True
    except:
        return False