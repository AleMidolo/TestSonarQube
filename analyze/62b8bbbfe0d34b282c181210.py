def append_text_to_file(file_name, text_buffer, encoding, overwrite=False):
    """
    Escribe en el archivo especificado el búfer de texto proporcionado.  
    Crea el archivo si es necesario.  
    :param file_name: Nombre del archivo.  
    :type file_name: str  
    :param text_buffer: Búfer de texto a escribir.  
    :type text_buffer: str  
    :param encoding: La codificación a utilizar.  
    :type encoding: str  
    :param overwrite: Si es verdadero, el archivo será sobrescrito.  
    :type overwrite: bool  
    :return: El número de bytes escritos o un valor menor que 0 si ocurre un error.  
    :rtype int  
    """
    try:
        mode = 'w' if overwrite else 'a'
        with open(file_name, mode, encoding=encoding) as file:
            bytes_written = file.write(text_buffer)
            return bytes_written
    except Exception as e:
        print(f"Error: {e}")
        return -1