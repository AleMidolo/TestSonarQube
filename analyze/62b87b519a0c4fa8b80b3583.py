def scale(self, other=None):
    """
    Ottieni o imposta la scala del grafico.

    Se *other* è ``None``, restituisce la scala di questo grafico.

    Se viene fornito un valore numerico per *other*, il grafico viene ridimensionato a quel valore.
    Se il grafico ha una scala sconosciuta o pari a zero, 
    il tentativo di ridimensionarlo genererà un'eccezione :exc:`~.LenaValueError`.

    Per ottenere risultati significativi, vengono utilizzati i campi del grafico.
    Solo l'ultima coordinata viene ridimensionata.
    Ad esempio, se il grafico ha coordinate *x* e *y*, 
    verrà ridimensionata *y*, mentre per un grafico tridimensionale 
    verrà ridimensionata *z*.
    Tutti gli errori associati vengono ridimensionati insieme alla loro coordinata.
    """
    if other is None:
        return self._scale
    
    if not isinstance(other, (int, float)):
        raise TypeError("Il valore di scala deve essere numerico.")
    
    if self._scale == 0 or self._scale is None:
        raise LenaValueError("Impossibile ridimensionare un grafico con scala sconosciuta o pari a zero.")
    
    # Ridimensiona l'ultima coordinata
    if hasattr(self, 'y'):
        self.y *= other
        if hasattr(self, 'y_err'):
            self.y_err *= other
    elif hasattr(self, 'z'):
        self.z *= other
        if hasattr(self, 'z_err'):
            self.z_err *= other
    else:
        raise AttributeError("Il grafico non ha coordinate ridimensionabili.")
    
    self._scale = other