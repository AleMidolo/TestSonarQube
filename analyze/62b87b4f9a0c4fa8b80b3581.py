def scale(self, other=None, recompute=False):
    """
    Calcular o establecer la escala (integral del histograma).

    Si *other* es ``None``, devuelve la escala de este histograma.
    Si su escala no se había calculado antes,
    se calcula y se almacena para uso posterior
    (a menos que se solicite explícitamente *recalcular*).
    Tenga en cuenta que después de modificar (rellenar) el histograma,
    es necesario recalcular explícitamente la escala
    si ya se había calculado previamente.

    Si se proporciona un valor flotante *other*, se reescala el histograma actual (*self*).

    Los histogramas con una escala igual a cero no pueden ser reescalados.
    Se lanza la excepción :exc:`.LenaValueError` si se intenta hacer esto.
    """
    if other is None:
        if not hasattr(self, '_scale') or recompute:
            self._scale = sum(self.histogram)  # Assuming self.histogram is a list of counts
        return self._scale
    else:
        if hasattr(self, '_scale') and self._scale == 0:
            raise LenaValueError("Cannot rescale a histogram with zero scale.")
        self.histogram = [count * (other / self._scale) for count in self.histogram]
        self._scale = other