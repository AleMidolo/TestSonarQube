def _create_converter(self) -> _converting._Converter:
    """
    Crea il convertitore dello stile dei parametri.

    Restituisce il convertitore dello stile dei parametri (:class:`._converting._Converter`).
    """
    from ._converting import _Converter
    return _Converter()