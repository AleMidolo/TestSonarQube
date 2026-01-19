def extract_all(self, output_path):
    """
    सभी ज़िप फ़ाइलों को निकालें और उन्हें निर्दिष्ट पथ में रखें
    :param output_path: स्ट्रिंग, निकाली गई फ़ाइल का स्थान
    :return: True या False, यह दर्शाता है कि निकासी प्रक्रिया सफल रही या नहीं
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_all("result/aaa")
    """
    import zipfile
    import os
    
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Open and extract the zip file
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_path)
        
        return True
    except Exception as e:
        return False