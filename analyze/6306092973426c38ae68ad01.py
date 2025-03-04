def get_deprecated_args(self):
    """
    अन्य विकल्पों को अप्रचलित करने वाले विकल्पों के साथ डिक्शनरी लौटाना
    """
    deprecated_args = {
        'generator': 'site',
        'maxlag': None,
        'debuglevel': 'debug',
        'compress': None,
        'retry': None,
        'host': 'url',
        'encoding': None,
        'max_retries': None,
        'retry_wait': None,
        'max_lag': None,
        'throttle': None,
        'use_api': None,
        'async': None,
    }
    return deprecated_args