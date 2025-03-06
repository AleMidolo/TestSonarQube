def _replace_url_args(url, url_args):
    """
    Replace any custom string URL items with values in args.

    Args:
        url (str): The URL string containing placeholders.
        url_args (dict): A dictionary of key-value pairs to replace in the URL.

    Returns:
        str: The URL with placeholders replaced by their corresponding values.
    """
    for key, value in url_args.items():
        placeholder = f"{{{key}}}"
        url = url.replace(placeholder, str(value))
    return url