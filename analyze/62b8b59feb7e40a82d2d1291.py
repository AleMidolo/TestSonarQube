def _getTargetClass(self):
    import inspect
    target_class = self.__class__.__name__
    if target_class.endswith('Py'):
        return target_class[:-2]
    elif target_class.endswith('Fallback'):
        return target_class[:-8]
    return target_class