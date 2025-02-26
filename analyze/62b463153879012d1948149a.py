def _group_files_by_xml_filename(source, xmls, files):
    """
    XML फ़ाइलों के बेस नाम के आधार पर फ़ाइलों को समूहित करें

    यह फ़ंक्शन XML फ़ाइलों के बेस नाम के आधार पर फ़ाइलों को समूहित करता है और डेटा को डिक्शनरी प्रारूप में लौटाता है।

    पैरामीटर्स (Parameters)
    ----------
    xml_filename : `str`  
        XML फ़ाइलों के नाम।  

    files : `list`  
        फ़ोल्डर या ज़िप फ़ाइल में मौजूद फ़ाइलों की सूची।  

    रिटर्न्स (Returns)
    -------
    dict  
        - key: XML फ़ाइलों के नाम।  
        - value: पैकेज (Package)।  
    """
    grouped_files = {}
    
    for xml in xmls:
        base_name = xml.split('.')[0]  # Extract base name from XML filename
        grouped_files[base_name] = []

    for file in files:
        for xml in xmls:
            base_name = xml.split('.')[0]
            if file.startswith(base_name):
                grouped_files[base_name].append(file)

    return grouped_files