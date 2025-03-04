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
            self._scale = self._calculate_scale()
        return self._scale

    if isinstance(other, float):
        if self._scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale.")
        self._rescale(other)
    else:
        raise TypeError("Expected a float value for 'other'.")