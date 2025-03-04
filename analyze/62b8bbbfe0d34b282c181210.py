def append_text_to_file(file_name, text_buffer, encoding, overwrite=False):
    """
    Write to the specified filename, the provided binary buffer
    Create the file if required.
    :param file_name:  File name.
    :type file_name: str
    :param text_buffer: Text buffer to write.
    :type text_buffer: str
    :param encoding: The encoding to use.
    :type encoding: str
    :param overwrite: If true, file is overwritten.
    :type overwrite: bool
    :return: The number of bytes written or lt 0 if error.
    :rtype int
    """
    try:
        # Set mode based on overwrite flag
        mode = 'w' if overwrite else 'a'
        
        # Open file with specified encoding
        with open(file_name, mode, encoding=encoding) as f:
            # Write text buffer to file
            f.write(text_buffer)
            
        # Get number of bytes written by encoding the text
        bytes_written = len(text_buffer.encode(encoding))
        return bytes_written
        
    except Exception as e:
        # Return negative number on error
        return -1