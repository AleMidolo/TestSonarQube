def _getTargetClass(self):
    """
    Defina esto para devolver la implementación en uso,
    sin el sufijo 'Py' o 'Fallback'.
    """
    class_name = self.__class__.__name__
    if class_name.endswith('Py'):
        return class_name[:-2]
    elif class_name.endswith('Fallback'):
        return class_name[:-8]
    return class_name