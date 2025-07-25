def _replace_url_args(url, url_args):
    """
    Sostituisci eventuali elementi personalizzati della stringa URL con i valori presenti in `args`.

    :param url: La stringa URL contenente eventuali segnaposto da sostituire.
    :param url_args: Un dizionario contenente i valori da sostituire nei segnaposto.
    :return: La stringa URL con i segnaposto sostituiti.
    """
    for key, value in url_args.items():
        placeholder = f'{{{key}}}'
        url = url.replace(placeholder, str(value))
    return url