def create_zip_file(self, files, output_file_name):
    """
        Comprime la lista de archivos especificada en un archivo zip y lo coloca en la ruta especificada
        :param files: lista de cadenas, Lista de archivos a comprimir
        :param output_file_name: cadena, Ruta de salida especificada
        :return: True o False, representando si la operación de compresión fue exitosa
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