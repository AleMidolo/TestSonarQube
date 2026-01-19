def read_xml(self):
    """
    Reads the XML file and returns the root element.
    :return: Element, the root element of the XML file.
    >>> xml_processor = XMLProcessor('test.xml')
    >>> root_element = xml_processor.read_xml()
    >>> print(root_element)
    <Element 'root' at 0x7f8e3b7eb180>
    """
    import xml.etree.ElementTree as ET
    tree = ET.parse(self.file_path)
    root = tree.getroot()
    return root