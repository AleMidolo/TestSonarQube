def extract_file(self, file_name, output_path):
    """
    Extrae el archivo con el nombre especificado del archivo zip y lo coloca en la ruta especificada
    :param file_name:string, El nombre del archivo que se va a descomprimir
    :param output_path:string, La ubicación del archivo extraído
    :return: True o False, que representa si la operación de extracción fue exitosa
    >>> zfp = ZipFileProcessor("aaa.zip")
    >>> zfp.extract_file("bbb.txt", "result/aaa")
    """
    try:
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            zip_file.extract(file_name, output_path)
        return True
    except:
        return False