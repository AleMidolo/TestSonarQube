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

    Si se proporciona un valor flotante *other*, se reescala el histograma actual (*self*) a *other*.

    Los histogramas con una escala igual a cero no pueden ser reescalados.
    Se lanza la excepción :exc:`.LenaValueError` si se intenta hacer esto.
    """
    if other is None:
        if not hasattr(self, '_scale') or recompute:
            self._scale = self._compute_scale()
        return self._scale
    else:
        if not isinstance(other, (int, float)):
            raise TypeError("El valor de escala debe ser un número flotante o entero.")
        if self._scale == 0:
            raise LenaValueError("No se puede reescalar un histograma con escala igual a cero.")
        scale_factor = other / self._scale
        self._data = [x * scale_factor for x in self._data]
        self._scale = other

def _compute_scale(self):
    """
    Calcula la escala del histograma como la suma de todos los valores en el histograma.
    """
    return sum(self._data)

class LenaValueError(Exception):
    pass