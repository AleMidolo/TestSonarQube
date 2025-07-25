def _replace_url_args(url, url_args):
    """
    किसी भी कस्टम स्ट्रिंग URL आइटम को `args` में दिए गए मानों से बदलें।
    """
    for key, value in url_args.items():
        url = url.replace(f'{{{key}}}', str(value))
    return url