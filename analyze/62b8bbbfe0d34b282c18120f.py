def file_to_textbuffer(file_name, encoding):
    """
    Cargar un archivo en un búfer de texto (UTF-8), utilizando la codificación especificada al leer.
    PRECAUCIÓN: Esto leerá todo el archivo EN MEMORIA.
    :param file_name: Nombre del archivo.
    :type file_name: str
    :param encoding: Codificación a utilizar.
    :type encoding: str
    :return: Un búfer de texto o 'None' en caso de error.
    :rtype: str
    """
    try:
        with open(file_name, 'r', encoding=encoding) as file:
            return file.read()
    except Exception as e:
        return None