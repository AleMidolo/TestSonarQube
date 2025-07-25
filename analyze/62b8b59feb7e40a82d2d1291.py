def _getTargetClass(self):
    """
    Define this to return the implementation in use,
    without the 'Py' or 'Fallback' suffix.
    """
    implementation_name = type(self).__module__.split('.')[0]
    if implementation_name.endswith('Py'):
        return implementation_name[:-2]
    elif implementation_name.endswith('Fallback'):
        return implementation_name[:-8]
    return implementation_name