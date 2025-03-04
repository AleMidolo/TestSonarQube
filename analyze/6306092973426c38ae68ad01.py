def get_deprecated_args(self):
    """
    अन्य विकल्पों को अप्रचलित करने वाले विकल्पों के साथ डिक्शनरी लौटाना
    """
    deprecated_args = {
        'generator': 'site',
        'maxlag': None,
        'useHtml': None,
        'badtitle': None,
        'notitle': None,
        'sysop': None,
        'step': None,
        'async': None,
        'followRedir': 'followRedirects',
        'followRedirects': None,
        'throttle': None,
    }
    return deprecated_args