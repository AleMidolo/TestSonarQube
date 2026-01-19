def read_xml(self):
    """
    XML फ़ाइल को पढ़ता है और रूट तत्व लौटाता है।
    :return: Element, XML फ़ाइल का रूट तत्व।
    >>> xml_processor = XMLProcessor('test.xml')
    >>> root_element = xml_processor.read_xml()
    >>> print(root_element)
    <Element 'root' at 0x7f8e3b7eb180>
    """
    import xml.etree.ElementTree as ET
    
    tree = ET.parse(self.filename)
    root = tree.getroot()
    return root