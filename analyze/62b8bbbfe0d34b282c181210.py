def append_text_to_file(file_name, text_buffer, encoding, overwrite=False):
    try:
        mode = 'w' if overwrite else 'a'
        with open(file_name, mode, encoding=encoding) as file:
            bytes_written = file.write(text_buffer)
            return bytes_written
    except Exception as e:
        return -1