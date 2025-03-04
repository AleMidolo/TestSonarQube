def get_deprecated_args(self):
    """
    Restituzione di un dizionario con opzioni che deprecano altre.
    """
    deprecated_args = {
        'family': 'font-family',
        'size': 'font-size',
        'weight': 'font-weight',
        'color': 'font-color',
        'align': 'text-align',
        'style': 'font-style',
        'variant': 'font-variant',
        'stretch': 'font-stretch',
        'location': 'path',
        'filename': 'file',
        'format': 'file-format',
        'type': 'file-type',
        'encoding': 'file-encoding',
        'compress': 'compression',
        'quality': 'image-quality',
        'dpi': 'resolution'
    }
    return deprecated_args