def _replace_url_args(url, url_args):
    """
    Replace any custom string URL items with values in args
    """
    if not url_args:
        return url
        
    for key, value in url_args.items():
        placeholder = '{' + key + '}'
        url = url.replace(placeholder, str(value))
        
    return url