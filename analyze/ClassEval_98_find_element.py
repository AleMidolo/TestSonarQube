def find_element(self, element_name):
    """
    Trova gli elementi XML con il nome specificato.
    :param element_name: stringa, il nome degli elementi da trovare.
    :return: lista, una lista di elementi trovati con il nome specificato.
    >>> xml_processor = XMLProcessor('test.xml')
    >>> root = xml_processor.read_xml()
    >>> items = xml_processor.find_element('item')
    >>> for item in items:
    >>>     print(item.text)
    mela
    banana
    arancia
    """
    if hasattr(self, 'root') and self.root is not None:
        return self.root.findall(f".//{element_name}")
    return []