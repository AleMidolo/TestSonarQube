def process_xml_data(self, file_name):
    """
        Modifica los datos en los elementos XML y escribe los datos XML actualizados en un nuevo archivo.
        :param file_name: cadena, el nombre del archivo para escribir los datos XML modificados.
        :return: bool, True si la operación de escritura es exitosa, False en caso contrario.
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
                elem.text = elem.text.strip() + '_processed'
        tree = ET.ElementTree(self.root)
        tree.write(file_name)
        return True
    except:
        return False