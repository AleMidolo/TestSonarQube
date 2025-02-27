def _replace_url_args(url, url_args):
    """
    Sostituisci eventuali elementi personalizzati della stringa URL con i valori presenti in `args`.
    """
    for key, value in url_args.items():
        url = url.replace(f'{{{key}}}', str(value))
    return url