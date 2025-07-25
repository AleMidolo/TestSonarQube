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
    packages = {}
    
    # Group files by XML base name
    for xml in xmls:
        xml_base = xml.rsplit('.', 1)[0]  # Remove extension
        package_files = []
        
        # Find all files that start with the XML base name
        for file in files:
            if file.startswith(xml_base):
                package_files.append(file)
                
        # Create package if files found
        if package_files:
            packages[xml] = {
                'source': source,
                'files': package_files
            }
            
    return packages