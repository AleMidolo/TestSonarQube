def read_xml(self):
    """
        Legge il file XML e restituisce l'elemento radice.
        :return: Elemento, l'elemento radice del file XML.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root_element = xml_processor.read_xml()
        >>> print(root_element)
        <Element 'root' at 0x7f8e3b7eb180>
        """
    try:
        tree = ET.parse(self.file_name)
        self.root = tree.getroot()
        return self.root
    except Exception as e:
        print(f'Error reading XML file: {e}')
        return None