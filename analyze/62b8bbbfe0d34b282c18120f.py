def file_to_textbuffer(file_name, encoding):
    """
    Load a file toward a text buffer (UTF-8), using the specify encoding while reading.
    CAUTION : This will read the whole file IN MEMORY.
    :param file_name: File name.
    :type file_name: str
    :param encoding: Encoding to use.
    :type encoding: str
    :return: A text buffer or None in case of error.
    :rtype str
    """
    try:
        with open(file_name, 'r', encoding=encoding) as file:
            text_buffer = file.read()
        return text_buffer
    except Exception as e:
        print(f"Error reading file: {e}")
        return None