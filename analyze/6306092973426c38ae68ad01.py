def get_deprecated_args(self):
    """
    अन्य विकल्पों को अप्रचलित करने वाले विकल्पों के साथ डिक्शनरी लौटाना
    """
    deprecated_args = {
        'generator': 'site',
        'maxlag': None,
        'useHtml': None,
        'nopreload': None,
        'throttle': None,
        'sysop': 'user',
        'async': None,  # async is a reserved word in Python 3.7
    }
    return deprecated_args