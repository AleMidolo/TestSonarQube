def extract_file(self, file_name, output_path):
    """
    निर्दिष्ट नाम के साथ फ़ाइल को ज़िप फ़ाइल से निकालें और इसे निर्दिष्ट पथ में रखें
    :param file_name:string, अनकंप्रेस की जाने वाली फ़ाइल का नाम
    :param output_path:string, निकाली गई फ़ाइल का स्थान
    :return: True या False, यह दर्शाता है कि निष्कर्षण प्रक्रिया सफल रही या नहीं
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_file("bbb.txt", "result/aaa")
    """
    import zipfile
    import os
    
    try:
        # Ensure output directory exists
        os.makedirs(output_path, exist_ok=True)
        
        # Open the zip file
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            # Check if the file exists in the zip
            if file_name not in zip_ref.namelist():
                return False
            
            # Extract the specific file to the output path
            zip_ref.extract(file_name, output_path)
            
        return True
    except Exception as e:
        return False