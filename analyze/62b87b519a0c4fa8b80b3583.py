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
        return self.current_scale  # Restituisce la scala attuale del grafico

    if not isinstance(other, (int, float)) or other <= 0:
        raise LenaValueError("La scala deve essere un valore numerico positivo.")

    # Supponiamo che self.coordinates contenga le coordinate del grafico
    if hasattr(self, 'coordinates'):
        last_coordinate = self.coordinates[-1]  # Ottieni l'ultima coordinata
        scale_factor = other / last_coordinate if last_coordinate != 0 else None
        
        if scale_factor is None:
            raise LenaValueError("Impossibile ridimensionare con una scala sconosciuta o zero.")

        # Ridimensiona l'ultima coordinata e gli errori associati
        self.coordinates[-1] *= scale_factor
        for error in self.errors:  # Supponendo che self.errors contenga errori associati
            error.scale(scale_factor)  # Ridimensiona ogni errore

        self.current_scale = other  # Aggiorna la scala attuale
    else:
        raise LenaValueError("Il grafico non ha coordinate valide.")