import zipfile
import os
from collections import defaultdict
import xml.etree.ElementTree as ET

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
    """
    data_dict = defaultdict(list)

    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for file_info in zip_file.infolist():
            if file_info.filename.endswith('.xml'):
                basename = os.path.basename(file_info.filename)
                with zip_file.open(file_info.filename) as file:
                    xml_content = file.read()
                    data_dict[basename].append(xml_content)

    return dict(data_dict)