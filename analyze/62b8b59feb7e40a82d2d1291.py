def _getTargetClass(self):
    """
    Definire questo metodo per restituire l'implementazione in uso, 
    senza il suffisso 'Py' o 'Fallback'.
    """
    implementation = type(self).__name__
    if implementation.endswith('Py'):
        return implementation[:-2]
    elif implementation.endswith('Fallback'):
        return implementation[:-8]
    return implementation