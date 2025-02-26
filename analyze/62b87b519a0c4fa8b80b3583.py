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
        return self.scale_value  # Assuming scale_value is an attribute of the class

    if not isinstance(other, (int, float)) or other <= 0:
        raise LenaValueError("La scala deve essere un valore numerico positivo.")

    # Assuming the graph has a method to resize the last coordinate
    self.resize_last_coordinate(other)
    return self.scale_value  # Return the new scale value