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
            if file_name not in zip_file.namelist():
                return False
            zip_file.extract(file_name, output_path)
            extracted_path = os.path.join(output_path, file_name)
            target_path = os.path.join(output_path, os.path.basename(file_name))
            if extracted_path != target_path:
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                if os.path.exists(extracted_path):
                    os.rename(extracted_path, target_path)
        return True
    except:
        return False