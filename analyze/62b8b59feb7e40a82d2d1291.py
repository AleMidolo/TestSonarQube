def _getTargetClass(self):
    """
    Defina esto para devolver la implementación en uso,
    sin el sufijo 'Py' o 'Fallback'.
    """
    implementation = type(self).__module__
    if implementation.endswith('Py'):
        return implementation[:-2]
    elif implementation.endswith('Fallback'):
        return implementation[:-8]
    return implementation