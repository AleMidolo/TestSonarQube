def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
        if not all:

    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
    """
    attrs = {}
    for name, attr in self.namesAndDescriptions_impl(all):
        attrs[name] = attr.getDoc()
    return attrs