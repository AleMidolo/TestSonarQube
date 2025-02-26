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

    # Assuming the graph has attributes for coordinates and errors
    if hasattr(self, 'coordinates') and len(self.coordinates) > 0:
        last_coordinate = self.coordinates[-1]
        # Scale the last coordinate
        scaled_coordinate = last_coordinate * other
        self.coordinates[-1] = scaled_coordinate

        # Scale associated errors if they exist
        if hasattr(self, 'errors'):
            for i in range(len(self.errors)):
                self.errors[i] *= other

        self.scale_value = other  # Update the scale value
    else:
        raise LenaValueError("La scala del grafico è sconosciuta o pari a zero.")