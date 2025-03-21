def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    """
    Convierte un :class:`.histogram` en un :class:`.graph`.

    *make_value* es una función para establecer el valor de un punto en el gráfico.
    Por defecto, este valor es el contenido del bin.
    *make_value* acepta un único valor (el contenido del bin) sin contexto.

    Esta opción puede ser utilizada para crear barras de error en el gráfico.
    Por ejemplo, para crear un gráfico con errores a partir de un histograma
    donde los bins contienen una tupla nombrada con los campos *mean*, *mean_error* y un contexto,
    se podría usar:

    >>> make_value = lambda bin_: (bin_.mean, bin_.mean_error)

    *get_coordinate* define cuál será la coordenada de un punto en el gráfico
    creado a partir de un bin del histograma. Puede ser "left" (por defecto), "right" o "middle".

    *field_names* establece los nombres de los campos del gráfico. Su número
    debe coincidir con la dimensión del resultado.
    Para un *make_value* como el anterior, los nombres serían
    *("x", "y_mean", "y_mean_error")*.

    *scale* define la escala del gráfico (desconocida por defecto).
    Si es ``True``, utiliza la escala del histograma.

    *hist* debe contener únicamente bins numéricos (sin contexto)
    o *make_value* debe eliminar el contexto al crear un gráfico numérico.

    Devuelve el gráfico resultante.
    """
    if make_value is None:
        make_value = lambda bin_: bin_

    if scale is True:
        scale = hist.scale

    graph_data = []
    for bin_ in hist.bins:
        if get_coordinate == "left":
            x = bin_.left
        elif get_coordinate == "right":
            x = bin_.right
        elif get_coordinate == "middle":
            x = (bin_.left + bin_.right) / 2
        else:
            raise ValueError("get_coordinate debe ser 'left', 'right' o 'middle'")

        value = make_value(bin_.content)
        if isinstance(value, tuple):
            graph_data.append((x,) + value)
        else:
            graph_data.append((x, value))

    return type('Graph', (), {
        'data': graph_data,
        'field_names': field_names,
        'scale': scale
    })