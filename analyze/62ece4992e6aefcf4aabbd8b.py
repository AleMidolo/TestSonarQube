def force_string(obj):
    """
    如果对象是 `numpy.bytes` 或 `bytes` 类型，则强制使用 'utf-8' 解码。

    参数：
      obj: 一致性配置
    返回值：
      如果对象是字符串类型，则返回对应的 UTF-8 编码的字节对象；否则，直接返回该对象。

    此函数在对象是字符串的情况下，返回对应的 UTF-8 编码的字节对象。
    """
    if isinstance(obj, (bytes, np.bytes_)):
        return obj.decode('utf-8')
    elif isinstance(obj, str):
        return obj.encode('utf-8')
    else:
        return obj