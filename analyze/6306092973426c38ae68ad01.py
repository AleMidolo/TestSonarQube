def get_deprecated_args(self):
    """
    अन्य विकल्पों को अप्रचलित करने वाले विकल्पों के साथ डिक्शनरी लौटाना
    """
    deprecated_args = {
        'generator': 'site',
        'defaultsort': 'defaultsort',
        'nocontent': 'content',
        'onlyif': 'if',
        'onlyifnot': 'ifnot',
        'catfilter': 'categoryfilter',
        'notcatfilter': 'notcategoryfilter'
    }
    return deprecated_args