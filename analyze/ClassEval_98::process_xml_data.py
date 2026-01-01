def process_xml_data(self, file_name):
    """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        :param file_name: string, the name of the file to write the modified XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> success = xml_processor.process_xml_data('processed.xml')
        >>> print(success)
        True
        """
    if self.root is None:
        return False
    try:
        for elem in self.root.iter():
            if elem.text and elem.text.strip():
                elem.text = elem.text.upper()
        tree = ET.ElementTree(self.root)
        tree.write(file_name)
        return True
    except:
        return False