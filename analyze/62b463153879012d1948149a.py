def _group_files_by_xml_filename(source, xmls, files):
    grouped_files = {}
    
    for xml in xmls:
        xml_basename = xml.split('.')[0]  # Get the basename of the XML file
        grouped_files[xml_basename] = []

        for file in files:
            if file.startswith(xml_basename):
                grouped_files[xml_basename].append(file)

    return grouped_files