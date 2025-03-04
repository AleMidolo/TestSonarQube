def _replace_url_args(url, url_args):
    """
    Replace any custom string URL items with values in args
    """
    if not url_args:
        return url
        
    # Replace any {arg} in URL with corresponding value from url_args
    for key, value in url_args.items():
        placeholder = '{' + key + '}'
        if placeholder in url:
            url = url.replace(placeholder, str(value))
            
    return url