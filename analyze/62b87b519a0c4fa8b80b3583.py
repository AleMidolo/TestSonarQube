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
        return self.scale_value  # Restituisce la scala attuale

    if not isinstance(other, (int, float)):
        raise ValueError("Il valore di 'other' deve essere un numero.")

    if self.scale_value is None or self.scale_value == 0:
        raise LenaValueError("La scala è sconosciuta o pari a zero.")

    # Ridimensiona l'ultima coordinata
    if self.dimension == 2:
        self.y_scale *= other
    elif self.dimension == 3:
        self.z_scale *= other

    # Ridimensiona gli errori associati
    for error in self.errors:
        error.scale *= other

    return self.scale_value