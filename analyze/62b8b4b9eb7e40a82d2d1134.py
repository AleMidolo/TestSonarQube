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
    for name, attr in self._InterfaceClass__attrs.items():
        if all or not attr.queryTaggedValue('_hidden', False):
            yield name, attr.getDoc()