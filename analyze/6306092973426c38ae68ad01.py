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
        'bbox': 'bounding-box',
        'rotation': 'text-rotation',
        'x': 'position-x',
        'y': 'position-y'
    }
    return deprecated_args