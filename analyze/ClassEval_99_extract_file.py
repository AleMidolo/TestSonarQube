def extract_file(self, file_name, output_path):
    """
    Estrae il file con il nome specificato dall'archivio zip e lo salva nel percorso specificato
    :param file_name:string, Il nome del file da decomprimere
    :param output_path:string, La posizione del file estratto
    :return: True o False, che rappresenta se l'operazione di estrazione è stata completata con successo
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_file("bbb.txt", "result/aaa")
    """
    import zipfile
    import os
    
    try:
        # Crea la directory di output se non esiste
        os.makedirs(output_path, exist_ok=True)
        
        # Apri l'archivio zip
        with zipfile.ZipFile(self.zip_file, 'r') as zip_ref:
            # Verifica se il file esiste nell'archivio
            if file_name not in zip_ref.namelist():
                return False
            
            # Estrai il file specifico
            zip_ref.extract(file_name, output_path)
            
        return True
    except Exception as e:
        return False