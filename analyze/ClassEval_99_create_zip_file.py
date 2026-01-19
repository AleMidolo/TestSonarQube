import zipfile
import os

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
        # Crear el directorio de salida si no existe
        output_dir = os.path.dirname(output_file_name)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Asegurar que el nombre del archivo tenga extensión .zip
        if not output_file_name.endswith('.zip'):
            output_file_name += '.zip'
        
        # Crear el archivo zip
        with zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                # Verificar si el archivo existe
                if os.path.exists(file):
                    # Agregar el archivo al zip con solo su nombre base
                    zipf.write(file, os.path.basename(file))
                else:
                    # Si algún archivo no existe, retornar False
                    return False
        
        return True
    
    except Exception as e:
        # En caso de cualquier error, retornar False
        return False