def find_element(self, element_name):
    """
    Encuentra los elementos XML con el nombre especificado.
    :param element_name: cadena, el nombre de los elementos a encontrar.
    :return: lista, una lista de elementos encontrados con el nombre especificado.
    >>> xml_processor = XMLProcessor('test.xml')
    >>> root = xml_processor.read_xml()
    >>> items = xml_processor.find_element('item')
    >>> for item in items:
    >>>     print(item.text)
    apple
    banana
    orange
    """
    if self.root is None:
        return []
    
    return self.root.findall(f".//{element_name}")