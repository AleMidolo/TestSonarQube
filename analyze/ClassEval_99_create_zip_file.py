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
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_file_name)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Add .zip extension if not present
        if not output_file_name.endswith('.zip'):
            output_file_name += '.zip'
        
        # Create the zip file
        with zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                # Check if file exists before adding
                if os.path.exists(file):
                    # Add file to zip, using just the filename (not full path) as arcname
                    zipf.write(file, os.path.basename(file))
                else:
                    # If any file doesn't exist, return False
                    return False
        
        return True
    except Exception as e:
        # If any error occurs, return False
        return False