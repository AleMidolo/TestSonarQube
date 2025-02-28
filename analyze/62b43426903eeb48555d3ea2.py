def _create_converter(self) -> _converting._Converter:
    """
    创建参数样式转换器。

    返回参数样式转换器 (:class:`._converting._Converter`)。
    """
    return _converting._Converter()