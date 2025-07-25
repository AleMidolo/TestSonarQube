def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
    if not all:

    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
    """
    attributes = self.get_attributes()  # Assuming there's a method to get attributes
    if not all:
        attributes = [attr for attr in attributes if attr.is_defined()]
    
    return {attr.name: attr.description for attr in attributes}