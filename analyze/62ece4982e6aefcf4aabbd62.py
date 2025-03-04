def _replace_url_args(url, url_args):
    """
    Reemplace cualquier elemento personalizado de la URL con los valores en `args`.
    """
    if not url_args:
        return url
        
    for key, value in url_args.items():
        if value is not None:
            placeholder = '{' + key + '}'
            url = url.replace(placeholder, str(value))
            
    return url