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
    if not hasattr(self, '_scale') or recompute:
        # Calcola la scala come integrale dell'istogramma
        self._scale = sum(self.bins) * self.bin_width
    
    if other is None:
        return self._scale
    elif isinstance(other, float):
        if self._scale == 0:
            raise LenaValueError("Cannot scale a histogram with zero scale.")
        scale_factor = other / self._scale
        self.bins = [bin * scale_factor for bin in self.bins]
        self._scale = other
    else:
        raise TypeError("Expected a float or None for 'other'.")