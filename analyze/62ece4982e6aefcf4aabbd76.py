def match(filename):
    """
    检查给定文件名的类型是否为 'doxyfile'

    参数：
      filename: 要检查的文件名
    返回值：
      如果给定文件名的类型（小写形式）是 'doxyfile'，则返回真

    检查文件名是否为此模块支持的类型

    参数：
      filename: 要匹配的文件名
    返回值：
      如果不匹配，返回假；如果支持，返回真
    """
    return filename.lower() == 'doxyfile'