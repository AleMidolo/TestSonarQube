def create_zip_file(self, files, output_file_name):
    """
        Comprimi l'elenco di file specificato in un file zip e lo salva nel percorso specificato
        :param files: lista di stringhe, Elenco dei file da comprimere
        :param output_file_name: stringa, Percorso di output specificato
        :return: True o False, che rappresenta se l'operazione di compressione è stata riuscita
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.create_zip_file(["bbb.txt", "ccc.txt", "ddd.txt"], "output/bcd")
        """
    try:
        with zipfile.ZipFile(output_file_name, 'w') as zip_file:
            for file in files:
                zip_file.write(file)
        return True
    except:
        return False