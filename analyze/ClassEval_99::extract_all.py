def extract_all(self, output_path):
    """
        Estrae tutti i file zip e li salva nel percorso specificato
        :param output_path: stringa, La posizione del file estratto
        :return: True o False, che rappresenta se l'operazione di estrazione è stata completata con successo
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_all("result/aaa")
        """
    try:
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            zip_file.extractall(output_path)
        return True
    except:
        return False