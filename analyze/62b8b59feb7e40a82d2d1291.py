def _getTargetClass(self):
    """
    Defina esto para devolver la implementación en uso,
    sin el sufijo 'Py' o 'Fallback'.
    """
    class_name = self.__class__.__name__
    if class_name.endswith('Py') or class_name.endswith('Fallback'):
        return class_name[:-2]
    return class_name