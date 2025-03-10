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
    import numpy as np
    from collections import namedtuple

    if make_value is None:
        make_value = lambda bin_: bin_

    if scale is None:
        scale = hist.scale if hasattr(hist, 'scale') else None

    bins = hist.bins
    bin_edges = hist.bin_edges

    if get_coordinate == "left":
        x_coords = bin_edges[:-1]
    elif get_coordinate == "right":
        x_coords = bin_edges[1:]
    elif get_coordinate == "middle":
        x_coords = (bin_edges[:-1] + bin_edges[1:]) / 2
    else:
        raise ValueError("get_coordinate deve essere 'left', 'right' o 'middle'")

    values = [make_value(bin_) for bin_ in bins]

    if isinstance(values[0], (tuple, list, np.ndarray)):
        num_fields = len(values[0])
        if len(field_names) != num_fields + 1:
            raise ValueError("Il numero di field_names deve essere uguale alla dimensione del risultato di make_value più uno per la coordinata x")
        Graph = namedtuple('Graph', field_names)
        graph_data = [Graph(x, *value) for x, value in zip(x_coords, values)]
    else:
        if len(field_names) != 2:
            raise ValueError("Il numero di field_names deve essere 2 per un grafico semplice")
        Graph = namedtuple('Graph', field_names)
        graph_data = [Graph(x, value) for x, value in zip(x_coords, values)]

    return graph_data