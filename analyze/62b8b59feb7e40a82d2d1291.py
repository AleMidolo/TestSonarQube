def _getTargetClass(self):
    """
    Define this to return the implementation in use,
    without the 'Py' or 'Fallback' suffix.
    """
    class_name = self.__class__.__name__
    if class_name.endswith('Py'):
        return class_name[:-2]
    elif class_name.endswith('Fallback'):
        return class_name[:-8]
    return class_name