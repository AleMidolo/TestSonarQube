def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
        if not all:

    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
    """
    result = {}
    for name, attr in self.namesAndDescriptions_impl(all):
        if isinstance(attr, str):
            result[name] = attr
        elif hasattr(attr, 'getDoc'):
            result[name] = attr.getDoc()
        else:
            result[name] = ''
    return result

def namesAndDescriptions_impl(self, all):
    """Helper implementation method that gets names and descriptions"""
    attrs = []
    
    # Get all attributes if all=True, otherwise just direct attributes
    if all:
        for base in self.__bases__:
            if hasattr(base, 'namesAndDescriptions_impl'):
                attrs.extend(base.namesAndDescriptions_impl(all))
    
    # Add direct interface attributes
    for name in self._InterfaceClass__attrs:
        attrs.append((name, self._InterfaceClass__attrs[name]))
        
    return attrs