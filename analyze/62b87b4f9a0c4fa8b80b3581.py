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
            self._scale = sum(self.bins)
        return self._scale
    elif isinstance(other, float):
        if not hasattr(self, '_scale') or recompute:
            self._scale = sum(self.bins)
        if self._scale == 0:
            raise LenaValueError("Cannot scale a histogram with zero scale.")
        scale_factor = other / self._scale
        self.bins = [bin_value * scale_factor for bin_value in self.bins]
        self._scale = other
    else:
        raise TypeError("Expected a float or None for 'other'.")