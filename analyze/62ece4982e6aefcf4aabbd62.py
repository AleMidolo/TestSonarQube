def _replace_url_args(url, url_args):
    """
    Replace any custom string URL items with values in args.

    Args:
        url (str): The URL string containing placeholders to be replaced.
        url_args (dict): A dictionary containing the key-value pairs for replacement.

    Returns:
        str: The URL with placeholders replaced by the corresponding values from url_args.
    """
    for key, value in url_args.items():
        placeholder = f'{{{key}}}'
        url = url.replace(placeholder, str(value))
    return url