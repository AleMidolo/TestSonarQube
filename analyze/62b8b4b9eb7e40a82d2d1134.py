def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
        if not all:

    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
    """
    attrs = {}
    for name, attr in self.namesAndDescriptions_impl(all):
        attrs[name] = attr
    return attrs

def namesAndDescriptions_impl(self, all=False):
    """Helper method that implements the actual attribute gathering logic"""
    for name, attr in self._attrs.items():
        if all or not self._isReserved(name):
            yield name, attr.getDoc()
            
def _isReserved(self, name):
    """Check if an attribute name is reserved"""
    return name.startswith('__') or name.startswith('_v_')