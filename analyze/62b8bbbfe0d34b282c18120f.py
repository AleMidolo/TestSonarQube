def file_to_textbuffer(file_name, encoding):
    """
    将文件加载到文本缓冲区（UTF-8），在读取时使用指定的编码。
    注意：此操作会将整个文件加载到内存中。

    :param file_name: 文件名。
    :type file_name: str
    :param encoding: 要使用的编码。
    :type encoding: str
    :return: 文本缓冲区，若发生错误则返回 None。
    :rtype: str
    """
    try:
        with open(file_name, 'r', encoding=encoding) as file:
            text_buffer = file.read()
        return text_buffer
    except Exception as e:
        print(f"Error reading file: {e}")
        return None