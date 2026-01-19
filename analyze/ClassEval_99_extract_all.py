def extract_all(self, output_path):
    """
    Estrae tutti i file zip e li salva nel percorso specificato
    :param output_path: stringa, La posizione del file estratto
    :return: True o False, che rappresenta se l'operazione di estrazione è stata completata con successo
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_all("result/aaa")
    """
    import zipfile
    import os
    
    try:
        # Crea la directory di output se non esiste
        os.makedirs(output_path, exist_ok=True)
        
        # Apre il file zip e estrae tutti i contenuti
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_path)
        
        return True
    except Exception as e:
        return False