import os

def _group_files_by_xml_filename(source, xmls, files):
    """
    XML फ़ाइलों के बेस नाम के आधार पर फ़ाइलों को समूहित करें

    यह फ़ंक्शन XML फ़ाइलों के बेस नाम के आधार पर फ़ाइलों को समूहित करता है और डेटा को डिक्शनरी प्रारूप में लौटाता है।

    पैरामीटर्स (Parameters)
    ----------
    source : `str`
        स्रोत फ़ोल्डर या ज़िप फ़ाइल का पथ।
    
    xmls : `list`
        XML फ़ाइलों की सूची।
    
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
        xml_basename = os.path.splitext(os.path.basename(xml))[0]
        grouped_files[xml_basename] = []
        
        for file in files:
            if xml_basename in file:
                grouped_files[xml_basename].append(file)
    
    return grouped_files