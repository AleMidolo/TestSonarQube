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
    elif isinstance(other, (int, float)):
        if self._scale == 0 or self._scale is None:
            raise LenaValueError("La scala del grafico è sconosciuta o pari a zero.")
        scale_factor = other / self._scale
        self._scale = other
        # Ridimensiona l'ultima coordinata
        if hasattr(self, 'y'):
            self.y *= scale_factor
            if hasattr(self, 'y_err'):
                self.y_err *= scale_factor
        elif hasattr(self, 'z'):
            self.z *= scale_factor
            if hasattr(self, 'z_err'):
                self.z_err *= scale_factor
        else:
            raise LenaValueError("Nessuna coordinata valida trovata per il ridimensionamento.")
    else:
        raise TypeError("Il valore di scala deve essere un numero o None.")