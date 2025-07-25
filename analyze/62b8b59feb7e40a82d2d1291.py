def _getTargetClass(self):
    """
    Definire questo metodo per restituire l'implementazione in uso,
    senza il suffisso 'Py' o 'Fallback'.
    """
    class_name = self.__class__.__name__
    if class_name.endswith('Py') or class_name.endswith('Fallback'):
        return class_name[:-2]
    return class_name