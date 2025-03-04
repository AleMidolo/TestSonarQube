def _replace_url_args(url, url_args):
    """
    Sostituisci eventuali elementi personalizzati della stringa URL con i valori presenti in `args`.
    """
    if not url_args:
        return url
        
    for key, value in url_args.items():
        placeholder = '{' + key + '}'
        url = url.replace(placeholder, str(value))
        
    return url