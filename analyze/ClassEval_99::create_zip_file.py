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
        output_dir = os.path.dirname(output_file_name)
        if output_dir and (not os.path.exists(output_dir)):
            os.makedirs(output_dir)
        with zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in files:
                if os.path.exists(file_path):
                    arcname = os.path.basename(file_path)
                    zipf.write(file_path, arcname)
                else:
                    return False
        return True
    except Exception:
        return False