def get_deprecated_args(self):
    """
    Restituzione di un dizionario con opzioni che deprecano altre.
    """
    deprecated_args = {
        'family': 'font-family',
        'size': 'font-size', 
        'weight': 'font-weight',
        'color': 'text-color',
        'background': 'background-color',
        'align': 'text-align',
        'style': 'font-style',
        'decoration': 'text-decoration',
        'spacing': 'letter-spacing',
        'height': 'line-height'
    }
    return deprecated_args