def read_xml(self):
    """
        XML फ़ाइल को पढ़ता है और रूट तत्व लौटाता है।
        :return: Element, XML फ़ाइल का रूट तत्व।
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root_element = xml_processor.read_xml()
        >>> print(root_element)
        <Element 'root' at 0x7f8e3b7eb180>
        """
    try:
        tree = ET.parse(self.file_name)
        self.root = tree.getroot()
        return self.root
    except ET.ParseError:
        return None
    except FileNotFoundError:
        return None