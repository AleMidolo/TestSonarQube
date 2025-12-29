def process_xml_data(self, file_name):
    """
        Modifica i dati negli elementi XML e scrive i dati XML aggiornati in un nuovo file.
        :param file_name: stringa, il nome del file in cui scrivere i dati XML modificati.
        :return: bool, True se l'operazione di scrittura ha successo, False altrimenti.
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
                elem.text = elem.text.strip() + '_modified'
        tree = ET.ElementTree(self.root)
        tree.write(file_name)
        return True
    except:
        return False