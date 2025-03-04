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
    # Se other è None, calcola e restituisce la scala
    if other is None:
        # Se la scala non è stata calcolata o viene richiesto il ricalcolo
        if self._scale is None or recompute:
            # Calcola l'integrale dell'istogramma sommando i contenuti dei bin
            self._scale = sum(self._contents)
        return self._scale
        
    # Se viene fornito un valore per riscalare
    else:
        # Calcola la scala corrente
        current_scale = self.scale()
        
        # Controlla se la scala è zero
        if current_scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale")
            
        # Calcola il fattore di scala
        scale_factor = float(other) / current_scale
        
        # Riscala i contenuti dei bin
        self._contents = [c * scale_factor for c in self._contents]
        
        # Aggiorna la scala memorizzata
        self._scale = other