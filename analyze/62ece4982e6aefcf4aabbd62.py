def _replace_url_args(url, url_args):
    """
    किसी भी कस्टम स्ट्रिंग URL आइटम को `args` में दिए गए मानों से बदलें।
    """
    if not url_args:
        return url
        
    for key, value in url_args.items():
        placeholder = '{' + key + '}'
        url = url.replace(placeholder, str(value))
        
    return url