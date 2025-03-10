import os
import xml.etree.ElementTree as ET
from collections import defaultdict

def _explore_folder(folder):
    """
    फ़ोल्डर से पैकेज का डेटा प्राप्त करें।  

    फ़ाइलों को उनके XML बेसनाम के आधार पर समूहित करता है और डेटा को डिक्शनरी (dict) प्रारूप में लौटाता है।  

    पैरामीटर  
    folder : str
        पैकेज का फ़ोल्डर।  

    रिटर्न्स  
    dict
    """
    data_dict = defaultdict(list)
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(root, file)
                try:
                    tree = ET.parse(file_path)
                    root_element = tree.getroot()
                    base_name = os.path.splitext(file)[0]
                    data_dict[base_name].append(root_element)
                except ET.ParseError as e:
                    print(f"Error parsing {file_path}: {e}")
    
    return dict(data_dict)