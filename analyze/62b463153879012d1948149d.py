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
    import os
    import xml.etree.ElementTree as ET
    from collections import defaultdict

    package_data = defaultdict(list)

    for filename in os.listdir(folder):
        if filename.endswith('.xml'):
            base_name = os.path.splitext(filename)[0]
            file_path = os.path.join(folder, filename)
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                package_data[base_name].append(root)
            except ET.ParseError as e:
                print(f"Error parsing {file_path}: {e}")

    return dict(package_data)