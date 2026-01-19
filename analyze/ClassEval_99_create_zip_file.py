import zipfile
import os

def create_zip_file(self, files, output_file_name):
    """
    निर्दिष्ट फ़ाइल सूची को एक ज़िप फ़ाइल में संकुचित करें और इसे निर्दिष्ट पथ में रखें
    :param files: स्ट्रिंग की सूची, संकुचित करने के लिए फ़ाइलों की सूची
    :param output_file_name: स्ट्रिंग, निर्दिष्ट आउटपुट पथ
    :return: True या False, यह दर्शाता है कि संकुचन संचालन सफल था या नहीं
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.create_zip_file(["bbb.txt", "ccc,txt", "ddd.txt"], "output/bcd")
    """
    try:
        # Ensure output directory exists
        output_dir = os.path.dirname(output_file_name)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Add .zip extension if not present
        if not output_file_name.endswith('.zip'):
            output_file_name += '.zip'
        
        # Create zip file
        with zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                # Check if file exists
                if os.path.exists(file):
                    # Add file to zip with just its basename
                    zipf.write(file, os.path.basename(file))
                else:
                    # If file doesn't exist, return False
                    return False
        
        return True
    except Exception as e:
        # Return False if any error occurs
        return False