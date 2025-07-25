import zipfile
import os
from xml.etree import ElementTree as ET

def _explore_zipfile(zip_path):
    """
    ज़िप पथ से पैकेजों का डेटा प्राप्त करता है।

    फ़ाइलों को उनके XML बेसनाम (basename) के आधार पर समूहित करता है और डेटा को डिक्शनरी (dict) प्रारूप में लौटाता है।

    पैरामीटर (Parameters)
    ----------
    zip_path : str
        ज़िप फ़ाइल का पथ।

    रिटर्न्स (Returns)
    -------
    dict
        XML फ़ाइलों के डेटा को समूहित करके एक डिक्शनरी के रूप में लौटाता है।
    """
    data_dict = {}
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith('.xml'):
                basename = os.path.basename(file_name)
                with zip_ref.open(file_name) as xml_file:
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    data_dict[basename] = root
    
    return data_dict