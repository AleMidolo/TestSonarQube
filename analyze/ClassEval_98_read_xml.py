def read_xml(self):
    """
    Lee el archivo XML y devuelve el elemento raíz.
    :return: Elemento, el elemento raíz del archivo XML.
    >>> xml_processor = XMLProcessor('test.xml')
    >>> root_element = xml_processor.read_xml()
    >>> print(root_element)
    <Element 'root' at 0x7f8e3b7eb180>
    """
    import xml.etree.ElementTree as ET
    
    tree = ET.parse(self.filename)
    root = tree.getroot()
    return root