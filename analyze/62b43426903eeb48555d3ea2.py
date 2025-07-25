def _create_converter(self) -> _converting._Converter:
    """
    Crear el convertidor de estilo de parámetros.

    Devuelve el convertidor de estilo de parámetros (:class:`._converting._Converter`).
    """
    from ._converting import _Converter
    return _Converter()