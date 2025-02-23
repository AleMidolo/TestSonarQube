def _replace_url_args(url, url_args):
    """
    Reemplace cualquier elemento personalizado de la URL con los valores en `args`.
    """
    for key, value in url_args.items():
        url = url.replace(f'{{{key}}}', str(value))
    return url