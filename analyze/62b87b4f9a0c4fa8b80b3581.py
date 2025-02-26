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
        if not hasattr(self, 'scale_value') or recompute:
            self.scale_value = sum(self.histogram)  # Assuming self.histogram is a list of counts
        return self.scale_value
    else:
        if hasattr(self, 'scale_value') and self.scale_value == 0:
            raise LenaValueError("Cannot rescale a histogram with a scale of zero.")
        self.scale_value = other * (self.scale_value / self.scale_value)  # Rescale logic