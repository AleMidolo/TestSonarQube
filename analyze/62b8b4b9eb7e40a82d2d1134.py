def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
    if not all:

    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
    """
    attributes = self.get_attributes()  # Assuming there's a method to get attributes
    if not all:
        attributes = {k: v for k, v in attributes.items() if self.is_defined(k)}  # Filter defined attributes
    return {k: v.description for k, v in attributes.items()}  # Assuming each attribute has a description