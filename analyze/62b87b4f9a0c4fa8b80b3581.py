def scale(self, other=None, recompute=False):
    """
    Calcola o imposta la scala (integrale dell'istogramma).

    Se *other* è ``None``, restituisce la scala di questo istogramma.  
    Se la scala non è stata calcolata in precedenza, viene calcolata e memorizzata per un utilizzo successivo (a meno che non venga esplicitamente richiesto di *ricalcolare*).  
    Nota che, dopo aver modificato (riempito) l'istogramma, è necessario ricalcolare esplicitamente la scala se era stata calcolata in precedenza.

    Se viene fornito un valore float in *other*, l'oggetto corrente (*self*) viene riscalato al valore di *other*.

    Gli istogrammi con scala pari a zero non possono essere riscalati.  
    Viene sollevata un'eccezione :exc:`.LenaValueError` se si tenta di farlo.
    """
    if other is None:
        if not hasattr(self, '_scale') or recompute:
            self._scale = self._compute_scale()
        return self._scale
    elif isinstance(other, float):
        if self._scale == 0:
            raise LenaValueError("Cannot rescale a histogram with zero scale.")
        scale_factor = other / self._scale
        self._rescale(scale_factor)
        self._scale = other
    else:
        raise TypeError("Expected a float or None for 'other'.")

def _compute_scale(self):
    """
    Calcola la scala dell'istogramma come l'integrale dei bin.
    """
    return sum(bin_content for bin_content in self.bins)

def _rescale(self, scale_factor):
    """
    Riscalare i contenuti dei bin per un fattore di scala dato.
    """
    self.bins = [bin_content * scale_factor for bin_content in self.bins]

class LenaValueError(Exception):
    """
    Eccezione sollevata quando si tenta di riscalare un istogramma con scala zero.
    """
    pass