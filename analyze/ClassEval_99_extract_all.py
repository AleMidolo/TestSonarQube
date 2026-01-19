def extract_all(self, output_path):
    """
        Extrae todos los archivos zip y los coloca en la ruta especificada
        :param output_path: cadena, La ubicación del archivo extraído
        :return: True o False, que representa si la operación de extracción fue exitosa
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_all("result/aaa")
        """
    try:
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            zip_file.extractall(output_path)
        return True
    except:
        return False