def _replace_url_args(url, url_args):
    """
    Reemplace cualquier elemento personalizado de la URL con los valores en `args`.

    :param url: La URL que contiene elementos personalizados a reemplazar.
    :param url_args: Un diccionario con los valores para reemplazar en la URL.
    :return: La URL con los elementos personalizados reemplazados.
    """
    for key, value in url_args.items():
        placeholder = f'{{{key}}}'
        url = url.replace(placeholder, str(value))
    return url