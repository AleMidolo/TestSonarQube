def append_text_to_file(file_name, text_buffer, encoding, overwrite=False):
    """
    将文本缓冲区中的数据写入文件
    将提供的文本缓冲区写入指定的文件名。  
    如果文件不存在，则创建文件。  

    :param file_name: 文件名。  
    :type filename: str
    :param text_buffer: 要写入的文本缓冲。  
    :type text_buffer: str
    :param encoding: 使用的编码格式。  
    :type encoding: str
    :param overwrite: 如果为真，则覆盖文件内容。  
    :type overwrite: bool
    :return: 写入的字节数。如果发生错误，则返回小于 0 的值。  
    :rtype: int
    """
    try:
        mode = 'w' if overwrite else 'a'
        with open(file_name, mode, encoding=encoding) as file:
            bytes_written = file.write(text_buffer)
        return bytes_written
    except Exception as e:
        print(f"Error writing to file: {e}")
        return -1