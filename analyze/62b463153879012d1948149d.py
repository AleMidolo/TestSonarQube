import os
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
                base_name = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)
                data_dict[base_name].append(file_path)
    
    return dict(data_dict)