def get_deprecated_args(self):
    """
    अन्य विकल्पों को अप्रचलित करने वाले विकल्पों के साथ डिक्शनरी लौटाना
    """
    deprecated_args = {
        'generator': 'site',
        'defaultsort': 'defaultsort',
        'nocategories': 'categories',
        'notalkid': 'talkid',
        'nocontentmodel': 'contentmodel', 
        'nosharedupload': 'sharedupload',
        'nocontentmodel': 'contentmodel',
        'noimages': 'images',
        'nolinks': 'links',
        'nolanguagelinks': 'langlinks',
        'notemplates': 'templates',
        'noexternallinks': 'externallinks',
        'nocategories': 'categories'
    }
    return deprecated_args