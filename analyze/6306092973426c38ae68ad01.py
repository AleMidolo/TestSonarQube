def get_deprecated_args(self):
    """
    अन्य विकल्पों को अप्रचलित करने वाले विकल्पों के साथ डिक्शनरी लौटाना
    """
    deprecated_args = {
        'generator': 'site',
        'followRedirects': 'follow_redirects',
        'returndict': 'return_dict', 
        'encodeTitle': 'encode_title',
        'notitle': 'no_title',
        'noredirect': 'no_redirect',
        'throttle': None,
        'sysop': None,
        'async': None,
    }
    return deprecated_args