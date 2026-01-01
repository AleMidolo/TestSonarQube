def extract_file(self, file_name, output_path):
    """
        निर्दिष्ट नाम के साथ फ़ाइल को ज़िप फ़ाइल से निकालें और इसे निर्दिष्ट पथ में रखें
        :param file_name:string, अनकंप्रेस की जाने वाली फ़ाइल का नाम
        :param output_path:string, निकाली गई फ़ाइल का स्थान
        :return: True या False, यह दर्शाता है कि निष्कर्षण प्रक्रिया सफल रही या नहीं
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_file("bbb.txt", "result/aaa")
        """
    try:
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            if file_name not in zip_file.namelist():
                return False
            zip_file.extract(file_name, output_path)
            extracted_path = os.path.join(output_path, file_name)
            if os.path.dirname(output_path) != output_path:
                if not output_path.endswith(os.path.basename(file_name)):
                    target_path = output_path
                    if os.path.isdir(output_path):
                        target_path = os.path.join(output_path, os.path.basename(file_name))
                    if extracted_path != target_path:
                        os.makedirs(os.path.dirname(target_path), exist_ok=True)
                        if os.path.exists(target_path):
                            os.remove(target_path)
                        os.rename(extracted_path, target_path)
            return True
    except:
        return False