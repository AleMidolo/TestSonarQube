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
        output_dir = os.path.dirname(output_file_name)
        if output_dir and (not os.path.exists(output_dir)):
            os.makedirs(output_dir)
        with zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                if os.path.exists(file):
                    zipf.write(file, os.path.basename(file))
                else:
                    continue
        return True
    except Exception as e:
        print(f'Error creating zip file: {e}')
        return False