def write_xml(self, file_name):
    """
        Scrive i dati XML nel file specificato.
        :param file_name: stringa, il nome del file in cui scrivere i dati XML.
        :return: bool, True se l'operazione di scrittura ha avuto successo, False altrimenti.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> success = xml_processor.write_xml('output.xml')
        >>> print(success)
        True
        """
    try:
        tree = ET.ElementTree(self.root)
        tree.write(file_name)
        return True
    except:
        return False