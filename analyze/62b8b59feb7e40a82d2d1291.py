def _getTargetClass(self):
    return self.__class__.__name__.replace('Py', '').replace('Fallback', '')