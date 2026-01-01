def extract_file(self, file_name, output_path):
    """
        Estrae il file con il nome specificato dall'archivio zip e lo salva nel percorso specificato
        :param file_name:string, Il nome del file da decomprimere
        :param output_path:string, La posizione del file estratto
        :return: True o False, che rappresenta se l'operazione di estrazione è stata completata con successo
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_file("bbb.txt", "result/aaa")
        """
    try:
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            zip_file.extract(file_name, output_path)
        return True
    except:
        return False