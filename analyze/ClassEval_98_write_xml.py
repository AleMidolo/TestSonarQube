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
        if hasattr(self, 'tree') and self.tree is not None:
            self.tree.write(file_name, encoding='utf-8', xml_declaration=True)
            return True
        else:
            return False
    except Exception:
        return False