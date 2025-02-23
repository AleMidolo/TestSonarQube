def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    """
    Converti un :class:`.histogram` in un :class:`.graph`.

    *make_value* è una funzione utilizzata per impostare il valore di un punto del grafico.
    Per impostazione predefinita, il valore è il contenuto del bin.
    *make_value* accetta un singolo valore (contenuto del bin) senza contesto.

    Questa opzione può essere utilizzata per creare barre di errore nel grafico.
    Ad esempio, per creare un grafico con errori a partire da un istogramma
    dove i bin contengono una named tuple con i campi *mean*, *mean_error* e un contesto,
    si potrebbe utilizzare:

    >>> make_value = lambda bin_: (bin_.mean, bin_.mean_error)

    *get_coordinate* definisce quale sarà la coordinata di un punto del grafico
    creato a partire da un bin dell'istogramma. Può essere "left" (sinistra, predefinito),
    "right" (destra) o "middle" (centro).

    *field_names* imposta i nomi dei campi del grafico. Il loro numero deve essere
    uguale alla dimensione del risultato. Per un *make_value* come quello sopra,
    i nomi dei campi sarebbero *("x", "y_mean", "y_mean_error")*.

    *scale* diventa la scala del grafico (sconosciuta per impostazione predefinita).
    Se è ``True``, utilizza la scala dell'istogramma.

    *hist* deve contenere solo bin numerici (senza contesto) oppure *make_value*
    deve rimuovere il contesto quando crea un grafico numerico.

    Restituisce il grafico risultante.
    """
    if make_value is None:
        make_value = lambda bin_: bin_

    coordinates = []
    values = []

    for bin_ in hist:
        if get_coordinate == "left":
            coordinate = bin_.left
        elif get_coordinate == "right":
            coordinate = bin_.right
        elif get_coordinate == "middle":
            coordinate = bin_.center
        else:
            raise ValueError("Invalid value for get_coordinate")

        value = make_value(bin_)
        coordinates.append(coordinate)
        values.append(value)

    if scale is True:
        # Implement scaling logic based on histogram if needed
        pass

    graph = {field_names[i]: values[i] for i in range(len(field_names))}
    graph['coordinates'] = coordinates

    return graph