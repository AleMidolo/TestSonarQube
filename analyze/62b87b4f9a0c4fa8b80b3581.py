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
        if self.scale() == 0:
            raise LenaValueError("No se puede reescalar un histograma con escala igual a cero.")
        current_scale = self.scale()
        self._rescale(other / current_scale)
        self._scale = other

def _compute_scale(self):
    """
    Calcula la escala del histograma como la integral del histograma.
    """
    return sum(self.bins) * self.bin_width

def _rescale(self, factor):
    """
    Reescala los bins del histograma por un factor dado.
    """
    self.bins = [bin_value * factor for bin_value in self.bins]

class LenaValueError(Exception):
    """
    Excepción lanzada cuando se intenta reescalar un histograma con escala cero.
    """
    pass