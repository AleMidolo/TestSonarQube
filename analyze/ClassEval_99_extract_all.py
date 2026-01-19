def extract_all(self, output_path):
    """
    Extrae todos los archivos zip y los coloca en la ruta especificada
    :param output_path: cadena, La ubicación del archivo extraído
    :return: True o False, que representa si la operación de extracción fue exitosa
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_all("result/aaa")
    """
    import zipfile
    import os
    
    try:
        # Crear el directorio de salida si no existe
        os.makedirs(output_path, exist_ok=True)
        
        # Abrir el archivo zip y extraer todos los archivos
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_path)
        
        return True
    except Exception as e:
        return False